#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 08:37:00 by horarivo            #+#    #+#            #
#   Updated: 2026/07/24 08:37:01 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from alchemy.elements import create_earth, create_air
from alchemy.elements import create_fire, create_water


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}'"
        f" and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{create_fire()}'"
        f" and '{create_water()}'"
    )
