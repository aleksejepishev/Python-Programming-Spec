import random

class Pet():
    
    normal_hunger = 5
    normal_boredom = 5
    boredom_bottom = 0
    hunger_bottom = 0
    
    
    def __init__(self, name: str, hunger: int, boredom: int, sounds: list):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.sounds = sounds.copy()
        
    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1
        
    def mood(self):
        if self.boredom <= self.normal_boredom and self.hunger <= self.normal_hunger:
            return 'happy'
        elif self.hunger > self.normal_hunger:
            return 'hungry'
        else:
            return 'bored'
        
    def reduce_boredom(self):
        if self.boredom == 0:
            return self.boredom
        else:
            self.boredom -= 1
            return self.boredom
    
    def reduce_hunger(self):
        if self.hunger == 0:
            return self.hunger
        else:
            self.hunger -= 1
            return self.hunger
    
    def teach(self, word):
        return self.sounds.append(word)
    
    def hi(self):
        self.reduce_boredom()
        print(self.sounds[random.randrange(len(self.sounds))])
            
    def feed(self):
        self.reduce_hunger()
        
    def __str__(self):
        state = 'I am ' + self.name +'.'
        state += ' I feel ' + self.mood() + '.'
        return state
    
dolphin = Pet('Pizdulpis', 5, 3, ['Hello', 'Feed me'])
dolphin.teach('Kek')
dolphin.teach('Lel')
dolphin.hi()
dolphin.feed()
dolphin.feed()
dolphin.hi()
print(dolphin)