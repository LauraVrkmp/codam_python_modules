# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_station.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/12 14:50:59 by laveerka        #+#    #+#               #
#  Updated: 2026/11/14 15:15:35 by laveerka        ###   ########.fr        #
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
    is_operational: bool
    notes: str | None = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("========================================")
    station_id: str = "ISS001"
    name: str = "International Space Station"
    crew_size: int = 6
    power_level: float = 85.5
    oxygen_level: float = 92.3
    last_maintenance: datetime = datetime(2023, 10, 11)
    is_operational: bool = True
    notes: str | None = "Central station"
    try:
        instance = SpaceStation(station_id=station_id, name=name, crew_size=crew_size, power_level=power_level, oxygen_level=oxygen_level, last_maintenance=last_maintenance, is_operational=is_operational, notes=notes)
        print("Valid station created:")
        print(f"ID: {instance.station_id}")
        print(f"Name: {instance.name}")
        print(f"Crew: {instance.crew_size} people")
        print(f"Power: {instance.power_level}%")
        print(f"Oxygen: {instance.oxygen_level}%")
        if instance.is_operational:
            print(f"Status: Operational")
        else:
            print("Out of operation")
    except ValidationError as e:
        print(f"Invalid data provided: {e}")
    invalid_crew = 23
    try:
        invalid_instance = SpaceStation(station_id=station_id, name=name, crew_size=invalid_crew, power_level=power_level, oxygen_level=oxygen_level, last_maintenance=last_maintenance, is_operational=is_operational, notes=notes)
        print("Valid station created:")
        print(f"ID: {invalid_instance.station_id}")
        print(f"Name: {invalid_instance.name}")
        print(f"Crew: {invalid_instance.crew_size} people")
        print(f"Power: {invalid_instance.power_level}%")
        print(f"Oxygen: {invalid_instance.oxygen_level}%")
        if invalid_instance.is_operational:
            print(f"Status: Operational")
        else:
            print("Out of operation")
    except ValidationError as e:
        print(f"Invalid data provided: {e}")


if __name__ == "__main__":
    main()
