class Pet:
    def __init__(self, name, species, age):
        self.adopted = False
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"Pet name: {self.name}, Species: {self.species}, Age: {self.age}, Adopted: {self.adopted}")

    def mark_adopted(self):
        self.adopted = True

    def birthday(self):
        self.age += 1

    def rename(self, new_name):
        self.name = new_name


def non_adopted(pets):
    for pet in pets:
        if not pet.adopted:
            pet.display_info()
  



pet1 = Pet("Max", "Dog", 3)
pet2 = Pet("ivan", "Cat", 2)
pet3 = Pet("samir", "butterfly", 1)


pet1.birthday()
pet2.mark_adopted()
pet3.rename("jojo")

pet1.display_info()
pet2.display_info()
pet3.display_info()

pet_list = [pet1, pet2, pet3]

print("Non-adopted pets:")
non_adopted(pet_list)
