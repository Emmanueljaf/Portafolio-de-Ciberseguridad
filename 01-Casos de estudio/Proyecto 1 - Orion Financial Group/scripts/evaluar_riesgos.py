import csv
from pathlib import Path

# 1. Localizar y leer los registros simulados
archivo = (
    Path.home()
    / "Proyecto8"
    / "datos"
    / "eventos_orion_simulados.csv"
)

with archivo.open(newline="", encoding="utf-8") as f:
    eventos = list(csv.DictReader(f))

# 2. Calcular indicadores básicos
fallos = [
    e for e in eventos
    if e["event_type"] == "authentication"
    and e["result"] == "FAILED"
]

exitos = [
    e for e in eventos
    if e["event_type"] == "authentication"
    and e["result"] == "SUCCESS"
]

descargas = [
    e for e in eventos
    if e["event_type"] == "file_download"
    and e["result"] == "SUCCESS"
]

denegados = [
    e for e in eventos
    if e["result"] == "DENIED"
]

alertas = [
    e for e in eventos
    if e["event_type"] == "siem_alert"
]

# 3. Mostrar la matriz de evaluación
print("=" * 65)
print(" MATRIZ INICIAL DE EVALUACION - CASO ORION")
print(" DATOS FICTICIOS PARA FORMACION")
print("=" * 65)

print("\nINDICADOR 1: AUTENTICACIONES FALLIDAS")
print(f"Eventos registrados: {len(fallos)}")
print("Evaluacion: investigar la secuencia y su contexto.")

print("\nINDICADOR 2: AUTENTICACION EXITOSA")
print(f"Eventos registrados: {len(exitos)}")
print("Evaluacion: verificar identidad, dispositivo y legitimidad.")

print("\nINDICADOR 3: DESCARGAS DE ARCHIVOS")
print(f"Descargas registradas: {len(descargas)}")

for evento in descargas:
    print(f'  - {evento["timestamp"]}: {evento["resource"]}')

print("Evaluacion: verificar autorizacion y necesidad de acceso.")

print("\nINDICADOR 4: ACCESOS DENEGADOS")
print(f"Eventos registrados: {len(denegados)}")

for evento in denegados:
    print(f'  - {evento["timestamp"]}: {evento["resource"]}')

print("Evaluacion: revisar el motivo del rechazo y los permisos.")

print("\nINDICADOR 5: ALERTAS DEL SIEM")
print(f"Eventos registrados: {len(alertas)}")
print("Evaluacion: consultar la regla y la evidencia que genero la alerta.")

# 4. Registrar los limites de la evaluacion
print("\n" + "=" * 65)
print("LIMITES Y CONCLUSIONES")
print("=" * 65)

print("- Los registros pertenecen a un escenario simulado.")
print("- Los intentos fallidos no prueban por si solos un ataque.")
print("- Una autenticacion exitosa no demuestra un compromiso.")
print("- Las descargas no demuestran por si solas una exfiltracion.")
print("- Un acceso denegado no demuestra una escalada de privilegios.")
print("- La IP de origen requiere validacion contextual independiente.")

print("\nResultado: se identifican actividades que requieren investigacion.")
print("No se confirma un compromiso de cuenta con estos datos solamente.")
