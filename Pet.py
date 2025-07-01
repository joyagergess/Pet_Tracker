class Pet :
    def __init__(self,name,species,age):
        self.adopted=False
        self.name=name
        self.species=species
        self.age=age

    def display_info(self):
       print(f"Pet name : {self.name} , Pet specie: {self.species}, Pet age :{self.age}, Adopted status :{self.adopted}")

pet1 = Pet("Max", "Dog", 3)
pet1.display_info()
