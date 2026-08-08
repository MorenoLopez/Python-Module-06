#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 08:38:54 by horarivo            #+#    #+#            #
#   Updated: 2026/07/24 08:38:55 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


LIGHT_ALLOWED: list[str] = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    lower = ingredients.lower()
    for allowed in LIGHT_ALLOWED:
        if allowed in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
