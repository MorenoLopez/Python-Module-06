#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 08:37:48 by horarivo            #+#    #+#            #
#   Updated: 2026/07/24 17:33:25 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from alchemy.grimoire import light_spell_record

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(
    f"Testing record light spell: "
    f"{light_spell_record('Fantasy', 'Earth, wind and fire')}"
)
