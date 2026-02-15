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
    print("anthropic library niet gevonden. Installeer met: pip install anthropic")


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

    # Ternary operators voor compacte code: als lijst leeg is, gebruik "geen".
    allergenen_tekst = ", ".join(allergenen_lijst) if allergenen_lijst else "geen"
    dieet_tekst = ", ".join(dieet_lijst) if dieet_lijst else "geen"

    # De feitelijke vraag aan de AI.
    prompt = f"""Maak een recept met: {ingredienten_tekst}

RESTRICTIES:
- Allergieën: {allergenen_tekst}
- Dieet: {dieet_tekst}
- Personen: {personen}"""

    # Optionele categorie
    if categorie:
        prompt += f"\nGEWENSTE CATEGORIE: {categorie}"

    # Optionele tijdslimiet
    if max_tijd:
        prompt += f"\nMAXIMALE BEREIDINGSTIJD: {max_tijd} minuten"

    prompt += "\n\nGebruik het exacte output formaat zoals beschreven in je instructies."

    return prompt


#  RECEPT GENERATIE

def genereer_recept(ingredienten_lijst, allergenen_lijst=None, dieet_lijst=None,
                    categorie=None, personen=2, max_tijd=None):
    """
    Genereert een recept via Claude AI.

    Dit is de hoofdfunctie die aangeroepen wordt vanuit de applicatie.

    Args:
        ingredienten_lijst: lijst van ingrediënten ["pasta", "tomaat", "ui"]
        allergenen_lijst: lijst van allergenen ["noten", "lactose"]
        dieet_lijst: lijst van dieetwensen ["vegetarisch"]
        categorie: optioneel - gewenste categorie
        personen: aantal personen (standaard 2)
        max_tijd: optioneel - max bereidingstijd in minuten

    Returns:
        dict met recept info of None bij fout
        {
            'titel': str,
            'categorie': str,
            'bereidingstijd': int,
            'personen': int,
            'ingredienten': str,
            'instructies': str,
            'tip': str,
            'is_easter_egg': bool
        }
    """
    # Validatie
    if not ingredienten_lijst or len(ingredienten_lijst) == 0:
        print("Geef minstens 1 ingrediënt op.")
        return None

    # Client aanmaken
    client = maak_ai_client()
    if not client:
        return None

    # Prompts bouwen
    systeem_prompt = bouw_systeem_prompt()
    gebruiker_prompt = bouw_gebruiker_prompt(
        ingredienten_lijst, allergenen_lijst, dieet_lijst, categorie, personen, max_tijd
    )

    try:
        # API call naar Claude
        bericht = client.messages.create(
            model=AI_MODEL,
            max_tokens=AI_MAX_TOKENS,
            system=systeem_prompt,
            messages=[
                {"role": "user", "content": gebruiker_prompt}
            ]
        )

        # Response tekst ophalen
        response_tekst = bericht.content[0].text

        # Parsen naar dictionary
        recept = parse_recept_response(response_tekst)

        return recept

    except anthropic.APIConnectionError:
        print("Geen internetverbinding. Controleer je netwerk.")
        return None
    except anthropic.RateLimitError:
        print("Te veel verzoeken. Wacht even en probeer opnieuw.")
        return None
    except anthropic.AuthenticationError:
        print("Ongeldige API key. Controleer je .env bestand.")
        return None
    except anthropic.APIStatusError as fout:
        print(f"API fout: {fout.message}")
        return None
    except Exception as fout:
        print(f"Onverwachte fout bij recept generatie: {fout}")
        return None


# RESPONSE PARSING

def parse_recept_response(tekst):
    """
    Leest de AI tekst regel voor regel en stopt dit in een dictionary.
    Werkt als een staatsmachine: kijkt naar headers (TITEL:, INGREDIENTEN:)
    en verandert van modus.
    """
    # Basisstructuur met veilige standaarden.
    recept = {
        'titel': 'Onbekend Recept',
        'categorie': 'Diner',
        'bereidingstijd': 30,
        'personen': 2,
        'ingredienten': '',
        'instructies': '',
        'tip': '',
        'is_easter_egg': False,
        'raw_response': tekst
    }

    # Veiligheid: Als het formaat compleet mis is, geef ruwe tekst terug.
    if "MODUS:" not in tekst and "TITEL:" not in tekst:
        recept['instructies'] = tekst
        recept['titel'] = "Suggestie van de Chef"
        return recept

    regels = tekst.split('\n')
    huidige_sectie = None
    ingredienten_lijst = []
    instructies_lijst = []

    for regel in regels:
        regel = regel.strip()
        if not regel and huidige_sectie is None:
            continue # Sla lege regels over in header.

        # Header detectie (State switching)
        bovenstuk = regel.upper()
        
        if bovenstuk.startswith('MODUS:'):
            recept['is_easter_egg'] = 'BUITENAARDS' in bovenstuk
            huidige_sectie = None

        elif regel.upper().startswith('TITEL:'):
            recept['titel'] = regel.split(':', 1)[1].strip()
            huidige_sectie = None

        elif regel.upper().startswith('CATEGORIE:'):
            cat = regel.split(':', 1)[1].strip()
            geldige_categorieen = ['Ontbijt', 'Lunch', 'Diner', 'Snack', 'Dessert']
            for geldige_cat in geldige_categorieen:
                if geldige_cat.lower() in cat.lower():
                    recept['categorie'] = geldige_cat
                    break
            huidige_sectie = None

        elif regel.upper().startswith('TIJD:'):
            tijd_tekst = regel.split(':', 1)[1].strip()
            cijfers = ''.join(c for c in tijd_tekst if c.isdigit())
            if cijfers:
                recept['bereidingstijd'] = int(cijfers)
            huidige_sectie = None

        elif regel.upper().startswith('PERSONEN:'):
            pers_tekst = regel.split(':', 1)[1].strip()
            cijfers = ''.join(c for c in pers_tekst if c.isdigit())
            if cijfers:
                recept['personen'] = int(cijfers)
            huidige_sectie = None

        # === SECTIES ===
        elif regel.upper().startswith('INGREDIENTEN:') or regel.upper().startswith('INGREDIËNTEN:'):
            huidige_sectie = 'ingredienten'

        elif regel.upper().startswith('BEREIDING:'):
            huidige_sectie = 'bereiding'

        elif regel.upper().startswith('TIP:'):
            recept['tip'] = regel.split(':', 1)[1].strip()
            huidige_sectie = 'tip'

        # === SECTIE INHOUD ===
        elif huidige_sectie == 'ingredienten':
            if regel.startswith('-') or regel.startswith('•'):
                ingredienten_lijst.append(regel)
            elif regel and not regel.upper().startswith(('BEREIDING', 'TIP')):
                ingredienten_lijst.append(f"- {regel}")

        elif huidige_sectie == 'bereiding':
            if regel.upper().startswith('TIP:'):
                recept['tip'] = regel.split(':', 1)[1].strip()
                huidige_sectie = 'tip'
            elif regel:
                instructies_lijst.append(regel)

        elif huidige_sectie == 'tip':
            if regel:
                recept['tip'] += ' ' + regel

    # Lijsten samenvoegen tot tekst
    recept['ingredienten'] = '\n'.join(ingredienten_lijst)
    recept['instructies'] = '\n'.join(instructies_lijst)

    return recept


#  BOODSCHAPPENLIJST

def genereer_boodschappenlijst(recept):
    """
    Maakt een boodschappenlijst van een recept.

    Args:
        recept: dict met recept informatie (moet 'ingredienten' key hebben)

    Returns:
        string met boodschappenlijst of None bij fout
    """
    if not recept or 'ingredienten' not in recept:
        return None

    ingredienten_tekst = recept['ingredienten']
    if not ingredienten_tekst.strip():
        return None

    regels = ingredienten_tekst.split('\n')
    boodschappen = []

    for regel in regels:
        regel = regel.strip()
        if regel:
            # Verwijder het streepje/bullet en maak er een checkbox van
            schoon = regel.lstrip('-•').strip()
            if schoon:
                boodschappen.append(f"[ ] {schoon}")

    if not boodschappen:
        return None

    header = f"BOODSCHAPPENLIJST - {recept.get('titel', 'Recept')}\n"
    header += f"   Voor {recept.get('personen', 2)} personen\n"
    header += "=" * 40 + "\n"

    return header + '\n'.join(boodschappen)


#  RECEPT WEERGAVE (voor terminal output)

def formatteer_recept(recept):
    """
    Formatteert een recept dictionary naar mooie terminal output.

    Args:
        recept: dict met recept informatie

    Returns:
        string met geformatteerd recept
    """
    if not recept:
        return "Geen recept beschikbaar."

    lijn = "=" * 50

    output = f"\n{lijn}\n"

    # Easter egg indicator
    if recept.get('is_easter_egg'):
        output += "BUITENAARDS RECEPT GEDETECTEERD\n"
        output += f"{lijn}\n"

    output += f"  {recept.get('titel', 'Onbekend Recept').upper()}\n"
    output += f"{lijn}\n"
    output += f"Categorie:      {recept.get('categorie', 'Onbekend')}\n"
    output += f"Bereidingstijd: {recept.get('bereidingstijd', '?')} minuten\n"
    output += f"Personen:       {recept.get('personen', '?')}\n"

    # Ingrediënten
    output += f"\n{'─' * 50}\n"
    output += "INGREDIENTEN:\n"
    output += f"{'─' * 50}\n"
    ingredienten = recept.get('ingredienten', 'Geen ingredienten')
    output += f"{ingredienten}\n"
    
    # Bereiding
    output += f"\n{'─' * 50}\n"
    output += "BEREIDING:\n"
    output += f"{'─' * 50}\n"
    instructies = recept.get('instructies', 'Geen bereiding')
    output += f"{instructies}\n"

    # Tip
    if recept.get('tip'):
        output += f"\nTIP: {recept['tip']}\n"

    output += f"\n{lijn}\n"

    return output


#  TEST FUNCTIE
def test_ai_verbinding():
    """
    Test of de AI verbinding werkt met een minimale API call.
    Returns: True als verbinding werkt, False anders
    """
    if not check_api_configuratie():
        return False

    try:
        client = maak_ai_client()
        if not client:
            return False

        bericht = client.messages.create(
            model=AI_MODEL,
            max_tokens=50,
            messages=[
                {"role": "user", "content": "Zeg alleen: verbinding OK"}
            ]
        )

        response = bericht.content[0].text
        print(f"AI verbinding werkt. Response: {response.strip()}")
        return True

    except Exception as fout:
        print(f" AI verbinding mislukt: {fout}")
        return False


#  HELPER: INGREDIËNTEN SPLITSEN
def splits_ingredienten(tekst):
    """
    Splitst een komma-gescheiden tekst naar een schone lijst.

    Args:
        tekst: "pasta, tomaat, ui, knoflook"

    Returns:
        ["pasta", "tomaat", "ui", "knoflook"]
    """
    if not tekst or not tekst.strip():
        return []

    items = tekst.split(',')
    schone_lijst = []

    for item in items:
        schoon = item.strip().lower()
        if schoon:
            schone_lijst.append(schoon)

    return schone_lijst


#  DIRECT UITVOEREN (voor snelle test)
if __name__ == "__main__":
    print("=" * 50)
    print("  Kookcompas AI Module - Directe Test")
    print("=" * 50)

    print(f"\nModel: {AI_MODEL}")
    print(f"API Key: {'***' + ANTHROPIC_API_KEY[-6:] if ANTHROPIC_API_KEY and len(ANTHROPIC_API_KEY) > 6 else 'NIET INGESTELD'}")

    print("\n--- Test 1: Verbinding ---")
    if test_ai_verbinding():
        print("\n--- Test 2: Normaal Recept ---")
        recept = genereer_recept(
            ingredienten_lijst=["pasta", "tomaat", "ui", "knoflook"],
            allergenen_lijst=["noten"],
            dieet_lijst=["vegetarisch"]
        )
        if recept:
            print(formatteer_recept(recept))

        print("\n--- Test 3: Easter Egg ---")
        gek_recept = genereer_recept(
            ingredienten_lijst=["bakstenen", "gordijnen", "een stuk zetel"],
            allergenen_lijst=[],
            dieet_lijst=[]
        )
        if gek_recept:
            print(formatteer_recept(gek_recept))
    else:
        print("Kan niet verder testen zonder werkende verbinding.")
