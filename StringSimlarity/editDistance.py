from sys import argv

def calEditDistance(word1: str, word2: str) -> int:
    if not word1 and not word2:
        return 0
    elif not word1:
        return len(word2)
    elif not word2:
        return len(word1)
    
    prev_row = [j for j in range(0, len(word2)+1)]
    word1_len = len(word1)
    
    for i in range(1, word1_len+1):
        new_row = [i]
        for j in range(1, len(word2)+1):
            if word1[i-1] != word2[j-1]:
                new_row.append(min([prev_row[j]+1, new_row[j-1]+1, prev_row[j-1]+1]))
            else: 
                new_row.append(prev_row[j-1])
        prev_row = new_row
    
    return prev_row[-1]

if __name__ == "__main__":
    calEditDistance(argv[1], argv[2])