
class merocar:
    def __init__(self, stock):
        self.stock = stock

    def displaycar(self):
        print("Total numbers of cars in the stock", self.stock )

    def rentforcar(self, quantity):
        if quantity <= 0:
            print("Enter the positive value of greater then Zero")
        elif quantity > self.stock:
            print("Tyati dherai saman xaina stock ma ")
        else:
            self.stock = self.stock - quantity  
            print("Total Price", quantity*1000) 
            print("Total Cars Remanining in the Stock", self.stock)


while True:
    obj = merocar(150)
    choice = int(input('''
    1 Total Stock
    2 Enter Ouantity of cars you want to Rent \n
    3 exit    '''))
    
    if choice ==1:
        obj.displaycar()
    elif choice ==2:
        n = int(input("Enter the quantity of car yo want to rent. : "))
        obj.rentforcar(n)

    else:
        break
    


