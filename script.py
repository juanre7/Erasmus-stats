import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import matplotlib.lines as mlines

def crear_grafico_dispersion(archivo_excel):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_excel)

    # Usar las columnas por posición
    posiciones = df.iloc[:, 0].values  # Primera columna (Puesto ordenación)
    destinos = [df.iloc[:, i] for i in range(1, 4)]  # Columnas 2-4 (Destino1, 2, 3)

    # Contar frecuencia total de cada letra
    todas_letras = []
    for destino in destinos:
        todas_letras.extend([letra for letra in destino.values if pd.notna(letra)])

    # Crear diccionario de frecuencias y ordenar letras
    frecuencias = Counter(todas_letras)
    letras_unicas = sorted(frecuencias.keys(), key=lambda x: frecuencias[x])
    letra_a_x = {letra: i for i, letra in enumerate(letras_unicas)}

    # Crear una lista de colores para cada columna de destino
    colores = ['red', 'orange', 'green']

    # Configurar el gráfico
    plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # Para cada columna de destino (Ploteo de los puntos)
    for idx, destino in enumerate(destinos):
        valores = destino.values
        for pos, letra in zip(posiciones, valores):
            if pd.notna(letra):
                plt.scatter(letra_a_x[letra], pos, c=colores[idx], alpha=0.6, s=100, zorder=2)

    # Configurar los ejes
    plt.xticks(range(len(letras_unicas)), letras_unicas, fontsize=12, rotation=0)
    plt.yticks(np.arange(0, max(posiciones) + 20, 20), fontsize=12)
    plt.ylim(-15, max(posiciones) + 10)
    plt.xlim(-1, len(letras_unicas))

    # Añadir el número de apariciones DEBAJO de cada letra
    for letra in letras_unicas:
        plt.text(letra_a_x[letra], -23, str(frecuencias[letra]),
                 ha='center', va='top', fontsize=10)

    # Crear los handles para la leyenda
    red_line = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                              markersize=8, label='1ª Opción')
    orange_line = mlines.Line2D([], [], color='orange', marker='o', linestyle='None',
                                 markersize=8, label='2ª Opción')
    green_line = mlines.Line2D([], [], color='green', marker='o', linestyle='None',
                                markersize=8, label='3ª Opción')

    # Añadir la leyenda al gráfico
    plt.legend(handles=[red_line, orange_line, green_line], loc='upper right', fontsize=12)

    # Etiquetas y título
    plt.xlabel('Países (Nº indica cantidad de apariciones)', fontsize=14, labelpad=15)
    plt.ylabel('Puesto ordenación', fontsize=14, labelpad=10)
    plt.title('Distribución de destinos por puesto', fontsize=16, pad=20)

    # Mejorar la apariencia de la grid
    plt.grid(True, linestyle='--', alpha=0.7, zorder=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Añadir la línea roja horizontal en y=110
    plt.axhline(y=110, color='red', linestyle='-', linewidth=2, zorder=1)

    # Añadir la marca "yo" junto a la línea
    plt.text(x=ax.get_xlim()[1]+0.5, y=110, s='yo', color='red', fontsize=12, va='center', ha='left')

    plt.tight_layout(pad=2)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    crear_grafico_dispersion('Solicitudes_Ind.xlsx')