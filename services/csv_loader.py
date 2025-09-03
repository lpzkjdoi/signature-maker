import csv

from entities.person import Person


class CSVLoaderService:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_persons(self):
        persons = []
        with open(self.filepath, mode="r", newline="") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                person = Person(**row)
                persons.append(person)
        return persons
