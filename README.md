# **Predicción de Precios de Viviendas con Redes Neuronales**

## **Descripción del Proyecto**
Este proyecto tiene como objetivo desarrollar un modelo de redes neuronales para predecir el precio de viviendas a partir de diversas características estructurales y de ubicación. Se utilizará un dataset histórico disponible en Kaggle y se aplicará un enfoque de aprendizaje profundo para mejorar la precisión de las predicciones en comparación con modelos tradicionales como la regresión lineal.

## **Dataset**
El dataset utilizado proviene de Kaggle:

[Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)

### **Características de Entrada:**
- `area`: Área total de la vivienda en pies cuadrados.
- `bedrooms`: Número de habitaciones.
- `bathrooms`: Número de baños.
- `stories`: Número de pisos.
- `mainroad`: Si la casa está en una calle principal (Sí/No).
- `guestroom`: Si tiene habitación de invitados (Sí/No).
- `basement`: Si cuenta con sótano (Sí/No).
- `hotwaterheating`: Si tiene calefacción de agua caliente (Sí/No).
- `airconditioning`: Si cuenta con aire acondicionado (Sí/No).
- `parking`: Número de plazas de estacionamiento.
- `prefarea`: Si está en una zona preferencial (Sí/No).
- `furnishingstatus`: Estado del mobiliario (Amueblado, Semiamueblado, No amueblado).

### **Variable Objetivo:**
- `price`: Precio de venta de la propiedad (variable continua a predecir).

---

## **Estructura del Proyecto**
1. **Business Case Discovery**
   - Contexto del negocio y objetivos.
   - Identificación de stakeholders y requisitos.
   - Definición de métricas de éxito.

2. **Procesamiento de Datos**
   - Carga y exploración inicial del dataset.
   - Análisis de correlación entre variables.
   - Preprocesamiento (manejo de valores nulos, codificación de variables categóricas, normalización).
   - División de los datos en conjuntos de entrenamiento y prueba (80/20).

3. **Planificación del Modelo**
   - Definición del problema y tipo de modelo (Regresión con red neuronal).
   - Diseño de la arquitectura de la red neuronal.
   - Selección de función de pérdida, optimizador y métricas de evaluación.

4. **Construcción y Entrenamiento del Modelo**
   - Implementación del modelo en Keras.
   - Entrenamiento con diferentes hiperparámetros (épocas, tamaño de batch, tasas de aprendizaje).
   - Evaluación del rendimiento mediante validación cruzada.

5. **Evaluación y Resultados**
   - Análisis de predicciones y errores.
   - Comparación con un modelo de regresión lineal.
   - Visualización de resultados mediante gráficos.

6. **Despliegue del Modelo**
   - Serialización del modelo entrenado.
   - Implementación de una API con Flask para realizar predicciones en tiempo real.

---
