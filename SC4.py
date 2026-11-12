#Name: Owyn Jones
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.

#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all the ratings.

ratingList = []
players = int(input("How many players? "))
for i in range(players):
    rating = int(input(f"Player {i + 1} rating (1-5): "))
    if rating > 5 or rating < 1:
        valid = False
        print("Invalid rating")
        break
    valid = True
    ratingList.append(rating)
if valid:
    ratingAverage = sum(ratingList) / players
    print(round(ratingAverage, 2))
