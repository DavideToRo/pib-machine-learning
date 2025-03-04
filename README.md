# pib-machine-learning
# Teneis el CSV subido para poder trabajar con el codigo, lo podeis importar a colab por si es mas comodo con el entorno.

# Predicción del PIB con Machine Learning

## 📊 Descripción
Este proyecto utiliza **Machine Learning** para predecir el **PIB** de un país a partir de indicadores de salud. Se emplean técnicas de preprocesamiento, reducción de dimensionalidad (**PCA**), clustering (**K-Means**) y modelos predictivos como **Regresión Lineal** y **Random Forest** para mejorar la precisión de la predicción.

## 🚀 Tecnologías Utilizadas
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SHAP)
- **PCA** para reducción de dimensionalidad
- **K-Means** para clustering
- **Regresión Lineal** y **Random Forest** para predicción del PIB
- **Explicabilidad con SHAP**

## 🔍 Análisis del Dataset
Se utilizaron datos sobre indicadores de salud en distintos países, incluyendo:
- Esperanza de vida
- Mortalidad adulta
- Gasto en salud (% del PIB)
- Vacunación
- Índice de recursos económicos
- Escolarización

El dataset fue limpiado, transformado y optimizado para mejorar la calidad de las predicciones.

## 🌟 Resultados Clave
- **Random Forest** obtuvo un **R² de 0.92** con un **RMSE bajo**, superando a la Regresión Lineal.
- **K-Means** ayudó a identificar patrones ocultos en los datos.
- **SHAP** permitió interpretar las variables más influyentes en la predicción.

## 📄 Estructura del Proyecto
```
/
├── data/               # Dataset limpio
├── notebooks/          # Análisis exploratorio y modelado en Jupyter Notebook
├── src/                # Scripts Python para preprocesamiento y modelado
├── README.md           # Documentación del proyecto
└── requirements.txt    # Librerías necesarias
```
## Imagenes del analisis
Matriz de Correlación
![Captura desde 2025-03-04 12-56-43](https://github.com/user-attachments/assets/7008e7f1-976d-4409-92d2-48eab54dbee7)

Detectando outliers
![Captura desde 2025-03-04 12-56-10](https://github.com/user-attachments/assets/4cf70eba-f73f-44cd-a9ea-96d4132e4675)

Comparacion del PIB real y el PREDIDICHO por nuestro modelo de IA 
![Captura desde 2025-03-04 13-00-23](https://github.com/user-attachments/assets/6a7f29ec-3c55-4d10-9f51-493a43f82c8e)




## 💌 Contacto

- **Autor:** David Torres
- **LinkedIn:** [Tu Perfil](https://www.linkedin.com/in/david-torres-robles-913453117/)
- **GitHub:** [Tu GitHub](https://github.com/DavideToRo)

🚀 Si te interesa el proyecto, **no dudes en contribuir o compartir feedback!**


