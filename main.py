import random
import numpy as np

if __name__ == '__main__':
    matrix_inp = []

    z_values = []
    states_model_values = []
    states_theory_values = []
    with open("states3.txt", "r") as f:
        lines = f.readlines()
        size = len(lines)
        for i in range(size):
            numbers = lines[i].split()
            row = [eval(j) for j in numbers]
            matrix_inp.append(row)
    f.close()
    matrix = np.array(matrix_inp)
    transitions = [0 for i in range(size)]
    z = int(input('Введите начальное состояние: '))
    stoch_state = np.full(size, 1 / size)
    #stoch_state = np.zeros(size)
    #stoch_state[z] = 1
    steps_number = int(input('Введите количество шагов: '))
    for i in range(steps_number):
        rand_n = random.random()
        border = 0.0
        prob_ints = sorted(range(size), key=lambda k: matrix[z][k])
        for j in range(size):
            border += matrix[z][prob_ints[j]]
            if rand_n <= border:
                transitions[prob_ints[j]] += 1
                probabilities = []
                s = sum(transitions)
                for k in range(size):
                    p = transitions[k] / s
                    probabilities.append(p)
                states_model_values.append(probabilities)
                z = prob_ints[j]
                z_values.append(z)
                break
        stoch_state = np.dot(stoch_state, matrix)
        states_theory_values.append(stoch_state)

    with open("results3.txt", "w") as f2:
        for i in range(steps_number):
            states_model_formatted = ['%.3f' % elem for elem in states_model_values[i]]
            states_model_formatted = "[{0}]".format(', '.join(map(str, states_model_formatted)))
            np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
            states_theorie_formatted = np.array2string(states_theory_values[i], separator=', ')
            f2.write(str(i) + "\t" + str(z_values[i]) + "\t" + str(states_model_formatted) + "\t" + str(states_theorie_formatted) + "\n")
    f2.close()
