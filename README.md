![](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/Imagenes/IMG-20240227-WA0143%20(1).jpg)


### Esquema de contenido

- [Contexto](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#contexto)
- [Desarrollo](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#desarrollo)
 - [Transformaciones y Análisis Exploratorio de Datos (EDA)](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#transformaciones-y-an%C3%A1lisis-exploratorio-de-datos-eda)
 - [Panel](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#panel)
- [Informe Final](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#informe-final)
- [Conclusiones](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#conclusiones)
- [Recursos](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/README.md#conclusiones)

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



#### Informe final

Finalmente, se realiza un reporte en formato WORD con un resumen de análisis realizado con las respectivas conclusiones encontradas durante el trabajo del presente proyecto.

Se puede acceder al reporte por este medio [Informe](https://github.com/paulorlv/Proyecto2_Siniestros_Viales/blob/main/INFORME.docx) , donde se explica detalladamente el análisis requerido.

#### Conclusiones

 Después de plantear indicadores de desempeño relacionados con el análisis y conclusiones encontradas en cada uno de los tres aspectos evaluados, se encuentra que la reducción de la accidentalidad tiene un comportamiento poco favorable, pues no se cumplen constante ni certeramente los objetivos en los periodos de tiempo planteados, por lo tanto, se recomienda establecer acciones tales como 

•	 Jornadas de educación vial.
    
•	Sensibilización a la ciudadanía sobre el impacto social que presenta un siniestro vial.
    
•	 Mayor rigurosidad en las pruebas teóricas y prácticas para la obtención de la licencia de conducir

#### Recursos

 El archivo principal 'Homicidios' se obtuvo desde [Data Buenos Aires](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales). Se utilizaron recursos adicionales que fueron obtenidos desde [API Buenos Aires](https://datosabiertos-usig-apis.buenosaires.gob.ar/datos_utiles) y desde [Censo Buenos Aires](https://es.wikipedia.org/wiki/Buenos_Aires).


