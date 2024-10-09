import random

def unique_random_ints(how_many, max_num) -> list:
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""

    # Type your code here. #
    global retries 
    random_int = []
    for i in range(how_many):
        temp_num = random.randint(0, max_num)
        
        while temp_num in random_int:
            retries += 1
            temp_num = random.randint(0, max_num)
        
        random_int.append(temp_num)

    return random_int
    


if __name__ == '__main__':
    seed = int(input())
    how_many = int(input())
    max_num = int(input())
    retries = 0

    # Type your code here. #
    random.seed(seed)
    rand_num = unique_random_ints(how_many, max_num)
    for i in rand_num:
        print(i, end=' ')
    print(f'retries={retries}')
    
