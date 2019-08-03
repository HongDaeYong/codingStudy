from itertools import combinations


def solution(relation):
    answer_list = []
    num_row = len(relation)
    num_col = len(relation[0])

    def checkIfUnique(column):
        if len(column) != 0 and len(column) == len(set(column)):
            return True
        else:
            return False

    def make_tuples_list(relation_dict, keys):
        if len(keys) == 1:
            return relation_dict[keys[0]]
        tuples_list = []
        for i in range(num_row):
            one_case = []
            for key in keys:
                one_case.append(relation_dict[key][i])
            tuples_list.append(tuple(one_case))
        return tuples_list

    col_relation = {i: [] for i in range(num_col)}
    for row in relation:
        for i, ele in enumerate(row):
            col_relation[i].append(ele)

    for i in range(num_col):
        key_list = list(combinations(col_relation.keys(), i+1))
        for keys in key_list:

            need_to_examine = True
            for ele in answer_list:
                if set(keys).issubset(set(ele)) or set(ele).issubset(set(keys)):
                    need_to_examine = False

            if need_to_examine:
                combinations_list = make_tuples_list(col_relation, keys)
                if checkIfUnique(combinations_list):
                    answer_list.append(keys)
    print(answer_list)
    return len(answer_list)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))

