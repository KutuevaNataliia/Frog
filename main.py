import random
import numpy as np

if __name__ == '__main__':
    matrix_inp = []

    z_values = []
    states_model_values = []
    states_teory_values = []
    with open("states.txt", "r") as f:
        lines = f.readlines()
        size = len(lines)
        for i in range(size):
            numbers = lines[i].split()
            row = [eval(j) for j in numbers]
            matrix_inp.append(row)
    f.close()
    matrix = np.array(matrix_inp)
    transitions = [[0 for i in range(size)] for j in range(size)]
    z = int(input('Введите начальное состояние: '))
    stoch_state = np.zeros(size)
    stoch_state[z] = 1
    steps_number = int(input('Введите количество шагов: '))
    for i in range(steps_number):
        z_values.append(z)
        rand_n = random.random()
        border = 0.0
        for j in range(size):
            if rand_n <= (border + matrix[z][j]):
                transitions[z][j] += 1
                probabilities = []
                s = sum(transitions[z])
                for k in range(size):
                    p = transitions[z][k] / s
                    probabilities.append(p)
                states_model_values.append(probabilities)
                z = j
                break
            border += matrix[z][j]
        stoch_state = np.dot(stoch_state, matrix)
        states_teory_values.append(stoch_state)

    with open("results.txt", "w") as f2:
        for i in range(steps_number):
            f2.write(str(i) + "\t" + str(z_values[i]) + "\t" + str(states_model_values[i]) + "\t" + str(states_teory_values[i]) + "\n")
    f2.close()


    # print(matrix)

