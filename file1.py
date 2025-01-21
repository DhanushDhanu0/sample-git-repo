class Vechile:
    def __init__(self,model,price,engine,type):
        self.model=model
        self.price=price
        self.engine=engine
        self.type=type
        
    def get_details(self):
        if self.type=='car':
            print(self.model,self.price,self.engine)
        
        

        
        
        
vech=Vechile('hondai5',20000000,'germany','car')
print(vech.get_details())      