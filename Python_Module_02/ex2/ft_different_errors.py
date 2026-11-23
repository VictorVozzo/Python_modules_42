# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_first_exception.py                              :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/08 14:05:22 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/08 14:05:25 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

def garden_operations(operation_number: int) -> None:
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            1 / 0
        elif operation_number == 2:
            open('/non/existent/file')
        elif operation_number == 3:
            "2" + 2
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5, 1):
        print(f"Testing operation {i}...")
        garden_operations(i)
    print("Operation completed successfully")
    print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
