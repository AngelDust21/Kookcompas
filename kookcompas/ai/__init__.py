# AI Module - De Hersenen van Kookcompas
#
# Dit bestand werkt als een soort receptioniste voor de 'ai' map.
# Het zorgt ervoor dat je de belangrijke functies direct kunt aanroepen
# via 'from ai import ........', zonder dat je in submappen hoeft te graven.
#
# Hier bepalen we wat er "in de etalage" staat voor de rest van de app.

from ai.recepten_ai import (genereer_recept, genereer_boodschappenlijst, check_api_configuratie, test_ai_verbinding, splits_ingredienten, formatteer_recept)
