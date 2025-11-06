# student no - 124394031

from character import Character

class Enemy(Character):
    """
    Class to represent enemies
    inheriting from character
    they increase attributes like strength or speed when a Player eliminates it

    Attributes
    Name - str - name of character
    Health - int - health of character
    Strength - Int - strength of character
    Speed - int - speed of character
    equipped - Weapon - current equipped weapon - None describes no item equipped
    stat - str - states the stat that will be boosted on killing an enemy
    statAmount - int - amount the stat is increased by    

    """

    def __init__(self, name, Health, Strength, Speed,stat,statAmount):
        '''
        Constructor for Enemy
        calls for superclass init method

        params:
        name - str
        health - int
        strenght - int
        Speed - int
        stat - str - must be valid stat - ["health","strength","speed","money"]
        statAmount - int

        '''
        allowedStat = ["health","strength","speed","money"]

        super().__init__(name, Health, Strength, Speed)

        if type(stat) is not str:
            raise TypeError("stat must be of type str")
        if stat not in allowedStat:
            raise ValueError("stat must be a valid attribute i.e health,strenght,speed,money")
        
        if type(statAmount) is not int:
            raise TypeError("statAmount must be of type int")
        if statAmount < 0:
            raise ValueError("statAmount must be a positive number")
        
        self._stat = stat
        self._statAmount = statAmount


    def __str__(self):
        '''
        str method for Enemy 
        Calls Character str method and adds stat and stat amount
        '''
        return super().__str__() + f' stat: {self.stat} StatAmount: {self.statAmount}'
    

    @property
    def stat(self):
        '''
        Getter for stat

        returns stat
        '''
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
        allowedStat = ["health","strength","speed","money"]
        if type(stat) is not str:
            raise TypeError("stat must be of type str")
        if stat not in allowedStat:
            raise ValueError("stat must be a valid attribute i.e health,strenght,speed,money")
        
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

    