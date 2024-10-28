Sistema de Recomendaciones de Películas - Filtrado Basado en Contenido

Este proyecto implementa un sistema de recomendaciones de películas basado en contenido, en el cual las recomendaciones se generan a partir de las características de las películas (géneros) que el usuario ha calificado anteriormente.

S.T.A.R

Situación:
Los usuarios requieren una forma de descubrir contenido que se adapte a sus gustos, sin necesidad de evaluar todas las opciones de entretenimiento que existen.

Tarea: Crear un sistema de recomendaciones que sugiera películas basándose en las características de las películas previamente vistas por el usuario, en lugar de depender de otros usuarios.

Acción:

1. Recolección de Datos: Se utilizan dos conjuntos de datos: movies.csv (información sobre películas) y ratings.csv (calificaciones de usuarios).

2. Matriz de Características de Películas: Se genera una matriz one-hot de géneros para representar cada película según sus características.

3. Perfil de Usuario: Se calcula un perfil de usuario al ponderar cada género por la calificación asignada a las películas correspondientes.

4. Similitud y Recomendación: Se compara el perfil del usuario con todas las películas mediante la similitud de coseno para recomendar películas con características similares.

Resultado: El sistema genera una lista de recomendaciones que reflejan el interés del usuario en películas con géneros específicos, ayudando a personalizar la experiencia.

Instalación:

Clonar el Repositorio:

git clone https://github.com/juancfaz/Recommendation-System.git

cd MovieRecommender2

Instalar dependencias: 

pip install pandas numpy scikit-learn

Ejecución:

python filtrado_contenido.py