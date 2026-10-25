# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 18:18:29 by laveerka        #+#    #+#               #
#  Updated: 2026/10/22 14:57:29 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
import site


def virtual() -> None:
    """Function to print information on the virtual environment"""
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(f"{site.getsitepackages()[0]}")

    

def non_virtual() -> None:
    """Function to print information on the system"""
    print("\nMATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def main() -> None:
    if sys.prefix != sys.base_prefix:
        virtual()
    else:
        non_virtual()


if __name__ == "__main__":
    main()
