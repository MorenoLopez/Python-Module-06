#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   __init__.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 08:36:51 by horarivo            #+#    #+#            #
#   Updated: 2026/07/24 16:31:56 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from alchemy.elements import create_air
from alchemy.potions import healing_potion, strength_potion
from alchemy.transmutation.recipes import lead_to_gold

heal = healing_potion

__all__ = ["create_air", "strength_potion", "heal", "lead_to_gold"]
