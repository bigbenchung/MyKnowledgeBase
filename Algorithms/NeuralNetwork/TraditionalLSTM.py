import numpy as np
from math import tanh, exp

class TraditionalLSTM:
    
    def __init__(self, initial_variables: dict) -> None:
        self.wf, self.bf = initial_variables["forget"]
        self.wi, self.bi = initial_variables["input"]
        self.wa, self.ba = initial_variables["activation"]
        self.wo, self.bo = initial_variables["output"]
        
        self.time_stamp = 0
        self.prev_y = 0
        self.prev_s = 0

    def inputVar(self, input):
        self.time_stamp += 1
        print()
        print(f"Time: {self.time_stamp}")
        print(f"Input values: {input}")
        print(f"(s{self.time_stamp-1}, y{self.time_stamp-1}) = ({self.prev_s}, {self.prev_y})\n")
        
        x, y = input[:-1], input[-1]
        
        f = self.forgetGate(x)
        print(f"f{self.time_stamp}: {f}")
        
        i = self.inputGate(x)
        print(f"i{self.time_stamp}: {i}")
        
        a = self.activationGate(x)
        print(f"a{self.time_stamp}: {a}")
        
        # Update internal state
        s = f * self.prev_s + i * a
        print(f"s{self.time_stamp}: {s}")
        
        o = self.outputGate(x)
        print(f"o{self.time_stamp}: {o}")
        
        pred_y = o * tanh(s)
        print(f"y{self.time_stamp}: {pred_y}")
        
        print(f"Error: {pred_y - y}")
        
        self.prev_s, self.prev_y = s, pred_y
        
    def forgetGate(self, input) -> float:
        return self.sigmoid(self.wf.dot(np.concatenate((input, np.array([self.prev_y])))) + self.bf)
    
    def inputGate(self, input) -> float:
        return self.sigmoid(self.wi.dot(np.concatenate((input, np.array([self.prev_y])))) + self.bi)
    
    def activationGate(self, input) -> float:
        return tanh(self.wa.dot(np.concatenate((input, np.array([self.prev_y])))) + self.ba)
    
    def outputGate(self, input) -> float:
        return self.sigmoid(self.wo.dot(np.concatenate((input, np.array([self.prev_y])))) + self.bo)
    
    def sigmoid(self, num) -> float:
        return 1/(1+exp(-num))
    
if __name__ == "__main__":
    initial_variables = {
        "forget": (np.array([0.7, 0.4, 0.1]), 0.1),
        "input": (np.array([0.2, 0.6, 0.7]), 0.4),
        "activation": (np.array([0.3, 0.2, 0.1]), 0.3),
        "output": (np.array([0.6, 0.3, 0.1]), 0.2)
    }
    
    # initial_variables = {
    #     "forget": (np.array([0.7, 0.3, 0.4]), 0.4),
    #     "input": (np.array([0.2, 0.3, 0.4]), 0.2),
    #     "activation": (np.array([0.4, 0.2, 0.1]), 0.5),
    #     "output": (np.array([0.8, 0.9, 0.2]), 0.3)
    # }
    
    t = TraditionalLSTM(initial_variables)
    
    # in form of x1, x2, y
    # inputs = [[0.1, 0.4, 0.3], [0.7, 0.9, 0.5]]
    inputs = [[0.3, 0.6, 0.2], [0.1, 1.0, 0.4]]
    for input in inputs:
        t.inputVar(np.array(input))