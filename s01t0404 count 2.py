# Creamos una lista de estudiantes 
student_list_01 = ['Valeria','Omar','Joss','Daniel','Patocro','Pancracio']

def random_function(students):
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)
    for student in students:
        print("Sele suma 1 a total") # O(1)
        total += 1 # O(n)
        new_list.append(student) # O(n)

    print("Imprimiendo estudiantes")
    print(new_list) # O(1)
    return total # O(1)
print(f"Tamaño de la lista: {1en(student_list_01)}")
print(random_function(student_list_01))
print("")
# Calcular O(?)
#Calcular O(2n)+O(5)=O5
"""
#O(3n + 5) = O(3n) = O(n)
R Final O=(n)
"""