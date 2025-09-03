from entities.person import Person


class FileManagerService:
    @staticmethod
    def generate_path(person: Person):
        return person.last_name.lower() + "_" + person.first_name.lower() + "_signature.png"
