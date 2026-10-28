import csv
from collections import Counter

archivo = "/home/emmanuel/Proyecto8/datos/eventos_orion_simulados.csv"

with open(archivo, newline="", encoding="utf-8") as f:
    eventos = list(csv.DictReader(f))

print("=== ANALISIS DE EVENTOS SIMULADOS ===")
print(f"Total de eventos: {len(eventos)}")

autenticaciones = [
    evento for evento in eventos
    if evento["event_type"] == "authentication"
]

resultados = Counter(evento["result"] for evento in autenticaciones)

print("\nResultados de autenticacion:")
for resultado, cantidad in sorted(resultados.items()):
    print(f"  {resultado}: {cantidad}")

fallos = [
    evento for evento in autenticaciones
    if evento["result"] == "FAILED"
]

exitos = [
    evento for evento in autenticaciones
    if evento["result"] == "SUCCESS"
]

print(f"\nIntentos fallidos: {len(fallos)}")
print(f"Autenticaciones exitosas: {len(exitos)}")

if fallos and exitos:
    print(
        "\nOBSERVACION: los datos simulados contienen "
        "intentos fallidos y una autenticacion exitosa."
    )
    print(
        "Esto requiere contexto adicional; por si solo, "
        "no demuestra un compromiso de cuenta."
    )
