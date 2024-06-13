def levenshtein_distance(s1, s2):
    d = []
    for i in range(len(s1) + 1):
        row = []
        for j in range(len(s2) + 1):
            row.append(0)
        d.append(row)

    for i in range(len(s2) + 1):
        d[0][i] = i
    for i in range(len(s1) + 1):
        d[i][0] = i

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2)+ 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + cost)
    return d

if __name__ == '__main__':
    s1 = "kitten"
    s2 = "sitting"
    matrix = levenshtein_distance(s1, s2)
    print(f'Full matrix is {matrix}')
    print(f'Shortest distance is {matrix[len(s1)][len(s2)]}')
    