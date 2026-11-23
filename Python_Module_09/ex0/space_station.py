# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   space_station.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/03 15:14:52 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/07 10:00:41 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    space_station_1 = SpaceStation(station_id="ISS001",
                                   name="International Space Station",
                                   crew_size=6,
                                   power_level=85.5,
                                   oxygen_level=92.3,
                                   last_maintenance=datetime.fromisoformat(
                                       "2025-12-24T00:00:00+00:00")
                                   )

    print(f"ID: {space_station_1.station_id}")
    print(f"Name: {space_station_1.name}")
    print(f"Crew: {space_station_1.crew_size} people")
    print(f"Power: {space_station_1.power_level}%")
    print(f"Oxygen: {space_station_1.oxygen_level}%")
    if space_station_1.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not operational")

    print("\n========================================")
    print("Expected validation error:")
    try:
        space_station_2 = SpaceStation(station_id="ISS001",
                                       name="International Space Station",
                                       crew_size=50,
                                       power_level=85.5,
                                       oxygen_level=92.3,
                                       last_maintenance=datetime.fromisoformat(
                                           "2025-12-24T00:00:00+00:00")
                                       )
        print(space_station_2.crew_size)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
