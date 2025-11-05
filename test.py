from character import Character
from player import Player
from enemy import Enemy
from item import Item
from consumeable import Consumeable
from weapon import Weapon
from inventory import Inventory


def TestCharacter():
    #testing the __init__ methods error checking
    print("TEST BLOCK FOR CHARACTER CLASS")
    print()
    print('testing the __init__ methods error checking')
    print()
    print('NAME')
    try: 
        char = Character(2,'2','hi this is a test to see if error checking for character works','4')

    except TypeError as e:
        print(e)
    
    print()
    print('HEALTH')
    
    try:
        char = Character('hi','g',2,2)
    except TypeError as e:
        print(e)
    
    try:
        char = Character('hi',-2,2,2)
    except ValueError as e:
        print(e)
    print()
    print('STRENGTH')

    try:
        char = Character('hi',2,'2',2)
    except TypeError as e:
        print(e)

    try:
        char = Character('hi',2,-2,2)
    except ValueError as e:
        print(e)
    print()
    print("SPEED")
    
    try:
        char = Character('hi',2,2,'g')
    except TypeError as e:
        print(e)
    
    try:
        char = Character('hi',2,2,-2)
    except ValueError as e:
        print(e)
    print()
    
    
    print()
    print('Testing getters and setters for each instance var')
    print()
    newChar = Character('Ben',20,40,60)
    print(f'name:{newChar.name}')
    newChar.name = 'Benjamin'
    print(f'name:{newChar.name}')
    try:
        newChar.name = 2
    except TypeError as e:
        print(e)
    
    
    print()
    print(f'health:{newChar.health}')
    newChar.health = 100
    print(f'health:{newChar.health}')
    try:
        newChar.health = 'hi'
    except TypeError as e:
        print(e)

    try:
        newChar.health = -100
    except ValueError as e:
        print(e)
    
    print()
    print(f'strength:{newChar.strength}')
    newChar.strength = 100
    print(f'strength:{newChar.strength}')
    try:
        newChar.strength = 'hi'
    except TypeError as e:
        print(e)
    
    try:
        newChar.strength = -1
    except ValueError as e:
        print(e)

    print()
    print(f'speed: {newChar.speed}')
    newChar.speed = 100
    print(f'speed: {newChar.speed}')
    try:
        newChar.speed = 'hi'
    except TypeError as e:
        print(e)
    try:
        newChar.speed = -1
    except ValueError as e:
        print(e)
    

    print(f'equipped: {newChar.equipped}')
    newChar.equipped = Weapon("iron sword",2,2,2)
    print(f'equipped: {newChar.equipped}')
    try:
        newChar.equipped = 2
    except TypeError as e:
        print(e)


    print()
    print("TESTING METHODS")
    other = Character("EVIL BEN", 100,20,1)
    other2 = Character('EVEN MORE EVIL BEN',100,2,1000000)
    run_test = newChar.run(other)
    if run_test:
        print("you successfully escaped")
    else:
        print("you cant escape")
    run_test = newChar.run(other2)
    if run_test:
        print("you successfully escaped")
    else:
        print("you cant escape")


    print()
    print("Testing Damage methods and isDead property")
    print(other)
    print(other.isDead)
    newChar.hitCharacter(other)
    print(other)
    print(other.isDead)

    print(newChar.damage) #should be 2(strenght)
    newChar.equipped = None
    print(newChar.damage) #should be same as strenght value i.e 100
    

def TestPlayer():
    print("TEST BLOCK FOR PLAYER CLASS")
    print()

    player = Player("Ben",100,20,20) #money will be 0 by default

    '''
    Just need to test money
    '''
    print("MONEY INIT ERROR CHECKS")
    
    try:
        player2 = Player("hi",2,2,2,'h')
    except TypeError as e:
        print(e)
    
    try: 
        player2 = Player('hi',2,2,2,-2)
    except ValueError as e:
        print(e)

    print()
    print('testing getter and setter for money')
    print(player.money)
    player.money = 100
    print(player.money)
    try:
        player.money = 'h'
    except TypeError as e:
        print(e)
    
    try:
        player.money = -2
    except ValueError as e:
        print(e)


    print()
    print('Testing str method')
    print(player)

    print()
    print('testing inventory getter property')
    print(player.inventory)

    print()
    print("Testing Item pickup method")
    item = Consumeable("health potion",1,1,'health',20)
    player.pickUp(item)
    print(player)
    print(player.inventory)
    item2 = Weapon('MASSIVE HAMMER',2000,20000000,1000000)
    player.pickUp(item2) #should print saying you are not strong enough

    print()
    print('Testing remove from inventory method')
    print(player)
    print(player.inventory)
    player.dropItem(0)
    print(player)
    print(player.inventory)

    print()
    print('Testing equip item from inventory method')
    item3 = Weapon('HAMMER',2,20,2)
    player.pickUp(item3)
    print(player)
    player.equipItem(0)
    print(player)
    player.pickUp(Weapon("large sword",2,4,3))
    print(player)
    print(player.inventory)
    player.equipItem(0)
    print(player)
    print(player.inventory)

    print()
    print('testing the specialised HitChatacter method')
    evilMonster = Enemy("John Pork",20,1,1,'health',20)
    print(player) #health 100
    player.hitCharacter(evilMonster)
    print(evilMonster.isDead)
    print(player) #monster is dead so health should be 120 now

    print()
    print("TESTING SELL ITEM METHOD")
    player.pickUp(Weapon('expensive weapon',2,100,2))
    print(player.inventory)
    player.equipItem(1) #equips the expensive weapon
    print(f'equipped: {player.equipped}')
    print(f'money: {player.money}')
    player.sellItem()
    print(f'equipped: {player.equipped}')
    print(f'money: {player.money}')

    


def TestEnemy():
    print("TEST BLOCK FOR ENEMY CLASS")
    print()

    print('Testing init Error Checking for Stat and StatAmount')
    print()
    try:
        evilMonster = Enemy('hi',1,2,3,900,900)
    
    except TypeError as e:
        print(e)
    
    try:
        evilMonster = Enemy('hi',1,2,3,'aura',900)
    
    
    except ValueError as e:
        print(e)

    try:
        evilMonster = Enemy('hi',1,2,3,'health','hi')
    
    except TypeError as e:
        print(e)
    
    try:
        evilMonster = Enemy('hi',1,2,3,'health',-900)
    
    except ValueError as e:
        print(e)
    
    print()
    print('Testing Getters and Setters for stat and statAmount')
    print()

    evilMonster = Enemy('EVIL',100,20,20,'speed',10)
    print(evilMonster)
    evilMonster.stat = 'health'
    print(evilMonster)
    try:
        evilMonster.stat = 2
    except TypeError as e:
        print(e)

    try:
        evilMonster.stat = 'aura'
    except ValueError as e:
        print(e)
    
    print(evilMonster)
    evilMonster.statAmount = 20
    print(evilMonster)
    try:
        evilMonster.statAmount = -2
    except ValueError as e:
        print(e)

    try:
        evilMonster.statAmount = 'aura'
    except TypeError as e:
        print(e)
    

def TestInventory():
    inventory = Inventory()
    print("TEST BLOCK FOR INVENTORY")
    print()
    #populating the inventory with some sample items
    print("TESTING ADD METHOD")
    print(inventory)
    for i in range(10):
        inventory.add(Item(f'SAMPLE{i}',1,10))
    print(inventory)

    try:
        inventory.add(2)
    except TypeError as e:
        print(e)
    
    print()
    print("TESTING GET METHOD")
    item = inventory.get(0) #should get sample0
    print(item)
    try:
        item = inventory.get(100)
    except IndexError as e:
        print(e)

    try:
        item = inventory.get('g')
    except TypeError as e:
        print(e)

    print()
    print("TESTING REMOVE METHOD")
    print(inventory)
    item = inventory.remove(0) #should remove and return SAMPLE0
    print(f'item: {item}')
    print(inventory)

    try:
        inventory.remove('g')
    except TypeError as e:
        print(e)

    try:
        inventory.remove(10000)
    except IndexError as e:
        print(e)






# TestCharacter()
# TestPlayer()
# TestEnemy()
# TestInventory()
