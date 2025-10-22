# Cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa.

## Modificación del Diseño

Si este microservicio tuviera que comunicarse con otro servicio encargado de almacenar el historial de cálculos en una base de datos externa, el diseño debería incluir un componente adicional responsable de la comunicación entre servicios.

## Implementación

Después de calcular el factorial y determinar su paridad, el microservicio podría enviar los resultados al servicio de historial mediante una petición HTTP POST, enviando un objeto JSON con la información del cálculo.

### Ejemplo de código:
```python
import requests

# Datos del cálculo
data = {
    "numero recibido": n, 
    "factorial": fact, 
    "paridad": paridad
}

# Enviamos al servicio de historial
requests.post("http://historial-service/guardar", json=data)
```

## Ventajas

- **Separación de responsabilidades**: Se sigue cumpliendo una sola responsabilidad —realizar el cálculo—, mientras que el otro servicio se encarga de registrar la información en la base de datos

- **Independencia y escalabilidad**: Los componentes mantienen su independencia y pueden actualizarse o desplegarse de manera separada

- **Bajo acoplamiento**: Los servicios se comunican a través de una interfaz bien definida sin depender de las implementaciones internas del otro


## Pequeño diagrama
```
Cliente 
   ↓
Microservicio Factorial (calcula)
   ↓
HTTP POST
   ↓
Microservicio Historial (persiste)
   ↓
Base de Datos
```
