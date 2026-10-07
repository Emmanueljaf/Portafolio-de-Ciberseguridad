-- =====================================================================
-- PROYECTO: Aplicar filtros a consultas SQL para investigaciones de seguridad
-- Entorno: MariaDB | Tablas: log_in_attempts y employees
-- =====================================================================

-- INVESTIGACIÓN 1: Intentos fallidos de inicio de sesión fuera del horario laboral
-- Objetivo: Recuperar intentos de inicio de sesión fallidos después de las 18:00 horas.
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = FALSE;


-- INVESTIGACIÓN 2: Intentos de inicio de sesión en fechas específicas (8 y 9 de mayo de 2022)
-- Objetivo: Ampliar la ventana temporal de análisis alrededor del evento sospechoso.
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';


-- INVESTIGACIÓN 3: Intentos de inicio de sesión fuera de México
-- Objetivo: Excluir los accesos originados en México para analizar ubicaciones externas.
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';


-- INVESTIGACIÓN 4: Empleados de Marketing del edificio East
-- Objetivo: Identificar dispositivos de empleados específicos para actualizaciones de seguridad.
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';


-- INVESTIGACIÓN 5: Empleados de Finance o Sales
-- Objetivo: Localizar empleados pertenecientes a cualquiera de los dos departamentos clave.
SELECT *
FROM employees
WHERE department = 'Finance' OR department = 'Sales';


-- INVESTIGACIÓN 6: Empleados que no pertenecen a IT
-- Objetivo: Identificar al resto de los departamentos que requieren la actualización de seguridad.
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';