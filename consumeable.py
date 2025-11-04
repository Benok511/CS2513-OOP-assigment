# student no - 124394031

from item import Item

class Consumeable(Item):
    """
    Class for a Consumeable Item
    Inherits from Item

    Gives stat bonuses to a player

    Variables:
    name - str - name of conesumeable
    weight - str - weight of consumeable
    value - int - value of the consumeable
    stat - str - must be a valid stat
    statAmount - int - amount of a stat that is gained on consumption
    """
    
    def __init__(self, name, weight, value,stat,statAmount):
        '''
        cxtr for Consumeable

        calls superclass cxtr

        params:
        name - str
        weight - str
        value - int
        stat - str - must be a valid stat
        statAmount - int

        returns n/a

        exceptions:
        TypeError if StatAmmount is not int or if stat is not a str
        ValueError if Statammount is less than 0 and if stat is not a valid stat
        '''
        super().__init__(name, weight, value)

        allowedStat = ["health","strength","speed"]

        if type(stat) is not str:
            raise TypeError("stat must be of type str")
        if stat not in allowedStat:
            raise ValueError("stat must be a valid attribute i.e health")
        
        if type(statAmount) is not int:
            raise TypeError("statAmount must be of type int")
        if statAmount < 0:
            raise ValueError("statAmount must be a positive number")

        self._stat = stat
        self._statAmount = statAmount


    def __str__(self):
        '''
        str method for Consumeable

        calls for the superclass str then adds stat and StatAmount
        '''
        return super().__str__() + f' stat: {self.stat} StatAmount: {self.statAmount}'
    
    @property
    def stat(self):
        """
        Getter for stat

        returns stat
        """
        return self._stat
    
    @stat.setter
    def stat(self,stat):
        """
        Setter for stat

        params:
        stat - str - must be valid stat

        returns n/a

        exceptions:
        TypeError if stat is not str
        ValueError if stat is not a valid stat
        """
        allowedStat = ["health","strength","speed"]
        if type(stat) is not str:
            raise TypeError("stat must be of type str")
        if stat not in allowedStat:
            raise ValueError("stat must be a valid attribute i.e health")
        
        self._stat = stat

    
    @property
    def statAmount(self):
        '''
        Getter for statAmount

        returns statAmount
        '''
        return self._statAmount

    @statAmount.setter
    def statAmount(self,statAmount):
        '''
        Setter for statAmount

        params:
        statAmount - int

        returns n/a

        exceptions
        TypeError if statAmount is not int
        ValueError if statAmount is a negative number
        '''
        if type(statAmount) is not int:
            raise TypeError("statAmount must be of type int")
        if statAmount < 0:
            raise ValueError("statAmount must be a positive number")
        
        self._statAmount = statAmount
        

    
    
    