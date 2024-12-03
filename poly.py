class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def info(self):
        print(f"i am a cat .My name is {self.name}.I am {self.age} years old.I live with my two siblins")
    
    def sound(self):
        print("meow")




class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def info(self):
        print(f"i am a dog .My name is {self.name}.I am {self.age} years old.I live with my owner ")
    
    def sound(self):
        print("bark")


c=cat("pinky",8)
d=dog("joy",10)

for animal in(c,d):
    animal.sound()
    animal.info()