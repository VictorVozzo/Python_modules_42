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

def input_temperature(temperature: str) -> int:
    return int(temperature)


def test_temperature(input_temp: str) -> None:
    print(f"Input data is '{input_temp}'")
    try:
        temperature = input_temperature(input_temp)
        print(f"Temperature is now {temperature}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print("\n")
    test_temperature("abc")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
