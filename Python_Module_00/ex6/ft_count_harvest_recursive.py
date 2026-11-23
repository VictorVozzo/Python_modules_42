def print_days(total_days, days) -> None:
    print(f"Day {days}")
    if days == total_days:
        return
    days = days + 1
    print_days(total_days, days)


def ft_count_harvest_recursive() -> None:
    total_days = int(input("Days until harvest: "))
    days = 1
    print_days(total_days, days)
    print("Harvest time!")
