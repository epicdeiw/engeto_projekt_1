# text
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

# Kosmetika
oddelovac = "=" * 35

import pprint

# Slovnik s uzivatelskymi daty
data = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'qwert'
}

# Vyžádá si od uživatele přihlašovací jméno a heslo
username = input("Enter your username: ")
heslo = input("Enter your password: ")
print(oddelovac)

# Overeni
if data.get(username) == heslo:
    print(f"Welcome to the app 'Text analyzer' {username}")

else:
    print("Wrong credentials, terminating the program!")
    print(oddelovac)
    quit()

print(oddelovac)

# Vyber textu
vyber = input("Select text you want to analyze (1-3): ")

while vyber != "1" and vyber != "2" and vyber != "3" and type(vyber) != int:
        vyber = input("This text does not exist, try again: ")
else:
    print(f"You selected no. {vyber}")
    vyber = int(vyber)

print(oddelovac)

#Cisteni vybraneho textu
vybrany_text = TEXTS[vyber - 1]
vycisteny_text = []

for slovo in vybrany_text.split():
    if slovo.isalpha():
        vycisteny_text.append(slovo.strip(".:;,"))
    else:
        continue

# Pocet slov
pocet_slov = len(vycisteny_text)
print(f"The number of words in this text is: {pocet_slov}")

# Pocet slov mala/velka
lowercase = 0
uppercase = 0

for slovo in vycisteny_text:
    if (slovo >= 'a' and slovo <= 'z'):
        # lowercase
        lowercase = lowercase + 1
    if (slovo >= 'A' and slovo <= 'Z'):
        # uppercase
        uppercase = uppercase + 1

print(f"There are {lowercase} lower case words in this text")
print(f"There are {uppercase} upper case words in this text")

# Numeric strings
soucet = 0

for y in vycisteny_text:
    if y.isdigit():
        soucet = soucet + 1

print(f"There are {soucet} numeric strings in this text")

# Suma vsech cisel
suma = 0

for x in vycisteny_text:
    if x.isdigit():
        suma = suma + int(x)

print(f"The sum of all the numbers is {suma}")

# delka slov
delky_slov = []
for slovo in vycisteny_text:
    delky_slov.append(len(slovo))

# Vyskyt delek
vyskyt_delek = {}

for slovo in delky_slov:
    if slovo not in vyskyt_delek:
        vyskyt_delek[slovo] = 1
    else:
        vyskyt_delek[slovo] = vyskyt_delek[slovo] + 1

# Tisk vyskytu delek
for atribut, hodnota in vyskyt_delek.items():
    hvezdicky = "*" * hodnota
    print(f"{(hodnota)} | {(hvezdicky)} | {(atribut)}")
print(oddelovac)






