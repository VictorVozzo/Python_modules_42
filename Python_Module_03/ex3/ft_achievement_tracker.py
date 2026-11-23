# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_achievement_tracker.py                          :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/15 14:32:15 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/15 14:32:18 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import random


def gen_player_achievements() -> set[str]:
    all_achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                        'Speed Runner', 'Survivor',
                        'Master Explorer', 'Treasure Hunter',
                        'Unstoppable', 'First Steps', 'Collector Supreme',
                        'Untouchable', 'Sharp Mind', 'Boss Slayer']
    number_achievements = random.randint(1, len(all_achievements))
    player_achievements = []

    i = 1
    while (i <= number_achievements):
        achievement = random.choice(all_achievements)
        player_achievements.append(achievement)
        i += 1

    return set(player_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_achievements}")

    intersection_achievements = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {intersection_achievements}")

    player_alice_only = alice.difference(bob, charlie, dylan)
    player_bob_only = bob.difference(alice, charlie, dylan)
    player_charlie_only = charlie.difference(alice, bob, dylan)
    player_dylan_only = dylan.difference(alice, bob, charlie)
    print(f"\nOnly Alice has: {player_alice_only}")
    print(f"Only Bob has: {player_bob_only}")
    print(f"Only Charlie has: {player_charlie_only}")
    print(f"Only Dylan has: {player_dylan_only}")

    intersection_without_alice = bob.union(charlie, dylan)
    alice_missing_achiev = intersection_without_alice.difference(alice)
    print(f"\nAlice is missing: {alice_missing_achiev}")

    intersection_without_bob = alice.union(charlie, dylan)
    bob_missing_achiev = intersection_without_bob.difference(bob)
    print(f"Bob is missing: {bob_missing_achiev}")

    intersection_without_charlie = alice.union(bob, dylan)
    charlie_missing_achiev = intersection_without_charlie.difference(charlie)
    print(f"Charlie is missing: {charlie_missing_achiev}")

    intersection_without_dylan = alice.union(bob, charlie)
    dylan_missing_achiev = intersection_without_dylan.difference(dylan)
    print(f"Dylan is missing: {dylan_missing_achiev}")


if __name__ == "__main__":
    main()
