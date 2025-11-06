# student no - 124394031

#all comments are based on pep standards and from how you formed them in lectures
from item import Item
from consumeable import Consumeable
from weapon import Weapon

class Character:

    '''
    A Base Class to define a basic character in a game

    attritbutes 
    Name - str - name of character
    Health - int - health of character
    Strength - Int - strength of character
    Speed - int - speed of character
    equipped - Item or subclass of Item - current equipped weapon - None describes no item equipped
    '''
    
    def __init__(self,name,Health,Strength,Speed):

        '''
        cxtr for character

        args:
        name - str
        Health - int
        Strength - int
        Speed - int
        equipped - item or subclass of item - initiaised to None
        

        exceptions:
        TypeError if any arg is not int or if name is not str
        ValueError if Health,Strength,Speed,Money < 0
        '''
        if type(name) is not str:
            raise TypeError("name must be of type str")

        if type(Health) is not int:
            raise TypeError('Health must be of type int')
        if Health < 0:
            raise ValueError('Health must be greater than 0')
        
        if type (Strength) is not int:
            raise TypeError('Strength must be of type int')
        if Strength < 0:
            raise ValueError('strength must be greater than 0')
        
        if type (Speed) is not int:
            raise TypeError('Speed must be of type int')
        if Speed < 0:
            raise ValueError('speed must be greater than 0')
        
        
        
        self._name = name
        self._health = Health
        self._strength = Strength
        self._speed = Speed
        self._equipped = None
        

    
    def __str__(self):
        return f'Name: {self._name} Health: {self._health} Strength: {self._strength} Speed: {self._speed} Equipped: {self._equipped}'
    
    @property
    def name(self):
        '''
        Getter for name
        args - n/a
        returns - name of char
        '''

        return self._name
    
    @name.setter
    def name(self,name):
        '''
        Setter for name
        args - name - str
        returns - n/a
        exceptions - TypeError if name is not str
        '''
        
        if type(name) is not str:
            raise TypeError("name must be of type str")
        
        self._name = name


    @property
    def health(self):
        '''
        Getter for health
        args - n/a
        returns - health of char
        '''
        return self._health
    
    @health.setter
    def health(self,health):
        '''
        Setter for health
        args - health - int
        returns - n/a
        exceptions - TypeError if Health is not int
                    ValueError if Health < 0
        '''
        if type(health) is not int:
            raise TypeError('Health must be of type int')
        
        if health < 0:
            raise ValueError('Health must be greater than 0')
        
        self._health = health
        
    @property
    def strength(self):
        '''
        Getter for strength
        args - n/a
        returns - strength of char
        '''
        return self._strength
    
    @strength.setter
    def strength(self,strength):
        '''
        Setter for strength
        args - Strength - int
        returns - n/a
        exceptions - TypeError if strength is not int
                    ValueError if strenght < 0
        '''
        if type(strength) is not int:
            raise TypeError('strength must be of type int')
        
        if strength < 0:
            raise ValueError('strength must be greater than 0')
        
        self._strength = strength

    @property
    def speed(self):
        """
        Getter for speed
        args - n/a
        returns - speed of char
        """
        return self._speed
    
    @speed.setter
    def speed(self,speed):
        '''
        Setter for speed
        args - speed - int
        returns - n/a
        exceptions - TypeError if speed is not int
                    ValueError if speed < 0
        '''
        if type(speed) is not int:
            raise TypeError('speed must be of type int')
        
        if speed < 0:
            raise ValueError('speed must be greater than 0')
        
        self._speed = speed

    @property
    def equipped(self):
        '''
        Getter for Equipped

        params: n/a

        returns equipped item
        '''
        return self._equipped
    
    @equipped.setter
    def equipped(self,item):
        '''
        Setter for equipped

        params: item - Item or subclass of item (Weapon,Consumable)
        '''
        if type(item) is not Item and type(item) is not Weapon and type(item) is not Consumeable and item is not None:
            raise TypeError("can only equip type item or subclasses of item")
        
        self._equipped = item


    
    def takeDmg(self,damage):
        '''
        applies damage to a character

        arguments - damage - int

        returns n/a

        exceptions
        TypeError if dmg is not an int
        ValueError if dmg < 0
        '''

        if type(damage) is not int:
            raise TypeError('Damage must be of type int')
        
        if damage < 0:
            raise ValueError('Damage must be 0 or greater')
        
        self._health -= damage
        if self._health < 0:
            self._health = 0

    @property
    def isDead(self):
        '''
        checks if character is dead

        arguments : n/a

        returns True if character is dead
                False if character is alive
        
        Exceptions n/a
        '''

        if self.health <= 0:
            return True
        return False
    
    def run(self,other):
        '''
        A method to run away from an enemy

        arguments - other character

        returns - True if successful
                False if not

        exceptions - TypeError if other is not an instance of character / subclass instance
        '''
 
        if not isinstance(other,Character):
            raise TypeError('Other should be of type Character or a subclass of character')
        
        if self._speed > other._speed:
            return True
        
        return False
    
    @property
    def damage(self):
        '''
        Property to calculate damage
        if no weapon is equipped the character will punch (ie strength)
        if weapon is equipped the damage multiplier will be applied to the characters strength

        args - None
        returns - damage that a character can deal based on which weapon and strength
        '''
        if self._equipped is None or type(self._equipped) is Consumeable or type(self.equipped) is Item:
            return self.strength
        
        
        return self.strength * self._equipped.multiplier
    
    def hitCharacter(self,other):
        if not isinstance(other,Character):
            raise TypeError("other must be of type Character or a subclass of character")
        
        other.takeDmg(self.damage)

