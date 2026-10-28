# PROYECTO 08B — ACTUALIZACION DEL CASO ORION

## 1. Datos del caso

- Identificador: ORION-SIM-001
- Organizacion: Orion Financial Group (escenario ficticio).
- Responsable de la actualizacion: SOC Analyst L1 (rol simulado).
- Destinatario: SOC L2 y responsables autorizados.
- Fecha y hora de la actualizacion: Pendiente de establecer.
- Estado: Pendiente de investigacion adicional.

## 2. Resumen

Los registros simulados muestran cinco intentos fallidos de autenticacion,
seguidos de una autenticacion exitosa. Posteriormente se registran dos
descargas de archivos corporativos, un acceso denegado a Finance-Shared
y una alerta SIEM.

El escenario indica que el usuario no reconoce la actividad y que el
dispositivo es inusual. Estos elementos justifican una investigacion
adicional, pero no confirman por si solos un compromiso de cuenta.

## 3. Evidencia disponible

- Archivo de eventos simulados:
  datos/eventos_orion_simulados.csv
- Registro inicial de hallazgos:
  hallazgos_iniciales.csv
- Informe de escalamiento:
  informe_escalamiento_soc_l1_l2.md

Los archivos enumerados son materiales del ejercicio formativo.
No representan exportaciones de sistemas corporativos reales.

## 4. Actividades completadas en el ejercicio

- Lectura y analisis de los registros CSV simulados.
- Organizacion cronologica de los eventos.
- Identificacion de indicadores que requieren investigacion.
- Documentacion de cinco hallazgos iniciales.
- Preparacion del informe de escalamiento.
- Elaboracion de un plan propuesto de respuesta.

## 5. Actividades pendientes

- Obtener y revisar registros originales de autenticacion y sesiones.
- Validar la identidad, el dispositivo y la legitimidad del acceso.
- Revisar los registros originales de almacenamiento y descargas.
- Examinar la regla y el contexto de la alerta SIEM.
- Determinar si corresponde aplicar medidas de contencion autorizadas.
- Registrar las decisiones y los resultados de la investigacion.

## 6. Riesgos y limitaciones

No se ha confirmado un compromiso de cuenta, una exfiltracion de datos
ni una escalada de privilegios.

No consta que se hayan bloqueado cuentas, revocado sesiones, aislado
dispositivos o aplicado otras medidas de contencion.

La evaluacion se basa en un escenario ficticio y debe actualizarse
cuando exista evidencia adicional.

## 7. Solicitud al equipo receptor

Se solicita revisar los indicadores documentados, validar la evidencia
disponible y determinar la prioridad y las siguientes acciones conforme
al procedimiento de respuesta a incidentes.

## 8. Registro de actualizaciones

| Fecha y hora | Cambio o resultado | Responsable | Estado |
|---|---|---|---|
| Pendiente | Primera documentacion del caso simulado | SOC L1 (rol simulado) | Preparado para revision |

## 9. Estado final de esta actualizacion

Documento preparado como parte de un ejercicio formativo.
No representa una comunicacion enviada ni una respuesta ejecutada
en una organizacion real.
