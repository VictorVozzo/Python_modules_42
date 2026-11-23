# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   decorator_mastery.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/08 19:47:19 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/10 13:51:13 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from collections.abc import Callable
from functools import wraps
from time import sleep, time


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def timer(*args, **kwargs) -> Callable:
        print(f"Casting {func.__name__}")
        start = time()
        result = func(*args, **kwargs)
        finish = time()
        print(f"Spell completed in {(finish - start):.3f} seconds")

        return result

    return timer


def power_validator(min_power: int) -> Callable:

    def func_validator(func: Callable) -> Callable:
        @wraps(func)
        def validator(*args, **kwargs) -> Callable | str:
            power = 0
            flag = False
            if kwargs:
                for key, value in kwargs.items():
                    if key == "power" and isinstance(value, int):
                        power = value
                        flag = True
                        break
            if flag is True:
                if power < min_power:
                    return ("Insufficient power for this spell")
                else:
                    return func(*args, **kwargs)
            else:
                return ("Power not found in the functions arguments, "
                        "please provide power=<int>")
        return validator
    return func_validator


def retry_spell(max_attempts: int) -> Callable:
    def func_retry(func: Callable) -> Callable:
        @wraps(func)
        def retry(*args, **kwargs) -> Callable | str | None:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt is not max_attempts:
                        print("Spell failed, retrying... (attempt "
                              f"{attempt}/{max_attempts})")
            if attempt == max_attempts:
                return f"Spell casting failed after {max_attempts} attempts"
            return None
        return retry
    return func_retry


@spell_timer
def fireball() -> str:
    sleep(3)
    return "Fireball cast!"


@retry_spell(3)
def arrow_rain(guild_name: str) -> None:
    if guild_name == "Archeary":
        print("Arrow rain successfully cast")
    else:
        raise


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and (name.replace(" ", "").isalpha())

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


if __name__ == "__main__":
    try:
        print("Testing spell timer: ")
        print(f"Result: {fireball()}")

        print("\nTesting retrying spell: ")

        print(arrow_rain("Mage"))
        print("Waaaaaaagh spelled !")

        print("\nTesting MageGuild: ")
        first_mage_name = "Wrozor Salos"
        second_mage_name = "3hondi"
        print(f"Testing validate_mage_name with '{first_mage_name}': "
              f"{MageGuild.validate_mage_name(first_mage_name)}")
        print(f"Testing validate_mage_name with '{second_mage_name}': "
              f"{MageGuild.validate_mage_name(second_mage_name)}")

        power_test = [15, 7]
        spells = ["Lightning", "Fireball"]
        guild = MageGuild()
        print(f"\nTesting cast_spell with power = {power_test[0]}: ")
        print(guild.cast_spell(spells[0], power=power_test[0]))
        print(f"Testing cast_spell with power = {power_test[1]}: ")
        print(guild.cast_spell(spells[1], power=power_test[1]))
    except Exception as e:
        print(e)
