# CHALLENGE MACHINE LEARNING ENGINEER

# Previo
Antes de comenzar a desarrollar la solución al problema planteado, se realiza una estandarización de la estructura del proyecto. Aquí suponemos que esta estructura es conocida por todo el equipo. Al estructurar el proyecto de esta forma se deben hacer algunas modificaciones al notebook entregado, específicamente a las rutas definidas. Por ejemplo, la ruta "dataset_SCL.csv" ahora se indica como a "data/dataset_SCL.csv". A continuación se detalla la estructura del proyecto:

    |
    |----- data/        <- Contiene la data del proyecto 
    |----- models/      <- Versiones de los modelos entrenados
    |----- notebooks/   <- Notebooks para explorar la data y entrenar modelos
    |----- src/         <- Código fuente del proyecto
    |----- Dockerfile   <- Archivo Dockerfile que construye la imagen Docker
    |----- README.md    <- Archivo README

# 1. Escoger modelo 
# 2. Implementar cambios a los modelos para mejorar performance
# 3.1 Serializar modelo seleccionado
# 3.2 Implementar API REST
# 4. Automatizar el proceso de build y deploy de la API utilizando uno o varios servicios cloud. Argumentar.
# 5. Pruebas de stress