# -*- coding: utf-8 -*-
"""Proyecto originalmente creado en Colab

David Torres Robles
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df=pd.read_csv('Life Expectancy Data.csv')
df.head()

df.info()
#observamos los nulos y pasamos las columnas al castellano para entenderlas mejor

# Renombrar las columnas al castellano
df.rename(columns={
    "Country": "País",
    "Year": "Año",
    "Status": "Estado",  # (Desarrollado o en Desarrollo)
    "Life expectancy ": "Esperanza de vida",
    "Adult Mortality": "Mortalidad adulta",
    "infant deaths": "Muertes infantiles",
    "Alcohol": "Consumo de alcohol",
    "percentage expenditure": "Gasto en salud (% PIB)",
    "Hepatitis B": "Vacunación Hepatitis B",
    "Measles ": "Casos de sarampión",
    " BMI ": "Índice de Masa Corporal",
    "under-five deaths ": "Muertes menores de 5 años",
    "Polio": "Vacunación Polio",
    "Total expenditure": "Gasto total en salud",
    "Diphtheria ": "Vacunación Difteria",
    "HIV/AIDS": "Mortalidad por VIH/SIDA",
    "GDP": "PIB",
    "Population": "Población",
    " thinness  1-19 years": "Delgadez 1-19 años",
    " thinness 5-9 years": "Delgadez 5-9 años",
    "Income composition of resources": "Índice de recursos económicos",
    "Schooling": "Escolarización"
}, inplace=True)

# Mostrar las primeras filas con los nuevos nombres
df.head()

"""Explicación del enfoque del modelo:

En este conjunto de datos, el target o objetivo es la esperanza de vida; sin embargo, en este análisis, vamos a utilizar el PIB (Producto Interior Bruto) como target. La idea es predecir el PIB de un país utilizando factores relacionados con la salud y el desglose sanitario de su economía.

Para ello, vamos a explorar diferentes variables y analizarlas en detalle, lo cual incluye identificar outliers (valores atípicos). En función de los resultados, decidiremos si es necesario eliminar datos o si sustituimos valores faltantes con medias o medianas. El objetivo es asegurarnos de que los datos sean lo más fiables y representativos posible para obtener una predicción precisa del PIB.
"""

df['País'].unique()#un primer vistazo a los paises que componen el data set

df.describe()

#visualizamos las columanas con nulos
df_nulos=df.isnull().sum()
df_nulos = df_nulos[df_nulos > 0]
df_nulos

"""Vemmos que en la esperanza de vida no hay valores o muy bajos o muy altos, por lo que vamos a rellenarlos con el promedio"""

plt.figure(figsize=(8, 5))
plt.hist(df["Esperanza de vida"].dropna(), bins=30, edgecolor="black", alpha=0.7)
plt.xlabel("Esperanza de vida")
plt.ylabel("Frecuencia")

plt.show()


df["Mortalidad adulta"].describe()

#Rellenar los valores nulos de  la esperanza de vida con el promedio
df.fillna({"Esperanza de vida": df["Esperanza de vida"].mean()}, inplace=True)


#Verificar que ya no haya valores nulos en esta columna
df["Esperanza de vida"].isnull().sum()

plt.figure(figsize=(8, 5))
plt.hist(df["Mortalidad adulta"].dropna(), bins=30, edgecolor="black", alpha=0.7)
plt.xlabel("Mortalidad adulta")
plt.ylabel("Frecuencia")

plt.show()

sns.boxplot(x=df["Mortalidad adulta"].dropna())
plt.ylabel("Mortalidad adulta")
plt.show()

#aqui vemos mas claro que tenemos algunos outliner por ahora solo remplazaremos los nulos por la mediana

plt.figure(figsize=(8, 5))
plt.hist(df["Mortalidad adulta"].dropna(), bins=30, edgecolor="black", alpha=0.7)
plt.xlabel("Mortalidad adulta")
plt.ylabel("Frecuencia")

plt.show()

"""Al usar la mediana para rellenar los valores nulos, nos aseguramos de que los outliers no afecten el valor, ya que la mediana es más robusta frente a ellos, representando el valor central sin verse influenciada por valores extremos."""

df.fillna({"Mortalidad adulta": df["Mortalidad adulta"].median()}, inplace=True)


df["Mortalidad adulta"].isnull().sum()

"""Para verlo de otra manera vamos a calcular la meidana y la media del siguiente campo.

obetenemos la diferencia entre los dos valores, nos da 0.84 de diferencia absoluta(ABS)por lo que interpretamos que la diferencia es poca.

Pero luego en la diferencia porcentual si el valor que nos da esta por valor de 10% podriamos coger la media, pero nos da 18, por lo que podemos interpretar que hay valores extremos por lo que vamos a usar la mediana.

Pero reflexionando aquie estamos indicando el consumo de alcohol en valores reales si hay paises que consumen mas alcohol que otros y eliminamos esa diferencia creo que podriamos estar realizando un sesgo, por lo que al final elegiremos la media

"""

media = df['Consumo de alcohol'].mean()   # Calcula la media
mediana = df["Consumo de alcohol"].median()  # Calcula la mediana

diferencia = abs(media - mediana)  # Calcula la diferencia absoluta entre ambas
porcentaje_diferencia = (diferencia / media) * 100  # Diferencia en porcentaje

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Diferencia absoluta: {diferencia}")
print(f"Diferencia porcentual: {porcentaje_diferencia:.2f}%")

df.fillna({"Consumo de alcohol": df["Consumo de alcohol"].mean()}, inplace=True)

df["Consumo de alcohol"].isnull().sum()

plt.hist(df['Vacunación Hepatitis B'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Vacunación Hepatitis B')
plt.ylabel('Frecuencia')
plt.show()

media=df['Vacunación Hepatitis B'].mean()
mediana=df['Vacunación Hepatitis B'].median()
diferencia=abs(media-mediana)
porcentaje_diferencia=(diferencia/media)*100
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Diferencia absoluta: {diferencia}")
print(f"Diferencia porcentual: {porcentaje_diferencia:.2f}%")

"""Con el boxplot sí que veo más claro que tenemos muchos valores bajos de vacunación, por lo que cogeremos la mediana, imagino porque en muchos países en vías de desarrollo tendrán una tasa baja y si usamos la media estaríamos quizás añadiendo un sesgo a los datos, ya que la media se ve afectada por los valores extremos y reduciría artificialmente la vacunación real en la mayoría de los países, mientras que la mediana nos permite reflejar mejor la realidad sin que los valores bajos tengan tanta influencia."""

sns.boxplot(x=df["Vacunación Hepatitis B"])
plt.ylabel("Vacunación Hepatitis B")
plt.show()

df.fillna({"Vacunación Hepatitis B": df["Vacunación Hepatitis B"].median()}, inplace=True)

df["Vacunación Hepatitis B"].isnull().sum()

#para refrescasr por donde vamos
df.info()

sns.boxplot(df['Índice de Masa Corporal'])

plt.hist(df['Índice de Masa Corporal'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Índice de Masa Corporal')
plt.ylabel('Frecuencia')
plt.show()

"""como en este caso no veo valores atipicos usare la media para rellenar los nulos"""

df.fillna({"Índice de Masa Corporal": df["Índice de Masa Corporal"].mean()}, inplace=True)

df["Índice de Masa Corporal"].isnull().sum()

sns.boxplot(df['Vacunación Polio'])

plt.hist(df['Vacunación Polio'])
plt.xlabel('Vacunación H')
plt.ylabel('Frecuencia')

"""como en el caso de la hepatitis, vamos a usar la mediana para reflejar que en la mayoria de los paises la vacunacion es alta"""

df.fillna({'Vacunación Polio':df['Vacunación Polio'].mean()}, inplace=True)
df['Vacunación Polio'].isnull().sum()

sns.boxplot(df['Gasto total en salud'])

media=df['Gasto total en salud'].mean()
mediana=df['Gasto total en salud'].median()

diferencia=abs(media-mediana)
porcentaje_diferencia=(diferencia/media)*100
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Diferencia absoluta: {diferencia}")
print(f"Diferencia porcentual: {porcentaje_diferencia:.2f}%")

"""Apreciamos que si que hay paises que gastan mas en salud que son los outliners pero viendo que la media  y mediana son similares, usaremos la media"""

df.fillna({'Gasto total en salud':df['Gasto total en salud'].mean()}, inplace=True)
df['Gasto total en salud'].isnull().sum()

sns.boxplot(df['Vacunación Difteria'])

plt.hist(df['Vacunación Difteria'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Vacunación Difteria')
plt.ylabel('Frecuencia')
plt.show()

"""vemos lo mismo que en otros casos de vacunacion, las vacunaciones suelen ser altar pero vemos outliners con valores muy bajos por lo que lo rellenaremos con la mediana para representar valores mas relaes y evitar sesgos"""

df.fillna({'Vacunación Difteria':df['Vacunación Difteria'].median()}, inplace=True)
df['Vacunación Difteria'].isnull().sum()

#volvemos a refrescar la info
df.info()

sns.boxplot(df['PIB'])

plt.hist(df['PIB'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('PIB')
plt.ylabel('Frecuencia')
plt.show()

"""Estamos observando que la gran mayoría de los países tienen un PIB muy bajo y que, en este caso, los outliers representan los PIB más altos. Pero como vamos a elegir el PIB como nuestro target, lo que vamos a hacer es usar la mediana, pero calculándola dentro de cada grupo según el campo "Estado", que diferencia entre países desarrollados y en desarrollo. De esta manera, los datos serán más precisos y representarán mejor la realidad económica de cada grupo."""

#Calcular la mediana del PIB segun si esta en desarrollo o en vias de desarrollo
mediana_pib_desarrollado = df[df["Estado"] == "Developed"]["PIB"].median()
mediana_pib_desarrollo = df[df["Estado"] == "Developing"]["PIB"].median()


for i in range(len(df)):
    if pd.isnull(df.loc[i, "PIB"]):  # Si el valor es nulo
        if df.loc[i, "Estado"] == "Developed":
            df.loc[i, "PIB"] = mediana_pib_desarrollado  #Rellenar con la mediana de países desarrollados
        else:
            df.loc[i, "PIB"] = mediana_pib_desarrollo  #Rellenar con la mediana de países en desarrollo

# verificamos
df["PIB"].isnull().sum()

"""esto fue una prueba que hice para eliminar los outliers pero el r2 y el mse daban peor resultado"""

'''Q1 = df["PIB"].quantile(0.25)
Q3 = df["PIB"].quantile(0.75)
IQR = Q3 - Q1
limite_superior = Q3 + 1.5 * IQR  # Solo filtraremos los outliers superiores

#contamos los valores superiores
outliers_superiores = (df["PIB"] > limite_superior).sum()

#filtramos el el dataset eliminando los outliers superiores
df_filtrado = df[df["PIB"] <= limite_superior]

#Comparar cuantas filas tenía antes y después
tamanio_original = df.shape[0]
tamanio_filtrado = df_filtrado.shape[0]

#ostrar resultados
outliers_superiores, tamanio_original, tamanio_filtrado'''

#Aplicar el filtrado de outliers superiores en el PIB
'''df = df[df["PIB"] <= limite_superior]

# Verificar el tamaño del dataset después de eliminar los outliers
df.shape'''

sns.boxplot(df['PIB'])

sns.boxplot(df['Población'])

plt.hist(df['Población'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Población')
plt.ylabel('Frecuencia')
plt.show()

"""En la pobalcion estamos viend que si usamos la media estara infulencida por los paises que tiene mucha poblacion, por lo que no representara a los la mayoria de los paises. por lo que usaremos la mediana"""

df.fillna({'Población':df['Población'].median()}, inplace=True)
df['Población'].isnull().sum()

"""vamos a eliminar los nulos de los campos de delgadez, dado que condiero que son pocos y creo que pueden no ser relevantes para nuestro target"""

df.dropna(subset=['Delgadez 1-19 años', 'Delgadez 5-9 años'], inplace=True)
df.info()

sns.boxplot(df['Índice de recursos económicos'])

plt.hist(df['Índice de recursos económicos'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Índice de recursos económicos')
plt.ylabel('Frecuencia')
plt.show()

df['Índice de recursos económicos']

"""quiero averiguar de donde proviene o como interpreto el outlier que tenemos con valor 0, y vemos que son 119 filas y que casi todos los maises son en vias de desarrollo"""

# Contar cuántos registros tienen el valor 0 en "Índice de recursos económicos"
cantidad_cero = (df["Índice de recursos económicos"] == 0).sum()

# Obtener los países únicos donde el "Índice de recursos económicos" es 0
paises_cero = df[df["Índice de recursos económicos"] == 0]["País"].unique()

# Mostrar la cantidad de registros con 0 y los países afectados
cantidad_cero, paises_cero

"""Como hicimos con el PIB sacaremos la mediana dependiento del estado (desarrollado o no) para que sean mas correctos los datos, primero sustituiremos los valores nulos y despues, los valores a 0 que consideramos outliners les añadiremos la mediana tambien siguiendo la misma logica.

En el Bucle lo de iterrows, no lo saque yo, fue la opcion que me daba gemini por que me daba un error con los indices, e imagino por que borre datos antes y los indices cambiaron(imagino)
"""

#primero vamos a rellenar los valores nulos con las medianas

mediana_recursos_desarrollado = df[df["Estado"] == "Developed"]["Índice de recursos económicos"].median()
mediana_recursos_desarrollo = df[df["Estado"] == "Developing"]["Índice de recursos económicos"].median()


for index, row in df.iterrows():
    if pd.isnull(row["Índice de recursos económicos"]):  #Si el valor es nulo
        if row["Estado"] == "Developed":
            df.loc[index, "Índice de recursos económicos"] = mediana_recursos_desarrollado
        else:
            df.loc[index, "Índice de recursos económicos"] = mediana_recursos_desarrollo

# Verificar que ya no haya valores nulos en esta columna
df["Índice de recursos económicos"].isnull().sum()

#y ahora vamos a reemplazar los valos a 0 con las medianas tambien
for index, row in df.iterrows():
    if row["Índice de recursos económicos"] == 0:  #Si el valor es 0(outlier)
        if row["Estado"] == "Developed":
            df.loc[index, "Índice de recursos económicos"] = mediana_recursos_desarrollado
        else:
            df.loc[index, "Índice de recursos económicos"] = mediana_recursos_desarrollo

#verificacion de valores a 0
cantidad_cero_final = (df["Índice de recursos económicos"] == 0).sum()

cantidad_cero_final

sns.boxplot(df['Índice de recursos económicos'])
#comprobamos que ya no hay otuliners

"""Ahora vemos como la columna que nos marcaba el pico con los recursos economicos a 0 se a balanceado entre el 0.1 y el 0.3. en mi opinon una interpretacion mas real de los datos, or lo que si reflejamos la realidad no añadiremos un sesgo en nuestro modelo"""

plt.hist(df['Índice de recursos económicos'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Índice de recursos económicos')
plt.ylabel('Frecuencia')
plt.show()

df.info()

sns.boxplot(df['Escolarización'])

plt.hist(df['Escolarización'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Escolarización')
plt.ylabel('Frecuencia')
plt.show()

"""Apreciamos valores muy bajos porlo que entendemos que puede ser una falta de escolarizacion en paises no desarrollados, y en el histrograma vemos esa campana de gaus con ese pequeño pico a la izq indicando la baja escolarizacion, eneste caso interpreto que podemos usar la media para completar los valores nulos si causar un sego a nuestros datos"""

df.fillna({'Escolarización':df['Escolarización'].mean()}, inplace=True)
df['Escolarización'].isnull().sum()

df.info()

# Guardar una copia del dataset limpio
#df.to_csv("Life_Expectancy_Cleaned.csv", index=False)

"""Llegamdo a este punto recordamos que vamos a predecir el PIB de un pais dependiendo en si de sus indicadores de salud. Por lo que por ejemplo el campo de Pais, lo podriamos eliminar, solo es un nombre unico y no una variable numerica.

Por lo que he estado indagando e informandome si dejara el campo Pais el modelo podria estar memorizando nombre y no aprendiendo patrones reales.

En cambio el 'Estado' si que lo vamos a transformar en un campo numerico para poder entrenarlo.

VAmos ha realizar estas 2 acciones y continuamos con el ejercicio.
"""

df.drop('País', axis=1, inplace=True)
df.head()

df["Estado"] = df["Estado"].map({"Developing": 0, "Developed": 1})

# Verificar que la transformación se ha realizado correctamente
print(df["Estado"].value_counts())  # Ver cuántos registros hay en cada categoría

"""Al realizar este ultimo punto, vemos que hay mas datos de desarrolo que en vias de desarroyo, por lo que tenemos la clase desbalanceada.

si no me equivoco como vamos a hacer una regresion y no una clasificacion no es un problema grave.

vamos a ver la correlacion entre variables para ver como proceder
"""

#Muevo la columna PIB(target) a la ultima posicion por comodidad
columnas = [col for col in df.columns if col != "PIB"]
columnas.append("PIB")
#Reordenar el DataFrame
df = df[columnas]

#Verificar que la columna PIB ahora está al final
df.head()

df.info()

"""Ahora vamos a mirar la correlacion de los datos, de esta manera si vemos que hay campos que nos dan la misma informacion se podria prescindir de ellos"""

correlacion = df.corr()


plt.figure(figsize=(12, 8))


sns.heatmap(correlacion, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)


plt.title("Matriz de Correlación")


plt.show()

"""por lo que estamos viendo tenemos bastantes variables relacionadas, como por ejemplo muertes infantiles -5años con muertes infantiles, o escolarizacion con indice de recursos economicos entreotros, por lo que vamos a usar PCA para reducir esta dimensionalidad, si fuera categorico usariomos LDA"""

df.info()

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

df_scaled=scaler.fit_transform(df.drop('PIB', axis=1))# eliminamos el target

pca=PCA()
pca.fit(df_scaled)

varianza=np.cumsum(pca.explained_variance_ratio_)

plt.figure(figsize=(10, 6))
plt.plot(varianza, marker='o', linestyle='-')
plt.xlabel('Número de Componentes Principales')
plt.ylabel('Varianza Explicada Acumulada')
plt.grid()

"""Recuerdo que en clase hablamos del "punto de codo", y aquí podemos verlo claramente. Según el gráfico, con 10 componentes principales retenemos casi el 90% de la información, mientras que con 12 componentes alcanzamos aproximadamente el 92%. Dado que la mejora después de 10 componentes es mínima, optaremos por 10 componentes para lograr un equilibrio entre reducción de dimensionalidad y retención de información. Ahora, procederemos a aplicarlo."""

pca_elegido=PCA(n_components=10)
df_pca=pca_elegido.fit_transform(df_scaled)

columnas_pca = [f"Componente_{i+1}" for i in range(10)]
df_pca = pd.DataFrame(df_pca, columns=columnas_pca)
df_pca["PIB"] = df["PIB"].values #me volvi loco para descubrir esto por que por algun motivo si no ponia el .values se añadian 34 valores nulos en el pib

df_pca.info()

df_pca.head()

"""Ahora entiendo por que en el esquema que nos pasastes ponias(no conoce los labels) me estaba peleando pero lei que pca crea nuevas variables

En la parte de clustering me siento un poco perdido, ya que entiendo que generalmente se usa en problemas de aprendizaje no supervisado, mientras que nosotros aplicaremos una regresión lineal. Sin embargo, ahora comprendo que el clustering en este caso nos puede ayudar a descubrir patrones ocultos en los datos y generar nuevas variables que mejoren nuestro dataset, mejorando así la predicción del PIB. Por ello, vamos a utilizar K-Means, que es el algoritmo que mejor comprendo
"""

from sklearn.cluster import KMeans

inercia=[]

k_rango=range(1,11)#probremos del uno al 10 que son los campos que hemos dejado

for k in k_rango:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_pca.drop(columns=["PIB"])) #Aplicamos clustering sobre los componentes principales
    inercia.append(kmeans.inertia_) #Guardamos la inercia (distancia dentro de cada cluster)

# Graficamos el método del codo
plt.figure(figsize=(8,5))
plt.plot(k_rango, inercia, marker='o', linestyle='--', color='b')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inercia')
plt.title('Método del Codo para Selección de K')
plt.grid()

# Mostrar el gráfico
plt.show()

"""mi apreciacion es que el punto de codo se encuentra en K=4, lo que indica que cuatro clusters es la mejor opción para agrupar los datos sin añadir complejidad innecesaria. Ahora, añadiremos la columna "Cluster" al dataset, permitiendo que el modelo identifique patrones ocultos y mejore la predicción del PIB (en teoria ;))"""

kmeans_final = KMeans(n_clusters=4, random_state=42, n_init=10)
df_pca["Cluster"] = kmeans_final.fit_predict(df_pca.drop(columns=["PIB"]))

#por si la liamos
#df_pca.to_csv("Life_Expectancy_Clusters.csv", index=False)

#comprobamos que se han guardado los cambios
df_pca.info()

"""Quiero comprobar donde a colocaado el promedio los clusters, en teoria los datos tendrian que estr dispersos pero los valores 2 y 3 los veo muy parejos"""

pib_por_cluster = df_pca.groupby("Cluster")["PIB"].mean().reset_index()

pib_por_cluster

# Crear un gráfico de dispersión para visualizar el PIB promedio por cluster

plt.scatter(pib_por_cluster["Cluster"], pib_por_cluster["PIB"], color='b', s=100, edgecolors='k')

# Etiquetas y título
plt.xlabel("Cluster")
plt.ylabel("PIB Promedio")
plt.title("PIB Promedio por Cluster")
plt.xticks(pib_por_cluster["Cluster"])
plt.grid()


plt.show()

"""K-Means ha identificado 4 grupos bien diferenciados en función del PIB. Si los clusters hubieran estado demasiado juntos o con valores de PIB similares, significaría que esta agrupación no aporta valor al dataset. Sin embargo, en este caso, hemos obtenido 4 clusters con diferencias claras en el PIB(a medias), lo que sugiere que esta nueva variable captura patrones útiles y puede ser beneficiosa para la predicción.

Por otro lado, cuando normalizábamos el dataset, pensé en agrupar los países por continentes, pero finalmente eliminamos esa variable. Ahora veo que, de alguna manera, K-Means ha logrado un efecto similar, agrupando los países en función de patrones económicos y de salud, sin necesidad de especificar la región geográfica.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X=df_pca.drop(columns=["PIB"])
y=df_pca["PIB"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

modelo=LinearRegression()
modelo.fit(X_train,y_train)

y_pred=modelo.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print(f"MSE: {mse}")
print(f"R2: {r2}")

"""como metrias cogeremos el coeficiente r2 y el error cuadratico medio, viendo que para el modelo, elegimos el Error Cuadrático Medio (MSE) como métrica debido a que penaliza de manera más significativa los grandes errores de predicción, lo cual es útil cuando estamos tratando con variables como el PIB, donde las diferencias entre los valores pueden ser grandes. Además, el coeficiente de determinación (R²) nos ayuda a evaluar cuán bien el modelo explica la variabilidad de los datos."""

rmse = np.sqrt(26265837.42)
print(f"RMSE: {rmse}")

"""el coeficiente r2, esta cerca del uno por lo que esta bien pero el error cuadratico medio vamos intentar mejoorarlo  con un arbol de decision"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


rf_model = RandomForestRegressor(n_estimators=100, random_state=42)


rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)


r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = mean_squared_error(y_test, y_pred_rf) ** 0.5


# ostrar métricas de evaluación
print(f"R² (Random Forest): {r2_rf:.4f}")
print(f"RMSE (Random Forest): {rmse_rf:.2f}")

"""Lo hemos hecho sin hiperparametros y vemos que hemos bajado el error cuadratico medio

En el grafico vemos una evolucion con
"""

plt.scatter(y_test, y_pred_rf, color='b', s=50, edgecolors='k')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red')
plt.xlabel("PIB Real")
plt.ylabel("PIB Predicho")
plt.title("Comparación entre PIB Real y Predicho (Random Forest)")
plt.grid()
plt.show()

"""El gráfico que compara el PIB real con el predicho muestra una buena relación entre ambos, lo que indica que el modelo está entendiendo bien la tendencia general. También se nota que hay más puntos en el rango de PIB bajo, lo que coincide con lo que vimos en los datos originales: la mayoría de los países tienen un PIB bajo. Esto sugiere que el modelo ha aprendido la distribución de los datos correctamente, pero podría ser útil revisar si el modelo está sobreajustado en el rango de PIB más alto, ya que esos valores están más dispersos."""

#esta configuracion a tardado 15 minutos y no ha ganado nada
'''from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd


rf_model = RandomForestRegressor(random_state=42)


param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [True]
}

y_train = y_train.ravel()
y_test = y_test.ravel()

#Realizar búsqueda de hiperparámetros con validación cruzada (cv=5)
grid_search = GridSearchCV(rf_model, param_grid, cv=5, scoring="neg_mean_squared_error", n_jobs=-1)
grid_search.fit(X_train, y_train)

#Obtener los mejores parámetros encontrados
best_params = grid_search.best_params_
print("Mejores parámetros encontrados:", best_params)

#Obtener el mejor número de árboles
best_n_estimators = best_params["n_estimators"]

#Entrenar Random Forest con los mejores parámetros encontrados
rf_best = RandomForestRegressor(**best_params, random_state=42)
rf_best.fit(X_train, y_train)

#Hacer predicciones con el conjunto de prueba
y_pred_best = rf_best.predict(X_test)


r2_best = r2_score(y_test, y_pred_best)
rmse_best = mean_squared_error(y_test, y_pred_best) ** 0.5


print("R² del modelo optimizado:", r2_best)
print("RMSE del modelo optimizado:", rmse_best)'''

"""**Este texto no es mio, es sacado de internet son apuntes para ir modificando los hiperparametros**

1️⃣ Más árboles (n_estimators) → Cuantos más árboles tenga el modelo, más estable será y menos dependerá de los datos de entrenamiento. Pero si pongo demasiados, puede tardar más sin mejorar mucho.

2️⃣ Limitar profundidad (max_depth) → Si los árboles crecen demasiado, pueden aprenderse los datos en lugar de encontrar patrones generales. Poner un límite como 20 o 30 ayuda a que el modelo no se pase de listo.

3️⃣ Ajustar min_samples_split y min_samples_leaf → Subir estos valores hace que el modelo no cree árboles súper detallados con datos muy específicos, lo que ayuda a que funcione mejor con datos nuevos.

4️⃣ Probar max_features='log2' → Si cambio de sqrt a log2, los árboles usarán diferentes combinaciones de datos en cada división, lo que puede hacer que el modelo sea más variado y generalice mejor.

Aqui susamos RandommizedSearchCV con la siguiente configuracion a tardado unos 40 segundos y mejorando los resultados anteriores
"""

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd


rf_model = RandomForestRegressor(random_state=42)

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5],
    'max_features': ['sqrt', 'log2'],
}

y_train = y_train.ravel()
y_test = y_test.ravel()


random_search = RandomizedSearchCV(rf_model, param_grid, n_iter=10, cv=3, scoring="neg_mean_squared_error", n_jobs=-1, random_state=42)
random_search.fit(X_train, y_train)


best_params = random_search.best_params_
print("Mejores parámetros encontrados:", best_params)


rf_best = RandomForestRegressor(**best_params, random_state=42)
rf_best.fit(X_train, y_train)


y_pred_best = rf_best.predict(X_test)


r2_best = r2_score(y_test, y_pred_best)
rmse_best = mean_squared_error(y_test, y_pred_best) ** 0.5

print("R² del modelo optimizado:", r2_best)
print("RMSE del modelo optimizado:", rmse_best)

print(f"RMSE (Mejor Random Forest): {rmse_best:.2f}")
print(f"Media del PIB: {y_test.mean():.2f}")

# Comparar el RMSE con la media del PIB
if rmse_best < y_test.mean():
    print("El RMSE es aceptable, ya que está por debajo de la media del PIB.")
else:
    print("El RMSE es alto, lo que sugiere que el modelo no está funcionando óptimamente.")

"""

Cuando evaluamos el modelo, para tener una referencia, la media del PIB en el conjunto de prueba es de 7137 aprox., y el error cuadrático medio en Random Forest es de 3937, lo que está por debajo de la media. Si además añadimos que el coeficiente de determinación (R²) es 0.92, podemos decir que el modelo que hemos seleccionado es bastante correcto.

Siempre se podría seguir ajustando hiperparámetros o trabajar con PIBs más altos para mejorar el entrenamiento."""

y_test_array = np.array(y_test)
y_pred_rf_array = np.array(y_pred_best)


plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test_array, y=y_pred_rf_array, alpha=0.5)
plt.plot([y_test_array.min(), y_test_array.max()],
         [y_test_array.min(), y_test_array.max()],
         linestyle='--', color='red')  # Línea de referencia


plt.xlabel("PIB Real")
plt.ylabel("PIB Predicho")
plt.title("Comparación entre PIB Real y Predicho (Random Forest)")
plt.grid()


plt.show()

"""vamos a usar el mismo modelo pero con los datos escalados para ver si tenemos.mejor resultado
Despues de hacer esto y lleer un poco nos damos cuenta que el random forest no se ve afectado apenas por el esacaldo de datos como si podria ser la regresion logistica
"""

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import pandas as pd

#Escalamos los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf_model = RandomForestRegressor(random_state=42)


param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [20, 30, None],
    'min_samples_leaf': [1, 2, 5],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [True]
}

y_train = y_train.ravel()
y_test = y_test.ravel()


random_search = RandomizedSearchCV(rf_model, param_grid, n_iter=10, cv=3, scoring="neg_mean_squared_error", n_jobs=-1, random_state=42)
random_search.fit(X_train_scaled, y_train)


best_params = random_search.best_params_
print("Mejores parámetros encontrados:", best_params)

rf_best = RandomForestRegressor(**best_params, random_state=42)
rf_best.fit(X_train_scaled, y_train)


y_pred_best = rf_best.predict(X_test_scaled)

r2_best = r2_score(y_test, y_pred_best)
rmse_best = mean_squared_error(y_test, y_pred_best) ** 0.5


print("R² del modelo optimizado:", r2_best)
print("RMSE del modelo optimizado:", rmse_best)

"""Ahora vamos con la parte de la explicabilidad."""

feature_importance = rf_best.feature_importances_


sorted_idx = np.argsort(feature_importance)[::-1]
feature_names = X_train.columns

plt.figure(figsize=(10,6))
plt.bar(range(len(feature_importance)), feature_importance[sorted_idx], align="center")
plt.xticks(range(len(feature_importance)), feature_names[sorted_idx], rotation=90)
plt.xlabel("Características")
plt.ylabel("Importancia")
plt.title("Importancia de las Características en el Modelo")
plt.show()

"""En la grafica se pueden ver las caracteristicas mas importantes del modelo. Como aplicamos PCA (reducción de dimensionalidad), perdimos los nombres originales de los campos, así que ahora aparecen como componentes numerados en vez de los nombres de las columnas de antes.

Aun asi, se nota que la Componente_1 es la que mas importa, lo que quiere decir que concentra mucha de la informacion relevante para el modelo. Tambien, en el puesto 7, tenemos el Cluster, que lo creamos con K-Means, asi que parece que sí aporta algo a la prediccion.

Con esto podemos hacernos una idea de qué cosas afectan más a los resultados y si todo lo que hicimos en el preprocesado valió la pena o no
"""

import seaborn as sns

plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test, y=y_pred_best, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle='--', color='red')  #Línea de referencia

plt.xlabel("PIB Real")
plt.ylabel("PIB Predicho")
plt.title("Comparación entre PIB Real y Predicho (Random Forest)")
plt.grid()
plt.show()

"""Este gráfico es el mismo que hemos visto antes, pero la verdad es que es el que mejor nos deja ver cómo de bien funciona el modelo.

Si miramos los puntos, se nota que la mayoría siguen la línea roja, lo que quiere decir que el modelo predice valores muy parecidos a los reales. Aunque hay algunos puntos más alejados, en general la tendencia se mantiene bastante bien, lo cual es una buena señal.

Tambien podemos ver que hay mas puntos en la zona baja del grafico, lo que tiene sentido porque la mayoria de los paises tienen PIBs bajos, y ahi es donde el modelo parece funcionar mejor. En los PIBs mas altos hay algo mas de dispersion, pero en general el modelo se comporta bastante bien.
"""

residuals = y_test - y_pred_best

plt.figure(figsize=(8,6))
sns.histplot(residuals, bins=30, kde=True)
plt.xlabel("Error (PIB Real - PIB Predicho)")
plt.ylabel("Frecuencia")
plt.title("Distribución de los Errores (Residuos)")
plt.show()

"""Para ver los errores del modelo, usamos este gráfico, que nos muestra cómo de cerca están las predicciones de los valores reales. Si hay muchos datos cerca de 0, significa que el modelo ha acertado bastante y los errores son pequeños.

En el gráfico se nota que hay más errores positivos (hacia la derecha), lo que quiere decir que el modelo tiende a predecir valores más bajos de lo que realmente son en algunos casos. Esto nos indica que cuando falla, suele subestimar el PIB real.

En general, parece que el modelo funciona bien, pero estos errores pueden servir para revisar si hay que ajustar algo más o si hay ciertos casos donde el modelo tiene más dificultad para predecir correctamente

"""

import shap

explainer = shap.Explainer(rf_best, X_train_scaled)
shap_values = explainer(X_test_scaled)

shap.summary_plot(shap_values, X_test_scaled, feature_names=X_train.columns)

"""Este grafico nos dice que tanto influye cada variable en la prediccion del modelo. Como hicimos PCA, las variables originales se convirtieron en componentes numeradas, pero igual podemos ver que Componente_1 es la que mas peso tiene en el resultado.

Los valores SHAP (barra de abajo, eje X) nos dicen si cada variable sube o baja la prediccion del PIB. Si el SHAP es alto, la prediccion tambien sube, si es bajo, la baja. Ademas, el color nos dice si el valor de la caracteristica era alto (rojo) o bajo (azul).

Por ejemplo, si vemos mucho rojo en la derecha, significa que cuando esa variable es alta, el PIB sube. Y si hay mucho azul a la izq, significa que cuando la variable es baja, el PIB tambien baja. Con esto podemos ver como afecta cada dato al modelo y si hay algo raro que nos haga ajustar el entrenamiento


Conclusiones
Este análisis ha permitido explorar cómo los indicadores de salud pueden influir en la predicción del PIB de un país, aplicando técnicas avanzadas de preprocesamiento, reducción de dimensionalidad y modelado predictivo. A lo largo del proyecto, se han tomado decisiones estratégicas en la selección y limpieza de datos, asegurando que las variables utilizadas reflejen la realidad económica de cada región.

Uno de los aspectos clave ha sido la aplicación de PCA, que permitió reducir la dimensionalidad del dataset sin perder información relevante, optimizando el rendimiento del modelo. Además, el uso de K-Means ha sido fundamental para generar una nueva variable que ha mejorado la precisión de la predicción, al identificar patrones ocultos en los datos.

En cuanto a la modelización, la comparación entre regresión lineal y Random Forest ha demostrado la importancia de elegir el algoritmo adecuado según la naturaleza del problema. Random Forest ha obtenido los mejores resultados con un R² de 0.92 y un error medio (RMSE) considerablemente bajo, lo que valida su capacidad para capturar la complejidad de la relación entre los factores de salud y el PIB.

Por otro lado, el análisis de la importancia de las características con SHAP ha proporcionado una visión más clara sobre qué factores tienen mayor peso en la predicción, permitiendo interpretar mejor los resultados del modelo. Este tipo de explicabilidad es clave en entornos donde la transparencia y la justificación de las decisiones algorítmicas son esenciales.

En futuras iteraciones, se podrían explorar otros enfoques, como técnicas de optimización más avanzadas o modelos basados en redes neuronales, para evaluar si se pueden mejorar aún más los resultados obtenidos. En definitiva, este proyecto demuestra cómo la combinación de técnicas de machine learning, análisis de datos y explicabilidad puede proporcionar modelos robustos y útiles para la toma de decisiones en el ámbito económico.
"""
