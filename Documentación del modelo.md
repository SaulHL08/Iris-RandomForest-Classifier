#Documentación del Modelo de Clasificación de Flores Iris

Este documento proporciona una descripción detallada del modelo de clasificación de flores Iris, incluyendo cómo cargar los datos, entrenar el modelo y realizar predicciones. El modelo utiliza el algoritmo de Random Forest para clasificar flores Iris en tres categorías: "Iris-setosa," "Iris-versicolor," y "Iris-virginica."

##Parte 1: Carga de Datos y Entrenamiento del Modelo
1.	Importación de Bibliotecas:
•	Se importan las bibliotecas necesarias, incluyendo pandas para manipular datos, scikit-learn para el modelo Random Forest, y métricas de evaluación como precisión, informe de clasificación y matriz de confusión.
2.	Carga de Datos:
•	Se especifica la ruta al archivo "Iris.csv" en Google Drive y se carga el conjunto de datos que contiene información sobre las flores Iris. El archivo se carga en un DataFrame de pandas llamado data.
3.	División de Datos:
•	El conjunto de datos se divide en características (X) y etiquetas (y). Se excluyen las columnas "Id" y "Species" de las características. Las características se almacenan en X, y las etiquetas en y.
4.	División en Conjuntos de Entrenamiento y Prueba:
•	Los datos se dividen en conjuntos de entrenamiento y prueba, con un 80% de los datos para entrenamiento y un 20% para prueba. Se utiliza una semilla aleatoria para garantizar la reproducibilidad.
5.	Creación del Modelo:
•	Se crea un modelo de Random Forest con 100 estimadores y una semilla aleatoria de 42.
6.	Entrenamiento del Modelo:
•	El modelo se entrena utilizando el conjunto de entrenamiento (X_train y y_train) para aprender a clasificar las flores.

##Parte 2: Visualización y Evaluación del Modelo
1.	Precisión del Modelo:
•	Se calcula la precisión del modelo en el conjunto de prueba utilizando el método accuracy_score.
2.	Clases de Flores y Precisión por Clase:
•	Se identifican las clases de flores presentes en el conjunto de datos y se calcula la precisión por clase en función de las predicciones en el conjunto de prueba. También se muestra la cantidad de muestras por clase.
3.	Importancia de las Características:
•	Se evalúa la importancia de las características en el modelo de Random Forest y se muestra gráficamente.

##Parte 3: Realización de Predicciones
1.	Solicitud de Características al Usuario:
•	El usuario ingresa las características de una flor Iris, incluyendo la longitud y la anchura del sépalo y del pétalo.
2.	Creación del Conjunto de Datos del Usuario:
•	Se crea un nuevo conjunto de datos de pandas llamado user_input con las características ingresadas por el usuario.
3.	Predicción:
•	El modelo de Random Forest realiza una predicción de la especie de la flor basándose en las características ingresadas.
4.	Resultado de la Predicción:
•	La especie predicha se imprime en la consola como resultado de la predicción.

##Resumen
Este flujo de trabajo permite a los usuarios cargar un modelo previamente entrenado y realizar predicciones sobre la especie de una flor Iris en función de las características ingresadas. El modelo es altamente preciso, como se demuestra en la precisión del conjunto de prueba y el informe de clasificación. Las características más importantes para el modelo se presentan en la gráfica de importancia de características. El código se ha diseñado para ser interactivo y fácil de usar para los usuarios.