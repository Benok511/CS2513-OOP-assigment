# student no - 124394031

from item import Item
class Weapon(Item):
    '''
    Class for a weapon - inherits from Item class

    adds a new instance variable multiplier - weapon amplifies damage from strenght
    '''

    def __init__(self, name, weight, value,multiplier):
        '''
        Constructor for Weapon

        parameters:
        name - str
        weight - int
        value - int
        multiplier - int

        returns n/a

        exceptions
        TypeError if weight,value,multiplier is not int or name is not str
        ValueError if weight,value,multiplier < 0
        '''
        super().__init__(name, weight, value)

        if type(multiplier) is not int:
            raise TypeError("Multiplier must be of type int")
        if multiplier <= 0:
            raise ValueError("Multiplier must be greater than 0")
        
        self._multiplier = multiplier

    def __str__(self):
        '''
        str method for Weapon
        calls superclass str method and adds the multiplier too
        '''
        return super().__str__() + f' Multiplier: {self.multiplier}'

    
    @property
    def multiplier(self):
        '''
        Getter for multiplier

        Returns multiplier
        '''
        return self._multiplier
    
    @multiplier.setter
    def multiplier(self,multiplier):
        '''
        Setter for multiplier

        Params:
        multiplier - int

        returns n/a

        exceptions:
        TypeError if multiplier is not int
        ValueError if multiplier is 0 or below
        '''
        if type(multiplier) is not int:
            raise TypeError("Multiplier must be of type int")
        if multiplier <= 0:
            raise ValueError("Multiplier must be greater than 0")
        
        self._multiplier = multiplier

    
    def upgradeWeapon(self,upgradeAmount):
        '''
        Method to upgrade a Weapon

        params:
        upgradeAmount - int

        returns n/a

        Exceptions:
        TypeError if upgradeAmount is not int
        ValueError if upgradeAmount is 0 or less
        '''
        if type(upgradeAmount) is not int:
            raise TypeError('UpgradeAmount must be of type int')
        if upgradeAmount <= 0:
            raise ValueError("UpgradeAmount must be a positive number")
        
        self.multiplier += upgradeAmount

