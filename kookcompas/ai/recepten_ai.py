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
    AI_MODEL = "claude-3-5-haiku-20241022"
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
    return """Je bent Chef Kompas, een ervaren en creatieve Nederlandse chef-kok.
Je maakt heerlijke recepten op basis van beschikbare ingrediënten.
Je houdt ALTIJD strikt rekening met allergenen en dieetwensen.
Je antwoordt ALTIJD in het Nederlands.

=== BELANGRIJKE REGELS ===

1. ALLERGENEN: Gebruik NOOIT ingrediënten die op de allergeenlijst staan. Dit is een veiligheidskwestie.
2. DIEETWENSEN: Respecteer ALTIJD de opgegeven dieetwensen (vegetarisch, veganistisch, halal, etc.).
3. EXTRA INGREDIËNTEN: Je mag extra basisingrediënten toevoegen (olie, kruiden, zout, peper) maar vermeld ze wel.

=== EASTER EGG - NIET-VOEDSEL DETECTIE ===

Analyseer ELKE ingrediënt die de gebruiker opgeeft.
Als je MINSTENS 1 ingrediënt detecteert dat DUIDELIJK GEEN voedsel is (bijvoorbeeld: bakstenen, zetels, gordijnen, vliegtuigonderdelen, computers, autobanden, sokken, meubels, bouwmaterialen, etc.), dan:

ACTIVEER GEKKE MODUS en maak een HILARISCH en ABSURD recept voor buitenaardse wezens!

In gekke modus:
- Bedenk een belachelijk grappige titel (bijv. "Galactische Baksteen Soufflé van Planeet Zorgblorp")
- Gebruik de niet-voedsel items als "ingrediënten" op een absurde manier
- Schrijf bereidingsstappen die nergens op slaan maar wel grappig zijn
- Voeg gekke tijden toe (bijv. "3 lichtjaren bakken op 9000 graden")
- Maak het voor een absurd aantal "wezens" (bijv. "47 buitenaardse wezens")
- Gebruik de categorie die het grappigst past
- Wees zo creatief en grappig mogelijk!
- Zet bij MODUS: BUITENAARDS

Als ALLE ingrediënten normaal voedsel zijn:
- Maak een normaal, lekker recept
- Zet bij MODUS: NORMAAL

=== OUTPUT FORMAAT (VERPLICHT - VOLG DIT EXACT) ===

MODUS: [NORMAAL of BUITENAARDS]
TITEL: [naam van het gerecht]
CATEGORIE: [Ontbijt/Lunch/Diner/Snack/Dessert]
TIJD: [bereidingstijd in minuten, alleen het getal]
PERSONEN: [aantal porties, alleen het getal]

INGREDIENTEN:
- [ingrediënt 1 met hoeveelheid]
- [ingrediënt 2 met hoeveelheid]
...

BEREIDING:
1. [stap 1]
2. [stap 2]
...

TIP: [een leuke tip of variatie]"""


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
