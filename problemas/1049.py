nivel_1 = input()
nivel_2 = input()
nivel_3 = input()

animal = ''

if nivel_1 == "vertebrado":
    if nivel_2 == "ave":
        if nivel_3 == "carnivoro":
            animal = "aguia"
        else:
            animal = "pomba"
    else:
        if nivel_3 == "onivoro":
            animal = "homem"
        else:
            animal = "vaca"
else:
    if nivel_2 == "inseto":
        if nivel_3 == "hematofago":
            animal = "pulga"
        else:
            animal = "lagarta"
    else:
        if nivel_3 == "hematofago":
            animal = "sanguessuga"
        else:
            animal = "minhoca"

print(animal)