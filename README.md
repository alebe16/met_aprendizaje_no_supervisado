# Modelo No Supervisado - Agrupamiento de Rutas SITP

Se aplicaron técnicas de aprendizaje no supervisado al sistema de transporte masivo de Bogotá (SITP) con el fin de agrupar rutas similares según variables como distancia, transbordos, hora del día y demanda. A diferencia del aprendizaje supervisado, aquí no se usan etiquetas, sino que se buscan patrones ocultos en los datos.

**Dataset Utilizado**

Fuente:

Dataset sintético simulado: rutas_sitp_ml.csv

**Columnas:**

- origen: estación de inicio del trayecto

- destino: estación de destino

- ruta_directa: 1 si existe ruta directa, 0 si requiere transbordo

- transbordos: cantidad de transbordos requeridos

- distancia_km: distancia aproximada de la ruta

- hora_dia: hora de inicio del viaje

- dia_semana: número del día (1: lunes, ..., 7: domingo)

- demanda: nivel de demanda de la ruta (alta, media, baja)

**Preprocesamiento:**

Se convierte la columna hora_dia en hora_minutos

Se aplica one-hot encoding a demanda 

Se estandarizan variables numéricas con StandardScaler

**Modelo No Supervisado:** K-Means Clustering

**Objetivo:**

Agrupar rutas similares con base en sus características (distancia, hora, transbordos, nivel de demanda).

**Ventajas:**

Sencillo de implementar

Intuitivo para visualizar agrupaciones

Permite descubrir patrones no evidentes

**Variables Seleccionadas para Clustering:**

distancia_km

transbordos

hora_minutos

demanda_alta, demanda_media, demanda_baja (one-hot)

**Implementación:**

Se explora el número óptimo de clusters usando el Método del Codo

Se elige k=3 como valor óptimo

Se entrena un modelo KMeans con 3 clusters

Se visualizan los resultados con PCA en 2 dimensiones

**Resultados Generados:**

resultados/rutas_clusters.csv: archivo con cada ruta y su cluster asignado

resultados/elbow_method.png: gráfico del método del codo

resultados/clusters_pca.png: visualización PCA de los clusters

**Principales Hallazgos**

Se identificaron 3 grupos naturales de rutas con comportamientos distintos.

La distancia y la hora del día son las variables más influyentes.

Las rutas en hora pico tienden a formar clusters consistentes.

El modelo permite detectar patrones sin necesidad de variables objetivo.

**Aplicaciones Prácticas**

- Optimizar la distribución de buses según la agrupación de rutas

- Apoyar la planificación de nuevas rutas en zonas con alta demanda

- Estudiar el comportamiento de usuarios en diferentes horarios

**Limitaciones**

1. Dependencia de la calidad de los datos de entrada (distancias, horarios)

2. Sensibilidad a outliers (valores atípicos pueden afectar los clusters)

3. Requiere escalado previo para garantizar comparaciones justas

**Conclusión**

Este proyecto evidencia el potencial del aprendizaje no supervisado para analizar y mejorar el sistema de transporte público en entornos urbanos. A partir de variables clave como la distancia, la hora y la demanda, el modelo K-Means logró agrupar rutas con patrones similares, lo que facilita la toma de decisiones en logística, planificación y servicio al usuario. El enfoque es escalable y puede enriquecerse con datos reales del SITP, permitiendo a futuro una segmentación más precisa del comportamiento del sistema.

