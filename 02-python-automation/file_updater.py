# =====================================================================
# PROYECTO: Actualizar un archivo mediante un algoritmo de Python
# Propósito: Automatizar la revisión y control de acceso de IPs autorizadas.
# =====================================================================

# Asignar el nombre del archivo a la variable import_file
import_file = "allow_list.txt"

# Definir la lista de direcciones IP que deben perder el acceso
remove_list = ["192.168.2.50", "192.168.1.100"]

# 1. Abrir el archivo en modo lectura ('r') utilizando la sentencia with
print(f"[*] Abriendo el archivo '{import_file}' para lectura...")
with open(import_file, "r") as file:
    # 2. Leer el contenido del archivo y almacenarlo como un string
    ip_addresses = file.read()

# 3. Convertir el string en una lista utilizando el método .split()
ip_addresses = ip_addresses.split()

# 4. Recorrer la lista de direcciones que deben eliminarse mediante un bucle for
print("[*] Procesando la lista de eliminación de accesos...")
for element in remove_list:
    # 5. Comprobar si la dirección existe en la lista y eliminarla con .remove()
    if element in ip_addresses:
        ip_addresses.remove(element)
        print(f"[+] IP retirada de los permisos: {element}")

# 6. Convertir la lista actualizada nuevamente en un string usando .join() con saltos de línea
ip_addresses = "\n".join(ip_addresses)

# 7. Abrir el archivo nuevamente en modo escritura ('w') para sobrescribir con el contenido actualizado
print(f"[*] Actualizando y guardando el archivo '{import_file}'...")
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("[✔] Proceso completado con éxito. Control de accesos actualizado.")