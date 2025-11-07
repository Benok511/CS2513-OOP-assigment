# student no - 124394031


from character import Character
from inventory import Inventory
from item import Item
from consumeable import Consumeable
from weapon import Weapon
from enemy import Enemy


class Player(Character):

    '''
    Player Class

    Inherits From Character
    extended with inventory - type - Inventory

    player can pick up items unlike enemies
    '''
    # https://stackoverflow.com/questions/36321344/how-to-set-default-value-for-variable had to look up how to set a default variable
    # for an instance variable
    def __init__(self, name, Health, Strength, Speed,money = 0):
        '''
        cxtr for Player
        calls for superclass cxtr and adds inventory - empty at start

        args:
        name - str
        Health - int
        Strength - int
        Speed - int
        money - int - 0 by default
        inventory - Inventory

        exceptions:
        TypeError if Health,Strengh,Speed,money arg is not int or if name is not str
        ValueError if Health,strength,speed,money is negative
        '''
        super().__init__(name,Health, Strength, Speed)

        if type(money) is not int:
            raise TypeError("Money must be of type int")
        if money < 0:
            raise ValueError("Cannot have Negative money")

        self._money = money
        
        self._inventory = Inventory() #extension and composition

    def __str__(self):
        return 'Player | ' + super().__str__() + f' Money:{self.money} Inventory: {len(self._inventory._body)} items' #specialisation 

    
    @property
    def inventory(self):
        '''
        Getter for inventory

        args:
        n/a

        returns inventory
        '''
        return self._inventory
    
    @property
    def money(self):
        '''
        getter for money
        returns money
        '''
        return self._money
    
    @money.setter
    def money(self,money):
        '''
        Setter for money

        params:
        money - int

        returns n/a

        exceptions:
        TypeError if money is not int
        ValueError if money is negative
        '''
        if type(money) is not int:
            raise TypeError("money must be of type int")
        if money < 0:
            raise ValueError("Cannot have Negative money")
        
        self._money = money
    


    
    def pickUp(self,item):

        '''
        Method to pick up an item

        args:
        item - Item or subclass of item

        returns:
        None

        prints message if player is not strong enough to carry

        adds item if otherwise
        '''

        if self._inventory._weight + item.weight > self.strength:
            print('You are Not strong enough to carry this item!')
        
        else:
            self._inventory.add(item)

    
    def dropItem(self,i):
        '''
        method to drop an item

        args:
        i - int - index of item

        returns None

        removes item if index is valid

        Exceptions - IndexError if index is invalid
        TypeError if i is not an int
        '''
        if type(i) is not int:
            raise TypeError("'i' must be of type int")
        if i < 0 or i >= len(self._inventory._body):
            raise IndexError('Index is Invalid')
        
        self._inventory.remove(i)

    
    def equipItem(self,i):
        '''
        method to equip an item

        args:
        i - int - index of item to equip

        returns None

        equips selected item and if an item is equipped already it adds it to inventory
        '''

        if i < 0 or i >= len(self._inventory._body):
            raise IndexError('Index is Invalid')

        olditem = self._equipped
        self._equipped = self._inventory.get(i)
        self._inventory.remove(i)
        
        if olditem is not None:
            self._inventory.add(olditem)

    def useConsumeable(self):

        '''
        Method to use a Consumeable that is currently equipped

        parameters:
        none

        returns None

        exceptions:
        TypeError if equipped item is not a consumeable

        '''

        if type(self.equipped) is not Consumeable:
            raise TypeError("must be of type Consumeable")
        
        
        stat = self.equipped._stat

        if stat == 'health':
            self.health += self.equipped.statAmount
        
        elif stat == 'strength':
            self.strength += self.equipped.statAmount
        
        else:
            self.speed += self.equipped.statAmount

        self.equipped = None

    def hitCharacter(self, other):
        '''
        Specialised hit character for player
        (super().hitCharacter(other) was autofilled by vscode when I went to specialise the method so I decided to use it
        because it saves me writing the damage logic again!!)

        args - Other - Character or subclass of character

        returns n/a

        '''
        super().hitCharacter(other) 
        if other.isDead and type(other) is Enemy:
            stat = other._stat
            print(f'You gained {other._statAmount} {other._stat}')

            if stat == 'health':
                self.health = self.health + other.statAmount
        
            elif stat == 'strength':
                self.strength = self.strength + other.statAmount

            elif stat == 'money':
                self.money += other.statAmount
        
            else:
                self.speed = self.speed + other.statAmount

    
    def sellItem(self):
        '''
        method to sell the item equipped in hand
        removes item from player if they have one equipped
        then adds the value of the item to their total money
        if no item equipped - prints message

        params n/a

        returns n/a
        '''

        if self.equipped:
            value = self.equipped.value
            self.money += value
            self.equipped = None
            print(f'You gained {value} coins your total is now {self.money}')
        
        else:
            print("Nothing in your hand to sell")
        
            
    def buyStats(self,stat,statAmount):
        allowedStat = ["health","strength","speed"]

        if type(stat) is not str:
            raise TypeError("stat must be of type str")
        if stat not in allowedStat:
            raise ValueError("stat must be a valid attribute i.e health,strenght,speed")
        
        if type(statAmount) is not int:
            raise TypeError("statAmount must be of type int")
        if statAmount < 0:
            raise ValueError("statAmount must be a positive number")
        
        if statAmount > self.money:
            print('You do not have enough money to buy these stats')
        
        else:
            self.money -= statAmount
            
            if stat == 'health':
                self.health = self.health + statAmount
        
            elif stat == 'strength':
                self.strength = self.strength + statAmount

            elif stat == 'money':
                self.money += statAmount
        
            else:
                self.speed = self.speed + statAmount
            
            print(f'You bought {statAmount} {stat} your new total is {self.money}')




            
        

