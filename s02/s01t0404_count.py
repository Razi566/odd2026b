# Creamos una lista de estudiantes 
student_list_01 = ['Valeria','Omar','Joss','Daniel']

def random_function(students):
    first = students[0] # O(n)
    total = 0 # O(n)
    new_list = [] # O(1)
    for student in students:
        total += 1 # O(n)
        new_list.append(student) # O(1)
    print(new_list) # O(1)
    return total # O(1)
print(random_function(student_list_01))
# Calcular O(?)
#O(3n + 5) = O(n)
