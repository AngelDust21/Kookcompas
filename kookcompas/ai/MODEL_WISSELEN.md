# Model Wisselen - Handleiding

## Hoe werkt het

Op de Anthropic website (console.anthropic.com) kun je ALLEEN:
- API keys aanmaken en beheren
- Gebruik en kosten bekijken
- Credits toevoegen

Het model kiezen doe je NIET op de website maar IN DE CODE. Bij elke API call geef je mee welk model je wilt gebruiken. Dit betekent dat je met dezelfde API key alle modellen kunt gebruiken.

---

## Model Wijzigen

### Stap 1: Open config.py

Het bestand `config.py` in de hoofdmap van kookcompas.

### Stap 2: Zoek de AI_MODEL regel

```python
AI_MODEL = "claude-sonnet-4-20250514"
```

### Stap 3: Vervang door gewenst model

Verander de waarde naar een ander model (zie lijst hieronder).

### Stap 4: Opslaan en testen

Sla het bestand op en test met:
```bash
python -c "from ai.recepten_ai import test_ai_verbinding; test_ai_verbinding()"
```

---

## Beschikbare Modellen

### Claude Sonnet 4 (Huidig)
```python
AI_MODEL = "claude-sonnet-4-20250514"
```
- Balans tussen kwaliteit en snelheid
- Goed voor de meeste taken
- Gemiddelde kosten

### Claude Haiku 3.5 (Snelste)
```python
AI_MODEL = "claude-3-5-haiku-20241022"
```
- Snelste model
- Laagste kosten
- Iets minder creatief
- Prima voor simpele recepten

### Claude Haiku 3 (Oudere versie, goedkoopste)
```python
AI_MODEL = "claude-3-haiku-20240307"
```
- Zeer snel
- Zeer goedkoop
- Basis kwaliteit
- Goed voor testen

### Claude Sonnet 3.5 (Vorige generatie)
```python
AI_MODEL = "claude-3-5-sonnet-20241022"
```
- Goede kwaliteit
- Gemiddelde snelheid
- Gemiddelde kosten

### Claude Opus 4 (Beste kwaliteit)
```python
AI_MODEL = "claude-opus-4-20250514"
```
- Hoogste kwaliteit
- Meest creatief
- Traagste
- Duurste (gebruik met mate)

---

## Vergelijking

Model               | Snelheid | Kwaliteit | Kosten
--------------------|----------|-----------|--------
Haiku 3             | Snel     | Basis     | Laag
Haiku 3.5           | Snel     | Goed      | Laag
Sonnet 3.5          | Gemiddeld| Goed      | Gemiddeld
Sonnet 4 (huidig)   | Gemiddeld| Hoog      | Gemiddeld
Opus 4              | Traag    | Excellent | Hoog

---

## Aanbevelingen voor Kookcompas

**Voor dagelijks gebruik:**
- Claude Sonnet 4 (huidig) - beste balans

**Voor veel recepten genereren (budget):**
- Claude Haiku 3.5 - snel en goedkoop

**Voor speciale gelegenheden (kwaliteit):**
- Claude Opus 4 - meest creatieve recepten

**Voor testen tijdens ontwikkeling:**
- Claude Haiku 3 - goedkoopst

---

## Voorbeeld: Wisselen naar Haiku

1. Open `config.py`

2. Verander:
```python
AI_MODEL = "claude-sonnet-4-20250514"
```

   Naar:
```python
AI_MODEL = "claude-3-5-haiku-20241022"
```

3. Sla op

4. Start de app opnieuw

---

## Max Tokens Aanpassen

Je kunt ook de maximale lengte van het antwoord aanpassen in `config.py`:

```python
AI_MAX_TOKENS = 1024  # Standaard
```

- Meer tokens = langere recepten mogelijk
- Meer tokens = hogere kosten
- Voor recepten is 1024 meestal voldoende
- Maximum verschilt per model (meestal 4096 of 8192)

---

## Kosten Indicatie

Kosten zijn per 1 miljoen tokens (input + output):

- Haiku 3: ongeveer 0.25 - 1.25 dollar
- Haiku 3.5: ongeveer 0.80 - 4.00 dollar
- Sonnet 3.5/4: ongeveer 3.00 - 15.00 dollar
- Opus 4: ongeveer 15.00 - 75.00 dollar

Voor kookcompas (korte prompts, korte antwoorden) zijn de kosten minimaal. Je kunt honderden recepten genereren voor minder dan een euro met Haiku.

---

## Problemen

### "Model not found" fout
- Controleer of de model naam exact klopt
- Kopieer de model naam uit dit document

### "Rate limit" fout
- Te veel requests in korte tijd
- Wacht even en probeer opnieuw
- Haiku heeft hogere rate limits

### Slechte recepten
- Probeer een krachtiger model (Sonnet of Opus)
- Geef meer ingredienten als input

---

## Snel Wisselen Tip

Je kunt meerdere modellen klaarzetten in config.py:

```python
# Kies een model door commentaar te verwijderen

# Budget optie (snel en goedkoop)
# AI_MODEL = "claude-3-5-haiku-20241022"

# Standaard optie (balans)
AI_MODEL = "claude-sonnet-4-20250514"

# Premium optie (beste kwaliteit)
# AI_MODEL = "claude-opus-4-20250514"
```

Dan hoef je alleen de # te verplaatsen om te wisselen.
