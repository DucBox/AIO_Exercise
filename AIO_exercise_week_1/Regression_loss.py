#Calc loss value using regression loss function

import math
import sys
import random
from statistics import mean

def calc_mae(y, yhat):
    loss_list = []
    for i in range(len(y)):
        loss = abs(y[i] - yhat[i])
        print(f"sample: {i}, pred: {yhat[i]}, target: {y[i]}, loss: {loss}")
        loss_list.append(loss)
    final_loss = mean(loss_list)
    print(f"Final MAE loss value: {final_loss}")
    
def calc_mse(y, yhat):
    loss_list = []
    for i in range(len(y)):
        loss = (y[i] - yhat[i]) ** 2
        print(f"sample: {i}, pred: {yhat[i]}, target: {y[i]}, loss: {loss}")
        loss_list.append(loss)
    final_loss = mean(loss_list)
    print(f"Final MSE loss value: {final_loss}")
    
def calc_rmse(y, yhat):
    loss_list = []
    for i in range(len(y)):
        loss = (y[i] - yhat[i]) ** 2
        print(f"sample: {i}, pred: {yhat[i]}, target: {y[i]}, loss: {loss}")
        loss_list.append(loss)
    final_loss = math.sqrt(mean(loss_list))
    print(f"Final RMSE loss value: {final_loss}")
    
def check_samples_input_valid(num_samples):
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return False
    
if __name__ == '__main__':
    y = []
    yhat = []
    num_samples = input("Input number of samples ( integer number ) which are generated: ")
    loss_function = input("Input loss function's name (mae|mse|rmse): ")
    
    if check_samples_input_valid(num_samples) == False:
        sys.exit()
    else:
        for i in range(int(num_samples)):
            random_y_value = random.uniform(0, 9)
            y.append(random_y_value)
            random_yhat_value = random.uniform(0,9)
            yhat.append(random_yhat_value)
        if loss_function == 'mae':
            calc_mae(y, yhat)
        elif loss_function == 'mse':
            calc_mse(y, yhat)
        else:
            calc_rmse(y, yhat)
        
            
        
    