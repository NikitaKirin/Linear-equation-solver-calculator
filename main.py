import core.method_of_Cramer as calc

matrix_of_variables = []
matrix_of_free = []
while True:
    line = input(
        'Вводите коэффициенты при неизвестных построчно через пробел! - для остановки ввода введите Stop' + '\n')
    if line == "Stop":
        break
    else:
        line = line.split(' ')
        current_line = [int(i) for i in line]
    matrix_of_variables.append(current_line)

while True:
    line = input(
        'Вводите свободные переменные построчно! - для остановки ввода введите Stop' + '\n')
    if line == "Stop":
        break
    else:
        line = line.split(' ')
        current_line = [int(i) for i in line]
    matrix_of_free.append(current_line)

answer = calc.method_of_cramer(matrix_of_variables, matrix_of_free)

print('Ответ:' + '\n')
for j in range(len(answer)):
    print(f'X{j + 1} = {answer[j]}')
