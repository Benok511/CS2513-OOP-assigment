This is my assignment for my programming module where I had to use object oriented programming features to create anything I wanted. I chose to model my project on a game because I love
gaming and anything game related. I use encapsulation, Inheritance, composition, aggregation, properties to model my game where there are players and enemies fighting and lots of nice loot
to gain such as weapons and consumeables.

Encapsulation is seen in every class to protect the instance variables and they are only accessed through getter and setter properties
all instance variable are are properties using the decorator method and also the standard method.

My base classes are Character Item and Inventory all the rest of my classes Inherit from either Character or Item

The Character class is the Base class for any living thing in this game - it is composed of name,health,strength,speed and equipped
the equipped variable aggregates character with the Item class and

The Inventory class is used to manage a players items the player has an inventory and a inventory consists of items.
The inventory also keeps track of the total weight as a player can only carry as much as his strength allows.

Player and Enemy inherit from character - player extends character by adding a money instance variable and an inventory, it is also specialised with many environmental methods allowing the player to pick up items in it's environment (if it was an actual game in this model a player could hypothetically pick up any item it wanted).Players can also make use of consumeables but enemies cannot, Players can also sell items to increase their money. Player also specialises character with the hitCharacter method where it also checks to see if the character killed was an enemy and if so it will gain the rewards based on the enemys stat and statAmount attributes.

Enemy extends character by adding a stat and a statAmount variables. Stat indicates which stat that is upgraded on elimination of this enemy and statAmount states how much of this stat will be granted to a player.Enemies are much more simpler than a player since they are not the primary character in the game they allow a player to get stronger and stronger as they progress

Players and Enemys interact with eachother by hitting eachother "fights" in a sense

Item is the base class from which Weapon and Consumeable inherit from, items and Weapons are used by Characters but only Players make use of Consumeables (just a design choice) base items are composed of name,weight,value.

Weapon extends this by having a multiplier which works in tandem with a characters strength to increase the characters damage output

Consumeable extends this by having a stat and StatAmount so that when a player uses a consumeable it increases the stat listed int "stat" and increases it by statAmount.


hope you enjoy my project 😄
