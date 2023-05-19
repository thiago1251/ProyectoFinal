SELECT centros.nombre AS Centro, adultos.Nombre, adultos.Apellido 
FROM centros INNER JOIN adultos ON centros.nombre = adultos.centro 
WHERE centros.nombre = 'colina' ORDER BY adultos.Apellido;


SELECT categorias.nombre, actividades.nombre, actividades.fecha, actividades.Descripcion, centros.Direccion
FROM (categorias INNER JOIN actividades ON categorias.idCategoria = actividades.iDCategoria)
INNER JOIN centros ON centros.nombre = actividades.Centro
WHERE actividades.fecha >= CURDATE()
ORDER BY actividades.fecha;


SELECT actividades.nombre, adultos.nombre, inscripcion.Calificacion 
FROM (adultos INNER JOIN inscripcion ON adultos.idAdulto = inscripcion.idAdulto) 
INNER JOIN actividades ON actividades.idActividad = inscripcion.idActividad 
WHERE actividades.idActividad = '2' ORDER BY inscripcion.Calificacion DESC;

SELECT adultos.Nombre, adultos.Apellido 
FROM adultos INNER JOIN inscripcion ON adultos.idAdulto = inscripcion.idAdulto INNER JOIN actividades 
ON actividades.idActividad = inscripcion.idActividad 
WHERE actividades.idActividad = '2';


SELECT actividades.Fecha, actividades.Nombre AS Actividad, inscripcion.Calificacion 
FROM actividades INNER JOIN inscripcion ON actividades.idActividad = inscripcion.IdActividad 
WHERE inscripcion.IdAdulto = '4444';
