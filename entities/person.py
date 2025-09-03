from dataclasses import dataclass


@dataclass
class Person:
    last_name: str
    first_name: str
    email: str
    job: str
    tel1: str
    tel2: str