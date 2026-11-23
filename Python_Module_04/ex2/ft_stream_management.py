# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_stream_management.py                            :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/16 18:13:37 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/16 18:13:38 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    number_args = len(sys.argv)
    if (number_args == 1):
        print("Usage: ft_ancient_text.py <file>\n")
        return
    file_name = sys.argv[1]

    print(f"Accessing file '{file_name}'")
    f = None
    try:
        f = open(file_name)
        print("---\n")
        content = f.read()
        print(content)
        print("---")
    except Exception as e:
        print("[STDERR] Error opening file "
              f"'{file_name}': {e}\n", file=sys.stderr)
        if f is not None:
            f.close()
        return
    if f is not None:
        f.close()
        print(f"File '{file_name}' closed.")

    print("\nTransform data:")
    print("---\n")
    content_list = content.splitlines()
    i = 0
    for line in content_list:
        content_list[i] = line + "#\n"
        print(content_list[i], end="")
        i += 1

    print("\n---")
    print("Enter new file name (or empty): ", end="", flush=True)
    new_file_name = sys.stdin.readline().strip()
    if new_file_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file_name}'")
        f = None
        try:
            f = open(new_file_name, "w")
            for line in content_list:
                f.write(line)
            print(f"Data saved in file '{new_file_name}'.\n")
        except Exception as e:
            print("[STDERR] Error opening file "
                  f"'{new_file_name}': {e}\n", file=sys.stderr)
            return
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
