#Create a program that allows you to search for images in gif format. 
# The program should allow you to enter a search word. 
# Using this word, search for GIFs using the Giphy API. 
# As a result, print the links to the GIFs.

import requests
user_input = str(input('what gif do you want to see?')) 

giphy = requests.get(
    'https://api.giphy.com/v1/gifs/search', 
    params={
        'api_key':'lNBxZsiLW91HYr1wTh2KYcIyYPfmaTUd',
        'q':user_input,
        'limit': 1,
        })

print(giphy.json()['data'][0]['url'])