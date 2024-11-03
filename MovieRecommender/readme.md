Sistema de Recomendaciones de Películas - Filtrado Basado en Contenido

Este proyecto implementa un sistema de recomendaciones de películas basado en filtrado contenido. Este se basa en recomendar elementos a los usuarios en funcion de la similitud entre elementos a los que el usuario evaluó. 

S.T.A.R

Situación:

Los usuarios encuentran difícil elegir qué ver debido a la gran variedad de opciones.

Tarea:

Desarrollar un sistema que proporcione recomendaciones de películas basadas en las calificaciones de las películas que el usuario ya vió y en el rating que le dió.

Acción:

1. Recolección de Datos: Se utilizan dos conjuntos de datos: movies.csv (información sobre películas) y ratings.csv (calificaciones de usuarios). ml-latest-small: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

2. Construir el perfil del usuario, para cada película (movieId) tiene su respectiva calificación (rating).

3. Luego codificamos los generos de las películas con el metodo One Hot Encoding (OHE).

4. Multiplicamos el vector del perfil del usuario por la codificación de generos de las películas ya vistas.

5. Hacemos una ponderación para llevar de la matriz para normalizar los resultados a escala 0-1. Nos indica que generos le gustan al usuario.

6. Ahora codificamos en OHE los generos de las peliculas que el usuario no ha evaluado.

7. Para poder recomendar las peliculas debemos multiplicar el perfil del usuario, ya calculada, por la matriz de generos que no ha visto.

8. Retornamos las top_n películas de la mas probable a la menos probable.


Resultado:

El sistema proporciona recomendaciones de películas para cada usuario.


Instalación:

Clonar el Repositorio:

git clone https://github.com/juancfaz/Recommendation-System.git

cd MovieRecommender

Instalar dependencias: 

pip install pandas

Ejecución:

python filtrado_contenido.py
