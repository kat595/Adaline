import Adaline_model
import numpy as np
import Dataset

adalines = [Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5), Adaline_model.Adaline(7 * 5)] # tablica Adaline dla kazdej cyfry


def learn(): # funkcja do nauki dla perceptronu prawidlowych wzorcow
    data_x = [np.array(t).flatten() for t in Dataset.Data]

    for i in range(10):
        data_y = np.zeros(10)
        data_y[i] = 1
        adalines[i].train(data_x, data_y)


def decide(num): # funkcja rozpoznajaca wyklikany wzor na matrycy i pokazujaca w konsoli ktora to cyfra
    data_matrix = np.array(Dataset.Matrix).flatten()
    array_numbers = [[]] * 10
    max_value = 0
    # odszumianie automatyczne (% szans poprawności cyfry najbardziej prawdopodobnej zostaje zwiekszone)
    for i in range(10):
        array_numbers[i] = (int)(adalines[i].output(data_matrix) * 100)
        if array_numbers[i] > max_value:
            max_value = array_numbers[i]

    for i in range(10):
        if (int)(adalines[i].output(data_matrix) * 100) == max_value:
            print(i, ':', (int)(adalines[i].output(data_matrix) * 100 + num), '%')
        else:
            print(i, ':', (int)(adalines[i].output(data_matrix) * 100), '%')


def zaszum(): # przypisujemy większy wzrost % szans najprawdopodobniejszej cyfry
    decide(10)
