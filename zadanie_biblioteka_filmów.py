import datetime
from faker import Faker
fake = Faker()
from faker.providers import DynamicProvider

class Filmy:
  def __init__(self, Tytuł, Rok_wydania, Gatunek, Liczba_odtworzeń):
    self.Tytuł = Tytuł
    self.Rok_wydania = Rok_wydania
    self.Gatunek = Gatunek
    self.Liczba_odtworzeń = Liczba_odtworzeń
    
  def play(self, step=1):
    self.Liczba_odtworzeń += step
  
  def __str__(self):
    return f'{self.Tytuł} ({self.Rok_wydania}) ' 

  def __eq__(self, other):
    return (
        self.Tytuł == other.Tytuł and
        self.Rok_wydania == other.Rok_wydania and
        self.Gatunek == other.Gatunek and
        self.Liczba_odtworzeń == other.Liczba_odtworzeń
    )

Szrek = Filmy(Tytuł= "Shrek", Rok_wydania="2001", Gatunek="bajka", Liczba_odtworzeń=0)
Zielona_mila = Filmy(Tytuł= "Zielona_mila", Rok_wydania="1999", Gatunek="dramat", Liczba_odtworzeń=0)
Gladiator = Filmy(Tytuł= "Gladiator", Rok_wydania="2000", Gatunek="Dramat historyczny", Liczba_odtworzeń=0)
Nietykalni = Filmy(Tytuł= "Nietykalni", Rok_wydania="2011", Gatunek="Biograficzny/Dramat/Komedia", Liczba_odtworzeń=0)
Incepcja = Filmy(Tytuł= "Incepcja", Rok_wydania="2010", Gatunek="Thriller/Sci-Fi", Liczba_odtworzeń=0)

class Seriale(Filmy):
  def __init__(self, Numer_odcinka,Numer_sezonu , *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.Numer_odcinka = Numer_odcinka
    self.Numer_sezonu = Numer_sezonu

  def __str__(self):
    if self.Numer_odcinka <10 :
      return f'{self.Tytuł} S0{self.Numer_sezonu} E0{self.Numer_odcinka} ' 
    else:
      return f'{self.Tytuł} S{self.Numer_sezonu} E{self.Numer_odcinka} ' 

def liczba_odcinków(serial_title):
    count = 0
    for item in Lista:
        if isinstance(item, Seriale) and item.Tytuł == serial_title:
            count += 1
    return count

Prawo_ulicy = Seriale(Tytuł="Prawo ulicy", Rok_wydania="2002", Gatunek="kryminał", Liczba_odtworzeń=0, Numer_odcinka = 1, Numer_sezonu =3)
Gra_o_tron = Seriale(Tytuł="Gra_o_tron", Rok_wydania="2011", Gatunek="Dramat/Fantasy/Przygodowy", Liczba_odtworzeń=0, Numer_odcinka = 1, Numer_sezonu =3)
Sherlock = Seriale(Tytuł="Sherlock", Rok_wydania="2010", Gatunek="Dramat/Kryminał", Liczba_odtworzeń=0, Numer_odcinka = 11, Numer_sezonu =3)
print("")
Lista = [Szrek, Zielona_mila,Gladiator,Nietykalni, Prawo_ulicy,Incepcja,Gra_o_tron,Sherlock]
def biblioteka_filmów():
  print("Biblioteka filmów")
  for i in Lista:
    print(i)

biblioteka_filmów()

filmy_i_seriale_provider =  DynamicProvider(
  provider_name = "filmy_i_seriale",
  elements = [Szrek, Zielona_mila,Gladiator,Nietykalni, Prawo_ulicy,Incepcja,Gra_o_tron,Sherlock],
)
fake.add_provider(filmy_i_seriale_provider)

def get_movies():
  by_alphabet = sorted(Lista, key=lambda filmy: filmy.Tytuł)
  for i in by_alphabet:
    if type(i) == Filmy:
      print(i)

def get_series():
  by_alphabet = sorted(Lista, key=lambda seriale: seriale.Tytuł)
  for i in by_alphabet:
    if type(i) == Seriale:
      print(i)

def search():
  Title = input("Podaj tytuł filmu,serialu ")
  for i in Lista:
    if i.Tytuł == Title:
      print(i)




def generate_views():
  fake.filmy_i_seriale().Liczba_odtworzeń += fake.random_int(min=1, max=100)



generate_views()

def generate_views_10():
    for _ in range(10):
        generate_views()

def dodawanie_sezonów(tytuł, rok_wydania, gatunek, numer_sezonu, liczba_odcinków):
    for i in range(1, liczba_odcinków + 1):
        serial = Seriale(
            Tytuł=tytuł,
            Rok_wydania=rok_wydania,
            Gatunek=gatunek,
            Liczba_odtworzeń=0,
            Numer_odcinka=i,
            Numer_sezonu=numer_sezonu
        )
        Lista.append(serial)

def top_titles(ile):
    by_view = sorted(Lista[:ile], key=lambda top_titles: top_titles.Liczba_odtworzeń, reverse=True)
    data = datetime.date.today().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {data}:")
    for i in by_view:
        print(i)

top_titles(3)