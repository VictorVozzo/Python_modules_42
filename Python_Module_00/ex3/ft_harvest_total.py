def ft_harvest_total() -> None:
    Day_1_harvest = int(input("Day 1 harvest: "))
    Day_2_harvest = int(input("Day 2 harvest: "))
    Day_3_harvest = int(input("Day 3 harvest: "))
    total = Day_1_harvest + Day_2_harvest + Day_3_harvest
    print(f"Total harvest: {total}")
