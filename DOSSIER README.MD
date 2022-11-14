# Andrés de la Hoz Camiroaga
### Dossier: Fundamentos de Bases de Datos
###### Ana Lazcano de Rojas
##### Universidad Francisco de Vitoria
---  
&nbsp;

1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crear la tabla TDEPTO  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/1ocho3/database_fundamentals/blob/main/files/dossier_required/DONE.png?raw=true" alt="drawing" width="23"/>  

2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crear la tabla TCENTR  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/1ocho3/database_fundamentals/blob/main/files/dossier_required/DONE.png?raw=true" alt="drawing" width="23"/>  

3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crear la tabla TEMPLE  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/1ocho3/database_fundamentals/blob/main/files/dossier_required/DONE.png?raw=true" alt="drawing" width="23"/> 

&nbsp; 

4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar la comisión, nombre y salario de los empleados con más de 3 hijos ordenados por comisión y dentro de la comisión por orden alfabético.  

```sql
SELECT COMIS, NOMEM, SALAR
FROM TEMPLE
WHERE NUMHI > 3 
ORDER BY COMIS, NOMEM
```
&nbsp;

5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener una relación por orden alfabético de los departamentos cuyo presupuesto es inferior a 5000. El nombre de los departamentos debe aparecer ordenado a su vez por el presupuesto.
```sql
SELECT NOMDE
FROM TDEPTO
WHERE PRESU>5000
ORDER BY NOMDE, PRESU
```  
&nbsp;

6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener salario y nombre de los empleados sin hijos, por orden decreciente de salario y a la vez por orden alfabético de nombre.
```sql
SELECT SALAR , NOMEM
FROM TEMPLE
WHERE NUMHI = 0
ORDER BY SALAR DESC, NOMEM
```  
&nbsp;

7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabético los nombres de los departamentos cuyo director lo es en funciones y no en propiedad.
```sql
SELECT NOMDE
FROM TDEPTO
WHERE TIDIR='F'
ORDER BY NOMDE
```  
&nbsp;

8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Realizar la join entre las tablas temple y Tdepto.
```sql
SELECT *
FROM TEMPLE
JOIN TDEPTO ON TEMPLE.NUMDE=TDEPTO.NUMD
```  
&nbsp;

9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener nombre, número de empleado y extensión telefónica de los empleados del departamento 112.

```sql
SELECT NOMEM, NUMEM, EXTEL
FROM TEMPLE
WHERE NUMDE = 112
```  
&nbsp;

10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Llamaremos presupuesto medio mensual al resultado de dividir el presupuesto anual por 12, supongamos que se decide aumentar los presupuestos medios mensuales de todos los departamentos en un 10%. Para los departamentos cuyo presupuesto mensual es más de 500 €, hallar por orden alfabético el nombre de departamento y su presupuesto anual total después del incremento. Los cambios realizados son a partir del mes de octubre.

```sql
SELECT NOMDE, (PRESU/12)*9 + (PRESU/12)*3.3 PRESUPUESTO 
FROM TDEPTO
WHERE (PRESU)/12 > 500 
ORDER BY NOMDE
```  
&nbsp;

11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener en orden creciente una selección de todas las extensiones telefónicas de los empleados.  

```sql
SELECT EXTEL
FROM TEMPLE
ORDER BY EXTEL
```
  
&nbsp;

12.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suponiendo que los próximos 3 años el coste de la vida va a aumentar un 6% anual y que se suben los salarios en la misma proporción. Hallar para los empleados con más de 4 hijos su nombre y sueldo anual actual y sueldo para cada uno de los próximos 3 años, todo ello ordenado alfabéticamente.
```sql
SELECT NOMEM, (SALAR*12) SALARIO, (SALAR*12)*1.06 AÑO1, ((SALAR*12)*1.06)*1.06 AÑO2, (((SALAR*12)*1.06)*1.06)*1.06 AÑO3
FROM TEMPLE
WHERE NUMHI>4
ORDER BY 1
```
  
&nbsp;

13.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Halla el nombre de los empleados que trabajan en la calle Goya.

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO, TCENTR
WHERE SEÑAS LIKE '%C_%GOYA%%' AND TEMPLE.NUMDE=TDEPTO.NUMDE AND TDEPTO.NUMCE=TCENTR.NUMCE

--Devuelve "no data found" ya que no hay centros en la calle Goya.
--Se puede comprobar que la consulta es correcta, si se cambia la consulta de la calle Goya, por Atocha, de la siguiente forma:

SELECT NOMEM
FROM TEMPLE, TDEPTO, TCENTR
WHERE SEÑAS LIKE '%C_%ATOCHA%%' AND TEMPLE.NUMDE=TDEPTO.NUMDE AND TDEPTO.NUMCE=TCENTR.NUMCE
```
  
&nbsp;

14.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre de los empleados, extensión telefónica y nombre de departamento para todos aquellos empleados que tengan más de 3 hijos.

```sql
SELECT NOMEM NOMBRE, EXTEL EXTENSIÓN_TELEFÓNICA, NOMDE DEPARTAMENTO
FROM TEMPLE, TDEPTO
WHERE NUMHI>3 AND TEMPLE.NUMDE=TDEPTO.NUMDE
```

  
&nbsp;

15.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener la media de los salarios para todos aquellos empleados que trabajen en el departamento de finanzas.
```sql
SELECT AVG(SALAR)
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND NOMDE LIKE '%FINANZAS%'
```

  
&nbsp;

16.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre de empleado/s que trabajen en el departamento de organización cuya comisión sea nula.

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE COMIS IS NULL AND NOMDE = 'ORGANIZACION'
```

17.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar los empleados que trabajan en el departamento “proceso de datos” con comisión no nula o más de dos hijos.


18.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre de los empleados cuyo salario supera el 90% de la comisión de Horacio Torres.

```sql
SELECT NOMEM
FROM TEMPLE 
WHERE SALAR > (SELECT COMIS FROM TEMPLE WHERE NOMEM = '"TORRES,HORACIO"')*0.9
```

19.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabético los nombres de los empleados tales que si se les da una gratificación de 100€ por hijos el total de esa gratificación no supere su mitad del salario.


20.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para los empleados del departamento 112 hallar, el nombre y el salario total de cada empleado, por orden de salario total decreciente y dentro del mismo por orden alfabético.


21.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden de número de empleado el nombre, y el salario total de los empleados cuyo salario supere los 300€ mensuales.


22.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener los números de departamento en los que se halle algún empleado cuya comisión supere el 20% de su salario.


23.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabético los nombres de los departamentos que, o bien tienen director en funciones, o bien tienen director en propiedad y su presupuesto anual excede los 9000€ o bien no depende de ningún otro.

```sql
SELECT NOMDE
FROM TDEPTO
WHERE TIDIR='F' OR (TIDIR='P' AND PRESU>9000) OR DEPDE=0
ORDER BY 1
```


24.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar si hay algún departamento de reciente creación que aún no tenga empleados asignados, ni director en propiedad.



25.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar el número de empleado, el nombre y el salario total, de los empleados cuyo salario supera  al salario mínimo en 111€.


26.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular cuantos departamentos hay y el presupuesto anual medio de ellos.


27.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar cuantos departamentos hay y el presupuesto anual medio de ellos para los departamentos que no tienen director en propiedad.


28.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar la masa salarial anual, salario + comisión suponiendo que ofrecemos 14 pagas anuales.


29.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar la diferencia entre el salario más alto y el salario más bajo.


30.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para los empleados que no tienen comisión, obtener por orden alfabético el nombre y el cociente entre su salario y el número de hijos, siempre y cuando supere al salario mínimo en 100€.


31.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar el número medio de hijos por empleado, para todos los empleados que no tienen más de dos hijos.


32.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo salario este comprendido entre 250 y 300.


33.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener  por orden alfabético los nombres de los empleados que trabajan en el mismo departamento que Gálvez, Pilar o Flor, Dorotea.


34.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar el salario medio de los empleados cuyo salario no supera en más de un 20% al salario mínimo de los empleados que tienen algún hijo siendo el salario por hijo mayor que 100€.


35.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para los departamentos cuyo director lo sea en funciones hallar el número de empleados y la suma de sus salarios, comisiones y número de hijos.


36.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabéticos los nombres de los empleados que son directores en funciones.


37.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo primer apellido es mora o comienza por Mora.


38.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados que tengan un apellido de 7 letras


39.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo apellido sea de 6 o más letras.


40.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo apellido termina en “ez” su nombre termina en o y este último tiene al menos 3 letras.


41.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados que comenzaron a trabajar en el año 66.


42.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Se desea hacer un regalo de un 1% del salario a los empleados en el día de su onomástica. Hallar por ordena alfabético los nombres de los empleados y la cuantía de los regalos en € para los que celebren su santo en el día de San Honorio.


43.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el número de empleados que hay por cada departamento.


44.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular los departamentos que tengan 3 o más empleados trabajando.




## Consultas improvisadas en clase:  

1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nombre de los empleados que trabajan en el centro 10

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TDEPTO.NUMCE = 10 AND TEMPLE.NUMDE=TDEPTO.NUMDE
```

2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener el salario y la comisión anual de los empleados que comparten departamento con Flor Dorotea.

```sql
SELECT (SALAR + COMIS)*12 
FROM TEMPLE
WHERE NUMDE = (SELECT NUMDE FROM TEMPLE WHERE NOMEM = '"FLOR,DOROTEA"') AND COMIS IS NOT NULL
UNION 
SELECT (SALAR)*12 
FROM TEMPLE
WHERE NUMDE = (SELECT NUMDE FROM TEMPLE WHERE NOMEM = '"FLOR,DOROTEA"') AND COMIS IS NULL

--Otra forma de hacerlo:

SELECT (SALAR + NVL(COMIS,0))*12 
FROM TEMPLE
WHERE NUMDE = (SELECT NUMDE FROM TEMPLE WHERE NOMEM = '"FLOR,DOROTEA"')
```

3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NOMBRE DEL DIRECTOR QUE TRABAJA EN EL DEPARTAMENTO 100
```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMEM = TDEPTO.DIREC AND TEMPLE.NUMDE = 100

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE NUMEM = DIREC AND TEMPLE.NUMDE =100 AND TDEPTO.NUMDE = 100

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE
WHERE NUMEM = (SELECT DIREC FROM TDEPTO WHERE NUMDE =100)
```

4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DIRECTOR DEL DEPARTAMENTO DE FLOR DOROTEA

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMEM = TDEPTO.DIREC AND TEMPLE.NUMDE = (SELECT NUMDE FROM TEMPLE WHERE NOMEM LIKE '"FLOR,DOROTEA"')
```

5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NOMBRE DE LA PERSONA QUE MAS COBRA DE TODOS

```sql
SELECT NOMEM
FROM TEMPLE
WHERE SALAR >= ALL(SELECT SALAR FROM TEMPLE)
```

6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OBTENER LOS EMPLEADOS QUE COMPARTEN DEPARTAMENTO CON FLOR DOROTEA Y CLAUDIA FIERRO
```sql
SELECT NOMEM
FROM TEMPLE
WHERE NUMDE = SOME(SELECT NUMDE FROM TEMPLE WHERE NOMEM ='"FLOR,DOROTEA"' OR NOMEM ='"FIERRO,CLAUDIA"')

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE
WHERE NUMDE = ALL(SELECT NUMDE FROM TEMPLE WHERE NOMEM ='"FLOR,DOROTEA"' OR NOMEM ='"FIERRO,CLAUDIA"')
```

7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre del departamento cuyo presupuesto sea superior a la media de presupuestos de la empresa

```sql
SELECT NOMDE
FROM TDEPTO
WHERE (SELECT AVG(PRESU) FROM TDEPTO) < PRESU
```

8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre del departamento cuyo presupuesto sea superior a todos los presupuestos de la empresa
```sql
SELECT NOMDE
FROM TDEPTO
WHERE PRESU>=(SELECT MAX(PRESU) FROM TDEPTO) 
```

9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR EL NOMBRE DE LOS EMPLEADOS QUE COMPARTEN EXTENSION TELEFONICA (APODO A UNA COLUMNA )

```sql
SELECT NOMEM, EXTEL
FROM TEMPLE A
WHERE EXTEL IN (SELECT EXTEL FROM TEMPLE WHERE A.NOMEM <> TEMPLE.NOMEM)
```

13.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SALARIO MEDIO POR DEPARTAMENTO

```sql
SELECT AVG(SALAR) SALARIO_MEDIO, NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
```
11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NÚMERO DE PERSONAS EN CADA DEPARTAMENTO

```sql
SELECT COUNT(NOMEM) Nº_PERSONAS, NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
```

12.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMPLEADOS POR DEPARTAMENTO QUE NO SON EL DIRECTOR Y QUE SEA MAYOR QUE 1 Y SALARIO MAYOR QUE 2000
```sql
---Este ejercicio fue ampliado más allá del enunciado, durante su resolución.
SELECT COUNT(NOMEM), NUMDE, AVG(SALAR)
FROM TEMPLE
WHERE COMIS IS NULL AND NUMEM NOT IN (SELECT DIREC FROM TDEPTO) AND NUMHI > 0
GROUP BY NUMDE
HAVING COUNT(NUMEM) > 1 AND AVG(SALAR) > 2000
```

13.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR EL NOMBRE DEL DIRECTOR CUYO DEPARTAMENTO SEA EL QUE TIENE LA MEDIA DE SALARIOS MÁS ALTA QUE LA MEDIA DE TODOS LOS DEPARTAMENTOS MENOS EL SUYO, SI SOLO SE TIENE EN CUENTA A LOS EMPLEADOS QUE TIENEN HIJOS.
```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMEM=TDEPTO.DIREC AND TEMPLE.NUMDE IN (SELECT NUMDE
                                                FROM TEMPLE A
                                                WHERE NUMHI>0
                                                GROUP BY NUMDE
                                                HAVING AVG(SALAR)>=ALL( SELECT AVG(SALAR)
                                                FROM TEMPLE
                                                WHERE A.NUMDE<>TEMPLE.NUMDE AND NUMHI>0
                                                GROUP BY NUMDE))

```

14.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CALCULAR EL SALARIO MEDIO POR DEPARTAMENTO PARA AQUELLOS DEPARTAMENTOS QUE TENGAN MÁS DE 3 EMPLEADOS Y CUYA SUMA DE LAS COMISIONES SEA MAYOR A LA MEDIA DE LAS COMISIONES DE SU DEPARTAMENTO

```sql
SELECT AVG(SALAR) SALARIOMEDIO, NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
HAVING COUNT(*)>3 AND SUM(COMIS)>AVG(COMIS)
```
