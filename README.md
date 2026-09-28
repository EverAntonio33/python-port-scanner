# Escáner de Puertos Básico en Python

Este es un proyecto de redes y ciberseguridad desarrollado en Python. Permite escanear un rango de puertos TCP en una dirección IP o nombre de dominio para determinar qué servicios se encuentran abiertos.

## 🚀 Características
- Resolución de nombres de dominio (DNS) a direcciones IP mediante `socket.gethostbyname()`.
- Verificación de puertos TCP mediante sockets con tiempo de espera (*timeout*) configurado a 0.3s.
- Manejo de interrupciones de teclado (`Ctrl + C`).
- Interfaz sencilla e interactiva por línea de comandos.

## 🛠️ Tecnologías utilizadas
- **Lenguaje:** Python 3
- **Librerías estándar:** `socket`, `sys`, `datetime`
- **Entorno de ejecución:** Linux (Ubuntu / Kali)

## 📋 Requisitos e Instalación
No requiere instalar librerías de terceros. Solo necesitas tener instalado **Python 3**.

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/EverAntonio33/python-port-scanner.git](https://github.com/EverAntonio33/python-port-scanner.git)
