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