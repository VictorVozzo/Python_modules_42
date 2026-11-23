# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_vault_security.py                               :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/16 11:54:40 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/16 15:14:19 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

def secure_archive(file_name: str, action: str,
                   content: str = "") -> tuple[bool, str]:
    if action == "r":
        try:
            with open(file_name, action) as f:
                file = f.read()
            return (True, file)
        except Exception as e:
            return (False, str(e))
    elif action == "w":
        try:
            with open(file_name, action) as f:
                file = f.write(content)
            return (True, content)
        except Exception as e:
            return (False, str(e))
    else:
        return (False, "Invalid action. Use 'r' (read) or 'w' (write).")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("testeinac.txt", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("teste.txt", "r"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("teste.txt", "w", "We did it!"))

    print("\nUsing 'secure_archive' to read from the previous file:")
    print(secure_archive("teste.txt", "r"))
