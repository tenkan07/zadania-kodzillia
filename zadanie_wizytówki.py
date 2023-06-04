from faker import Faker
fake = Faker()

class BaseContact():
  def __init__(self, imię, nazwisko, telefon, adres_email):
    self.imię = imię
    self.nazwisko = nazwisko
    self.telefon = telefon
    self.adres_email = adres_email

  def __str__(self):
    return f'{self.imię} {self.nazwisko} {self.telefon} {self.adres_email}' 

  @property
  def label_length(self):
      return len(self.imię) + len(self.nazwisko)

BaseContact_1 = BaseContact(imię= "Jan", nazwisko="Kowalski", telefon="+48 123456789", adres_email="JanKowalski@gmail.com" )

class BusinessContact(BaseContact):
  def __init__(self, stanowisko,nazwa_firmy, telefon_służbowy , *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.stanowisko = stanowisko
    self.nazwa_firmy = nazwa_firmy
    self.telefon_służbowy = telefon_służbowy

  def __str__(self):
    return f'{self.imię} {self.nazwisko} {self.telefon} {self.adres_email}{self.stanowisko} {self.nazwa_firmy} {self.telefon_służbowy} ' 

  @property
  def label_length(self):
      return len(self.imię) + len(self.nazwisko)

BusinessContact_1 = BusinessContact(imię="Jan" , nazwisko="Kowalski", telefon="+48 123456789", adres_email="JanKowalski@gmail.com ", stanowisko="kierowca", nazwa_firmy="abc", telefon_służbowy="+48 123456789" )


def contact(numer_telefonu,imię, nazwisko):
  print(f"Wybieram numer {numer_telefonu} i dzwonie do {imię} {nazwisko}")

contact(BaseContact_1.telefon, BaseContact_1.imię, BaseContact_1.nazwisko)
contact(BusinessContact_1.telefon_służbowy, BusinessContact_1.imię, BusinessContact_1.nazwisko)
print("\n")

def create_contacts(tobc, quantity):
  if tobc == BaseContact:
    for i in range(quantity):
      Random_BaseContact = BaseContact(imię= fake.unique.first_name(), nazwisko=fake.unique.last_name(), telefon=fake.unique.phone_number(), adres_email=fake.unique.ascii_email() )
      print(Random_BaseContact)
  elif tobc == BusinessContact:
    for i in range(quantity):
      Random_BusinessContact = BusinessContact(imię= fake.unique.first_name(), nazwisko=fake.unique.last_name(), telefon=fake.unique.phone_number(), adres_email=fake.unique.ascii_email(), stanowisko=fake.unique.job(), nazwa_firmy=fake.unique.company(), telefon_służbowy=fake.unique.phone_number() )
      print(Random_BusinessContact)

create_contacts(BaseContact,7)
print("\n")
create_contacts(BusinessContact,5)

print(BaseContact_1.label_length) 
print(BusinessContact_1.label_length)