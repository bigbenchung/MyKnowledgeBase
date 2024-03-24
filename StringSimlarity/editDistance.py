from sys import argv

def calEditDistance(word1: str, word2: str) -> int:
    def generateMatrix(word1: str, word2: str) -> list[list[int]]:
        matrix = list()
        
        for i in range(0, len(word1)+1):
            if i == 0:
                matrix.append([j for j in range(0, len(word2)+1)])
            else:
                matrix.append([i])
                for j in range(1, len(word2)+1):
                    if word1[i-1] != word2[j-1]:
                        matrix[i].append(min([matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+1]))
                    else: 
                        matrix[i].append(matrix[i-1][j-1])
                    
        return matrix
    return generateMatrix(word1, word2)[len(word1)][len(word2)]

if __name__ == "__main__":
    calEditDistance(argv[1], argv[2])