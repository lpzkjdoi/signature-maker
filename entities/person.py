from dataclasses import dataclass


@dataclass
class Person:
    last_name: str
    first_name: str
    email: str
    job: str
    tel1: str
    tel2: str

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_tel(self):
        if self.tel2:
            return self.tel1 + " - " + self.tel2
        else:
            return self.tel1
