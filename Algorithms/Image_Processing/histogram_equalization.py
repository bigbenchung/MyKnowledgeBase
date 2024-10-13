import numpy as np

def hist_equalize(image: np.ndarray, rk:np.ndarray, rounding_digit:int=0):
    flattened_image = image.flatten()
    N = flattened_image.size
    
    unique_elements, counts = np.unique(flattened_image, return_counts=True)
    
    pr_rk = dict()
    
    for r in rk:
        pr_rk[r] = 0
        
    for i, element in enumerate(unique_elements):
        pr_rk[element] = counts[i] / N
    
    print(f"Pr(r_k) = {pr_rk}")
    
    s_k = dict()
    curr_v = 0
    for k, v in pr_rk.items():
        curr_v += v
        s_k[k] = curr_v
    
    print(f"S_k * 1/7 = {s_k}")
    
    del pr_rk, curr_v
    
    output_mapper = dict()
    
    for k, v in s_k.items():
        output_mapper[k] = round(v * rk.max(), rounding_digit)
    
    print(f"Gray levels = {output_mapper}")
    
    vectorized_mapper = np.vectorize(output_mapper.get)
    return vectorized_mapper(image)

if __name__ == "__main__":
    image = np.array([[5,6,7,5,6], [7,1,5,6,5], [6,0,1,6,5], [7,7,5,3,7], [3,6,4,3,5]])
    print(hist_equalize(image, np.array([0,1,2,3,4,5,6,7]), 0))