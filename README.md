![](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/Imagenes/IMG-20240227-WA0143%20(1).jpg)


### Esquema de contenido

- [Contexto](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#contexto)
- [Desarrollo](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#desarrollo)
 - [ETL](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#etl)
 - [Panel](https://github.com/paulorlv/Proyecto1_SteamGames_Henry/blob/main/README.md#feature-engineering)
- [EDA](https://github.com/paulorlv/Proyecto1_SteamGames_Henry/blob/main/README.md#eda)
- [Modelo de aprendizaje automático](https://github.com/paulorlv/Proyecto1_SteamGames_Henry/blob/main/README.md#modelo-de-aprendizaje-autom%C3%A1tico)

### Contexto
En este proyecto, el Observatorio de Movilidad y Seguridad Vial (OMSV), un centro de estudio que está bajo la órbita del Ministerio de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires, nos pide que preparemos un proyecto de análisis de datos, con el fin de generar información que permita a las autoridades locales tomar medidas para reducir el número de fatalidades por accidentes de tránsito. Para ello, nos proporcionan un conjunto de datos sobre homicidios en accidentes de tránsito ocurridos en la Ciudad de Buenos Aires durante el período 2016-2021.


### Desarrollo
#### Transformaciones y Análisis Exploratorio de Datos (EDA)
La Extracción, Transformación y Carga (ETL) se realizaron utilizando la biblioteca Pandas.
Se aplicaron estrategias para manejar datos anidados y se eliminaron columnas irrelevantes o con muchos valores nulos.
Las tablas de Hechos y Víctimas se unieron mediante un 'merge' para obtener una única tabla con toda la información relevante.
Se agregó información de una API proporcionada por el gobierno de la Ciudad de Buenos Aires, con información sobre las coordenadas de cada barrio, lo que llevó a la formación de una nueva columna "Barrio".

Los demas detalles del ETL y EDA se puede ver en [ETLy EDA](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/tree/main/ETL%20y%20EDA)

#### Panel

Se creó un panel en PowerBI destacando los conjuntos de análisis establecidos en el EDA.

ANALISIS TEMPORAL

![](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/Imagenes/ANALISIS%20TEMPORAL.png)

ANALISIS GEOGRAFICO

![](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/Imagenes/ANALISIS%20GEOGRAFICO.png)

ANALISIS POR VICTIMA

![](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/Imagenes/ANALISIS%20VICTIMAS.png)

Se presenta un enfoque en 3 Indicadores Clave de Rendimiento (KPIs) en el panel basado en el análisis y las conclusiones de cada análisis.

![](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/Imagenes/KPIs.png)



#### Modelo de aprendizaje automático
Se crearon dos modelos de recomendación, que generan cada uno, una lista de 5 juegos ya sea ingresando el nombre de un juego o el id de un usuario.

En el primer caso, el modelo tiene una relación ítem-ítem, esto es, se toma un juego y en base a que tan similar es ese juego con el resto de los juegos se recomiendan similares. En el segundo caso, el modelo aplicar un filtro usuario-juego, es decir, toma un usuario, encuentra usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.

Para generar estos modelos se adoptaron algoritmos basados en la memoria, los que abordan el problema del filtrado colaborativo utilizando toda la base de datos, tratando de encontrar usuarios similares al usuario activo (es decir, los usuarios para los que se les quiere recomendar) y utilizando sus preferencias para predecir las valoraciones del usuario activo.

Para medir la similitud entre los juegos (item_similarity) y entre los usuarios (user_similarity) se utilizó la similitud del coseno que es una medida comúnmente utilizada para evaluar la similitud entre dos vectores en un espacio multidimensional. En el contexto de sistemas de recomendación y análisis de datos, la similitud del coseno se utiliza para determinar cuán similares son dos conjuntos de datos o elementos, y se calcula utilizando el coseno del ángulo entre los vectores que representan esos datos o elementos.

El desarrollo para la creación de los dos modelos se presenta en [Modelo](https://github.com/paulorlv/Proyecto1_SteamGames_Henry/tree/main/Modelo)

#### Desarrollo de API
Para el desarrolo de la API se decidió utilizar el framework FastAPI, creando las siguientes funciones:
- **developer(desarrollador: str)**: Retorna la cantidad de ítems y el porcentaje de contenido gratis por año para un desarrollador dado.
- **userdata(User_id: str)**: Retorna el dinero gastado, cantidad de ítems y el porcentaje de comentarios positivos en la revisión para un usuario dado.
- **UserForGenre(género: str)**: Retorna al usuario que acumula más horas para un género dado y la cantidad de horas por año.
- **best_developer_year(año: int)**: Retorna los tres desarrolladores con más juegos recomendados por usuarios para un año dado.
- **developer_rec(desarrolladora: str)**: Retorna una lista con la cantidad de usuarios con análisis de sentimiento positivo y negativo para un desarrollador dado.
- ** user_recommend(user:str)**: Esta función recomienda 5 juegos para un usuario especifico usando un filtro colaborativo.

#### Deployment

Para el deploy de la API se seleccionó la plataforma Render que es una nube unificada para crear y ejecutar aplicaciones y sitios web, permitiendo el despliegue automático desde GitHub. Para esto se siguieron estos pasos:

- Generación de un entorno virtual dentro de mi terminal de visual studio code, donde se instalaron todos los requerimientos necesarios para asi generar el archivo requeriments,txt que luego seria consumido por render..
- Se generó un servicio nuevo en render.com, conectado al presente repositorio y utilizando Docker como Runtime.
- Finalmente, el servicio queda corriendo en https://proyecto-steamgames-paulolara.onrender.com/docs.

#### Video

[Presentacion de Proyecto Steam](https://drive.google.com/file/d/1tyZWx3-vOmyHwSl_mRDd5wvvXSUoDKYK/view?usp=drive_link)
