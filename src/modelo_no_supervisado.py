import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import os

os.makedirs('resultados', exist_ok=True)

# 1. Cargar datos
try:
    data = pd.read_csv('data/rutas_sitp_ml.csv')
    print("Datos cargados correctamente. Primeras filas:")
    print(data.head())
except Exception as e:
    print(f"Error cargando datos: {e}")
    exit()

# 2. Preprocesamiento
try:
    print("\nColumnas disponibles:", data.columns.tolist())
    
    # Convertir hora a minutos
    data['hora_minutos'] = data['hora_dia'].apply(
        lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))
    
    # Verificar y limpiar columna 'demanda'
    print("\nValores únicos en 'demanda':", data['demanda'].unique())
    data['demanda'] = data['demanda'].str.lower().str.strip()
    
    # One-hot encoding para demanda
    data = pd.get_dummies(data, columns=['demanda'], prefix='demanda')
    print("\nColumnas después de one-hot:", data.columns.tolist())
    
    # Seleccionar features para clustering
    required_columns = ['distancia_km', 'transbordos', 'hora_minutos']
    for col in ['demanda_alta', 'demanda_media', 'demanda_baja']:
        if col in data.columns:
            required_columns.append(col)
    
    print("\nColumnas seleccionadas:", required_columns)
    X = data[required_columns]
    
    # Estandarizar datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
except Exception as e:
    print(f"\nError en preprocesamiento: {str(e)}")
    print("DataFrame actual:", data.head())
    exit()

# 3. Método del codo para encontrar k óptimo
inertia = []
for k in range(1, 6):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Graficar método del codo
plt.figure(figsize=(8, 5))
plt.plot(range(1, 6), inertia, marker='o')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inercia')
plt.title('Método del Codo para K óptimo')
plt.savefig('resultados/elbow_method.png')
plt.close()
print("Gráfico de método del codo guardado.")

# 4. Entrenar modelo con k=3
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
data['cluster'] = clusters

data.to_csv('resultados/rutas_clusters.csv', index=False)
print("Resultados de clustering guardados.")

# 5. Visualización con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=clusters, 
                palette='viridis', s=100)
plt.title('Clusters de Rutas SITP (PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.savefig('resultados/clusters_pca.png')
plt.close()
print("Gráfico de clusters guardado.")

print("\nProceso completado exitosamente!")
