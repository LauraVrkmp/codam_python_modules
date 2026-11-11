# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/11 09:31:21 by laveerka        #+#    #+#               #
#  Updated: 2026/11/11 11:26:10 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import sys


def check_files(git_ignore: str, example_file: str, environment_file: str) -> None:
    if not os.path.exists(git_ignore):
        print(f"The file {git_ignore} doesn't exist.")
        print(f"Create it and add {environment_file}")
        print("so it excludes the environment file from the repository")
        exit(1)
    elif not os.path.exists(example_file):
        print(f"The file {example_file} doesn't exist.")
        print("Create it and specify the environment variables")
        print("necessary to run this program:")
        print("MATRIX_MODE\nDATABASE_URL\nAPI_KEY\nLOG_LEVEL\nZION_ENDPOINT")
        exit(1)
    elif not os.path.exists(environment_file):
        print(f"The file {environment_file} doesn't exist.")
        print(f"Create it with 'cp {example_file} {environment_file}',")
        print("specify the values for the variables")
        print("or supply them on the command line.")
        exit(1)


def check_environment() -> object:
    if sys.prefix != sys.base_prefix:
        try:
            from dotenv import load_dotenv
            return load_dotenv
        except ImportError:
            print(f"python-dotenv is not installed")
            print("Install it with:")
            print("-   pip install python-dotenv")
            exit(1)
    else:
        print("You're not running a virtual environment.")
        print("Create it with:")
        print("-   python3 -m venv matrix_env")
        print("Activate it with:")
        if "linux" in sys.platform.lower():
            print("   - source matrix_env/bin/activate")
        elif "win" in sys.platform.lower():
            print("   - matrix_env\\Scripts\\activate\n")
        exit(1)

def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    git_ignore = ".gitignore"
    example_file = "env.example"
    environment_file = ".env"
    check_files(git_ignore, example_file, environment_file)
    loaded_dotenv = check_environment()




if __name__ == "__main__":
    main()