# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/16 20:22:28 by laveerka        #+#    #+#               #
#  Updated: 2026/11/20 11:27:20 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable


def bash(target: str, power: int) -> str:
    return f"{target} bashed it's opponent by {power} HP"


def charm(target: str, power: int) -> str:
    return f"{target} charmed the opponent with {power} HP"


def fireball(target: str, power: int) -> str:
    return f"{target} used fireball and inflicted damaged by {power} HP"


def heal(target: str, power: int) -> str:
    return f"{target} used heal and restored {power} HP"


def tackle(target: str, power: int) -> str:
    return f"{target} tackled it's opponent by {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target, power):
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


def valid_power(target: str, power: int) -> bool:
    return power > 0


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    com_result = combined(target="Dragon", power=7)
    print("\nCombined spell result:")
    for com_item in com_result:
        print(f"{com_item}")
    print("\nTesting power amplifier...")
    original_power = tackle("Goblin", 13)
    amplified_spell = power_amplifier(base_spell=tackle, multiplier=3)
    amplified_power = amplified_spell(target="Goblin", power=13)
    print(f"\nOriginal: {original_power}")
    print(f"Amplified: {amplified_power}")
    print("\nTesting conditional caster...")
    caster = conditional_caster(valid_power, charm)
    print(f"\nValid: {caster(target='Wizard', power=50)}")
    print(f"Invalid: {caster(target='Wizard', power=0)}")
    print("\nTesting spell sequence...\n")
    sequence = spell_sequence([bash, heal, tackle])
    sequence_list = sequence(target='Knight', power=14)
    for seq_item in sequence_list:
        print(f"{seq_item}")


if __name__ == "__main__":
    main()
