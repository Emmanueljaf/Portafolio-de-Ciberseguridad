# PROYECTO 08B — PLAN DE RESPUESTA AL INCIDENTE

## 1. Identificacion

- Organizacion: Orion Financial Group (escenario ficticio).
- Rol inicial: SOC Analyst L1.
- Escalamiento propuesto: SOC L2.
- Estado: Investigacion pendiente.
- Tipo de actividad: Ejercicio formativo con datos simulados.

## 2. Objetivo

Establecer una secuencia de investigacion y respuesta para validar
los indicadores observados, determinar si existe un incidente de
seguridad y recomendar medidas proporcionales a la evidencia.

## 3. Fase A — Validacion inicial

Acciones:
1. Revisar la cronologia de autenticaciones y actividades posteriores.
2. Obtener los registros originales de autenticacion y sesiones.
3. Revisar la alerta SIEM y la regla que la genero.
4. Verificar la identidad y el dispositivo asociado al acceso.
5. Confirmar con el usuario, mediante el procedimiento autorizado,
   si reconoce la actividad.

Resultado esperado:
Disponer de evidencia adicional para evaluar la legitimidad de la
actividad y determinar si corresponde mantener o modificar la
clasificacion preliminar.

Responsable propuesto:
SOC L1 para la revision inicial, con apoyo de SOC L2 cuando sea necesario.

Estado: Pendiente.

## 4. Fase B — Investigacion de actividad sobre archivos

Acciones:
1. Revisar los registros de acceso al almacenamiento corporativo.
2. Confirmar los permisos de la cuenta sobre los archivos.
3. Verificar la hora, el contexto y los detalles disponibles de las descargas.
4. Buscar evidencia adicional de transferencia o acceso posterior,
   si los registros y las herramientas disponibles lo permiten.
5. Documentar los resultados y las limitaciones de la evidencia.

Resultado esperado:
Determinar si las descargas estaban autorizadas y si existe evidencia
adicional de actividad no permitida.

Responsable propuesto:
SOC L2 en coordinacion con el equipo responsable del almacenamiento.

Estado: Pendiente.

## 5. Fase C — Evaluacion y posible contencion

Antes de aplicar medidas, validar la evidencia disponible, evaluar
el impacto potencial y seguir el procedimiento de respuesta de la
organizacion.

Medidas que podrian considerarse, segun los hallazgos y las
autorizaciones correspondientes:
- Revocar sesiones activas sospechosas.
- Restablecer las credenciales si existe fundamento para hacerlo.
- Aplicar controles temporales sobre la cuenta, cuando corresponda.
- Restringir temporalmente el acceso a recursos afectados.
- Aislar un dispositivo si se obtiene evidencia que lo justifique.

Estas medidas son recomendaciones condicionales. No consta que se
haya ejecutado ninguna de ellas en el escenario disponible.

Antes y despues de cualquier medida autorizada, documentar:
- Motivo de la decision.
- Responsable y autorizacion.
- Hora de ejecucion.
- Sistema o cuenta afectados.
- Resultado observado.
- Posibles efectos sobre la actividad legitima.
- Evidencia conservada.

Responsable propuesto:
SOC L2 y los responsables autorizados de identidad, infraestructura
o respuesta a incidentes, segun el procedimiento interno.

Estado: Pendiente de evaluacion.

## 6. Fase D — Escalamiento y coordinacion

Acciones:
1. Compartir el informe de escalamiento y los hallazgos disponibles.
2. Identificar la evidencia que falta obtener.
3. Solicitar una decision sobre la prioridad y las siguientes acciones.
4. Registrar las decisiones y los responsables asignados.
5. Mantener actualizado el estado del caso.

Criterio:
Escalar cuando la complejidad, el impacto potencial o los indicadores
superen el alcance de la investigacion inicial de SOC L1.

Estado: Escalamiento recomendado; recepcion no confirmada.

## 7. Fase E — Recuperacion y cierre

Solo si la investigacion confirma un incidente y se aplican medidas
de respuesta, evaluar:
- Recuperacion segura del acceso y de los servicios afectados.
- Validacion de que las medidas aplicadas fueron efectivas.
- Revision de posibles actividades residuales.
- Documentacion de la causa y del impacto confirmado.
- Lecciones aprendidas y oportunidades de mejora.

No se declara recuperacion ni cierre en esta etapa porque no hay
evidencia suficiente para confirmar un compromiso o una remediacion.

Estado: No iniciado.

## 8. Criterios para actualizar la evaluacion

Reevaluar el caso cuando se disponga de:
- Registros originales de autenticacion y sesion.
- Confirmacion independiente sobre la actividad del usuario.
- Informacion validada del dispositivo.
- Registros de almacenamiento y descargas.
- Detalles de la alerta SIEM.
- Evidencia adicional que confirme o descarte actividad no autorizada.

## 9. Estado general

Estado actual: Pendiente de investigacion adicional.

Los datos utilizados pertenecen al escenario simulado de Orion
Financial Group. Este documento es un plan propuesto y no demuestra
que las acciones descritas se hayan ejecutado.
