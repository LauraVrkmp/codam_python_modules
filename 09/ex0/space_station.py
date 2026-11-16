# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_station.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/12 14:50:59 by laveerka        #+#    #+#               #
#  Updated: 2026/11/16 17:49:36 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def print_instance(instance: SpaceStation):
    print("Valid station created:")
    print(f"ID: {instance.station_id}")
    print(f"Name: {instance.name}")
    print(f"Crew: {instance.crew_size} people")
    print(f"Power: {instance.power_level}%")
    print(f"Oxygen: {instance.oxygen_level}%")
    if instance.is_operational:
        print("Status: Operational")
    else:
        print("Out of operation")


def main():
    print("Space Station Data Validation")
    print("========================================")
    station_id = "ISS001"
    name = "International Space Station"
    crew_size = 6
    power_level = 85.5
    oxygen_level = 92.3
    last_maintenance = datetime(2023, 10, 11)
    is_operational = True
    notes = "Central station"
    try:
        instance = SpaceStation(station_id=station_id, name=name,
                                crew_size=crew_size, power_level=power_level,
                                oxygen_level=oxygen_level,
                                last_maintenance=last_maintenance,
                                is_operational=is_operational, notes=notes)
        print_instance(instance)
    except ValidationError as e:
        print("\n".join(f"{err['loc'][0]}: {err['msg']}"
                        for err in e.errors()))
    invalid_crew = 23
    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_instance = SpaceStation(station_id=station_id, name=name,
                                        crew_size=invalid_crew,
                                        power_level=power_level,
                                        oxygen_level=oxygen_level,
                                        last_maintenance=last_maintenance,
                                        is_operational=is_operational,
                                        notes=notes)
        print_instance(invalid_instance)
    except ValidationError as e:
        print("\n".join(f"{err['loc'][0]}: {err['msg']}"
                        for err in e.errors()))


if __name__ == "__main__":
    main()
