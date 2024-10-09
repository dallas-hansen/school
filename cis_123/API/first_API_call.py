import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def main():
    response = requests.get("http://api.open-notify.org/astros.json")
    people_list = response.json()['people']
    number_in_space = response.json()['number']
    
    person_name = ''
    craft_name = ''
    
    print(f'There are currently {number_in_space} people in space')
    
    for person in people_list:
        for k,v in person.items():
            if k == 'craft':
                craft_name = v
                if len(person_name) > 0 and len(craft_name) > 0:
                    print(f'Astronaut: {person_name} is on board {craft_name}')
            elif k == 'name':
                person_name = v

if __name__ == "__main__":
    main()