#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_1.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 08:37:54 by horarivo            #+#    #+#            #
#   Updated: 2026/07/24 18:28:29 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402

print(f"Testing dark spell: {dark_spell_record('Darkness', 'bats and frogs')}")
