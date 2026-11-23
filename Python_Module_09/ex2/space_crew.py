# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   space_crew.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/06 18:13:24 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/07 10:47:20 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing_extensions import Self


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def final_validation(self) -> Self:
        verification_flag = False
        errors = ""

        validation_comm_cap = False
        total_exper_crew = 0
        active_members = 0
        for member in self.crew:
            if (member.rank.value == "commander"
                    or member.rank.value == "captain"):
                validation_comm_cap = True
            if member.years_experience >= 5:
                total_exper_crew += 1
            if member.is_active is True:
                active_members += 1

        if self.mission_id[:1] != "M":
            verification_flag = True
            errors = errors + "\nmission_id must start with 'M'!"
        if validation_comm_cap is False:
            verification_flag = True
            errors = errors + ("\nMission must have at least "
                               "one Commander or Captain!")
        if (self.duration_days > 365 and
                (total_exper_crew / len(self.crew)) < 0.5):
            verification_flag = True
            errors = errors + ("\nLong missions "
                               "(> 365 days) need 50% "
                               "experienced crew (5+ years)!")
        if active_members != len(self.crew):
            verification_flag = True
            errors = errors + "\nAll crew members must be active!"

        if verification_flag is True:
            raise ValueError(errors)
        return self


def main() -> None:
    print("Space Mission Crew Validation")

    sarah_connor = CrewMember(
        member_id="001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=35,
        specialization="Mission Command",
        years_experience=15
    )

    john_smith = CrewMember(
        member_id="002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=45,
        specialization="Navigation",
        years_experience=15
    )

    alice_johnson = CrewMember(
        member_id="003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=28,
        specialization="Engineering",
        years_experience=4
    )

    print("=========================================")
    print("Valid mission created:")

    mission_1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2025-12-24T00:00:00+00:00"),
        duration_days=900,
        crew=[sarah_connor, john_smith, alice_johnson],
        budget_millions=2500.0
    )

    print(f"Mission: {mission_1.mission_name}")
    print(f"ID: {mission_1.mission_id}")
    print(f"Destination: {mission_1.destination}")
    print(f"Duration: {mission_1.duration_days} days")
    print(f"Budget: ${mission_1.budget_millions}M")
    print(f"Crew size: {len(mission_1.crew)}")

    print("Crew members:")
    for member in mission_1.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")

    print("\n=========================================")
    print("Expected validation error:")

    try:
        mission_2 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2025-12-24T00:00:00+00:00"),
            duration_days=900,
            crew=[john_smith, alice_johnson],
            budget_millions=2500.0
        )
        print(mission_2.mission_id)
    except ValidationError as e:
        print((e.errors()[0]['msg']).replace("Value error, \n", ""))


if __name__ == "__main__":
    main()
