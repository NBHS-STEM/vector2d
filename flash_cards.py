import random
from vector2d import Vector2d
def print_conversion(vector, str): 
    if str == "polar":  
        print(40 * "-")  
        print(f"Convert {vector.x}i + {vector.y}j to polar form")
        print(40 * "-")
    elif str == "rectangular":  
        print(40 * "-")
        print(f"Convert <{abs(vector)}, {vector.angle()}> to rectangular form") 
        print(40 * "-") 
    
def generate_vector():  
    random_x = random.randint(-20,21) 
    random_y = random.randint(-20,21)
    return Vector2d(random_x, random_y) 

def print_conversion_solution(vector, str): 
    if str == "polar": 
        print(f"<{abs(vector)}, {vector.angle()}>") 
    elif str == "rectangular": 
        print(f"{vector.x}i + {vector.y}j")