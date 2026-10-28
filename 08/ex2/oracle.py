# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 18:19:50 by laveerka        #+#    #+#               #
#  Updated: 2026/10/26 18:24:02 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import sys
from types import ModuleType
from importlib import import_module
from importlib.metadata import version, PackageNotFoundError


def read_file(file_name: str) -> list[str] | None:
    try:
        with open (file_name, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"The file {file_name} cannot be found")
        return None
    except OSError as e:
        print(f"The file {file_name} could not be read: {e}")
        return None


def check_requirements() -> dict[str, str | None]:
    requirements: dict[str, str | None] = {}
    file = "requirements.txt"
    lines = read_file(file)
    if lines:
        for line in lines:
            print(f"Line: {line}")
            line = line.strip()
            if ">=" in line:
                package, required_version = line.split(">=", 1)
                requirements[package.strip()] = required_version.strip()
            else:
                requirements[line.strip()] = None
    return requirements


def compare_versions(required_version: str, installed_version: str) -> bool:
    required = tuple(map(int, required_version.split(".")))
    clean = tuple(map(int, installed_version.split(".")))
    length = max(len(required), len(clean))
    required = required + (0,) * (length - len(required))
    clean = clean + (0,) * (length - len(clean))
    return clean >= required


def build_version_string(version_info: str | None) -> str | None:
    version_string  = ""
    digit = False
    dot = False
    if version_info:
        for char in version_info:
            if char.isdigit() and not dot:
                digit = True
                version_string +=  char
            elif char.isdigit() and dot:
                digit = True
                dot = False
                version_string += "." + char
            elif char == "." and digit:
                dot = True
                digit = False
            else:
                if digit or dot:
                    break
        if len(version_string) > 0:
            return version_string
    return None


def check_dependencies(required: dict[str, str | None]) -> list[tuple[str, str]]:
    present: list[tuple[str, str]] = []
    missing: list[tuple[str, str | None]] = []
    wrong_version: list[tuple[str, str, str | None]] = []
    missing_count = 0
    version_count = 0
    for package, required_version in required.items():
        try:
            installed_version = version(package)
            clean_installed = build_version_string(installed_version)
        except PackageNotFoundError:
            missing_count += 1
            missing.append((package, required_version))
            continue
        if required_version and clean_installed:
            if compare_versions(required_version, clean_installed):
                present.append((package, clean_installed))
            else:
                version_count += 1
                wrong_version.append((package, required_version, clean_installed))
        elif clean_installed:
            present.append((package, clean_installed))
    if missing:
        if missing_count == 1:
            print(f"\nYou have {missing_count} missing dependency.")
        elif missing_count > 1:
            print(f"\nYou have {missing_count} missing dependendies.")
        for package, required_version in missing:
            if required_version:
                print(f"- {package} version {required_version} is missing")
            else:
                print(f"- {package} is missing, no required version is specified")
    if wrong_version:
        if version_count == 1:
            print(f"\nYou have {version_count} dependency which version is inadequate.")
        elif version_count > 1:
            print(f"\nYou have {version_count} dependencies which version is inadequate. ")
        for package, required_version, installed in wrong_version:
            print(f"- {package} has version {installed} installed, whereas it needs version {required_version}")
    if missing or wrong_version:
        print("\nTo satisfy the dependency requirements")
        print("- install with pip:      python -m pip install -r requirements.txt")
        print("- run like so:           python loading.py")
        sys.exit(1)
    return present


def import_modules(packages: list[tuple[str, str]]) -> dict[str, ModuleType]:
    imported: dict[str, ModuleType] = {}
    for package, installed in packages:
        try:
            if package == "python-dotenv":
                package = "dotenv"
            module = import_module(package)
            imported[package] = module
        except ImportError:
            print(f"Unable to import dependency {package} of version {installed}")
    if len(packages) != len(imported):
        print("\nMake sure to install all dependencies with pip")
        sys.exit(1)
    return imported


def check_files(example_file: str, env_file: str, git_ignore: str) -> None:
    if not os.path.exists(example_file):
        print(f"The file {example_file} doesn't exist")
        print("Please create this file with the environmenal")
        print("variables necessary to run this program")
        sys.exit(1)
    elif not os.path.exists(env_file):
        print(f"The file {env_file} doesn't exist")
        print(f"Create it with: cp {example_file} {env_file}")
        print("and populate the file with values for the environment")
        print("variables required to run this program")
        exit(1)
    elif not os.path.exists(git_ignore):
        print(f"The file {git_ignore} doesn't exist")
        print(f"Create it and specify {env_file} is excluded from Git")
        exit(1)


def read_format(example_file: str) -> list[str] | None:
    file = read_file(example_file)
    if file:
        errors: list[str] = []
        variables: list[tuple[str, int]] = []
        for line_number, line in enumerate(file):
            add_line = True
            if not line.strip():
                continue
            if not line.endswith("="):
                errors.append(f"Line {line_number} must end with an equal sign")
                add_line = False
                name = line
            else:
                name = line[:-1]
            words = name.split("_")
            if any(not word for word in words):
                errors.append(f"Line {line_number} is incorrectly  split by underscores")
                add_line = False
            if any(not word.isascii() or not word.isalpha() or not word.isupper() for word in words):
                errors.append(f"Line {line_number} contains invalid characters")
                add_line = False
            existing = next(((entry_name, entry_line) for entry_name, entry_line in
                variables if entry_name == name),
                None
                )
            if existing is not None:
                errors.append(f"Line {line_number} is a duplicate variable of line {existing[1]}")
                add_line = False
            if add_line:
                variables.append((name, line_number))
        if not variables:
            raise ValueError(
                f"The file {example_file} does not contain valid variables"
            )
        else:
            if errors:
                raise ValueError(
                    "Invalid .env.example file" + "\n- ".join(errors)
                )
            format: list[str] = []
            for name, line_number in variables:
                format.append(name)
            if not format:
                return None
            return format
    else:
        return None


# def load_config(required: list[str]) -> dict[str, str]:
#     load_dotenv()
#     configuration = {
#         name: os.environ.get(name, "")
#         for name in required
#     }



def main() -> None:
    requirements: dict[str, str | None] = check_requirements()
    print(f"Requirements: {requirements}")
    present = check_dependencies(requirements)
    print(f"Present dependancies: {present}")
    imported = import_modules(present)
    print(f"Imported dependencies: {imported}")
    dotenv = imported["dotenv"]
    example_file = ".env.example"
    env_file = ".env"
    git_ignore = ".gitignore"
    check_files(example_file, env_file, git_ignore)
    try:
        config_format = read_format(example_file)
    except ValueError as e:
        print(e)
    print("here")
    required = (
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    )
    configuration = load_config(required)


if __name__ == "__main__":
    main()