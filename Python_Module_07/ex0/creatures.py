# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   creatures.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/25 11:50:16 by vivozzo-           #+#    #+#             #
#   Updated: 2026/06/27 14:38:05 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class Creature(ABC):
    name: str
    type: str

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):

    def __init__(self) -> None:
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = "Torragon"
        self.type = "Water"

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")
