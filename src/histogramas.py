import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde un archivo CSV
df = pd.read_csv('./data/2015.csv')

# Ver las primeras filas del DataFrame
print(df.head())

# Ver la información del DataFrame (tipos de datos y valores no nulos)
print(df.info())

# Ver estadísticas descriptivas de las variables numéricas
print(df.describe())

# Configurar el tamaño de la figura
plt.figure(figsize=(12, 8))

# Histograma de Happiness Score
plt.subplot(2, 2, 1)
plt.hist(df['Happiness Score'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Happiness Score')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')

# Histograma de Economy (GDP per Capita)
plt.subplot(2, 2, 2)
plt.hist(df['Economy (GDP per Capita)'], bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title('Histogram of GDP per Capita')
plt.xlabel('GDP per Capita')
plt.ylabel('Frequency')

# Histograma de Health (Life Expectancy)
plt.subplot(2, 2, 3)
plt.hist(df['Health (Life Expectancy)'], bins=20, color='coral', edgecolor='black', alpha=0.7)
plt.title('Histogram of Health (Life Expectancy)')
plt.xlabel('Health (Life Expectancy)')
plt.ylabel('Frequency')

# Histograma de Freedom
plt.subplot(2, 2, 4)
plt.hist(df['Freedom'], bins=20, color='gold', edgecolor='black', alpha=0.7)
plt.title('Histogram of Freedom')
plt.xlabel('Freedom to Make Life Choices')
plt.ylabel('Frequency')

# Ajustar el layout y mostrar los histogramas
plt.tight_layout()
plt.show()

# Boxplot de Happiness Score
plt.subplot(2, 2, 1)
plt.boxplot(df['Happiness Score'], patch_artist=True, boxprops=dict(facecolor='skyblue', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Boxplot of Happiness Score')
plt.ylabel('Happiness Score')

# Boxplot de Economy (GDP per Capita)
plt.subplot(2, 2, 2)
plt.boxplot(df['Economy (GDP per Capita)'], patch_artist=True, boxprops=dict(facecolor='lightgreen', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Boxplot of GDP per Capita')
plt.ylabel('GDP per Capita')

# Boxplot de Health (Life Expectancy)
plt.subplot(2, 2, 3)
plt.boxplot(df['Health (Life Expectancy)'], patch_artist=True, boxprops=dict(facecolor='coral', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Boxplot of Health (Life Expectancy)')
plt.ylabel('Health (Life Expectancy)')

# Boxplot de Freedom
plt.subplot(2, 2, 4)
plt.boxplot(df['Freedom'], patch_artist=True, boxprops=dict(facecolor='gold', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Boxplot of Freedom')
plt.ylabel('Freedom to Make Life Choices')

# Ajustar el layout y mostrar los boxplots
plt.tight_layout()
plt.show()

# Configurar el tamaño de la figura
plt.figure(figsize=(14, 10))

# Combinación de histogramas y boxplots para Happiness Score
plt.subplot(2, 2, 1)
plt.hist(df['Happiness Score'], bins=20, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')
plt.boxplot(df['Happiness Score'], patch_artist=True, positions=[0.5], boxprops=dict(facecolor='lightgray', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Happiness Score Distribution')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')
plt.legend()

# Combinación de histogramas y boxplots para Economy (GDP per Capita)
plt.subplot(2, 2, 2)
plt.hist(df['Economy (GDP per Capita)'], bins=20, color='lightgreen', edgecolor='black', alpha=0.7, label='Histogram')
plt.boxplot(df['Economy (GDP per Capita)'], patch_artist=True, positions=[0.5], boxprops=dict(facecolor='lightgray', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('GDP per Capita Distribution')
plt.xlabel('GDP per Capita')
plt.ylabel('Frequency')
plt.legend()

# Combinación de histogramas y boxplots para Health (Life Expectancy)
plt.subplot(2, 2, 3)
plt.hist(df['Health (Life Expectancy)'], bins=20, color='coral', edgecolor='black', alpha=0.7, label='Histogram')
plt.boxplot(df['Health (Life Expectancy)'], patch_artist=True, positions=[0.5], boxprops=dict(facecolor='lightgray', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Health (Life Expectancy) Distribution')
plt.xlabel('Health (Life Expectancy)')
plt.ylabel('Frequency')
plt.legend()

# Combinación de histogramas y boxplots para Freedom
plt.subplot(2, 2, 4)
plt.hist(df['Freedom'], bins=20, color='gold', edgecolor='black', alpha=0.7, label='Histogram')
plt.boxplot(df['Freedom'], patch_artist=True, positions=[0.5], boxprops=dict(facecolor='lightgray', color='black'), 
            medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Freedom Distribution')
plt.xlabel('Freedom to Make Life Choices')
plt.ylabel('Frequency')
plt.legend()

# Ajustar el layout y mostrar los gráficos
plt.tight_layout()
plt.show()

