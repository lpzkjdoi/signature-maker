from services.csv_loader import CSVLoaderService

loader = CSVLoaderService('fake_contacts_regenerated.csv')
persons = loader.load_persons()

print(persons)
