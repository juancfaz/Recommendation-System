Sistema de Recomendaciones de Películas - Filtrado Colaborativo

Este proyecto implementa un sistema de recomendaciones de películas basado en filtrado colaborativo. Utiliza las calificaciones de otros usuarios para sugerir películas a un usuario específico en función de la similitud con usuarios de gustos similares.

S.T.A.R

Situación:
Los usuarios encuentran difícil elegir qué ver debido a la gran variedad de opciones. Un sistema de recomendaciones eficaz ayuda a descubrir películas que probablemente disfrutarán.

Tarea: 
Desarrollar un sistema que proporcione recomendaciones de películas basadas en las calificaciones de usuarios con gustos similares, usando datos de calificaciones de usuarios.

Acción:

1. Recolección de Datos: Se utilizan dos conjuntos de datos: movies.csv (información sobre películas) y ratings.csv (calificaciones de usuarios).

2. Creación de la Matriz de Usuario-Película: Se construye una matriz en la que las filas representan usuarios y las columnas representan películas, con las calificaciones como valores.

3. Cálculo de Similitud: Se aplica la similitud de coseno para identificar usuarios con preferencias similares.

4. Generación de Recomendaciones: A partir de la similitud calculada, el sistema sugiere películas no vistas por el usuario basándose en las calificaciones de los usuarios similares.

Resultado:
El sistema proporciona recomendaciones de películas personalizadas para los usuarios. Los resultados se pueden observar al solicitar recomendaciones para un usuario específico.


Instalación:

Clonar el Repositorio:

git clone https://github.com/juancfaz/Recommendation-System.git

cd MovieRecommender

Instalar dependencias: 

pip install pandas numpy scikit-learn

Ejecución:

python filtrado_colaborativo.py