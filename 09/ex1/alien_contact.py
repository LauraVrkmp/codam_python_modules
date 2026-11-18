# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  alien_contact.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/12 14:51:27 by laveerka        #+#    #+#               #
#  Updated: 2026/11/18 10:42:44 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import StrEnum
from datetime import datetime


class ContactType(StrEnum):
    """Enum class for types of contact"""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """AlienContact class based on BaseModel"""
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_values(self):
        """"Custom validation function"""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at "
                             "least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self


def print_instance(instance: AlienContact):
    """Print the AlienContact variable values"""
    print("Valid contact report:")
    print(f"ID: {instance.contact_id}")
    print(f"Type: {instance.contact_type}")
    print(f"Location: {instance.location}")
    print(f"Signal: {instance.signal_strength}/10")
    print(f"Duration: {instance.duration_minutes} minutes")
    print(f"Witnesses: {instance.witness_count}")
    print(f"Message: {instance.message_received}")


def main():
    """Main to test valid and invalid AlienContact instances"""
    print("Alien Contact Log Validation")
    print("======================================")
    contact_id = "AC_2024_001"
    timestamp = datetime(2023, 5, 12)
    location = "Area 51, Nevada"
    contact_type = ContactType.RADIO
    signal_strength = 8.5
    duration_minutes = 45
    witnesses = 5
    message = "'Greetings from Zeta Reticuli'"
    is_verified = True
    try:
        instance = AlienContact(contact_id=contact_id, timestamp=timestamp,
                                location=location, contact_type=contact_type,
                                signal_strength=signal_strength,
                                duration_minutes=duration_minutes,
                                witness_count=witnesses,
                                message_received=message,
                                is_verified=is_verified)
        print_instance(instance)
    except ValidationError as e:
        print("\n".join(
                    err["msg"].removeprefix("Value error, ")
                    if err["type"] == "value_error"
                    else f"{err['loc'][0]}: {err['msg']}"
                    for err in e.errors()
                    ))
    print("\n======================================")
    print("Expected validation error:")
    contact_edited = ContactType.TELEPATHIC
    witnesses_edited = 2
    try:
        invalid_instance = AlienContact(contact_id=contact_id,
                                        timestamp=timestamp, location=location,
                                        contact_type=contact_edited,
                                        signal_strength=signal_strength,
                                        duration_minutes=duration_minutes,
                                        witness_count=witnesses_edited,
                                        message_received=message,
                                        is_verified=is_verified)
        print_instance(invalid_instance)
    except ValidationError as e:
        print("\n".join(
            err["msg"].removeprefix("Value error, ")
            if err["type"] == "value_error"
            else f"{err['loc'][0]}: {err['msg']}"
            for err in e.errors()
            ))


if __name__ == "__main__":
    main()
