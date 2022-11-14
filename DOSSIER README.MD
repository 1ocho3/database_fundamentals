# Andrés de la Hoz Camiroaga
### Dossier: Fundamentos de Bases de Datos
###### Ana Lazcano de Rojas
##### Universidad Francisco de Vitoria
---  
&nbsp;

1   Crear la tabla TDEPTO

2	Crear la tabla TCENTR

3	Crear la tabla TEMPLE

4	Hallar la comisión, nombre y salario de los empleados con más de 3 hijos ordenados por comisión y dentro de la comisión por orden alfabético.

```sql
SELECT COMIS, NOMEM, SALAR
FROM TEMPLE
WHERE NUMHI > 3 
ORDER BY COMIS, NOMEM
```

5	Obtener una relación por orden alfabético de los departamentos cuyo presupuesto es inferior a 5000. El nombre de los departamentos debe aparecer ordenado a su vez por el presupuesto.



6	Obtener salario y nombre de los empleados sin hijos, por orden decreciente de salario y a la vez por orden alfabético de nombre.


7	Hallar por orden alfabético los nombres de los departamentos cuyo director lo es en funciones y no en propiedad.


8	Realizar la join entre las tablas temple y Tdepto.


9	Obtener nombre, número de empleado y extensión telefónica de los empleados del departamento 112.

```sql
SELECT NOMEM, NUMEM, EXTEL
FROM TEMPLE
WHERE NUMDE = 112
```

10	Llamaremos presupuesto medio mensual al resultado de dividir el presupuesto anual por 12, supongamos que se decide aumentar los presupuestos medios mensuales de todos los departamentos en un 10%. Para los departamentos cuyo presupuesto mensual es más de 500 €, hallar por orden alfabético el nombre de departamento y su presupuesto anual total después del incremento. Los cambios realizados son a partir del mes de octubre.

```sql
SELECT NOMDE, (PRESU/12)*9 + (PRESU/12)*3.3 PRESUPUESTO 
FROM TDEPTO
WHERE (PRESU)/12 > 500 
ORDER BY NOMDE
```


11	Obtener en orden creciente una selección de todas las extensiones telefónicas de los empleados.



12	Suponiendo que los próximos 3 años el coste de la vida va a aumentar un 6% anual y que se suben los salarios en la misma proporción. Hallar para los empleados con más de 4 hijos su nombre y sueldo anual actual y sueldo para cada uno de los próximos 3 años, todo ello ordenado alfabéticamente.


13	Halla el nombre de los empleados que trabajan en la calle Goya.


14	Calcular el nombre de los empleados, extensión telefónica y nombre de departamento para todos aquellos empleados que tengan más de 3 hijos.

```sql
SELECT NOMEM, EXTEL, NOMDE
FROM TEMPLE, TDEPTO
WHERE NUMHI > 3 AND TEMPLE.NUMDE = TDEPTO.NUMDE
```

15  Obtener la media de los salarios para todos aquellos empleados que trabajen en el departamento de finanzas.

16  Calcular el nombre de empleado/s que trabajen en el departamento de organización cuya comisión sea nula.

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE COMIS IS NULL AND NOMDE = 'ORGANIZACION'
```

17  Hallar los empleados que trabajan en el departamento “proceso de datos” con comisión no nula o más de dos hijos.


18	Calcular el nombre de los empleados cuyo salario supera el 90% de la comisión de Horacio Torres.

```sql
SELECT NOMEM
FROM TEMPLE 
WHERE SALAR > (SELECT COMIS FROM TEMPLE WHERE NOMEM = '"TORRES,HORACIO"')*0.9
```

19	Hallar por orden alfabético los nombres de los empleados tales que si se les da una gratificación de 100€ por hijos el total de esa gratificación no supere su mitad del salario.


20	Para los empleados del departamento 112 hallar, el nombre y el salario total de cada empleado, por orden de salario total decreciente y dentro del mismo por orden alfabético.


21	Hallar por orden de número de empleado el nombre, y el salario total de los empleados cuyo salario supere los 300€ mensuales.


22	Obtener los números de departamento en los que se halle algún empleado cuya comisión supere el 20% de su salario.


23	Hallar por orden alfabético los nombres de los departamentos que, o bien tienen director en funciones, o bien tienen director en propiedad y su presupuesto anual excede los 9000€ o bien no depende de ningún otro.


24	Hallar si hay algún departamento de reciente creación que aún no tenga empleados asignados, ni director en propiedad.



25	Hallar el número de empleado, el nombre y el salario total, de los empleados cuyo salario supera  al salario mínimo en 111€.


26	Calcular cuantos departamentos hay y el presupuesto anual medio de ellos.


27	Hallar cuantos departamentos hay y el presupuesto anual medio de ellos para los departamentos que no tienen director en propiedad.


28	Hallar la masa salarial anual, salario + comisión suponiendo que ofrecemos 14 pagas anuales.


29	Hallar la diferencia entre el salario más alto y el salario más bajo.


30	Para los empleados que no tienen comisión, obtener por orden alfabético el nombre y el cociente entre su salario y el número de hijos, siempre y cuando supere al salario mínimo en 100€.


31	Hallar el número medio de hijos por empleado, para todos los empleados que no tienen más de dos hijos.


32	Obtener por orden alfabético los nombres de los empleados cuyo salario este comprendido entre 250 y 300.


33	Obtener  por orden alfabético los nombres de los empleados que trabajan en el mismo departamento que Gálvez, Pilar o Flor, Dorotea.


34	Hallar el salario medio de los empleados cuyo salario no supera en más de un 20% al salario mínimo de los empleados que tienen algún hijo siendo el salario por hijo mayor que 100€.


35	Para los departamentos cuyo director lo sea en funciones hallar el número de empleados y la suma de sus salarios, comisiones y número de hijos.


36	Hallar por orden alfabéticos los nombres de los empleados que son directores en funciones.


37	Obtener por orden alfabético los nombres de los empleados cuyo primer apellido es mora o comienza por Mora.


38	Obtener por orden alfabético los nombres de los empleados que tengan un apellido de 7 letras


39	Obtener por orden alfabético los nombres de los empleados cuyo apellido sea de 6 o más letras.


40	Obtener por orden alfabético los nombres de los empleados cuyo apellido termina en “ez” su nombre termina en o y este último tiene al menos 3 letras.


41	Obtener por orden alfabético los nombres de los empleados que comenzaron a trabajar en el año 66.


42	Se desea hacer un regalo de un 1% del salario a los empleados en el día de su onomástica. Hallar por ordena alfabético los nombres de los empleados y la cuantía de los regalos en € para los que celebren su santo en el día de San Honorio.


43	Calcular el número de empleados que hay por cada departamento.


44	Calcular los departamentos que tengan 3 o más empleados trabajando.




## Consultas improvisadas en clase:  

1   Nombre de los empleados que trabajan en el centro 10

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TDEPTO.NUMCE = 10 AND TEMPLE.NUMDE=TDEPTO.NUMDE
```

2   Obtener el salario y la comisión anual de los empleados que comparten departamento con Flor Dorotea.

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

3   NOMBRE DEL DIRECTOR QUE TRABAJA EN EL DEPARTAMENTO 100
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

4   DIRECTOR DEL DEPARTAMENTO DE FLOR DOROTEA

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMEM = TDEPTO.DIREC AND TEMPLE.NUMDE = (SELECT NUMDE FROM TEMPLE WHERE NOMEM LIKE '"FLOR,DOROTEA"')
```

5   NOMBRE DE LA PERSONA QUE MAS COBRA DE TODOS

```sql
SELECT NOMEM
FROM TEMPLE
WHERE SALAR >= ALL(SELECT SALAR FROM TEMPLE)
```

6   OBTENER LOS EMPLEADOS QUE COMPARTEN DEPARTAMENTO CON FLOR DOROTEA Y CLAUDIA FIERRO
```sql
SELECT NOMEM
FROM TEMPLE
WHERE NUMDE = SOME(SELECT NUMDE FROM TEMPLE WHERE NOMEM ='"FLOR,DOROTEA"' OR NOMEM ='"FIERRO,CLAUDIA"')

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE
WHERE NUMDE = ALL(SELECT NUMDE FROM TEMPLE WHERE NOMEM ='"FLOR,DOROTEA"' OR NOMEM ='"FIERRO,CLAUDIA"')
```

-Calcular el nombre del departamento cuyo presupuesto sea superior a la media de presupuestos de la empresa

SELECT NOMDE
FROM TDEPTO
WHERE (SELECT AVG(PRESU) FROM TDEPTO) < PRESU


-Calcular el nombre del departamento cuyo presupuesto sea superior a todos los presupuestos de la empresa

SELECT NOMDE
FROM TDEPTO
WHERE (SELECT MAX(PRESU) FROM TDEPTO) <= PRESU





-HALLAR EL NOMBRE DE LOS EMPLEADOS QUE COMPARTEN EXTENSION TELEFONICA (APODO A UNA COLUMNA )

SELECT NOMEM, EXTEL
FROM TEMPLE A
WHERE EXTEL IN (SELECT EXTEL FROM TEMPLE WHERE A.NOMEM <> TEMPLE.NOMEM)

-SALARIO MEDIO POR DEPARTAMENTO

SELECT AVG(SALAR), NUMDE
FROM TEMPLE
GROUP BY NUMDE

-PERSONAS EN CADA DEPARTAMENTO

SELECT COUNT(NOMEM), NUMDE
FROM TEMPLE
GROUP BY NUMDE

-EMPLEADOS POR DEPARTAMENTO QUE NO SON EL DIRECTOR Y QUE SEA MAYOR QUE 1 Y SALARIO MAYOR QUE 2000

SELECT COUNT(NOMEM), NUMDE, AVG(SALAR)
FROM TEMPLE
WHERE COMIS IS NULL AND NUMEM NOT IN (SELECT DIREC FROM TDEPTO) AND NUMHI > 0
GROUP BY NUMDE
HAVING COUNT(NUMEM) > 1 AND AVG(SALAR) > 2000
