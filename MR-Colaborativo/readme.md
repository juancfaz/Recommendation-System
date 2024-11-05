Sistema de Recomendaciones de Películas - Filtrado Colaborativo

Este proyecto implementa un sistema de recomendaciones de películas basado en filtrado colaborativo, el cual trabaja con perfiles de usuarios parecidos a nosotros. Supongamos que tenemos los mismos gustos que una determinada persona y esa persona vio una película que nosotros aun no hemos visto y le gustó, entonces el sistema puede que nos la recomiende.

S.T.A.R

Situación:
Los usuarios encuentran difícil elegir qué ver debido a la gran variedad de opciones.

Tarea:
Desarrollar un sistema que proporcione recomendaciones de películas basadas en calificaciones de otros usuarios.

Acción:

1. Recolección de Datos: Se utilizan dos conjuntos de datos: movies.csv (información sobre películas) y ratings.csv (calificaciones de usuarios). ml-latest-small: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

2. Se crea una matriz de calificación donde las filas representan a los usuarios y las columnas las películas, completando las celdas vacías con ceros. Esta matriz es fundamental para calcular la similitud entre los usuarios.

3. Utilizando la métrica de similitud de coseno, se calcula la similitud entre los usuarios en función de las calificaciones que han dado a las películas. Cuanto más similar sea la calificación de un usuario con la de otro, mayor será el valor de similitud.

4. Para un usuario específico, el sistema busca a los usuarios más similares (los que tienen una alta similitud). A continuación, se suman las calificaciones de las películas que no ha visto el usuario, ponderadas por la similitud con los usuarios similares.

5. Las películas recomendadas se ordenan y se devuelven al usuario.

Resultado:

El sistema proporciona una lista de películas recomendadas para el usuario especificado, basadas en las preferencias de otros usuarios con gustos similares.

Instalación:

Clonar el Repositorio:

git clone https://github.com/juancfaz/Recommendation-System.git

cd MovieRecommender2

Instalar dependencias: 

pip install pandas numpy scikit-learn

Ejecución:

python filtrado_colaborativo.py
