import funciones as fn
import os
import time


while True:
    fn.ver_menu()
    opcion=fn.validar_opcion()

    if opcion==1:
        fn.comprar()
    elif opcion==2:
        fn.ver_estadio()
        time.sleep(3)
    elif opcion==3:
        fn.lista_asistentes()
        time.sleep(3)
    elif opcion==4:
        fn.ganancias()
        time.sleep(3)
    else:
        print("Marcelo Vásquez 06-07-2023")
        break
