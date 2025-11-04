# student no - 124394031


class Item:

    '''
    Base class for an Item Has all the attribute of A standard item

    Attributes
    Name - str - name of item
    Weight - int - weight of item
    Value - int - value of item
    '''

    def __init__(self, name,weight,value):

        '''
        Constructor for Item class

        parameters:
        name - str 
        weight - int 
        value - int 

        return n/a

        exeptions:
        TypeError if weight and value is not int or name is not str
        ValueError if weight,value < 0
        '''

        if type(name) is not str:
            raise TypeError("Name must be of type str")
        
        if type(weight) is not int:
            raise TypeError("Weight must be of type int")
        if weight < 0:
            raise ValueError("weight must be a non negative number")
        
        if type(value) is not int:
            raise TypeError("Value must be of type int")
        if value < 0:
            raise ValueError("value must be a non negative number")
        
        self._name = name
        self._weight = weight
        self._value = value


    def __str__(self):
        '''
        str method for Item
        returns a string representations of the attributes
        '''
        return f'Name: {self._name}, Weight: {self._weight}, Value: {self._value}'
    

    def getName(self):
        '''
        Getter for name
        returns name
        '''
        return self._name
    
    def setName(self,name):
        '''
        Setter for name

        params:
        name - str

        returns n/a

        exceptions:
        TypeError if name is not of type str
        '''
        if type(name) is not str:
            raise TypeError("Name must be of type str")
        
        self._name = name

    def getWeight(self):
        '''
        Getter for weight
        returns weight
        '''
        return self._weight
    
    def setWeight(self,weight):
        '''
        Setter for weight

        params:
        weight - int

        returns n/a

        exceptions:
        TypeError if weight is not of type int
        ValueError if weight is negative
        '''
        if type(weight) is not int:
            raise TypeError("Weight must be of type int")
        if weight < 0:
            raise ValueError("Weight must have a value > 0")
        
        self._weight = weight
    
    def getValue(self):
        '''
        Getter for value
        returns value
        '''
        return self._value
    
    def setValue(self,value):
        '''
        Setter for value
        
        params:
        value - int

        returns n/a

        exceptions:
        TypeError if value isnt an int
        ValueError if value is negative
        '''
        if type(value) is not int:
            raise TypeError("Value must be of type int")

        if value < 0:
            raise ValueError("Value must have a value > 0")
        
        self._value = value
    
    name = property(getName,setName)
    weight = property(getWeight,setWeight)
    value = property(getValue,setValue)
