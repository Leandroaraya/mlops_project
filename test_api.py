import requests

# URL de tu API Flask corriendo en Docker
url = "http://127.0.0.1:5000/predict"

# Ejemplo de features: 31 valores (debes reemplazar con valores reales de tu dataset)
data = {
    "features": [
        17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471,
        0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904,
        0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0,
        0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189, 0.3416
    ]
}

# Hacer POST a la API
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except:
    print("Respuesta no es JSON:", response.text)
