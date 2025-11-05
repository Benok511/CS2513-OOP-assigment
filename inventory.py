# student no - 124394031

from item import Item


class Inventory:

    '''
    Class for a simple inventory

    attributes:
    body - list of Items - holds all the items
    weight - int - weight of the Inventory
    '''

    def __init__(self):

        '''
        Constructor for an inventory class
        no paramaters required
        sets up an empty inventory and sets weight to 0
        '''

        self._body = []
        self._weight = 0

    def __str__(self):

        '''
        str method for inventory:
        iterates through the list and calls str method for each item
        and returns a string with all current items stored in inventory
        '''
        s = ''
        if len(self._body) == 0:
            s = 'Empty\n'

        else:   
            for item in self._body:
                s += str(item)
                s += '\n'

        s+= f'Weight: {self._weight}'

        return s

    def get(self,i):
        '''
        Method to get an item in an inventory

        Parameters:
        i - int - index of item

        Returns:
        item at index i

        Exceptions:
        IndexError if i is not in range of inventory size
        TypeError if i is not an int
        '''
        if type(i) is not int:
            raise TypeError("i must be of type int")
        
        if i < 0 or i >= len(self._body):
            raise IndexError('Index Not in Range')
        
        
        
        return self._body[i]
    
    def add(self,item):
        '''
        Method to add an item to an inventory

        Paramaters:
        item - Item or subclass of item

        Returns n/a

        Exceptions:
        TypeError if item is not of Type item or subclass of item
        '''
        if not isinstance(item,Item):
            raise TypeError('Must be of type Item')
        
        self._body.append(item)
        self._weight += item.weight

    def remove(self,i):
        '''
        Method to remove an item in an inventory

        Parameters:
        i - int - index of item

        Returns:
        n/a

        Exceptions:
        IndexError if i is not in range of inventory size
        TypeError if i is not an int
        '''
        if type(i) is not int:
            raise TypeError('must be of type int')
        if i >= len(self._body) or i < 0:
            raise IndexError("i must be a valid index")
        
        item = self._body.pop(i) # this is slow but for simplicity I didnt worry for runtimes
        self._weight -= item.weight

        return item