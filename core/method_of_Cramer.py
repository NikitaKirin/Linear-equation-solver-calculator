import core.det as det
import copy as copy


def method_of_cramer(matrix_of_variables, matrix_of_free_values):
    # Вычисляем главный определитель матрицы
    main_det = det.get_determination(matrix_of_variables)
    # Если главный определитель равен нулю, выводим сообщение, соответствующее теории
    if main_det == 0:
        print('Решений нет или бесконечно много')
    else:
        # Создаем массив, в котором будем формировать результат
        result_solve = []
        # Внешним циклом бежим по строкам матрицы с коэффициентами при не известных, внутренним - по матрице со
        # свободными числами
        for i in range(len(matrix_of_variables)):
            # Копируем матрицу с коэффициентами в новую матрицу, для создания миноров
            new_matrix = copy.deepcopy(matrix_of_variables)
            # Формируем миноры и проводим с ними вычисления
            for j in range(len(matrix_of_free_values)):
                new_matrix[j][i] = matrix_of_free_values[j][0]
            # Вычисляем определитель для каждой неизвестной
            det_current = det.get_determination(new_matrix)
            answer_current = det_current / main_det
            result_solve.append(round(answer_current))
            new_matrix.clear()
    return result_solve
