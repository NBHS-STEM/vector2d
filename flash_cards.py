def print_conversion(vector, str): 
    if str == "polar":  
        print(30 * "-")
        print(f"Convert {vector.x}i + {vector.y}j to polar form") 
        print(30 * "-")
    elif str == "rectangular":  
        print(30 * "-")
        print(f"Convert <{abs(vector)}, {vector.angle()}> to rectangular form") 
        print(30 * "-")