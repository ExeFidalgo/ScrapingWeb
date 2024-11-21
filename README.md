# ScrapingWeb
Scraping Web que hice para la materia "Taller de Lenguajes" del profesor Pablo Pandolfo.

# Proyecto de Web Scraping: Rankings de Lenguajes de Programación

## Descripción
Este proyecto realiza scraping de datos sobre los lenguajes de programación más populares desde tres fuentes:
- [TIOBE Index](https://www.tiobe.com/tiobe-index/)
- [Tecsify](https://tecsify.com/blog/top-lenguajes-2024/)
- [StaticTimes](https://statisticstimes.com/tech/top-computer-languages.php)

Los datos se consolidan en un archivo de Excel (`ranking_lenguajes.xlsx`), donde cada fuente tiene una hoja separada.

## Requisitos Previos
### Dependencias
Este proyecto requiere Python y las siguientes bibliotecas:
- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`
