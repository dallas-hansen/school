import requests
import json

#Random cat facts api
#print(response.statuscode)
#print(response.json())
response = requests.get('https://meowfacts.herokuapp.com/')
#response2 = requests.get('https://meowfacts.herokuapp.com/?count=2')
#response3 = requests.get('https://meowfacts.herokuapp.com/?count=3')
#response4 = requests.get('https://meowfacts.herokuapp.com/?count=4')
#response5 = requests.get('https://meowfacts.herokuapp.com/?count=5')

#print(response.json())

def jprint():
    text = json.dumps(response.json(), indent=4)
    print(text)

# json.loads('')
# see facts about cats
def numcatFacts():
    #userinput = input("You can choose 1 - 5 facts. How many facts do you want? (press q to quit): ")
    if user_input == '1':
        print(f'Your fact is {response.json()}:')
    elif user_input == '2':
        print(f'Your facts are: {response.json()}\n{response.json()}')
    elif user_input == '3':
        print(f'Your facts are: {response3.json()}\n{response.json()}\n{response.json()}')
    elif user_input == '4':
        print(f'Your facts are: {response4.json()}\n{response.json()}\n{response.json()}\n{response.json()}')
    elif user_input == '5':
        print(f'Your facts are: {response5.json()}\n{response.json()}\n{response.json()}\n{response.json()}\n{response.json()}\n{response.json()}')
    else:
        print('Invalid input. Please try again.')



#print(response.json())

if __name__ == '__main__':
    user_input = input("You can choose 1 - 5 facts. How many facts do you want? (press q to quit): ")
    while user_input != 'q':
        numcatFacts()
        break
    else:
        print('Goodbye!')