import json
import os
import time

if os.path.exists("data.json"):
  with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

"""

Define the project:

Im going to be simulating a house in python.

Its going to have different rooms and everything.

"""

class Stove:
  def __init__(self, model, price):
    self.model = model
    self.price = price
  
  def turn_on(self):
    print("Turning on the stove")

  def turn_off(self):
    print("Turning off the stove.")
  
  def heat_up_stove(self):
    print("Heating up the stove... ")
    time.sleep(2)
    print("Stove heated up. ")

  def stop_heating_up_stove(self):
    print("Stopping heating up the stove")
    time.sleep(2)
    print("Stove stopped heating up. ")

class Refrigerator:
  def __init__(self, model, price):
    self.model = model
    self.price = price
    self.items = []

  def add_to_fridge(self, items):

    userInput = int(input("How many items are you adding to the fridge? (max 10) "))

    if userInput == 1:
      itemName = input("What is your ITEM NAME? ")
      itemDesc = input("What is your ITEM DESC? ")
      itemData = {"Name": itemName, "Desc": itemDesc}
      self.items.append(itemData)
      print("Item added to fridge! ") # For debugging.

    elif userInput > 1:
      print("Ok Multiple items...")
      i = 0
      while i < userInput:
        for i in range(userInput):
          itemName = input("What is your ITEM NAME? ")
          itemDesc = input("What is your ITEM DESC? ")
          itemData = {"Name": itemName, "Desc": itemDesc}
          self.items.append(itemData)
          print("Item added to fridge! ")
          print(f"Items in fridge: {[x["Name"] for x in self.items]}")
          with open("/practice/1/data/refridgerator.json", "w") as f:
            json.dump(self.items, f, indent=4)
    else:
      print(f"Item will not added to fridge. Insuffient amount of items: {userInput}")

  def remove_from_fridge(self):
    file_path = "/practice/1/data/refridgerator.json"
    if os.path.exists(file_path):
      with open(file_path, "r") as f:
        data = json.load(f)
    else:
      print("failed to load json> ERROR") # Debugging purposes. 

    userInput = input("What item do you want to remove from the fridge? ")

    new_data = [item for item in data if item["Name"] != userInput]

    if len(new_data) == len(data):
      print("Item not found in fridge. ")
    else:
      with open(file_path, "w") as f:
        json.dump(new_data, f, indent=4)
      print(f"Removed '{userInput}' from the fridge")
class Kitchen():
  def __init__(self):
    self.stove = Stove()
    self.refrigerator = Refrigerator()
    self.table = KitchenTable()
    self.island = Island()

class SmartHouse:
  def __init__(self, address, zipcode):
    self.address = address
    self.zipcode = zipcode

  def turn_on_lights(self):
    print("Turning on the lights...")

  def turn_off_lights(self):
    print("Turning off the lights...")