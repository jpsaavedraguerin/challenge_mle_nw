# CHALLENGE MACHINE LEARNING ENGINEER

# Previo
Antes de comenzar a desarrollar la solución al problema planteado, se realiza una estandarización de la estructura del proyecto. Aquí suponemos que esta estructura es conocida por todo el equipo. Al estructurar el proyecto de esta forma se deben hacer algunas modificaciones al notebook entregado, específicamente a las rutas definidas. Por ejemplo, la ruta "dataset_SCL.csv" ahora se indica como a "data/dataset_SCL.csv". A continuación se detalla la estructura del proyecto:

    |
    |----- data/                <- Contiene la data del proyecto 
    |----- models/              <- Versiones de los modelos entrenados
    |----- notebooks/           <- Notebooks para explorar la data y entrenar modelos
    |----- src/                 <- Código fuente del proyecto
            |----- train.py     <- Training model script
            |----- predict.py   <- Script for inference
    |----- Dockerfile           <- Archivo Dockerfile que construye la imagen Docker
    |----- README.md            <- Archivo README

Además, hubo que corregir algunos errores que se presentaron al correr el notebook. Es probable que existan diferencias entre las versiones de laslibrerías utilizadas al realizar los experimentos versus las instaladas al correrlos ahora. Al no contar con un archivo _requirements_ no es posible tener certeza de las versiones. Por lo tanto, se instalarán la ultima versión estable disponible de cada librería.

- Cambios en el código están documentados con "######" 
- iteritems() deprecated version pandas 1.50, new function: items()
- barplot error: one positional argument required but two given, changed from bartplot(input1, input2, ...) to barplot(x=input1, y=input2, ...)

# 1. Escoger modelo 
# 2. Implementar cambios a los modelos para mejorar performance
- Incluir ciudad de destino de vuelos no solo despegue
- Usar float en vez de bool para dummies
- Usar train/val/test set estratificado
- Hacer downsample de la clase minoritaria
- Probar RandomForest o Neural Network
# 3.1 Serializar modelo seleccionado
- Se incluyó en el noteebook una función para guardar el modelo entrenado
- Se se debe guardar el modelo y los nombres de las columnas utilizados en el objeto pikle
# 3.2 Implementar API REST


- endpoint: /predict



# 4. Automatizar el proceso de build y deploy de la API utilizando uno o varios servicios cloud. Argumentar.

- Github actions para deploy container cada vez que se hace push a master, en el caso de desarrollo del modelo
podría quedar configurado para que revise si cambió un archivo en específico, como model_to_delpoy.pkl, por ejemplo
- Credenciales AWS están almacenadas en github secrets por seguridad
- TODO: Mover modelo y data a S3 automáticamente
- En carpeta models/ debe exitir un archivo con nombre model_to_deploy.pkl para saber que es el mejor
- ECS: Ec2 t3.medium
- Task definition
- Public / Private VPC
- Public repository
- Added webhook
- Testing webhook

# 5. Pruebas de stress