import math

def p2p_distance(x1, y1, x2, y2):
    diff_x = (x2 - x1)^2
    diff_y = (y2 - y1)^2
    return math.sqrt(diff_x + diff_y)



def add_two_ints(a, b):
    return a + b

def main():
    print("\nWelcome to main\n")
    input1 = input("\nPlease enter first number")
    input2 = input("\nPlease enter second number")
    result = add_two_ints(input1, input2)
    print("\nResult of adding two numbers")
    print(result)

    print("\nFinding distance between (-2,-2) and (2,2)\n")
    result = p2p_distance(-2, -2, 2, 2)
    print("\nResult\n")
    print(result)
    print("\nEnd of main\n")

main()