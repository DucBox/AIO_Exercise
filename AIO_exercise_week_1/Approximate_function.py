#Calc approximate function value

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    
def calc_approximate_sin(x, n):
    sin_approx = 0
    for i in range(n): 
        sin_approx += ((-1) ** i) * ((x ** (2 * i + 1)) / factorial(2 * i + 1))
    print(f"Approximate Sin Vale: {sin_approx}")
    
def calc_approximate_cos(x, n):
    cos_approx = 0
    for i in range(n):
        cos_approx += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    print(f"Approximate Cos Vale: {cos_approx}")
    
def calc_approximate_sinh(x, n):
    sinh_approx = 0
    for i in range(n):
        sinh_approx += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    print(f"Approximate Sinh Vale: {sinh_approx}")

def calc_approximate_cosh(x, n):
    cosh_approx = 0
    for i in range(n):
        cosh_approx += (x ** (2 * i)) / factorial(2 * i)
    print(f"Approximate Cosh Vale: {cosh_approx}")

if __name__ == '__main__':
    # calc_approximate_sin(x = 3.14 , n = 10)
    # calc_approximate_cos(x = 3.14 , n = 10)
    # calc_approximate_sinh(x = 3.14 , n = 10)
    # calc_approximate_cosh(x = 3.14 , n = 10)
    # assert round( calc_approximate_cos ( x =1 , n =10) , 2) ==0.54
    calc_approximate_cosh ( x =3.14, n =10)