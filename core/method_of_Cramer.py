import core.det as det
import copy as copy


def method_of_cramer(matrix_of_variables, matrix_of_free_values):
    main_det = det.get_determination(matrix_of_variables)
    if main_det == 0:
        print('Решений нет или бесконечно много')
    else:
        result_solve = []
        for i in range(len(matrix_of_variables)):
            new_matrix = copy.deepcopy(matrix_of_variables)
            for j in range(len(matrix_of_free_values)):
                new_matrix[j][i] = matrix_of_free_values[j][0]
            det_current = det.get_determination(new_matrix)
            answer_current = det_current / main_det
            result_solve.append(round(answer_current))
            new_matrix.clear()
    return result_solve
