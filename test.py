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
    print("MONEY")
    
    try:
        char = Character("hi",2,2,2,'h')
    except TypeError as e:
        print(e)
    
    try: 
        char = Character('hi',2,2,2,-2)
    except ValueError as e:
        print(e)
    
    print()
    print('Testing getters and setters for each instance var')
    print()
    newChar = Character('Ben',20,40,60)
    print(newChar.name)
    newChar.name = 'Benjamin'
    print(newChar.name)
    try:
        newChar.name = 2
    except TypeError as e:
        print(e)
    
    print()
    print(newChar.health)
    newChar.health = 100
    print(newChar.health)
    try:
        newChar.health = 'hi'
    except TypeError as e:
        print(e)
    
    print()
    print(newChar.strength)
    newChar.strength = 100
    print(newChar.strength)
    try:
        newChar.strength = 'hi'
    except TypeError as e:
        print(e)

    print()
    print(newChar.speed)
    newChar.speed = 100
    print(newChar.speed)
    try:
        newChar.speed = 'hi'
    except TypeError as e:
        print(e)
    

    print(newChar.equipped)
    newChar.equipped = Weapon("iron sword",2,2,2)
    print(newChar.equipped)
    try:
        newChar.equipped = 2
    except TypeError as e:
        print(e)

    print(newChar.money)
    newChar.money = 5
    print(newChar.money)
    try:
        newChar.money = '2'
    except TypeError as e:
        print(e)
    try: 
        newChar.money = -2
    except ValueError as e:
        print(e)

    print()
    print("TESTING METHODS")
    other = Character("EVIL BEN", 100,20,1)
    run_test = newChar.run(other)
    if run_test:
        print("you successfully escaped")
    else:
        print("you cant escape")

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

    player = Player("Ben",100,20,20)

    '''
    No need to check for errors in init all of it is handled in character init method
    '''
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
    


# TestCharacter()
# TestPlayer()
TestEnemy()
