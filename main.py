import core.method_of_Cramer as calc

matrix_of_variables = []
matrix_of_free = []
count_line = 0
count_free_line = 0
while True:
    line = input(
        'Вводите коэффициенты при неизвестных построчно через пробел! - для остановки ввода введите Stop' + '\n')
    if line == "Stop":
        break
    else:
        line = line.split(' ')
        current_line = [int(i) for i in line]
        count_line += 1
    matrix_of_variables.append(current_line)

while True:
    line = input(
        'Вводите свободные переменные построчно! - для остановки ввода введите Stop' + '\n')
    if line == "Stop":
        break
    else:
        line = line.split(' ')
        current_line = [int(i) for i in line]
        count_free_line += 1
    matrix_of_free.append(current_line)

if count_line != count_free_line:
    print("Данные введены не в правильном формате")
else:
    answer = calc.method_of_cramer(matrix_of_variables, matrix_of_free)
    print('Ответ:' + '\n')
    for j in range(len(answer)):
        print(f'X{j + 1} = {answer[j]}')
