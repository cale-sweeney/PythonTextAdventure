#!/usr/bin/env python
from random import randint
import os

#Screen clearer
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Dice Roller
def diceroll():
	diceresult = randint(1,20)
	return diceresult

#Begin Game
cls()

print("Welcome to Cale's RPG")

print("What is your name?")
name = (input("Enter your name: "))

print ("Your name is: " + name)

cls()

#Look up how to do enumerations
print ("Choose a hero type: Cleric, Barbarian, Thief, Dwarf, Wizard, or Druid")
heroType = (input("Input your class: ")) 

print("Your hero type is: ")
print (heroType)

cls()

#develop a random number generator
#speed (how fast you can move)
speed = diceroll()
print("Speed: " + str(speed))

#stealth (ability not to be sensed)
stealth = randint(1,20)
print("Stealth: " + str(stealth))

#perception (ability to sense)
perception = randint(1,20)
print("Perception: " + str(perception))

#strength (physical offense)
strength = randint(1,20)
print("Strength: " + str(strength))

#toughness (physical defense)
#intelligence (attack magic) 
#wisdom (defense magic) 

#Look up how to do enumerations 
print("What land are you from? Plains, Mountains, Islands, Swamps, or Forest?")
homeLand = (input("Your home land is: ")) 
print ("Your home land is: " + homeLand)

cls()

print ("Hero Summary:") 
print(name) 
print(heroType) 
print(homeLand)
