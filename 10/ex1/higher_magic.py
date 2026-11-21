# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/16 20:22:28 by laveerka        #+#    #+#               #
#  Updated: 2026/11/20 23:15:38 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable


def bash(target: str, power: int) -> str:
    return f"{target} bashed it's opponent by {power} HP"


def charm(target: str, power: int) -> str:
    return f"{target} charmed the opponent with {power} HP"


def fireball(target: str, power: int) -> str:
    return f"{target} used fireball and damaged by {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


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
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    com_result = combined(target="Dragon", power=7)
    print(f"Combined spell result: {com_result}")
    print("\nTesting power amplifier...")
    original_power = tackle("Goblin", 13)
    amplified_spell = power_amplifier(base_spell=tackle, multiplier=3)
    amplified_power = amplified_spell("Goblin", 13)
    print(f"Original: {original_power}, Amplified: {amplified_power}")
    print("\nTesting conditional caster...")
    caster = conditional_caster(valid_power, charm)
    print("Valid power:")
    print(f"- {caster('Wizard', 50)}")
    print("Invalid power:")
    print(f"- {caster('Knight', 0)}")
    print("\nTesting spell sequence...")
    sequence = spell_sequence([bash, heal, tackle])
    print(f"{sequence('Unicorn', 14)}")


if __name__ == "__main__":
    main()
