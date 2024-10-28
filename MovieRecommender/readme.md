Sistema de Recomendaciones de Películas

Este proyecto implementa un sistema de recomendaciones
de películas utilizando técnicas de filtrado colaborativo.
El sistema sugiere películas a los usuarios en función de
las calificaciones que han dado y de la similitud con otros usuarios.

S.T.A.R

Situación:
En un mundo donde hay un montón de contenido multimedia, a veces es difícil elegir qué ver porque hay tantas opciones. Un sistema de recomendaciones que funcione bien puede ayudar a los usuarios a descubrir nuevas películas que realmente les gusten.

Tarea:
El objetivo de este proyecto es desarrollar un sistema que permita a los usuarios recibir recomendaciones de películas basadas en las calificaciones de otros usuarios con gustos similares. Para lograr esto, se utilizó un conjunto de datos que contiene información sobre películas y calificaciones de usuarios.

Accion:
1. Recolección de Datos: Se utilizaron dos conjuntos de datos: movies.csv (contiene información sobre las películas) y ratings.csv (contiene las calificaciones de los usuarios).

2. Creación de la Matriz de Usuario-Película: Se generó una matriz donde las filas representan a los usuarios y las columnas representan a las películas, con las calificaciones como valores.

3. Cálculo de Similitud: Se aplicó la similitud del coseno para encontrar usuarios similares en función de sus calificaciones.

4. Generación de Recomendaciones: Se desarrolló una función que calcula las calificaciones predichas para películas no calificadas por el usuario, utilizando un enfoque ponderado según la similitud de otros usuarios.

5. Pruebas y Validación: Se realizaron pruebas para asegurar que las recomendaciones fueran coherentes y útiles

Resultado:
El sistema proporciona recomendaciones de películas personalizadas para los usuarios. Los resultados se pueden observar al solicitar recomendaciones para un usuario específico.


Instalación:

1. Clonar el Repositorio: 
git clone https://github.com/juancfaz/Recommendation-System.git
cd MovieRecommender

2. Instalar dependencias:
pip install pandas numpy scikit-learn

3. Ejecutar la libreta jupyter