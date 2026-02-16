# AI Module - De Hersenen van Kookcompas
#
# Dit bestand werkt als een soort receptioniste voor de 'ai' map.
# Het zorgt ervoor dat je de belangrijke functies direct kunt aanroepen
# via 'from ai import ...', zonder dat je in submappen hoeft te graven.
#
# Hier bepalen we wat er "in de etalage" staat voor de rest van de app.

from ai.recepten_ai import (
    genereer_recept,           # De chef-kok
    genereer_boodschappenlijst, # Het boodschappenlijstje
    check_api_configuratie,    # Even checken of de sleutel werkt
    test_ai_verbinding,        # Hallo, ben je daar?
    splits_ingredienten,       # Hakwerk
    formatteer_recept          # Mooi opdienen
)

# WAAROM __all__?
# Zonder dit lijstje denkt je code-editor (zoals VS Code) dat de imports hierboven
# "dode code" zijn, omdat we ze niet *in dit bestand zelf* gebruiken.
#
# Door __all__ toe te voegen, zeggen we: "Nee, dit is de bedoeling! 
# Wij zijn de doorgeefluik voor deze functies."
#
# Dus: De code werkte altijd al (was niet dood), maar nu snapt de editor dat ook 
# en zijn de waarschuwingen (gele golfjes) weg.
__all__ = [
    "genereer_recept",
    "genereer_boodschappenlijst",
    "check_api_configuratie",
    "test_ai_verbinding",
    "splits_ingredienten",
    "formatteer_recept"
]
