my_grades = {
    'discussionForms': [7.78, 8.60, 10, 10, 9, 9.63, 8.67],
    'learningJournals': [9.80, 10, 10, 10, 10, 10],
    'assignments': [85, 80, 90],
}

# From Section 11.5 of:
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press.

# print(my_grades)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for grade in val:
            if grade not in inverse:
                inverse[grade] = [key]
            else:
                inverse[grade].append(key)
    return inverse

dic = invert_dict({'1': '10', '2': '10', '3': '20'})

print(dic)
# print(invert_dict({'1': 10, '2': 10, '3': 20}))
# grades = invert_dict(my_grades)

# print(grades)

# with open('grades.csv', 'w') as file:
#     file.write('grade, assignment(s)\n')
#     for g in sorted (grades):
#         file.write('{}, {}\n'.format(g, grades[g]))