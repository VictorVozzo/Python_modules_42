# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   lambda_spells.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/07 14:15:31 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/10 11:26:27 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    artifacts = sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    mages = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return mages


def spell_transformer(spells: list[str]) -> list[str]:
    spells = list(map(lambda spell: "*" + spell + "*", spells))
    return spells


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])
    min_power = min(mages, key=lambda mage: mage["power"])
    sum_power = 0
    for mage in mages:
        sum_power += mage["power"]
    avg_power = round(sum_power / len(mages), 2)
    return ({"max_power": max_power["power"],
             "min_power": min_power["power"],
             "avg_power": avg_power})


if __name__ == "__main__":
    try:
        artifacts = [{'name': 'Lightning Rod', 'power': 76, 'type': 'weapon'},
                     {'name': 'Storm Crown', 'power': 95, 'type': 'accessory'},
                     {'name': 'Ice Wand', 'power': 97, 'type': 'armor'},
                     {'name': 'Ice Shield', 'power': 75, 'type': 'accessory'}]
        mages = [{'name': 'Nova', 'power': 56, 'element': 'shadow'},
                 {'name': 'Sage', 'power': 75, 'element': 'light'},
                 {'name': 'Alex', 'power': 84, 'element': 'light'},
                 {'name': 'Jordan', 'power': 61, 'element': 'earth'},
                 {'name': 'Storm', 'power': 78, 'element': 'water'}]
        spells = ['freeze', 'tsunami', 'flash', 'tornado']

        print("Testing artifact sorter:")

        print("\nArtifacts list: ", artifacts)

        print("\nSorted artifacts list: ", artifact_sorter(artifacts))

        min_power = 62
        print(f"\n\nTesting power filter with min_power = {min_power}:")

        print("\nMages list: ", mages)

        print("\nMages list with filter: ", power_filter(mages, 62))

        print("\n\nTesting spell transformer:")

        print("\nList of spells: ", spells)

        print("\nList of spells transformed: ", spell_transformer(spells))

        print("\n\nTesting mage stats: ")

        print("\n", mage_stats(mages))
    except Exception as e:
        print(e)
