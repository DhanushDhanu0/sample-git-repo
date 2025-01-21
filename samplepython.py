class Person:
    
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        
    def person_details(self):
        if self.age>18:
            print(self.name,self.address)
        else:
            print("No need to enter")

obj1=Person('vikram',23,'hyderbad')
obj2=Person('Suresh',15,'Vijaywada')

print(obj1.person_details())
print(obj2.person_details())

        
        
        