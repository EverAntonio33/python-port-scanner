# Escáner de Puertos Básico en Python

Este proyecto es una herramienta ligera desarrollada en Python para la exploración de red y auditoría de seguridad. Permite identificar servicios activos en una máquina objetivo mediante el escaneo de puertos TCP.

---

## 🛠️ Desarrollo Técnico y Metodología

El script fue diseñado e implementado siguiendo un enfoque práctico en administración de redes y ciberseguridad:

1. **Gestión de Sockets y Conexión TCP (`socket`):**
   - Se utiliza `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` para establecer un flujo de socket IPv4 sobre el protocolo TCP.
   - Para evitar bloqueos indefinidos durante el análisis de puertos cerrados o filtrados, se implementó un tiempo de espera no bloqueante mediante `settimeout(0.3)`.
   - La comprobación del estado del puerto se realiza mediante `connect_ex()`, el cual devuelve `0` cuando la conexión es exitosa y el puerto se encuentra abierto.

2. **Resolución de Dominio y Control de Excepciones:**
   - Implementación de `socket.gethostbyname()` para traducir automáticamente nombres de dominio (FQDN) a direcciones IP.
   - Captura de errores de red con `socket.gaierror` para prevenir el colapso de la aplicación ante direcciones no válidas.
   - Manejo de la señal de interrupción del sistema mediante `KeyboardInterrupt` (`Ctrl + C`) para garantizar una salida limpia.

---

## 🚀 Características Principales
- Resolución dinámica de nombres de dominio (DNS) a IP.
- Verificación TCP con tiempo de respuesta optimizado (*timeout* a 300 ms).
- Control de interrupciones de usuario desde la línea de comandos.
- Interfaz interactiva para definir el objetivo y el rango de puertos a evaluar.

## 📋 Requisitos e Instalación
No requiere dependencias externas. Solo requiere un entorno con **Python 3**.

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/EverAntonio33/python-port-scanner.git](https://github.com/EverAntonio33/python-port-scanner.git)
