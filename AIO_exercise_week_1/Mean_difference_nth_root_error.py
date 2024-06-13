#Calculate Mean Difference of n_th Root Error Value

def md_nre_single_sample(y, yhat, n, p):
    final_md_nre_value = pow(y, 1/n) - pow(yhat, 1/n)
    print(f"Md_nre_single_value: {final_md_nre_value}")
    
if __name__ == '__main__':
    md_nre_single_sample(y = 0.6 ,yhat = 0.1, n = 2, p = 1)