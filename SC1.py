#Name: Owyn Jones
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemies = {
    "Skeleton" : {
        "damage" : 5,
        "health" : 20,
        "defense" : 1,
        "agility" : 3
    },
    "Creeper" : {
        "damage" : 10 ** 100,
        "health" : 15,
        "defense" : 3,
        "agility" : 4
    },
    "Zombie" : {
        "damage" : 3,
        "health" : 20,
        "defense" : 5,
        "agility" : 5
    },
    "Santa" : {
        "damage" : 1225,
        "health" : 1000000000000,
        "defense" : 1000000000000,
        "agility" : 100
    },
    "Lil Jimmy" : {
        "damage" : 1,
        "health" : 1,
        "defense" : 1,
        "agility" : 1
    }
}
enemy = input("Select the enemy whose damage you would like to change \n(Skeleton, Creeper, Zombie, Santa, or Lil Jimmy): ")
print("Current damage is: ", enemies[enemy]["damage"])
newDamage = float(input("Input the adjusted damage value: "))
enemies[enemy].update({"damage" : newDamage})
print("New damage is: ", enemies[enemy]["damage"])