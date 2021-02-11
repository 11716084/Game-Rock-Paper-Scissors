import random
name = input('Enter your name: ')
print("Hello, " + name)

player_rating = {}
with open('rating.txt', 'r') as rating_file:
    for line in rating_file:
        if line.split()[0] == name:
            score = int(line.split()[1])
            break
        else:
            score = 0

rating_file.close()

while True:
    user = input()
    lose_conditions = {"rock": "paper",
                       "paper": "scissors",
                       "scissors": "rock"}
    computer = random.choice(list(lose_conditions.keys()))
    if user == '!exit':
        print("Bye!")
        break
    if user == '!rating':
        print("Your rating: ", score)
        continue
    if user != computer and user != 'rock' and user != "paper" and user != "scissors" and user != '!rating':
        print("Invalid input")
        continue
    if user == computer:
        print(f"There is a draw {computer}")
        score += 50
    elif lose_conditions[user] == computer:
        print(f"Sorry, but the computer chose {computer}")
    elif lose_conditions[user] != computer:
        print(f"Well done. The computer chose {computer} and failed")
        score += 100





# import random
# name = input('Enter your name: ')
#
# print("Hello, " + name)
# player_rating = {}
# with open('rating.txt', 'r') as rating_file:
#     for rating in rating_file:
#         player_name, score = rating.split(sep=" ")
#         player_rating[player_name] = int(score)
#
# if name in player_rating:
#     player_score = int(score)
#
#
# while True:
#     user = input()
#     lose_conditions = {"rock": "paper",
#                        "paper": "scissors",
#                        "scissors": "rock"}
#     computer = random.choice(list(lose_conditions.keys()))
#     if user == '!exit':
#         print("Bye!")
#         break
#     if user == '!rating':
#         print("Your rating: " + str(player_rating[name]))
#         continue
#     if user != computer and user != 'rock' and user != "paper" and user != "scissors" and user != '!rating':
#         print("Invalid input")
#         continue
#     if user == computer:
#         print(f"There is a draw {computer}")
#         player_rating[name] += 50
#     elif lose_conditions[user] == computer:
#         print(f"Sorry, but the computer chose {computer}")
#     elif lose_conditions[user] != computer:
#         print(f"Well done. The computer chose {computer} and failed")
#         player_rating[name] += 100





