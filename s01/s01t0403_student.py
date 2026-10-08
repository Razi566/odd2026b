# NOTAS:
#1. identifico el tamaño de la entrada "N"
#EL tamaño de la entrada es el num de estudiantes
#2. Es ver cuanto creece el num de operaciones en mi algoritmo
#conforme creece el tamaño de la entrada
#Agrego las bigO identicadas
#Teniendo en cuenta la Cota superior: asintotica
#O(n) + 4*O(1) = O(n+4) = O(n)
...

# Creando una lista de estudiantes
student_list_01 = ['Valeria','Omar','Joss','Daniel']
student_list_02 = ['Karen','Emilio','Rubi','Juan']

# Verificando presencia de estudiante
def check_student(input_student, student_list):
    for student in student_list:
     if input_student == student: # O(n)
        print("Estudiante encontrado ✔") # O(1)
        return student
    # Si no se encuentra el estudiante
    print("Estudiante NO econtrado ❌") # O(1)
    return None # O()

# Probando el algoritmo
check_student("Joss",student_list_02)