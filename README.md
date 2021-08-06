# MCOC2021-P0

# Mi computador principal

* Marca/modelo: ASUS X541UV
* Tipo: Notebook
* Año adquisición: 2019
* Procesador:
  * Marca/Modelo: Intel Core i7-6500U
  * Velocidad Base: 2.50 GHz
  * Velocidad Máxima: 3.10 GHz
  * Numero de núcleos: 2 
  * Humero de hilos: 4
  * Arquitectura: x86_64
  * Set de instrucciones: Intel SSE4.1, Intel SSE4.2, Intel AVX2
* Tamaño de las cachés del procesador
  * L1d: 32KB
  * L1i: 32KB
  * L2: 256KB
  * L3: 4096KB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR4
  * Velocidad: 2133 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica 1
  * Marca / Modelo: Intel HD Graphics 520
  * Memoria dedicada: 128 MB
  * Resolución: 1366 x 768
* Tarjeta Gráfica 2
  * Marca / Modelo: Nvidia GeForce 920MX
  * Memoria dedicada: 2010 MB
  * Resolución: 1366 x 768
* Disco 1: 
  * Marca: Toshiba
  * Tipo: HDD
  * Tamaño: 1TB
  * Particiones: 6
  * Sistema de archivos: EXT4, swap, NTFS, FAT32

  
* Dirección MAC de la tarjeta wifi: b0:c0:90:bd:78:97
* Dirección IP (Interna, del router): 192.168.0.11
* Dirección IP (Externa, del ISP): 190.46.130.106
* Proveedor internet: VTR Banda Ancha S.A.


# Parte P02


## Desempeño MATMUL

![gráfico](Resultado_Gráfico.png)

## Respuestas:

* Los gráficos de mi equipo se muestran mas consistentes comparado con los del profesor/ayudante.
* La diferencias en cada corrida podría ser por una sobrecarga del cpu, y por lo tanto el aumento de la temperatura hace que se ralentize un poco y no se sobrecaliente (cada corrida podría haber tenido distinta temperatura).
* No se ve un comportamiento lineal pues, como se ve en el gráfico, mientras el CPU tenga capacidad, puede trabajar siempre a la misma velocidad. Así que una vez que tiene que trabajar mas de su capacidad ahí se empieza a ralentizar, pues se genera "cuello de botella" al tener mas datos de lo que la cpu pueda procesar.
* Python 3.9.6
* Numpy 1.21.1
* Se utilizan todos los procesadores (4):

![cpu](uso_de_cpu.png)