import numpy as np

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return np.sqrt(np.square(x1-x2) + np.square(y1-y2))

def G_sigma(sigma: float, x:float) -> float:
    return np.exp(-np.square(x)/(2*np.square(sigma))) / (2*np.pi*np.square(sigma))
    
def bilateral_filter(image: np.ndarray, spacial_sigma: float, range_sigma: float, kernel_size: int):
    def Wp(r: int, c: int) -> float:
        curr_sum = 0.0
        for r_offset in range(-center, center+1):
            for c_offset in range(-center, center+1):
                curr_sum += G_sigma(spacial_sigma, distance(r, c, r+r_offset, c+c_offset)) * G_sigma(range_sigma, image[r, c] - image[r+r_offset, c+c_offset])
        
        return curr_sum
    
    def BI(r: int, c: int) -> float:
        print(f"-----{r} {c}-----")
        W_p = Wp(r, c)
        print("W_p = ", W_p)
        
        curr_sum = 0.0
        for r_offset in range(-center, center+1):
            for c_offset in range(-center, center+1):
                curr_sum += G_sigma(spacial_sigma, distance(r, c, r+r_offset, c+c_offset)) * G_sigma(range_sigma, image[r, c] - image[r+r_offset, c+c_offset]) * image[r+r_offset, c+c_offset]
        print(curr_sum)
        return curr_sum / W_p
    
    row, col = image.shape
    
    center = kernel_size // 2
    output_img = np.zeros((row-center*2, col-center*2))
    output_img = output_img.astype(np.float32)
    
    for i in range(center, row-center):
        for j in range(center, col-center):
            output_img[i-center, j-center] = BI(i,j)
    
    return output_img
    

if __name__ == "__main__":
    image = np.array([[0,0,0,0,0,0], [0,1,1,1,1,0], [0,1,1,1,1,0], [0,1,0,0,1,0], [0,0,0,0,0,0]])
    print(bilateral_filter(image, 1,5,3))