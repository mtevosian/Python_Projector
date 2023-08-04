#1. Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
#To each file append a random number between 1 and 100. 
#Create a summary file (summary.txt) that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98

import random
summary_file = "summary.txt"
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in alphabet:
    with open(f"{i}.txt", 'a') as file1, open(summary_file, 'a') as summary:
        number = str(random.randint(1, 100))
        file1.write(number)
        summary.write(f" {i}.txt: ")
        summary.write(number)

# 2. Create a file with some content. As example, you can take this one:
# “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum”.
# Create a second file and copy the content of the first file to the second file in upper case.

with open("Lorem ipsum.txt", 'a') as lorem_ipsum:
    lorem_ipsum.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n'
                'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n'
                'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n'
                'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    
with open("Lorem ipsum.txt", 'r') as lorem_ipsum, open("Lorem ipsum uppercase.txt", 'a') as lorem_ipsum_uppercase:
    text = lorem_ipsum.read()
    lorem_ipsum_uppercase.write(text.upper())

#3. Write a program that will simulate user scores in a game. 
# Create a list with 5 players’ names after that simulate 100 rounds for each player. 
# As a result of the game create a list with the player's name and score (0-1000 range). 
# And save it to a CSV file. 
# The file should look like this:

# Player name, Score
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345
# ...

import csv

users = ['Kate', 'Mary', 'Luke', 'Mark', 'Josh']

with open('user_scores.csv', 'a') as score:
    header = ['Player name', 'Score']
    writer = csv.DictWriter(score, fieldnames=header)
    writer.writeheader()
    for i in range(10):
        for n in users:
            name = (f'{n}')
            number = random.randint(1, 1000)
            writer = csv.DictWriter(score, fieldnames=header)
            writer.writerow({'Player name':name, 'Score':number})


#4. Write a script that reads the data from the previous CSV file and creates a new file called high_scores.csv where each row contains the player name and their highest score. 
# The final score should be sorted by descending to the highest score. 
# The output CSV file should look like this:

# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345

kate_list = []
mary_list = []
luke_list  = []
mark_list  = []
josh_list = []

with open('user_scores.csv', 'r') as score, open('high_scores.csv', 'a') as high_score:
    reader = csv.DictReader(score)
    header = ['Player name', 'Highest Score']
    writer = csv.DictWriter(high_score, fieldnames=header)
    writer.writeheader()
    for row in reader:
        name = row['Player name']
        score_1 = int(row['Score'])
        if name == 'Kate':
            kate_list.append(score_1)
        elif name == 'Mary':
            mary_list.append(score_1)
        elif name == 'Luke':
            luke_list.append(score_1)
        elif name == 'Mark':
            mark_list.append(score_1)        
        elif name == 'Josh':
            josh_list.append(score_1)
    kate_list.sort(reverse = True)
    mary_list.sort(reverse = True)
    luke_list.sort(reverse = True)
    mark_list.sort(reverse = True)
    josh_list.sort(reverse = True)
    writer.writerow({'Player name': 'Kate', 'Highest Score': f'{kate_list[0]}'})
    writer.writerow({'Player name': 'Mary', 'Highest Score': f'{mary_list[0]}'})
    writer.writerow({'Player name': 'Luke', 'Highest Score': f'{luke_list[0]}'})
    writer.writerow({'Player name': 'Mark', 'Highest Score': f'{mark_list[0]}'})
    writer.writerow({'Player name': 'Josh', 'Highest Score': f'{josh_list[0]}'})