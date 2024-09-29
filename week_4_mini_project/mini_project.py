import json

def dictionary(word):

    file = open('week_4_mini_project\data.json', 'r')

    with open('week_4_mini_project\data.json', 'r') as file:
        data = json.load(file)
    