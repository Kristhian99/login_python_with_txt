def data (ruta):
    lista_login=open(ruta,'r+')
    return lista_login

def new_log (lista_login,user):
    lista_login.write(user+"\n")

def test (lista_login,e,contra):
    val = False
    lista_login.seek(0)
    a=lista_login.readlines()
    for x in range (0,len(a)):
        user_email=a[x].split(':')
        if (e==user_email[0] and contra==user_email[1].replace('\n','')):
            val= True
    return val        
            



list=data("list.txt")
while (True):

    opcion=input ("""Introduzce una opcion para iniciar
            1) Registrar un nuevo usuario
            2) Ingresar usuario 
            3) Salir 
            """)
    if (opcion=='1'):
        email=input("Ingresa tu Email:")
        password=input("Ingresa tu Password:")
        new_log(list,email+":"+password)
    elif (opcion=='2'):
        username=input("Ingresa tu email de usuario: ")
        passw=input("Ingresa tu Password: ")
        print("El ingreso fue exitoso")
        if(test(list,username,passw)):
            print("Acceso exitoso")
        else:
            print("Error al ingresar usuario o contrasena")
    elif (opcion=='3'):
        break
    else:
        print ("INTENTA OTRA VEZ")



    

    