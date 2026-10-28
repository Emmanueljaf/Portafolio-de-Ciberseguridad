import csv
from pathlib import Path
from collections import Counter
from datetime import datetime

# 1. Localizar el archivo CSV dentro del directorio personal
archivo = (
    Path.home()
    / "Proyecto8"
    / "datos"
    / "eventos_orion_simulados.csv"
)

# 2. Leer los registros del CSV
with archivo.open(newline="", encoding="utf-8") as f:
    eventos = list(csv.DictReader(f))

# 3. Ordenar los eventos por hora
eventos.sort(
    key=lambda evento: datetime.strptime(
        evento["timestamp"], "%H:%M"
    )
)

print("=" * 55)
print(" ANALISIS AMPLIADO DE EVENTOS SIMULADOS - ORION")
print("=" * 55)

print(f"\nArchivo analizado: {archivo}")
print(f"Total de eventos: {len(eventos)}")

# 4. Mostrar la cronologia completa
print("\n--- CRONOLOGIA DE EVENTOS ---")

for evento in eventos:
    print(
        f'{evento["timestamp"]} | '
        f'{evento["event_type"]} | '
        f'{evento["account"]} | '
        f'{evento["result"]} | '
        f'{evento["resource"]}'
    )

# 5. Analizar los resultados de autenticacion
autenticaciones = [
    evento for evento in eventos
    if evento["event_type"] == "authentication"
]

resultados = Counter(
    evento["result"] for evento in autenticaciones
)

print("\n--- RESUMEN DE AUTENTICACION ---")
print(f"Total de eventos de autenticacion: {len(autenticaciones)}")

for resultado, cantidad in sorted(resultados.items()):
    print(f"{resultado}: {cantidad}")

# 6. Identificar descargas registradas
descargas = [
    evento for evento in eventos
    if evento["event_type"] == "file_download"
]

print("\n--- DESCARGAS REGISTRADAS ---")
print(f"Cantidad de eventos de descarga: {len(descargas)}")

for evento in descargas:
    print(
        f'{evento["timestamp"]} | '
        f'{evento["resource"]} | '
        f'Cuenta: {evento["account"]} | '
        f'Resultado: {evento["result"]}'
    )

# 7. Identificar accesos denegados
denegados = [
    evento for evento in eventos
    if evento["result"] == "DENIED"
]

print("\n--- ACCESOS DENEGADOS ---")
print(f"Cantidad de eventos denegados: {len(denegados)}")

for evento in denegados:
    print(
        f'{evento["timestamp"]} | '
        f'Recurso: {evento["resource"]} | '
        f'Cuenta: {evento["account"]}'
    )

# 8. Mostrar una observacion prudente
fallos = [
    evento for evento in autenticaciones
    if evento["result"] == "FAILED"
]

exitos = [
    evento for evento in autenticaciones
    if evento["result"] == "SUCCESS"
]

print("\n--- OBSERVACION DEL ANALISTA ---")

if fallos and exitos:
    print(
        "Se observan autenticaciones fallidas y una exitosa "
        "en los registros simulados."
    )
    print(
        "Es necesario revisar el contexto, el origen del acceso "
        "y la legitimidad de la actividad."
    )
    print(
        "Estos eventos, por si solos, no confirman "
        "un compromiso de cuenta."
    )
else:
    print(
        "No se observa la combinacion de autenticaciones "
        "fallidas y exitosas en los registros analizados."
    )

print("\nAnalisis finalizado.")
