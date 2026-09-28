import socket
import sys
from datetime import datetime

def escanear():
    print("=" * 50)
    print("      ESCANER DE PUERTOS BASICO EN PYTHON      ")
    print("=" * 50)

    ip = input("IP a escanear (ej. 127.0.0.1): ").strip()
    try:
        ip_obj = socket.gethostbyname(ip)
    except socket.gaierror:
        print("IP no valida")
        sys.exit()

    p_ini = int(input("puerto inicial: "))
    p_fin = int(input("puerto final: "))

    print("\nEscaneando: " + ip_obj)

    try:
        for p in range(p_ini, p_fin + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            if s.connect_ex((ip_obj, p)) == 0:
                print(f"[+] puerto ABIERTO: {p}")
            s.close()
    except KeyboardInterrupt:
        print("\nCancelado.")
        sys.exit()

    print("\nEscaneo completado.")

if __name__ == "__main__":
    escanear()

