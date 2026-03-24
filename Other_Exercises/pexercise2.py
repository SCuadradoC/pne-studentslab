class Product:
    def __init__(self, name:str,price:float):
        self.name = str(name)
        self.price = float(price)
    
    def __str__(self):
        return f"{self.name} : {self.price}€"
    
    def to_dict(self):
        return {self.name:self.price}
    
    def get_info(self):
        return f"Product: {self.name} | Price: {self.price}€"

class Client:
    def __init__(self,name:str):
        self.cart = {}
        self.name = name
    
    def __str__(self):
        return self.name
    
    def add_to_cart(self, item:Product):
        self.cart.update(item.to_dict())
    
    def compute_total(self):
        total = 0
        for i in self.cart:
            total += self.cart[i]
        return total

    def print_total(self):
        print(f"""Customer: {self.name}
Total to pay: {self.compute_total()}""")
        
    
class VIPClient(Client):
    def __init__(self, name:str, discount:float):
        super().__init__(name)
        self.discount = discount
    
    def __str__(self):
        return super().__str__() + "(VIP)"

    def compute_total(self):
        return super().compute_total() * (1 - (self.discount / 100))

    def print_total(self):
        print(f"""Customer (VIP): {self.name}
Total to pay: {self.compute_total()}""")

Laptop = Product("Laptop",1200)
Chair = Product("Chair",90)
Scarf = Product("Scarf",24)

print(Laptop)
print(Chair)
print(Scarf)
print()

Alice = VIPClient("Alice",20)
Bob = Client("Bob")


Alice.add_to_cart(Scarf)
Alice.add_to_cart(Scarf)
Alice.add_to_cart(Chair)
Bob.add_to_cart(Scarf)
Bob.add_to_cart(Laptop)

Alice.print_total()
Bob.print_total()

