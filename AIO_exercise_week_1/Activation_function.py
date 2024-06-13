#Calculate activation functions: Sigmoid, Relu, Elu
import math

def calc_sig(x):
    z = 1 / (1 + math.exp(-x))
    return z

def calc_relu(x):
    return max(0, x)

def calc_elu(x, alpha = 0.01):
    if x > 0:
        return x
    else:
        z = alpha * (math.exp(x) - 1)
        return z
    
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    x = input("Enter an interger number: ")
    activation_function = input("Enter activation function's name (sigmoid, relu, elu): ")

    if not is_number(x):
        print("x must be a number")
    elif activation_function not in ["sigmoid", "relu", "elu"]:
        print(f"{activation_function} is not supported")
    else:
        x = float(x)
        result = 0
        if activation_function == "sigmoid":
            result = calc_sig(x)
        elif activation_function == "relu":
            result = calc_relu(x)
        elif activation_function == "elu":
            result = calc_elu(x, alpha=0.01)
        print(f"{activation_function}: f({x}) = {result}")
