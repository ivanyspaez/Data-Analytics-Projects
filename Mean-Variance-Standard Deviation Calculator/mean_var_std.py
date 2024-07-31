import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.reshape(lista, (3, 3))

    # Cálculo de las estadísticas
    mean = np.mean(matriz, axis=0).tolist()
    mean2 = np.mean(matriz, axis=1).tolist()
    mean3 = np.mean(matriz).tolist()

    var = np.var(matriz, axis=0).tolist()
    var2 = np.var(matriz, axis=1).tolist()
    var3 = np.var(matriz).tolist()

    std = np.std(matriz, axis=0).tolist()
    std2 = np.std(matriz, axis=1).tolist()
    std3 = np.std(matriz).tolist()

    max = np.max(matriz, axis=0).tolist()
    max2 = np.max(matriz, axis=1).tolist()
    max3 = np.max(matriz).tolist()

    min = np.min(matriz, axis=0).tolist()
    min2 = np.min(matriz, axis=1).tolist()
    min3 = np.min(matriz).tolist()

    sum = np.sum(matriz, axis=0).tolist()
    sum2 = np.sum(matriz, axis=1).tolist()
    sum3 = np.sum(matriz).tolist()

    # Crear el diccionario con los resultados
    resultados = {
        'mean': [mean, mean2, mean3],
        'variance': [var, var2, var3],
        'standard deviation': [std, std2, std3],
        'max': [max, max2, max3],
        'min': [min, min2, min3],
        'sum': [sum, sum2, sum3]
    }

    return resultados

# Ejemplo de uso
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(calculate(lista))
