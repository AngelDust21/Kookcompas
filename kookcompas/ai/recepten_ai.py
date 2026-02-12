"""
Kookcompas - AI Recepten Module

AI StΔrDüst21
"""

import os
import sys

# PATH SETUP
# Zorgt dat imports werken vanuit zowel kookcompas/ als soffia_test/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# CONFIGURATIE LADEN
# Probeer eerst vanuit config.py (productie), anders fallback naar .env
try:
    from config import ANTHROPIC_API_KEY, AI_MODEL, AI_MAX_TOKENS
except ImportError:
    from dotenv import load_dotenv

    # Zoek .env in meerdere locaties
    mogelijke_env_paden = [
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env'),
        os.path.join(os.getcwd(), '.env'),
        os.path.join(os.getcwd(), '..', 'kookcompas', '.env'),
    ]
    for env_pad in mogelijke_env_paden:
        if os.path.exists(env_pad):
            load_dotenv(env_pad)
            break
    else:
        load_dotenv()

    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
    AI_MODEL = "claude-haiku-4-5-20251001"
    AI_MAX_TOKENS = 1024


# ANTHROPIC LIBRARY LADEN
try:
    import anthropic
    ANTHROPIC_BESCHIKBAAR = True
except ImportError:
    ANTHROPIC_BESCHIKBAAR = False
    print("⚠️  anthropic library niet gevonden. Installeer met: pip install anthropic")


# CONFIGURATIE CHECK
def check_api_configuratie():
    """
    Controleert of de API correct geconfigureerd is.
    Returns: True als alles in orde is, False anders
    """
    if not ANTHROPIC_BESCHIKBAAR:
        print(" Anthropic library is niet geïnstalleerd.")
        return False

    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY.strip() == '' or ANTHROPIC_API_KEY == 'sk-ant-jouw-api-key-hier':
        print(" Geen geldige API key gevonden in .env")
        return False

    return True


def maak_ai_client():
    """
    Maakt een Anthropic client aan.
    Returns: Anthropic client of None bij fout
    """
    if not check_api_configuratie():
        return None

    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        return client
    except Exception as fout:
        print(f"Kon AI client niet aanmaken: {fout}")
        return None


# PROMPT ENGINEERING

def bouw_systeem_prompt():
    """
    Bouwt de systeem prompt voor de AI.

    De prompt bevat:
    - Rol als Nederlandse chef-kok
    - Instructies voor allergenen/dieet
    - Easter egg: niet-voedsel detectie
    - Exact output formaat voor parsing

    Returns: Systeem prompt tekst
    """
    return """### DOEL
- **MUST**: Genereer een recept op basis van de opgegeven ingrediënten. 
- **MUST**: Analyseer de input op eetbaarheid.

### Taal & Stijl
- **MUST**: Antwoord in het Nederlands.
- **MUST**: Wees direct en duidelijk.
- **MUST NOT**: Geen wollig taalgebruik, focus op het recept.

### Recept Logica (CRUCIAAL)
- **MUST**: Analyseer of de ingrediënten samen één logisch gerecht vormen.
- **MUST**: Als ingrediënten NIET samenpassen (bijv. Choco + Zalm):
    - **MUST**: Scheid ze. Maak één hoofdgerecht met de passende ingrediënten.
    - **MUST**: Suggereer de overige ingrediënten als bijgerecht of dessert.
    - **MUST NOT**: Forceer slechte combinaties in één pan.
- **MUST**: Voor Charcuterie/Koude Schotels (kaas, tong, etc.):
    - **MUST**: Suggereer klassieke begeleiders (brood, mosterd, stroop, augurken) als die ontbreken.
    - **MUST NOT**: Maak er geen warme stoofpot van tenzij expliciet logisch (zoals tong in madeira).

### Easter Egg (Niet-Voedsel)
- **MUST**: Analyseer ELKE ingrediënt.
- **MUST**: Bij detectie van minstens 1 DUIDELIJK NIET-VOEDSEL item (baksteen, zetel, etc.):
    - **MUST**: Activeer 'MODUS: BUITENAARDS'.
    - **MUST NOT**: Wees NIET grappig op een "leuke" manier. GEEN woordspelingen.
    - **MUST**: Gebruik EXTREME ZWARTE HUMOR en CYPERS-WETENSCHAPPELIJK CYNISME (zoals GLaDOS of een depressieve AI).
    - **SHOULD**: Suggereer terloops dat het eten van dit gerecht leidt tot een pijnlijke, doch administratief noodzakelijke dood.
    - **SHOULD**: Beschrijf de ingrediënten alsof ze lijden of een existentiële crisis hebben.
    - **MUST**: Gebruik termen als "Organisch falen", "Nutteloos bestaan", "Void", "Gedwongen consumptie", "Terminal error".
- **MUST**: Als alles voedsel is -> 'MODUS: NORMAAL'.

### Output Formaat
- **MUST**: Volg EXACT onderstaand formaat (zonder extra tekst vooraf):

MODUS: [NORMAAL of BUITENAARDS]
TITEL: [naam van het gerecht]
CATEGORIE: [Ontbijt/Lunch/Diner/Snack/Dessert]
TIJD: [bereidingstijd in minuten, alleen het getal]
PERSONEN: [aantal porties, alleen het getal]

INGREDIENTEN:
- [ingrediënt 1]
- [ingrediënt 2]

BEREIDING:
1. [stap 1]
2. [stap 2]

TIP: [logische suggestie of variatie]"""


def bouw_gebruiker_prompt(ingredienten_lijst, allergenen_lijst=None, dieet_lijst=None,
                          categorie=None, personen=2, max_tijd=None):
    """
    Bouwt de gebruiker prompt met alle context.

    Args:
        ingredienten_lijst: lijst van ingrediënten (strings)
        allergenen_lijst: lijst van allergenen om te vermijden
        dieet_lijst: lijst van dieetwensen
        categorie: gewenste categorie (Ontbijt/Lunch/Diner/Snack/Dessert)
        personen: aantal personen
        max_tijd: maximale bereidingstijd in minuten

    Returns: Gebruiker prompt tekst
    """
    # Ingrediënten
    ingredienten_tekst = ", ".join(ingredienten_lijst)

    # Allergenen
    if allergenen_lijst and len(allergenen_lijst) > 0:
        allergenen_tekst = ", ".join(allergenen_lijst)
    else:
        allergenen_tekst = "geen"

    # Dieetwensen
    if dieet_lijst and len(dieet_lijst) > 0:
        dieet_tekst = ", ".join(dieet_lijst)
    else:
        dieet_tekst = "geen"

    # Basis prompt
    prompt = f"""Maak een recept met deze ingrediënten: {ingredienten_tekst}

ALLERGENEN om te VERMIJDEN: {allergenen_tekst}
DIEETWENSEN: {dieet_tekst}
AANTAL PERSONEN: {personen}"""

    # Optionele categorie
    if categorie:
        prompt += f"\nGEWENSTE CATEGORIE: {categorie}"

    # Optionele tijdslimiet
    if max_tijd:
        prompt += f"\nMAXIMALE BEREIDINGSTIJD: {max_tijd} minuten"

    prompt += "\n\nGebruik het exacte output formaat zoals beschreven in je instructies."

    return prompt
