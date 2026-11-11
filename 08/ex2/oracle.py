# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/11 09:31:21 by laveerka        #+#    #+#               #
#  Updated: 2026/11/11 15:33:27 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import sys


def check_files(git_ignore: str, example_file: str, environment_file: str) -> None:
    if not os.path.exists(git_ignore):
        print(f"The file {git_ignore} doesn't exist.")
        print(f"Create it and add {environment_file}")
        print("so it excludes the environment file from the repository")
        sys.exit(1)
    elif not os.path.exists(example_file):
        print(f"The file {example_file} doesn't exist.")
        print("Create it and specify the environment variables")
        print("necessary to run this program:")
        print("\nMATRIX_MODE\nDATABASE_URL\nAPI_KEY\nLOG_LEVEL\nZION_ENDPOINT")
        sys.exit(1)
    elif not os.path.exists(environment_file):
        print(f"The file {environment_file} doesn't exist.")
        print(f"Create it with 'cp {example_file} {environment_file}',")
        print("specify the values for the variables")
        print("or supply them on the command line.")
        sys.exit(1)


def load_environment() -> object:
    if sys.prefix != sys.base_prefix:
        try:
            from dotenv import load_dotenv  # type: ignore
            load_dotenv(override=False)
        except ImportError:
            print(f"python-dotenv is not installed")
            print("Install it with:")
            print("-   pip install python-dotenv")
            sys.exit(1)
    else:
        print("You're not running a virtual environment.")
        print("Create it with:")
        print(" - python3 -m venv matrix_env")
        print("Activate it with:")
        if "linux" in sys.platform.lower():
            print(" - source matrix_env/bin/activate")
        elif "win" in sys.platform.lower():
            print(" - matrix_env\\Scripts\\activate\n")
        sys.exit(1)


def mode_config(mode: str | None) -> bool:
    valid = False
    if mode is None:
        print("Mode is not defined")
    elif mode == "":
        print("Mode is defined but empty")
    elif mode.lower() == "development" or mode.lower() == "production":
        valid = True
        print(f"Mode : {mode}")
    else:
        print("Mode has an invalid value")
    return valid


def url_config(url: str | None) -> bool:
    valid = False
    if url is None:
        print("Database is not defined")
    elif url == "":
        print("Database is defined but empty")
    elif url.lower() == "local" or url.lower() == "remote":
        valid = True
        print(f"Database: Connected to {url} instance")
    else:
        print("Database has an invalid value")
    return valid


def api_config(api: str | None) -> bool:
    valid = False
    if api is None:
        print("API key is not defined")
    elif api == "":
        print("API key is defined but empty")
    elif "provide" in api:
        print("No API key specified")
    else:
        valid = True
        print("API Access: Authenticated")
    return valid


def log_config(log: str | None) -> bool:
    valid = False
    if log is None:
        print("Log level is not defined")
    elif log == "":
        print("Log level is defined but empty")
    elif log == "INFORMATION" or log == "DEBUG" or log == "WARNING":
        valid = True
        print(f"Log Level: {log}")
    else:
        print("Log Level has an invalid value")
    return valid


def endpoint_config(endpoint: str | None) -> bool:
    valid = False
    if endpoint is None:
        print("Zion Network Endpoint is not defined")
    elif endpoint == "":
        print("Zion Network Endpoint is defined but empty")
    elif endpoint.lower() == "online" or endpoint.lower() == "offline":
        valid = True
        print(f"Zion Network: {endpoint}")
    else:
        print("Zion Network Endpoint has an invalid value")
    return valid


def print_configuration() -> list[str]:
    print("Configuration loaded:")
    MODE = os.getenv("MATRIX_MODE")
    valid_mode = mode_config(MODE)
    URL = os.getenv("DATABARE_URL")
    valid_url = url_config(URL)
    API = os.getenv("API_KEY")
    valid_api = api_config(API)
    LOG = os.getenv("LOG_LEVEL")
    valid_log = log_config(LOG)
    ENDPOINT = os.getenv("ZION_ENDPOINT")
    valid_end = endpoint_config(ENDPOINT)
    if valid_mode and valid_url and valid_api and valid_log and valid_end:
        valid_conf = "True"
    else:
        valid_conf = "False"
    return 


def security_check(MODE: str | None, URL: str | None, API: str | None, LOG: str | None, ENDPOINT: str | None, valid_conf: str):
    print("\nEnvironment security check:")
    if API and "secret" in API:
        print("[ERROR] Hardcoded secret detected")
    else:
        print("[OK] No hardcoded secrets detected")
    if not valid_conf:
        print("[ERROR] .env file not properly configured")
    else:
        print("[OK] .env file properly configured")
    if 



def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    git_ignore = ".gitignore"
    example_file = ".env.example"
    environment_file = ".env"
    check_files(git_ignore, example_file, environment_file)
    load_environment()
    MODE, URL, API, LOG, ENDPOINT, valid_conf = print_configuration()
    security_check(MODE, URL, API, LOG, ENDPOINT, valid_conf)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()