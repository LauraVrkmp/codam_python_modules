# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/16 20:23:29 by laveerka        #+#    #+#               #
#  Updated: 2026/11/21 02:11:29 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import time
from typing import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and hasattr(args[0], "__dict__"):
                power = args[2]
            else:
                power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < max_attempts:
                        print(f"Spell failed, retrying... (attempt "
                              f"{i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 2 and all(char.isalpha() or
                                 char == " " for char in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def flood_wave() -> str:
    time.sleep(0.23)
    return "A flood wave damaged your player!"


@power_validator(25)
def fire_blast(power: int) -> str:
    return f"A fire blast was cast with power {power}"


@retry_spell(4)
def wind_surge() -> str:
    import random
    if random.random() < 0.8:
        raise ValueError
    return "Wind surge sent to opponent!"


def main() -> None:
    print("Testing spell timer...\n")
    print(flood_wave())
    print("\nTesting power validator...\n")
    print(fire_blast(100))
    print(fire_blast(50))
    print(fire_blast(20))
    print("\nTesting retrying spell...\n")
    print(wind_surge())
    print("\nTesting MageGuild...\n")
    valid_name = "Gabe Syn"
    invalid_name = "Gabe$%!"
    mage = MageGuild()
    print(f"The name {valid_name} is valid: "
          f"{mage.validate_mage_name(valid_name)}")
    print(f"The name {invalid_name} is valid: "
          f"{mage.validate_mage_name(invalid_name)}")
    print(mage.cast_spell("Thunder wind", 20))
    print(mage.cast_spell("Blast storm", 40))
    print(mage.cast_spell("Wrecking power", 5))


if __name__ == "__main__":
    main()
