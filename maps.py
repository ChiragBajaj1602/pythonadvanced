my_pets=['alfred','tabitha','william','arla']
uppered_pets=[]
for pet in my_pets:
    pet=pet.upper()
    uppered_pets.append(pet)

my_pets=['alfred','tabitha','william','arla']
uppered_pets=list(map(str.upper,my_pets))
print(uppered_pets)
