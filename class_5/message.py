message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

def print_list():
    names = create_names_list()
    assignments = create_assignments_list()
    grades = create_grades_list()
    for name, assignment, grade in zip(names, assignments, grades):
        print(message.format(name, assignment, grade, int(grade) + int(assignment) * 2))

def create_names_list():
    i = 0
    names = []
    while i < 4:
        names.append(input("Entre com o nome do aluno: ".title()))
        i += 1
    return names

def create_assignments_list():
    i = 0
    assignments = []
    while i < 4:
        assignments.append(int(input("Entre com a quantidade de tarefas perdidas: ".title())))
        i += 1
    return assignments

def create_grades_list():
    i = 0
    grades = []
    while i < 4:
        grades.append(int(input("Entre o valor da nota: ".title())))
        i += 1
    return grades

print(print_list())
