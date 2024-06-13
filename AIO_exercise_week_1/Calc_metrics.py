#Calculate metrics: F1-Score
import math

def calc_f1_score(tp, fp, fn):
    if (type(tp) != int):
        print("TP mus be int")
    if (type(fp) != int):
        print("FP must be int")
    if ((type(fn) != int)):
        print("FN must be int")
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    return f1_score

def is_number(n):
    try:
        float(n)  
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    assert round ( calc_f1_score ( tp =2 , fp =3 , fn =5) , 2) == 0.33
    print ( round ( calc_f1_score ( tp =2 , fp =4 , fn =5) , 2) )
    assert is_number(3) == 1.0
    assert is_number('-2a') == 0.0
    print(is_number(1))  
    print(is_number('n')) 