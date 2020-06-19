import json
my_grades = {}

# From Section 11.5 of:
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press.

# Read json from file, it has our key value pairs
with open('input.json', 'r') as file:
    # This line will parse it and we'll have our dictionary in my_grades
    my_grades = json.load(file)

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


grades = invert_dict(my_grades)


with open('grades.csv', 'w') as file:
    file.write('grade, assignment(s)\n')
    for g in sorted(grades):
        file.write('{}, {}\n'.format(g, grades[g]))
