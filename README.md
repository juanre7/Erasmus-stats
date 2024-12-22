# Visualización de Estadísticas Erasmus 🇪🇺

Este proyecto crea una gráfica de dispersión que visualiza la distribución de destinos Erasmus según el puesto de ordenación en una lista de solicitudes.  ¡Ideal para analizar tendencias y preferencias! 📈

## Características principales ✨

* Lee datos de un archivo Excel (.xlsx). 📂
* Genera una gráfica de dispersión colorida y atractiva. 🌈
* Muestra la frecuencia de cada país de destino. 📊
* Incluye una leyenda clara para identificar las opciones de destino. 📌
* Formateado para una mejor legibilidad.  🤓
* Línea horizontal para destacar un valor específico. ➖


## Cómo empezar 🚀

1. **Clonar el repositorio:** `git clone https://github.com/juanre7/Erasmus-stats`
2. **Instalar dependencias:** `pip install pandas matplotlib numpy`
3. **Ejecutar el script:** `python script.py`  (Asegúrate de tener el archivo `Solicitudes_Ind.xlsx` en la misma carpeta).


## Datos de entrada 🗂️

El script espera un archivo Excel (`Solicitudes_Ind.xlsx`) con la siguiente estructura:

* **Columna 1:** Puesto de ordenación de la solicitud.
* **Columna 2:** Primera opción de destino Erasmus.
* **Columna 3:** Segunda opción de destino Erasmus.
* **Columna 4:** Tercera opción de destino Erasmus.


## Mejoras Planificadas 🚧

* **Unir puntos superpuestos:** Se usarán puntos más grandes para reducir la superposición y mejorar la legibilidad.
* **Distinguir estudiantes de máster:** Se usarán marcadores cuadrados para estudiantes de máster en lugar de círculos para estudiantes de grado.


## Contribuciones 🤝

Las contribuciones son bienvenidas!  Por favor, abre un *issue* para reportar errores o sugerir mejoras.


## Licencia 📄

[MIT License](https://opensource.org/licenses/MIT)

---

# Erasmus Statistics Visualization 🇪🇺

This project creates a scatter plot visualizing the distribution of Erasmus destinations based on the ranking position in a list of applications. Ideal for analyzing trends and preferences! 📈

## Main Features ✨

* Reads data from an Excel file (.xlsx). 📂
* Generates a colorful and attractive scatter plot. 🌈
* Shows the frequency of each destination country. 📊
* Includes a clear legend to identify destination options. 📌
* Formatted for better readability. 🤓
* Horizontal line to highlight a specific value. ➖


## Getting Started 🚀

1. **Clone the repository:** `git clone https://github.com/juanre7/Erasmus-stats`
2. **Install dependencies:** `pip install pandas matplotlib numpy`
3. **Run the script:** `python script.py` (Make sure you have the `Solicitudes_Ind.xlsx` file in the same folder).


## Input Data 🗂️

The script expects an Excel file (`Solicitudes_Ind.xlsx`) with the following structure:

* **Column 1:** Ranking position of the application.
* **Column 2:** First Erasmus destination option.
* **Column 3:** Second Erasmus destination option.
* **Column 4:** Third Erasmus destination option.


## Planned Improvements 🚧

* **Combine overlapping points:**  Larger points will be used to reduce overlap and improve readability.
* **Distinguish Master's students:** Square markers will be used for Master's students instead of circles for undergraduate students.


## Contributions 🤝

Contributions are welcome! Please open an *issue* to report bugs or suggest improvements.


## License 📄

[MIT License](https://opensource.org/licenses/MIT)