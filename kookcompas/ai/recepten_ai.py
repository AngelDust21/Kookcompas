"""
Kookcompas - AI Recepten Module
===============================
Teamlid 2: AI Developer

Verantwoordelijkheden:
- Claude API integratie
- Prompt engineering voor recepten
- Response parsing
- Error handling voor AI calls
- Boodschappenlijst generatie
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import ANTHROPIC_API_KEY, AI_MODEL, AI_MAX_TOKENS

# Probeer anthropic te importeren
try:
    import anthropic
    ANTHROPIC_BESCHIKBAAR = True
except ImportError:
    ANTHROPIC_BESCHIKBAAR = False
    print("Let op: anthropic library niet gevonden. Installeer met: pip install anthropic")


def check_api_configuratie():
    """
    Controleert of de API correct geconfigureerd is.
    Returns: True als alles in orde is, False anders
    """
    if not ANTHROPIC_BESCHIKBAAR:
        return False

    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY.strip() == '':
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
    except Exception as configuratie_fout:
        print(f"Kon AI client niet aanmaken: {configuratie_fout}")
        return None


def bouw_systeem_prompt():
    """
    Bouwt de systeem prompt voor de AI.
    Returns: Systeem prompt tekst
    """
    return """