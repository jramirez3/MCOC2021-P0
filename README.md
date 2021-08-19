# MCOC2021-P0

# Parte P03 : Desempeño INV

##   Comentarios:

* El procesador de mi PC solamente soporta single y double, por lo que se consideró poner de resultado únicamente esos dos tipos.

![uso de memoria](Tamaños_de_memoria.png) 

##    Respuestas:

* En el caso de numpy, resuelve la inversa mediante la ecuación A * x = I, usando un algoritmo basado en LAPACK (Linear Algebra Package). En Scipy hace lo mismo que en numpy, pero mas eficiente al contener mas funcionalidades como descomposicion LU, la descomposicion de Schur, y otras mejoras.
* En el caso de las operaciones singles en todo los casos mostraban mayor velocidad y actividad constante al máximo en todos los CPUs. En los casos de double son procesos mas lentos debido al mayor uso de memoria, en todos los casos el mismo comportamiento ondulatorio.








