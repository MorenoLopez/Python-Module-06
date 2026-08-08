#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 08:39:05 by horarivo            #+#    #+#            #
#   Updated: 2026/07/24 08:39:06 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from alchemy.elements import create_air, create_fire
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}'"
        f" mixed with '{create_fire()}'"
    )
