class Pet :
    def __init__(self,name,species,age):
        self.adopted=False
        self.name=name
        self.species=species
        self.age=age

    def display_info(self):
       print(f"Pet name : {self.name} , Pet specie: {self.species}, Pet age :{self.age}, Adopted status :{self.adopted}")
    
    def mark_adopted(self):
        self.adopted=True

    def birthday(self):
        self.age+=1

pet1 = Pet("Max", "Dog", 3)
pet2 = Pet("ivan", "Cat", 2)
pet3 = Pet("samir", "butterfly", 1)

pet1.display_info()
pet1.birthday()
pet1.mark_adopted()
pet1.display_info()


pet2.mark_adopted()
pet2.display_info()

pet3.display_info()
