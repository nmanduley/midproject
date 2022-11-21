# Proyecto de mitad de bootcamp Big Data y Machine Learning
### Autor: Nicolas Manduley
### Dataset: COVID-19 (kaggle.com)

Este dataset esta compuesto por tres archivos CSV con data global relativa al COVID-19:
    1. "confirmed_global.csv": casos confirmados
    2. "deaths_global.csv": muertes totales
    3. "recovered_global.csv": casos recuperados

Cada dataset contiene la lista de paises, sus respectivas coordenadas (latitud y longitud) y el numero de casos (confirmados, recuperados o muertes). 

## Data Cleaning
Cada fila contiene las coordenadas geograficas (latitud y longitud) y el numero de casos (confirmados, muertes y recuperados) correspondientes a cada pais. Algunos paises contienen la data clasificada por provincia/estado.

Para efectos de este proyecto, solo se ha tenido en cuenta la data por pais. Por lo tanto, los datos clasificados por provincia han sido sintetizados en una unica fila correspondiente a su respectivo pais. 

No hay valores NaN en las columnas de las fechas, por lo que esa parte del dataset no requiere tratamiento adicional. 

## Base de datos
Los datasets procesados fueron exportados como CSV y subidos a MongoDB para ser accesados a través de la API

## API
Se ha programado una API con sus respectivos endpoints para extraer los valores necesarios en cada etapa.

## Dashboard
Una interfaz grafica en Streamlit permite seleccionar el tipo de datos que se quiere obtener de cada dataset para su visualizacion. La interfaz permite seleccionar:
    1. Dataset (casos confirmados, muertes y recuperados)
    2. Pais o paises que se desea visualizar/comparar en las graficas
    3. Rango personalizado de fechas para la visualizacion