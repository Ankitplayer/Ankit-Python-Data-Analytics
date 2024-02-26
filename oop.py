class Human:
    def __init__(self,name,age,height,weight,gender,country):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.gender=gender
        self.country=country

    def show(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')
        print(f'Weight: {self.weight}')
        print(f'Gender: {self.gender}')
        print(f'Country: {self.country}')

# making objects
        
h1 = Human('Rahul', 28,5.8,80,'M','India')
h2 = Human('Prakash', 27, 5.6,68,'M','India')
h3 = Human('Shruti',25, 5.5,50,'F','India')

print(h1)
print(h2)
print(h3)

print(h1.name)
print(h2.name)

h1.show()
print('-'*15)
h2.show()
print('-'*15)
h3.show()
        