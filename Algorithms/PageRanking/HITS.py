import numpy as np

def HITS(connections: list[tuple[str, str]]):
    unique_node = set()
    temp_tracker = dict()
    
    for _from, _to in connections:
        if _from in temp_tracker.keys():
            temp_tracker[_from].add(_to)
        else:
            temp_tracker[_from] = {_to}
        unique_node.add(_to)
        unique_node.add(_from)
    
    n = len(unique_node)
    
    M = np.zeros((n,n))
    sorted_nodes = sorted(unique_node)
    
    for i in range(n):
        for j in range(n):
            from_node, to_node = sorted_nodes[i], sorted_nodes[j]
            if from_node in temp_tracker.keys():
                if to_node in temp_tracker[from_node]:
                    M[i][j] = 1
    
    del temp_tracker
    
    print(sorted_nodes)
    for i in range(n):
        print(sorted_nodes[i], M[i])
    
    def iterate(M: np.array, mode:str):
        matrix = np.dot(M, np.transpose(M)) if mode == "h" else np.dot(np.transpose(M), M)
        
        if mode == "h":
            print("\n------- Hub -------\n")
        else:
            print("\n---- Authority ----")
        
        print(sorted_nodes)
        for i in range(n):
            print(sorted_nodes[i], M[i])
        
        iteration_no = 1
        
        while True:
            print(f"*****Iteration: {iteration_no}*****")
            if iteration_no == 1:
                non_normalized, normalized = np.array([1]*n), np.array([1]*n)
                print(non_normalized, normalized)
            else:
                non_normalized = np.dot(normalized, matrix)
                print("non-normalized")
                print(sorted_nodes)
                print(non_normalized)
                
                new_normalized = non_normalized * n / np.sum(non_normalized)

                if all(new_normalized == normalized):
                    break
                
                normalized = new_normalized
            iteration_no += 1
            print()
        
    iterate(M, "h")
    iterate(M, "a")

if __name__ == "__main__":
    connections = [
        ("N", "N"),
        ("N", "A"),
        ("N", "M"),
        ("M", "A"),
        ("A", "M"),
        ("A", "N"),
    ]
    HITS(connections)