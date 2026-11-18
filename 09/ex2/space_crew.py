# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_crew.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/12 14:51:46 by laveerka        #+#    #+#               #
#  Updated: 2026/11/18 10:45:24 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import StrEnum
from datetime import datetime


class Rank(StrEnum):
    """Enum class for types of rank"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """CrewMember class based on BaseModel"""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """SpaceMission class based on BaseModel"""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_values(self):
        """Custom validation function"""
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(member.rank in ("captain, commander")
                   for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain")
        experienced = sum(member.years_experience >= 5 for member in self.crew)
        if self.duration_days > 365 and experienced / len(self.crew) < 0.5:
            raise ValueError("Long missions (> 365 days) "
                             "need 50%% experienced crew (5+ years)")
        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def create_members(valid: bool):
    """Functions to initialize crew members"""
    name_1 = "Sarah Connor"
    if valid:
        rank_1 = Rank.COMMANDER
    else:
        rank_1 = Rank.CADET
    specialization_1 = "Mission Command"
    name_2 = "John Smith"
    rank_2 = Rank.LIEUTENANT
    specialization_2 = "Navigation"
    name_3 = "Alice Johnson"
    rank_3 = Rank.OFFICER
    specialization_3 = "Engineering"
    crew_1 = CrewMember(member_id="SC1", name=name_1, rank=rank_1, age=29,
                        specialization=specialization_1, years_experience=6,
                        is_active=True)
    crew_2 = CrewMember(member_id="JS2", name=name_2, rank=rank_2, age=43,
                        specialization=specialization_2, years_experience=2,
                        is_active=True)
    crew_3 = CrewMember(member_id="AJ3", name=name_3, rank=rank_3, age=18,
                        specialization=specialization_3, years_experience=7,
                        is_active=True)
    return [crew_1, crew_2, crew_3]


def print_mission(instance: SpaceMission):
    """Print the SpaceMision variable values"""
    print("Valid mission created:")
    print(f"Mission: {instance.mission_name}")
    print(f"ID: {instance.mission_id}")
    print(f"Destination: {instance.destination}")
    print(f"Duration: {instance.duration_days} days")
    print(f"Budget: ${instance.budget_millions}M")
    print(f"Crew size: {len(instance.crew)}")
    print("Crew members:")
    for member in instance.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")


def main():
    """Main to test valid and invalid SpaceMission instances"""
    print("Space Mission Crew Validation")
    print("=========================================")
    mission_id = "M2024_MARS"
    name = "Mars Colony Establishment"
    destination = "Mars"
    launch_date = datetime(2042, 3, 29)
    duration = 900
    crew_members = create_members(True)
    mission_status = "en route"
    budget = 2500.0
    try:
        instance = SpaceMission(mission_id=mission_id, mission_name=name,
                                destination=destination,
                                launch_date=launch_date,
                                duration_days=duration, crew=crew_members,
                                mission_status=mission_status,
                                budget_millions=budget)
        print_mission(instance)
    except ValidationError as e:
        print("\n".join(
                    err["msg"].removeprefix("Value error, ")
                    if err["type"] == "value_error"
                    else f"{err['loc'][0]}: {err['msg']}"
                    for err in e.errors()
                    ))
    print("\n=========================================")
    print("Expected validation error:")
    crew_members_invalid = create_members(False)
    try:
        invalid_instance = SpaceMission(mission_id=mission_id,
                                        mission_name=name,
                                        destination=destination,
                                        launch_date=launch_date,
                                        duration_days=duration,
                                        crew=crew_members_invalid,
                                        mission_status=mission_status,
                                        budget_millions=budget)
        print_mission(invalid_instance)
    except ValidationError as e:
        print("\n".join(
                    err["msg"].removeprefix("Value error, ")
                    if err["type"] == "value_error"
                    else f"{err['loc'][0]}: {err['msg']}"
                    for err in e.errors()
                    ))


if __name__ == "__main__":
    main()
