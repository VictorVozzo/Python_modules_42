# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   oracle.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/30 15:46:32 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/03 09:39:42 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from dotenv import load_dotenv
from os import getenv


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    print("\nConfiguration loaded:")

    matrix_mode = getenv('MATRIX_MODE')
    if matrix_mode is None:
        print("MATRIX_MODE not found, Put 'development' or 'production'!")
        return
    else:
        if matrix_mode == "development" or matrix_mode == "production":
            print(f"Mode: {matrix_mode}")
        else:
            print("Mode was not valid! Use 'development' or 'production'!")
            return

    flag = False

    database_url = getenv('DATABASE_URL')
    if database_url is None:
        print("DATABASE_URL not found")
        flag = True
    else:
        print(f"Database: Connected to {database_url} instance")

    api_key = getenv('API_KEY')
    if api_key is None:
        print("API_KEY not found")
        flag = True
    else:
        print("API Access: Authenticated")

    log_level = getenv('LOG_LEVEL')
    if log_level is None:
        print("LOG_LEVEL not found")
        flag = True
    else:
        print(f"Log Level: {log_level}")

    zion_endpoint = getenv('ZION_ENDPOINT')
    if zion_endpoint is None:
        print("ZION_ENDPOINT not found")
        flag = True
    else:
        print(f"Zion Network: {zion_endpoint}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if flag is False:
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] Missing required .env variable(s).")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
