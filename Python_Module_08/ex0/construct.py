# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   construct.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/29 10:35:23 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/01 16:19:46 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


from sys import prefix, base_prefix, executable
from os import environ, path
from site import getsitepackages


def in_virtualenv() -> bool:
    return prefix != base_prefix


if __name__ == "__main__":
    print("MATRIX STATUS: ", end="")
    if in_virtualenv() is False:
        print("You're still plugged in")
        print(f"\nCurrent Python: {executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("Welcome to the construct")
        print(f"\nCurrent Python: {executable}")
        venv = environ.get("VIRTUAL_ENV", "")
        env_name = path.basename(venv)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {venv}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")

        for x in getsitepackages():
            if path.basename(x) == "site-packages":
                print(x)
                break
