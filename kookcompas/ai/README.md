# AI Module

## Overzicht

Deze module verzorgt de integratie met Claude AI (Anthropic) voor het genereren van recepten.

## Bestanden

- **recepten_ai.py**: Alle AI functionaliteit

## Configuratie

### API Key Verkrijgen

1. Ga naar console.anthropic.com
2. Maak een account aan (gratis)
3. Ga naar "API Keys"
4. Klik "Create Key"
5. Kopieer de key (begint met sk-ant-)

### API Key Instellen

Vul de key in het .env bestand:
```
ANTHROPIC_API_KEY=sk-ant-jouw-key-hier
```

## Technische Details

### Model

- **Model**: Claude Sonnet 4 (claude-sonnet-4-20250514)
- **Max tokens**: 1024
- **Kosten**: Laag (enkele euro per 1000 recepten)

### Prompt Structuur

**Systeem prompt**: Definieert de rol als chef-kok

**Gebruiker prompt**: Bevat:
- Beschikbare ingredienten
- Te vermijden allergenen
- Dieetwensen
- Gewenst output formaat

### Response Parsing

De AI response wordt geparsed naar een dictionary:
```python
{
    'titel': 'Pasta Pomodoro',
    'categorie': 'Diner',
    'bereidingstijd': 25,
    'personen': 2,
    'ingredienten': '- 250g pasta\n- 4 tomaten\n...',
    'instructies': '1. Kook de pasta\n2. ...'
}
```

## Gebruik

```python
from ai.recepten_ai import genereer_recept, check_api_configuratie

# Check of API werkt
if check_api_configuratie():
    recept = genereer_recept(
        ingredienten_lijst=['pasta', 'tomaat', 'ui'],
        allergenen_lijst=['noten', 'lactose'],
        dieet_lijst=['vegetarisch']
    )
    print(recept['titel'])
```

## Foutafhandeling

De module handelt deze fouten af:
- **APIConnectionError**: Geen internet
- **RateLimitError**: Te veel requests
- **APIStatusError**: Ongeldige API key of andere API fout
- **Parsing fouten**: Fallback waarden worden gebruikt

## Extra Functies

- **genereer_boodschappenlijst(recept)**: Maakt een boodschappenlijst van een recept
- **test_ai_verbinding()**: Test of de API werkt

## Tips

- Begin met simpele ingredienten voor betere resultaten
- Meer ingredienten geeft een creatiever recept
- De AI houdt altijd rekening met allergenen
