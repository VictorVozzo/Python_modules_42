# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_archive_creation.py                             :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/16 10:05:15 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/16 10:05:16 by vivozzo-         ###   ########.fr       #
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
        print(f"Error opening file '{file_name}': {e}\n")
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
    new_file_name = input("Enter new file name (or empty): ")
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
            print(f"Error opening file '{new_file_name}': {e}\n")
            return
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
