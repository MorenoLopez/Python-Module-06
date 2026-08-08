#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_validator.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 08:38:41 by horarivo            #+#    #+#            #
#   Updated: 2026/07/24 08:38:43 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower = ingredients.lower()
    for item in allowed:
        if item in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
