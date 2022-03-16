class HotBeverage:
    def __init__(self, sugars=0, milk=0):
        self.sugars = 0
        self.milk = 0

    def getMilk(self):
        return self.milk
    def getSugars(self):
        return self.sugars
    def addSugar(self):
        temp = True
        while temp:
            print("How many units of sugar would you like?")
            readSugars = int(input())
            if (self.milk + self.sugars + readSugars) > 3:
                print("Sorry that is too many condiments")
            else:
                self.sugars+=readSugars
                temp = False
    def addMilk(self):
        temp = True
        while temp:
            print("How many units of milk would you like?")
            readMilks = int(input())
            if (self.milk + self.sugars + readMilks) > 3:
                print("Sorry that is too many condiments")
            else:
                self.milk += readMilks
                temp = False

    def drinkType(self):
        return self.__class__.__name__
    def __str__(self):
        return "Here is your {} with {} units of milk and {} units of sugar".format(self.drinkType(),self.getMilk(), self.getSugars())
    

class Espresso(HotBeverage):
    def __init__(self, sugars=0, milk=0):
        super().__init__(sugars, milk)
    

class Americano(HotBeverage):
    def __init__(self, sugars=0, milk=0):
        super().__init__(sugars, milk)
    
class Latte(HotBeverage):
    def __init__(self, sugars=0, milk=0):
        super().__init__(sugars, milk)
  

class BlackTea(HotBeverage):
    def __init__(self, sugars=0, milk=0):
        super().__init__(sugars, milk)
    

class YellowTea(HotBeverage):
    def __init__(self, sugars=0, milk=0):
        super().__init__(sugars, milk)
    

class GreenTea(HotBeverage):
    def __init__(self, sugars=0, milk=0):
        super().__init__(sugars, milk)
   


class mainController:
    def __init__(self):
        print("What Beverage would you like:")
        print("(0) Espresso")
        print("(1) Americano")
        print("(2) Latte")
        print("(3) Black Tea")
        print("(4) Green Tea")
        print("(5) Yellow Tea")
        try:
            self.beverage = int(input())
        except ValueError or self.beverage > 5 or self.beverage < 0:
                self.beverage = ''
    def getBeverage(self):
        return self.beverage
    def milkMenu(self):
        print("How many units of milk would you like?")
        milks = int(input())
        return milks
    def sugarMenu(self):
        print("How many units of sugar would you like?")
        sugars = int(input())
        return sugars

        
def main():
    while True:
        menu = mainController()

        if menu.getBeverage() == 0:
            drink = Espresso()
        elif menu.getBeverage() == 1:
            drink = Americano()
        elif menu.getBeverage() == 2:
            drink = Latte()
        elif menu.getBeverage() == 3:
            drink = BlackTea()
        elif menu.getBeverage() == 4:
            drink = GreenTea()
        elif menu.getBeverage() == 5:
            drink = YellowTea()
        else:
            print("That's not a possible choice" + "\n")
            continue
        
        drink.addMilk()
        drink.addSugar()
        print(str(drink) + "\n")



if __name__ == "__main__":
    main()

