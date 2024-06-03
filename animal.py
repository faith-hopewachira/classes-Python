class Animal:
    def make_sound(self):
        pass

    def move(self):
        pass

    def habitat(self):
        pass
    


class Bird(Animal):
    def make_sound(self):
        print("Chirp")

    def move(self):
        print("The bird is flying")

    def habitat(self):
        print("Nest")


class Fish(Animal):
    def make_sound(self):
        print("Click")

    def move(self):
        print("Swimming")

    def habitat(self):
        print("Water")

class Dog(Animal):
    def make_sound(self):
        print("Barking")

    def move(self):
        print("The dog is running")

    def habitat(self):
        print("Wild dogs live in forests")



class Human(Animal):
    def make_sound(self):
        print("Talking")
    
    def move(self):
        print("Walking and running")

    def habitat(self):
        print("A human lives in a house")




    

    