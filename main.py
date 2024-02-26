#      IMPORTS SECTION
import random
import sys
from random import randint
from time import sleep

import replit

from Section2 import battle

#      FUNCTIONS SECTION



typing_speed = 50 #wpm

def slowPrint(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(random.random()*10.0/typing_speed)
    print('')

def giveQuest(name, requirements, inventory):
  print("You got a quest")
  for item in requirements:

    print(
        f"You have to get {requirements[item]['qty']} {requirements[item]['name']}"
    )
  if requirements in inventory:
    print('You have all the items you need')
    mainIN = input(f'Complete [{name}] Yes or No')
    if mainIN == 'Yes':
      take(requirements[item]['name'], requirements[item]['qty'])
    else:
      print('You did not complete the quest')
  else:
    print('You do not have the items you need')


def world(lvl, inv):
  ran = randint(1, 2)
  if lvl == 1:
    if ran == 1:
      print(
          "You come across an abandoned pagoda adorned in cobwebs and moss. You see a shrine with a scythe with special runes enscribed on it laying on the shrine"
      )
      give('Ancient Scythe', 1)
    elif ran == 2:
      print(
          "You come across a small cave with a small fire in the center of it. You sit by the fire and a hooded man comes out of the shadows and asks you a question"
      )
      print("Hooded Man:  I am getting sick with a horrible sickness")
      print("Hooded Man:  I need you to help me")
      print("Hooded Man:  Will you accept my quest")
      mainIN = input("Yes or No: ")
      if mainIN == "Yes":
        print("Hooded Man:  Thank you")
        giveQuest('Heal the Hooded man',
                  {'Lotus fern': {
                      'qty': 5,
                      'name': 'Lotus fern'
                  }}, inv)
      else:
        print("Hooded Man:  Okay")





def text_to_speech(text):
  #replit with the text to convertreplit(text)

  # Save the audio file to a temporary file
  speech_file = 'speech.mp3'
  speech.save(speech_file)

  # Play the audio file
  #play_audio_file(speech_file)
  # Remove the temporary audio file
  #os.remove(speech_file)


player_starter_kit = {
    "Katana": 1,
    "Kimono": 1,
    "Samurai Shield": 1,
    "Shurikens": 10
}


def error(cause):
  if cause == "program":
    print("[ERROR] programmer error:  Incorrect code")
  elif cause == "input":
    print("[ERROR] input error:  Incorrect input")
  else:
    print("[ERROR] undefined error")


def clear():
  replit.clear()


def loading(t):
  p = t / 100
  while t != p:

    clear()
    print(f"Loading {p}%")
    sleep(p)
    clear()
    p += p


def setup():
  global player_inventory
  global player_starter_kit
  print('Setting up...')
  player_inventory = player_starter_kit
  sleep(4)
  clear()
  print('Setup complete!')
  sleep(1)
  clear()


def give(item, qty):
  if item in japanese_game_items:
    if item in player_inventory:
      player_inventory[item] += qty
    else:
      player_inventory[item] = qty
  else:
    error("program")


def take(item, qty):
  if item in player_inventory:
    player_inventory[item] -= qty


#      ITEMS SECTION

effect_index = {
    "hpboost": {
      "name": "hpboost",
      "effect_modifier": "5",
      "effect_type": "add"
    },
    "heal": {
      "name": "heal",
      "effect_modifier": "5",
      "effect_type": "reset"
    }
}

japanese_game_items = {
    "Katana": {
        "value": 10,
        "class": "weapon",
        "class_value": 10
    },
    "Fist": {
        "value": 0,
        "class": "weapon",
        "class_value": 5
    },
    "Kimono": {
        "value": 15,
        "class": "armorS2",
        "class_value": 35
    },
    "Samurai Shield": {
        "value": 20,
        "class": "shield",
        "class_value": 45
    },
    "Shurikens": {
        "value": 25,
        "class": "weapon",
        "class_value": 3
    },
    "null": {
        "value": 0,
        "class": "null",
        "class_value": 0
    },
    "Lotus fern": {
        "value": 5,
        "class": "quest_item",
        "class_value": 0
    },
    "Ancient Scythe": {
       "value": 50,
       "class": "weapon",
       "class_value": 12
    },
    "Potion of tranquility": {
        "value": 10,
        "class": "potion",
        "subclass": "support potion",
        "effect": "hpboost"
      
    },
}

japanese_game_items["Katana"]["class_value"]
#      VARIABLES SECTION
player_health = 30
player_health_max = 30
player_money = 0
player_armorS1 = "null"
player_armorS2 = "null"
player_weapon = "Fist"
player_shield = "null"

player_ATK = japanese_game_items[player_weapon]["class_value"]
player_DEF = japanese_game_items[player_armorS1][
    "class_value"] + japanese_game_items[player_armorS2]["class_value"]
player_S = japanese_game_items[player_shield]["class_value"]

player_inventory = {
    "Katana": 1,
    "Kimono": 1,
    "Samurai Shield": 1,
    "Shurikens": 10
}
#      MAIN PROGRAM SECTION
mainCode = 'null'
setup()
slowPrint('Welcome to the world of Mahō no mori')
sleep(1)
slowPrint('It is a mystical world overrun with a band of evil samurai')
sleep(1)


while True:
   print('Type "help" for a list of commands')
   main = input("> ")

   if main == "arena":
     print("You have entered the Lotus Arena")
     sleep(1)
     print('Your opponent is...')
     sleep(1)
     print('The Evil Samurai')
     sleep(1)

     player_ATK = japanese_game_items[player_weapon]["class_value"]
     player_DEF = japanese_game_items[player_armorS1][
         "class_value"] + japanese_game_items[player_armorS2]["class_value"]
     player_S = japanese_game_items[player_shield]["class_value"]

     if battle(player_health, player_ATK, player_DEF, player_S, 30, 5, 2, 3,
               "Evil Samurai"):
       give("Samurai Shield", 1)

   elif main == "stats":
     #CALCULATE PLAYER STATS
     player_ATK = japanese_game_items[player_weapon]["class_value"]
     player_DEF = japanese_game_items[player_armorS1][
         "class_value"] + japanese_game_items[player_armorS2]["class_value"]
     player_S = japanese_game_items[player_shield]["class_value"]

     # PRINTS PLAYER STATS
     print(f"Health: {player_health}")
     print(f"Money: {player_money}")
     print(f"Armor: {player_armorS1} {player_armorS2}")
     print(f"Weapon: {player_weapon}")
     print(f"Shield: {player_shield}")
     print(f"\nATK: {player_ATK}")
     print(f"DEF: {player_DEF}")
     print(f"Inventory: {player_inventory}")
     print("Do equip to change what is in the Armor, Weapon, Shield slots")

   elif main == "equip":
     print("What would you like to equip?")
     equipIn = input("> ")
     if equipIn in player_inventory and equipIn in japanese_game_items:
       if japanese_game_items[equipIn]["class"] == "armorS1":
         player_armorS1 = equipIn
       elif japanese_game_items[equipIn]["class"] == "armorS2":
         player_armorS2 = equipIn
       elif japanese_game_items[equipIn]["class"] == "weapon":
         player_weapon = equipIn
       elif japanese_game_items[equipIn]["class"] == "shield":
         player_shield = equipIn
   elif main == "world":
     world(1, player_inventory)


