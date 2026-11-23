# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   alien_contact.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/06 14:22:33 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/07 10:25:24 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing_extensions import Self


class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def final_validation(self) -> Self:
        verification_flag = False
        errors = ""
        if self.contact_id[:2] != "AC":
            verification_flag = True
            errors = errors + "\ncontact_id does not start with AC!"
        if (self.contact_type == ContactType.PHYSICAL
                and self.is_verified is False):
            verification_flag = True
            errors = errors + "\nPhysical contact is not verified!"
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            verification_flag = True
            errors = errors + (
                "\nTelepathic contact "
                "requires at least 3 witnesses!"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            verification_flag = True
            errors = errors + "\nsignal_strength > 7.0 must have a message!"

        if verification_flag is True:
            raise ValueError(errors)
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    alien_contact_1 = AlienContact(contact_id="AC_2024_001",
                                   contact_type=ContactType.RADIO,
                                   location="Area 51, Nevada",
                                   signal_strength=8.5,
                                   duration_minutes=45,
                                   witness_count=5,
                                   message_received=("'Greetings from "
                                                     "Zeta Reticuli'"),
                                   timestamp=datetime.fromisoformat(
                                       "2025-12-24T00:00:00+00:00")
                                   )
    print(f"ID: {alien_contact_1.contact_id}")
    print(f"Type: {alien_contact_1.contact_type.value}")
    print(f"Location: {alien_contact_1.location}")
    print(f"Signal: {alien_contact_1.signal_strength}/10")
    print(f"Duration: {alien_contact_1.duration_minutes} minutes")
    print(f"Witness: {alien_contact_1.witness_count}")
    print(f"Message: {alien_contact_1.message_received}")
    print("\n======================================")
    print("Expected validation error:")
    try:
        alien_contact_2 = AlienContact(contact_id="AC_2024_001",
                                       contact_type=ContactType.TELEPATHIC,
                                       location="Area 51, Nevada",
                                       signal_strength=8.5,
                                       duration_minutes=45,
                                       witness_count=2,
                                       message_received=("'Greetings from "
                                                         "Zeta Reticuli'"),
                                       timestamp=datetime.fromisoformat(
                                           "2025-12-24T00:00:00+00:00")
                                       )
        print(alien_contact_2.contact_id)
    except ValidationError as e:
        print((e.errors()[0]['msg']).replace("Value error, \n", ""))


if __name__ == "__main__":
    main()
