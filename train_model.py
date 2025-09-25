import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Cargar datos
data = pd.read_csv("data.csv")  # coincide con tu archivo

# 2. Preparar variables
X = data.drop(["id", "diagnosis"], axis=1)
y = data["diagnosis"].map({"M":1, "B":0})

# 3. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entrenar modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluar modelo
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 6. Crear carpeta 'models' si no existe
os.makedirs("models", exist_ok=True)

# 7. Guardar modelo
joblib.dump(model, "models/breast_cancer_model.pkl")
print("Modelo guardado en models/breast_cancer_model.pkl")
