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
    temp = int(temperature)
    if temp >= 0 and temp <= 40:
        return temp
    elif temp > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")


def test_temperature(input_temp: str) -> None:
    print(f"Input data is '{input_temp}'")
    try:
        temperature = input_temperature(input_temp)
        print(f"Temperature is now {temperature}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    print("\n")
    test_temperature("abc")
    print("\n")
    test_temperature("100")
    print("\n")
    test_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
