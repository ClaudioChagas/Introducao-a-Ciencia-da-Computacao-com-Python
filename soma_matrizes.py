def soma_matrizes(m1, m2):
    if(len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        return False
    result = []
    for i in range(len(m1)):   
        result.append([])
        for j in range(len(m1[0])):
            result[i].append(m1[i][j] + m2[i][j])
    return result


m1 = input("Digite a primeira matriz: ")
m2 = input("Digite a segunda matriz: ")




