# PROYECTO 08B — INFORME DE ESCALAMIENTO SOC L1 → SOC L2

## 1. Identificación del caso

- Organización: Orion Financial Group (escenario ficticio).
- Tipo de documento: Informe de escalamiento.
- Nivel que documenta: SOC Analyst L1 (rol simulado).
- Destinatario: SOC Analyst L2.
- Estado: Pendiente de investigación adicional.
- Naturaleza de los datos: Registros simulados con fines formativos.

## 2. Resumen ejecutivo

Los registros simulados presentan cinco intentos fallidos de autenticación
para la cuenta cfernandez, seguidos de una autenticación exitosa desde la
misma IP de origen. Posteriormente, aparecen un acceso al almacenamiento
corporativo, dos descargas de archivos, un intento de acceso denegado a
un recurso del área de Finanzas y una alerta del SIEM.

El escenario también indica que el origen no aparece en el historial reciente
disponible, que el dispositivo es inusual y que el usuario no reconoce la
actividad.

La combinación de estos elementos justifica una investigación adicional
y el escalamiento del caso para su revisión por SOC L2. Sin embargo, los
datos disponibles no permiten confirmar por sí solos un compromiso de
cuenta ni una exfiltración de información.

## 3. Alcance y limitaciones

Este análisis se basa en un conjunto de registros CSV simulados para el
escenario Orion Financial Group. No se dispone aquí de una exportación
real del SIEM ni de registros originales de autenticación, sesiones,
dispositivos o almacenamiento corporativo.

Por tanto, las observaciones reflejan el contenido del escenario y no
constituyen evidencia de un incidente real en una organización.

La IP de origen se trata como un dato que requiere validación contextual.
Su presencia en los registros no demuestra que sea maliciosa.

## 4. Cronología de eventos

| Hora | Evento registrado en el escenario | Resultado |
|---|---|---|
| 09:54 | Intento de autenticación de cfernandez | Fallido |
| 09:55 | Intento de autenticación de cfernandez | Fallido |
| 09:56 | Intento de autenticación de cfernandez | Fallido |
| 09:57 | Intento de autenticación de cfernandez | Fallido |
| 09:58 | Intento de autenticación de cfernandez | Fallido |
| 09:59 | Autenticación de cfernandez | Exitosa |
| 10:03 | Acceso al almacenamiento corporativo | Exitoso |
| 10:06 | Descarga de clientes_Q3.xlsx | Exitosa |
| 10:08 | Descarga de contratos_clientes.zip | Exitosa |
| 10:10 | Intento de acceso a Finance-Shared | Denegado |
| 10:12 | Alerta SIEM relacionada con múltiples fallos | Alerta |

Las horas proceden de los registros simulados y no incluyen fecha completa
ni zona horaria. La cronología no debe interpretarse como una línea de
tiempo de actividad real verificada.

## 5. Hallazgos iniciales

### H-01. Secuencia de autenticación

**Evidencia disponible:** cinco intentos fallidos seguidos de una autenticación
exitosa para la misma cuenta y desde la misma IP, según el CSV simulado.

**Interpretación:** la secuencia requiere revisar el contexto de autenticación.

**Limitación:** no demuestra por sí sola un ataque de fuerza bruta ni un
compromiso de la cuenta.

**Acción recomendada:** revisar los registros de autenticación completos,
el método utilizado, los detalles de la sesión y la legitimidad del acceso.

### H-02. Descargas de archivos corporativos

**Evidencia disponible:** el escenario registra las descargas de
clientes_Q3.xlsx y contratos_clientes.zip.

**Interpretación:** las descargas requieren validación por la naturaleza
de los recursos y el contexto de la cuenta.

**Limitación:** no se dispone de evidencia que demuestre una transferencia
a terceros o una exfiltración.

**Acción recomendada:** revisar los registros del almacenamiento, los permisos
de la cuenta, el contexto de las descargas y la actividad posterior.

### H-03. Acceso denegado a Finance-Shared

**Evidencia disponible:** el escenario registra un intento de acceso denegado
al recurso Finance-Shared.

**Interpretación:** es necesario comprobar si el intento se relaciona con
la actividad legítima de la cuenta o con una conducta no autorizada.

**Limitación:** el rechazo no demuestra una escalada de privilegios.

**Acción recomendada:** verificar los permisos efectivos, el motivo del
rechazo y los eventos relacionados con el recurso.

### H-04. Alerta SIEM

**Evidencia disponible:** el CSV simulado contiene una alerta asociada a
múltiples intentos fallidos de autenticación.

**Interpretación:** la alerta requiere validación y correlación con los
registros que la originaron.

**Limitación:** no se dispone de la regla SIEM original, sus umbrales ni
los registros completos de correlación.

**Acción recomendada:** revisar la regla, su severidad, los eventos asociados
y el fundamento de la alerta.

### H-05. Contexto del origen y del dispositivo

**Evidencia disponible:** el escenario indica que la IP no aparece en el
historial reciente disponible y que el dispositivo es inusual. También
indica que el usuario no reconoce la actividad.

**Interpretación:** estos elementos aumentan la necesidad de verificar
la legitimidad del acceso.

**Limitación:** una IP desconocida o un dispositivo inusual no prueban
por sí solos una actividad maliciosa.

**Acción recomendada:** validar el dispositivo, revisar el historial de
acceso disponible y confirmar la actividad con el usuario mediante el
procedimiento autorizado.

## 6. Evaluación preliminar

El conjunto de eventos presenta indicadores que justifican una investigación
adicional. La secuencia de autenticación, las descargas, el acceso denegado,
la alerta SIEM y el contexto del dispositivo deben analizarse de forma
correlacionada.

Con la información disponible no es posible confirmar:

- Un compromiso de cuenta.
- Un ataque de fuerza bruta.
- Una exfiltración de datos.
- Una escalada de privilegios.
- La naturaleza maliciosa de la IP de origen.

La clasificación y prioridad definitivas deben determinarse conforme al
procedimiento de respuesta a incidentes de la organización y después de
validar la evidencia adicional.

## 7. Recomendaciones para SOC L2

1. Obtener y revisar los registros originales de autenticación y sesión.
2. Validar la identidad, el dispositivo y la legitimidad del acceso.
3. Correlacionar los eventos con la alerta SIEM y revisar la regla que la generó.
4. Revisar los registros de acceso y descarga del almacenamiento corporativo.
5. Verificar los permisos de la cuenta y el motivo del acceso denegado.
6. Determinar si corresponde aplicar medidas de contención de acuerdo con
   la evidencia y los procedimientos autorizados.
7. Documentar las decisiones, las evidencias consultadas y los resultados
   de cada verificación.

Las recomendaciones anteriores no significan que las medidas de contención
se hayan ejecutado. No hay evidencia en el material analizado que permita
afirmar que la cuenta fue bloqueada, que las sesiones fueron revocadas o
que un dispositivo fue aislado.

## 8. Motivo del escalamiento

Se recomienda escalar el caso a SOC L2 para investigar de forma correlacionada
la secuencia de autenticación, las descargas, el intento de acceso denegado,
la alerta SIEM y el contexto inusual de acceso indicado en el escenario.

El escalamiento se fundamenta en la necesidad de validar los hechos y
determinar si existe un incidente que requiera respuesta adicional. No
representa una confirmación de compromiso.

## 9. Estado del caso

- Estado actual: Pendiente de investigación adicional.
- Hallazgos: Cinco observaciones iniciales documentadas.
- Validación con el usuario: Indicada en el escenario como no reconocimiento
  de la actividad; no se dispone de un registro independiente de esa consulta.
- Contención: No consta como ejecutada.
- Conclusión definitiva: Pendiente de evidencia adicional.

## 10. Trazabilidad y naturaleza de los datos

El análisis se ha elaborado a partir del archivo
eventos_orion_simulados.csv y del contexto ficticio del caso Orion Financial
Group.

Los resultados de los scripts de Python y este informe forman parte de
un ejercicio formativo. No deben presentarse como registros extraídos de
un SIEM real.

Los archivos PCAPNG del laboratorio de red constituyen evidencias técnicas
separadas y no corroboran los eventos ficticios de Orion.
