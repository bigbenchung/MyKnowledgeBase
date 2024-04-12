import numpy as np
from math import tanh, exp

class GRU:
    
    def __init__(self, initial_variables: dict) -> None:
        self.wr, self.br = initial_variables["reset"]
        self.wa, self.ba = initial_variables["activate"]
        self.wu, self.bu = initial_variables["update"]
        
        self.time_stamp = 0
        self.prev_y = 0

    def inputVar(self, input):
        self.time_stamp += 1
        print()
        print(f"Time: {self.time_stamp}")
        print(f"Input values: {input}")
        print(f"y{self.time_stamp-1} = {self.prev_y}\n")
        
        x, y = input[:-1], input[-1]
        
        r = self.resetGate(x)
        print(f"r{self.time_stamp}: {r}")

        a = self.activationGate(x, r)
        print(f"a{self.time_stamp}: {a}")
        
        u = self.updateGate(x)
        print(f"u{self.time_stamp}: {u}")
        
        pred_y = (1 - u) * self.prev_y + u * a
        print(f"y{self.time_stamp}: {pred_y}")
        
        print(f"Error: {pred_y - y}")
        
        self.prev_y = pred_y
        
    def resetGate(self, input) -> float:
        return self.sigmoid(self.wr.dot(np.concatenate((input, np.array([self.prev_y])))) + self.br)

    def activationGate(self, input, r) -> float:
        return tanh(self.wa.dot(np.concatenate((input, np.array([r*self.prev_y])))) + self.ba)
    
    def updateGate(self, input) -> float:
        return self.sigmoid(self.wu.dot(np.concatenate((input, np.array([self.prev_y])))) + self.bu)
    
    def sigmoid(self, num) -> float:
        return 1/(1+exp(-num))
    
if __name__ == "__main__":
    # initial_variables = {
    #     "reset": (np.array([0.7, 0.3, 0.4]), 0.4),
    #     "activate": (np.array([0.2, 0.3, 0.4]), 0.3),
    #     "update": (np.array([0.4, 0.2, 0.1]), 0.5)
    # }
    
    initial_variables = {
        "reset": (np.array([0.5, 0.2, 0.3]), 0.2),
        "activate": (np.array([0.2, 0.4, 0.1]), 0.1),
        "update": (np.array([0.1, 0.3, 0.2]), 0.1)
    }
    
    t = GRU(initial_variables)
    
    # in form of x1, x2, y
    # inputs = [[0.1, 0.4, 0.3], [0.7, 0.9, 0.5]]
    inputs = [[0.3, 0.6, 0.2], [0.1, 1.0, 0.4]]
    
    for input in inputs:
        t.inputVar(np.array(input))