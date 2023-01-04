class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
    
    def noise(self):
        print(self.noise)

class Ninja:
    def __init__(self,first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    
#implement the following methods:
#- walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

#- feeds the ninja's pet invoking the pet eat() method      
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f'Feeding {self.pet.name} {food}')
            self.pet.eat()
        else:
            print("Oh no!! you need more pet food!")
        return self


# - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()


my_treats = ["Snausage", 'Bacon', "Trash bag"]
my_pet_food = ['Pizza', 'Burger']

nibbles = Pet("Mr. Nibbles", "Horse", ["nibbles on things", "is invisible"], "Hey Hey")

adrien = Ninja("Adrien", "Dion", my_treats, my_pet_food, nibbles)

adrien.feed();
adrien.feed();
adrien.feed();