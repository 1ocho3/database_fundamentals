# Andrés de la Hoz Camiroaga
### Dossier: Fundamentos de Bases de Datos
###### Ana Lazcano de Rojas
##### Universidad Francisco de Vitoria  
###### Las consultas están integradas en el documento como cuadros de código. Al pasar el ratón por encima de cada uno, se puede copiar el código que encuadra haciendo click sobre el icono que aparecerá en la esquina superior izquierda. El output de las consultas aparece en formato de tabla debajo de cada cuadro de código.
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
|COMIS|NOMEM|SALAR|
|---|---|---|
|0|"LOPEZ,ANTONIO"|5000|
|1000|"VAZQUEZ,HONORIA"|2000|
|- |"FLOR,DOROTEA"|2900|
|- |"VEIGA,JULIANA"|3000|

&nbsp;

5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener una relación por orden alfabético de los departamentos cuyo presupuesto es inferior a 5000. El nombre de los departamentos debe aparecer ordenado a su vez por el presupuesto.
```sql
SELECT NOMDE
FROM TDEPTO
WHERE PRESU>5000
ORDER BY NOMDE, PRESU
```  
|NOMDE|
|---|
|DIRECCION COMERCIAL|
|DIRECCION GENERAL|
|PROCESO DE DATOS|
|SECTOR SERVICIOS|  

&nbsp;

6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener salario y nombre de los empleados sin hijos, por orden decreciente de salario y a la vez por orden alfabético de nombre.
```sql
SELECT SALAR , NOMEM
FROM TEMPLE
WHERE NUMHI = 0
ORDER BY SALAR DESC, NOMEM
```  
|SALAR|NOMEM|
|---|---|
|9909|"FIERRO,CLAUDIA"|
|4500|"ALBA,ADRIANA"|
|4020|"GARCIA,AUGUSTO"|
|3080|"POLO,OTILIA"|
|2080|"DIEZ,AMELIA"|
|2010|"DURAN,LIVIA"|
|2010|"PEREZ,SABINA"|
|1805|"LARA,LUCRECIA"|
|1705|"MU�Z,AZUCENA"|
|1080|"MARTIN,MICAELA"|
|1080|"TORRES,HORACIO"|
|1000|"SANTOS,SANCHO"|
|440|"PEREZ,JULIO"|


&nbsp;

7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabético los nombres de los departamentos cuyo director lo es en funciones y no en propiedad.
```sql
SELECT NOMDE
FROM TDEPTO
WHERE TIDIR='F'
ORDER BY NOMDE
```  
|NOMDE|
|---|
|ORGANIZACION|
|SECTOR INDUSTRIAL|  

&nbsp;

8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Realizar la join entre las tablas temple y Tdepto.
```sql
SELECT NUMEM, TEMPLE.NUMDE, EXTEL, FECNA, FECIN, SALAR, COMIS, NUMHI, NOMEM, NUMCE, DIREC, TIDIR, PRESU, DEPDE, NOMDE
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE
```  
|NUMEM|NUMDE|EXTEL|FECNA|FECIN|SALAR|COMIS|NUMHI|NOMEM|NUMCE|DIREC|TIDIR|PRESU|DEPDE|NOMDE|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|210|100|200|09/28/1940|01/22/1989|3800|- |2|"GALVEZ,PILAR"|10|260|P|12000|0|DIRECCION GENERAL|
|260|100|555|01/01/1943|01/01/1965|5000|0|7|"LOPEZ,ANTONIO"|10|260|P|12000|0|DIRECCION GENERAL|
|250|100|250|10/27/1966|03/01/2000|4500|- |0|"ALBA,ADRIANA"|10|260|P|12000|0|DIRECCION GENERAL|
|510|110|550|05/04/1966|11/01/1986|2000|- |1|"CAMPOS,ROMULO"|20|180|P|15000|100|DIRECCION COMERCIAL|
|180|110|508|10/18/1984|03/18/2005|480|50|2|"PEREZ,MARCOS"|20|180|P|15000|100|DIRECCION COMERCIAL|
|390|110|500|02/19/1966|10/08/1999|2015|- |1|"MORAN,CARMEN"|20|180|P|15000|100|DIRECCION COMERCIAL|
|440|111|760|09/26/1966|02/28/1986|2010|1000|0|"DURAN,LIVIA"|20|180|F|11|110|SECTOR INDUSTRIAL|
|160|111|740|07/09/1979|11/11/1999|310|110|2|"AGUIRRE,AUREO"|20|180|F|11|110|SECTOR INDUSTRIAL|
|500|111|750|10/08/1965|01/01/1987|2000|1000|4|"VAZQUEZ,HONORIA"|20|180|F|11|110|SECTOR INDUSTRIAL|
|240|111|760|02/26/1972|02/24/2001|2800|1000|3|"SANZ,LAVINIA"|20|180|F|11|110|SECTOR INDUSTRIAL|
|550|111|780|01/10/1970|01/21/1988|1000|1200|0|"SANTOS,SANCHO"|20|180|F|11|110|SECTOR INDUSTRIAL|
|480|111|760|04/04/1965|02/28/1986|2100|1000|1|"PINO,DIANA"|20|180|F|11|110|SECTOR INDUSTRIAL|
|400|111|780|08/18/1969|11/01/1987|1805|- |0|"LARA,LUCRECIA"|20|180|F|11|110|SECTOR INDUSTRIAL|
|360|111|750|10/29/1958|10/10/1977|2050|1000|2|"LARA,DORINDA"|20|180|F|11|110|SECTOR INDUSTRIAL|
|120|112|840|06/09/1977|10/01/2004|350|110|1|"LASA,MARIO"|20|270|P|9000|110|SECTOR SERVICIOS|
|270|112|800|05/21/1955|09/10/2000|3080|800|3|"GARCIA,OCTAVIO"|20|270|P|9000|110|SECTOR SERVICIOS|
|130|112|810|09/09/1955|02/01/1987|290|110|2|"TORRES,LUCIANO"|20|270|P|9000|110|SECTOR SERVICIOS|
|490|112|880|06/06/1964|01/01/1988|1080|1000|0|"TORRES,HORACIO"|20|270|P|9000|110|SECTOR SERVICIOS|
|450|112|880|10/21/1966|02/28/1986|2010|1000|0|"PEREZ,SABINA"|20|270|P|9000|110|SECTOR SERVICIOS|
|330|112|850|08/19/1968|03/01/2003|2080|900|0|"DIEZ,AMELIA"|20|270|P|9000|110|SECTOR SERVICIOS|
|380|112|880|03/30/1968|01/01/1981|1080|- |0|"MARTIN,MICAELA"|20|270|P|9000|110|SECTOR SERVICIOS|
|290|120|910|11/30/1947|02/14/1999|2070|- |3|"GIL,GLORIA"|10|150|F|3000|100|ORGANIZACION|
|150|121|340|08/10/1990|01/15/1993|440|- |0|"PEREZ,JULIO"|10|150|P|2000|120|PERSONAL|
|110|121|350|11/10/1947|02/15/1990|310|- |3|"PONS,CESAR"|10|150|P|2000|120|PERSONAL|
|370|121|360|06/22/1967|01/20/1985|1090|- |1|"RUIZ,FABIOLA"|10|150|P|2000|120|PERSONAL|
|190|121|350|05/12/1982|02/11/2010|3000|- |4|"VEIGA,JULIANA"|10|150|P|2000|120|PERSONAL|
|410|122|660|07/14/1968|10/13/1988|1705|- |0|"MU�Z,AZUCENA"|10|350|P|6000|120|PROCESO DE DATOS|
|350|122|610|04/13/1959|09/10/2004|4050|- |1|"CAMPS,AURELIO"|10|350|P|6000|120|PROCESO DE DATOS|
|285|122|620|10/25/1949|02/15/1999|3080|- |0|"POLO,OTILIA"|10|350|P|6000|120|PROCESO DE DATOS|
|430|122|650|02/26/1967|11/19/1988|2100|- |1|"MORA,VALERIANA"|10|350|P|6000|120|PROCESO DE DATOS|
|320|122|620|12/25/1957|02/05/1987|4005|- |2|"SANZ,CORNELIO"|10|350|P|6000|120|PROCESO DE DATOS|
|310|130|480|11/21/1946|01/15/1988|4020|- |0|"GARCIA,AUGUSTO"|10|310|P|2000|100|FINANZAS|
|280|130|410|01/11/1978|10/08/2008|2900|- |5|"FLOR,DOROTEA"|10|310|P|2000|100|FINANZAS|
|420|130|450|10/22/1966|11/19/1988|9909|- |0|"FIERRO,CLAUDIA"|10|310|P|2000|100|FINANZAS|




&nbsp;

9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener nombre, número de empleado y extensión telefónica de los empleados del departamento 112.

```sql
SELECT NOMEM, NUMEM, EXTEL
FROM TEMPLE
WHERE NUMDE = 112
```  
|NOMEM|NUMEM|EXTEL|
|---|---|---|
|"DIEZ,AMELIA"|330|850|
|"GARCIA,OCTAVIO"|270|800|
|"LASA,MARIO"|120|840|
|"MARTIN,MICAELA"|380|880|
|"PEREZ,SABINA"|450|880|
|"TORRES,HORACIO"|490|880|
|"TORRES,LUCIANO"|130|810|


&nbsp;

10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Llamaremos presupuesto medio mensual al resultado de dividir el presupuesto anual por 12, supongamos que se decide aumentar los presupuestos medios mensuales de todos los departamentos en un 10%. Para los departamentos cuyo presupuesto mensual es más de 500 €, hallar por orden alfabético el nombre de departamento y su presupuesto anual total después del incremento. Los cambios realizados son a partir del mes de octubre.

```sql
SELECT NOMDE, (PRESU/12)*9 + (PRESU/12)*3.3 PRESUPUESTO 
FROM TDEPTO
WHERE (PRESU)/12 > 500 
ORDER BY NOMDE
```  
|NOMDE|PRESUPUESTO|
|---|---|
|DIRECCION COMERCIAL|15375|
|DIRECCION GENERAL|12300|
|SECTOR SERVICIOS|9225|

&nbsp;

11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener en orden creciente una selección de todas las extensiones telefónicas de los empleados.  

```sql
SELECT EXTEL
FROM TEMPLE
ORDER BY EXTEL
-- La consulta superior busca la extensión de cada empleado.
-- Si quisiéramos sacar las extensiones que existen, sin repetición, solo falta añadir DISTINCT.
```  
|EXTEL|
|---|
|200|
|250|
|340|
|350|
|350|
|360|
|410|
|450|
|480|
|500|
|508|
|550|
|555|
|610|
|620|
|620|
|650|
|660|
|740|
|750|
|750|
|760|
|760|
|760|
|780|
|780|
|800|
|810|
|840|
|850|
|880|
|880|
|880|
|910|
  
&nbsp;

12.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suponiendo que los próximos 3 años el coste de la vida va a aumentar un 6% anual y que se suben los salarios en la misma proporción. Hallar para los empleados con más de 4 hijos su nombre y sueldo anual actual y sueldo para cada uno de los próximos 3 años, todo ello ordenado alfabéticamente.
```sql
SELECT NOMEM, (SALAR*12) SALARIO, (SALAR*12)*1.06 AÑO1, ((SALAR*12)*1.06)*1.06 AÑO2, (((SALAR*12)*1.06)*1.06)*1.06 AÑO3
FROM TEMPLE
WHERE NUMHI>4
ORDER BY 1
```  
|NOMEM|SALARIO|AÑO1|AÑO2|AÑO3|
|---|---|---|---|---|
|"FLOR,DOROTEA"|34800|36888|39101.28|41447.3568|
|"LOPEZ,ANTONIO"|60000|63600|67416|71460.96|

  
&nbsp;

13.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Halla el nombre de los empleados que trabajan en la calle Goya.

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO, TCENTR
WHERE SEÑAS LIKE '%C_%GOYA%' AND TEMPLE.NUMDE=TDEPTO.NUMDE AND TDEPTO.NUMCE=TCENTR.NUMCE

--Devuelve "no data found" ya que no hay centros en la calle Goya.
--Se puede comprobar que la consulta es correcta, si se cambia la consulta de la calle Goya, por Atocha, de la siguiente forma:

SELECT NOMEM
FROM TEMPLE, TDEPTO, TCENTR
WHERE SEÑAS LIKE '%C_%ATOCHA%' AND TEMPLE.NUMDE=TDEPTO.NUMDE AND TDEPTO.NUMCE=TCENTR.NUMCE
```  
###### *Tabla de la segunda consulta (comprobación)  
|NOMEM|
|---|
|"AGUIRRE,AUREO"|
|"CAMPOS,ROMULO"|
|"DIEZ,AMELIA"|
|"DURAN,LIVIA"|
|"GARCIA,OCTAVIO"|
|"LARA,DORINDA"|
|"LARA,LUCRECIA"|
|"LASA,MARIO"|
|"MARTIN,MICAELA"|
|"MORAN,CARMEN"|
|"PEREZ,MARCOS"|
|"PEREZ,SABINA"|
|"PINO,DIANA"|
|"SANTOS,SANCHO"|
|"SANZ,LAVINIA"|
|"TORRES,HORACIO"|
|"TORRES,LUCIANO"|
|"VAZQUEZ,HONORIA"|
  
&nbsp;

14.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre de los empleados, extensión telefónica y nombre de departamento para todos aquellos empleados que tengan más de 3 hijos.

```sql
SELECT NOMEM NOMBRE, EXTEL EXTENSIÓN_TELEFÓNICA, NOMDE DEPARTAMENTO
FROM TEMPLE, TDEPTO
WHERE NUMHI>3 AND TEMPLE.NUMDE=TDEPTO.NUMDE
```  
|NOMBRE|EXTENSIÓN_TELEFÓNICA|DEPARTAMENTO|
|---|---|---|
|"LOPEZ,ANTONIO"|555|DIRECCION GENERAL|
|"VAZQUEZ,HONORIA"|750|SECTOR INDUSTRIAL|
|"VEIGA,JULIANA"|350|PERSONAL|
|"FLOR,DOROTEA"|410|FINANZAS|

  
&nbsp;

15.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener la media de los salarios para todos aquellos empleados que trabajen en el departamento de finanzas.
```sql
SELECT AVG(SALAR)  SALARIO_MEDIO
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND NOMDE LIKE '%FINANZAS%'
```  
|SALARIO_MEDIO|
|:---:|
|5609.66666666666666666666666666666666667|
  
&nbsp;

16.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre de empleado/s que trabajen en el departamento de organización cuya comisión sea nula.

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE COMIS IS NULL AND NOMDE = 'ORGANIZACION'
```  
|NOMEM|
|---|
|"ALBA,ADRIANA"|
|"CAMPOS,ROMULO"|
|"CAMPS,AURELIO"|
|"FIERRO,CLAUDIA"|
|"FLOR,DOROTEA"|
|"GALVEZ,PILAR"|
|"GARCIA,AUGUSTO"|
|"GIL,GLORIA"|
|"LARA,LUCRECIA"|
|"MARTIN,MICAELA"|
|"MORA,VALERIANA"|
|"MORAN,CARMEN"|
|"MU�Z,AZUCENA"|
|"PEREZ,JULIO"|
|"POLO,OTILIA"|
|"PONS,CESAR"|
|"RUIZ,FABIOLA"|
|"SANZ,CORNELIO"|
|"VEIGA,JULIANA"|
  
&nbsp;


17.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar los empleados que trabajan en el departamento “proceso de datos” con comisión no nula o más de dos hijos.
``` sql
SELECT NOMEM 
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND ((NOMDE LIKE 'PROCESO DE DATOS' AND COMIS IS NOT NULL) OR NUMHI>2)
```  
|NOMEM|
|---|
|"LOPEZ,ANTONIO"|
|"VAZQUEZ,HONORIA"|
|"SANZ,LAVINIA"|
|"GARCIA,OCTAVIO"|
|"GIL,GLORIA"|
|"PONS,CESAR"|
|"VEIGA,JULIANA"|
|"FLOR,DOROTEA"|
  
&nbsp;


18.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre de los empleados cuyo salario supera el 90% de la comisión de Horacio Torres.

```sql
SELECT NOMEM
FROM TEMPLE 
WHERE SALAR > (SELECT COMIS FROM TEMPLE WHERE NOMEM = '"TORRES,HORACIO"')*0.9
```  
|NOMEM|
|---|
|"ALBA,ADRIANA"|
|"CAMPOS,ROMULO"|
|"CAMPS,AURELIO"|
|"DIEZ,AMELIA"|
|"DURAN,LIVIA"|
|"FIERRO,CLAUDIA"|
|"FLOR,DOROTEA"|
|"GALVEZ,PILAR"|
|"GARCIA,AUGUSTO"|
|"GARCIA,OCTAVIO"|
|"GIL,GLORIA"|
|"LARA,DORINDA"|
|"LARA,LUCRECIA"|
|"LOPEZ,ANTONIO"|
|"MARTIN,MICAELA"|
|"MORA,VALERIANA"|
|"MORAN,CARMEN"|
|"MU�Z,AZUCENA"|
|"PEREZ,SABINA"|
|"PINO,DIANA"|
|"POLO,OTILIA"|
|"RUIZ,FABIOLA"|
|"SANTOS,SANCHO"|
|"SANZ,CORNELIO"|
|"SANZ,LAVINIA"|
|"TORRES,HORACIO"|
|"VAZQUEZ,HONORIA"|
|"VEIGA,JULIANA"|
  
&nbsp;


19.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabético los nombres de los empleados tales que si se les da una gratificación de 100€ por hijos el total de esa gratificación no supere su mitad del salario.
```sql
SELECT NOMEM
FROM TEMPLE
WHERE NUMHI>0 AND NUMHI*100<SALAR/2
ORDER BY NOMEM 
```
|NOMEM|
|---|
|"CAMPOS,ROMULO"|
|"CAMPS,AURELIO"|
|"FLOR,DOROTEA"|
|"GALVEZ,PILAR"|
|"GARCIA,OCTAVIO"|
|"GIL,GLORIA"|
|"LARA,DORINDA"|
|"LASA,MARIO"|
|"LOPEZ,ANTONIO"|
|"MORA,VALERIANA"|
|"MORAN,CARMEN"|
|"PEREZ,MARCOS"|
|"PINO,DIANA"|
|"RUIZ,FABIOLA"|
|"SANZ,CORNELIO"|
|"SANZ,LAVINIA"|
|"VAZQUEZ,HONORIA"|
|"VEIGA,JULIANA"|

  
&nbsp;


20.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para los empleados del departamento 112 hallar, el nombre y el salario total de cada empleado, por orden de salario total decreciente y dentro del mismo por orden alfabético.
```sql
SELECT NOMEM, SALAR+NVL(COMIS,0) SALARIO_TOTAL
FROM TEMPLE
WHERE NUMDE=112
ORDER BY 2 DESC, NOMEM
```
|NOMEM|SALARIO_TOTAL|
|---|---|
|"GARCIA,OCTAVIO"|3880|
|"PEREZ,SABINA"|3010|
|"DIEZ,AMELIA"|2980|
|"TORRES,HORACIO"|2080|
|"MARTIN,MICAELA"|1080|
|"LASA,MARIO"|460|
|"TORRES,LUCIANO"|400|


  
&nbsp;


21.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden de número de empleado el nombre, y el salario total de los empleados cuyo salario supere los 300€ mensuales.
```SQL
SELECT NOMEM, SALAR+NVL(COMIS,0) SALARIO_TOTAL
FROM TEMPLE
WHERE SALAR>300
ORDER BY NUMEM
```
|NOMEM|SALARIO_TOTAL|
|---|---|
|"PONS,CESAR"|310|
|"LASA,MARIO"|460|
|"PEREZ,JULIO"|440|
|"AGUIRRE,AUREO"|420|
|"PEREZ,MARCOS"|530|
|"VEIGA,JULIANA"|3000|
|"GALVEZ,PILAR"|3800|
|"SANZ,LAVINIA"|3800|
|"ALBA,ADRIANA"|4500|
|"LOPEZ,ANTONIO"|5000|
|"GARCIA,OCTAVIO"|3880|
|"FLOR,DOROTEA"|2900|
|"POLO,OTILIA"|3080|
|"GIL,GLORIA"|2070|
|"GARCIA,AUGUSTO"|4020|
|"SANZ,CORNELIO"|4005|
|"DIEZ,AMELIA"|2980|
|"CAMPS,AURELIO"|4050|
|"LARA,DORINDA"|3050|
|"RUIZ,FABIOLA"|1090|
|"MARTIN,MICAELA"|1080|
|"MORAN,CARMEN"|2015|
|"LARA,LUCRECIA"|1805|
|"MU�Z,AZUCENA"|1705|
|"FIERRO,CLAUDIA"|9909|
|"MORA,VALERIANA"|2100|
|"DURAN,LIVIA"|3010|
|"PEREZ,SABINA"|3010|
|"PINO,DIANA"|3100|
|"TORRES,HORACIO"|2080|
|"VAZQUEZ,HONORIA"|3000|
|"CAMPOS,ROMULO"|2000|
|"SANTOS,SANCHO"|2200|

  
&nbsp;


22.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener los números de departamento en los que se halle algún empleado cuya comisión supere el 20% de su salario.
```sql
SELECT DISTINCT NUMDE
FROM TEMPLE
WHERE COMIS>=SALAR*0.2
```
|NUMDE|
|---|
|112|
|111|

  
&nbsp;


23.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabético los nombres de los departamentos que, o bien tienen director en funciones, o bien tienen director en propiedad y su presupuesto anual excede los 9000€ o bien no depende de ningún otro.

```sql
SELECT NOMDE
FROM TDEPTO
WHERE TIDIR='F' OR (TIDIR='P' AND PRESU>9000) OR DEPDE=0
ORDER BY 1
```  
|NOMDE|
|---|
|DIRECCION COMERCIAL|
|DIRECCION GENERAL|
|ORGANIZACION|
|SECTOR INDUSTRIAL|
  
&nbsp;


24.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar si hay algún departamento de reciente creación que aún no tenga empleados asignados, ni director en propiedad.
```sql
SELECT NOMDE
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND TIDIR<>'P'
GROUP BY TEMPLE.NUMDE,NOMDE
HAVING COUNT(NUMEM)=0

--Otra forma de hacerlo:

SELECT * 
FROM TDEPTO
WHERE NUMDE NOT IN (SELECT NUMDE FROM TEMPLE) AND TIDIR<>'P'

--no data found 
```

  
&nbsp;


25.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar el número de empleado, el nombre y el salario total, de los empleados cuyo salario supera  al salario mínimo en 111€.
```sql
SELECT NUMEM, NOMEM NOMBRE, (SALAR+NVL(COMIS,0))*12 SALARIO_TOTAL
FROM TEMPLE
WHERE SALAR-111>=(SELECT MIN(SALAR) FROM TEMPLE)
```  
|NUMEM|NOMBRE|SALARIO_TOTAL|
|---|---|---|
|250|"ALBA,ADRIANA"|54000|
|510|"CAMPOS,ROMULO"|24000|
|350|"CAMPS,AURELIO"|48600|
|330|"DIEZ,AMELIA"|35760|
|440|"DURAN,LIVIA"|36120|
|420|"FIERRO,CLAUDIA"|118908|
|280|"FLOR,DOROTEA"|34800|
|210|"GALVEZ,PILAR"|45600|
|310|"GARCIA,AUGUSTO"|48240|
|270|"GARCIA,OCTAVIO"|46560|
|290|"GIL,GLORIA"|24840|
|360|"LARA,DORINDA"|36600|
|400|"LARA,LUCRECIA"|21660|
|260|"LOPEZ,ANTONIO"|60000|
|380|"MARTIN,MICAELA"|12960|
|430|"MORA,VALERIANA"|25200|
|390|"MORAN,CARMEN"|24180|
|410|"MU�Z,AZUCENA"|20460|
|150|"PEREZ,JULIO"|5280|
|180|"PEREZ,MARCOS"|6360|
|450|"PEREZ,SABINA"|36120|
|480|"PINO,DIANA"|37200|
|285|"POLO,OTILIA"|36960|
|370|"RUIZ,FABIOLA"|13080|
|550|"SANTOS,SANCHO"|26400|
|320|"SANZ,CORNELIO"|48060|
|240|"SANZ,LAVINIA"|45600|
|490|"TORRES,HORACIO"|24960|
|500|"VAZQUEZ,HONORIA"|36000|
|190|"VEIGA,JULIANA"|36000|

  
&nbsp;


26.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular cuantos departamentos hay y el presupuesto anual medio de ellos.
```sql
SELECT COUNT(NOMDE) n_DEPARTAMENTOS, AVG(PRESU*12) Ppto_Medio_Anual
FROM TDEPTO
```  
|N_DEPARTAMENTOS|PPTO_MEDIO_ANUAL|
|---|---|
|8|73516.5|

  
&nbsp;


27.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar cuantos departamentos hay y el presupuesto anual medio de ellos para los departamentos que no tienen director en propiedad.
```SQL
SELECT COUNT(NUMDE), AVG(PRESU)
FROM TDEPTO
WHERE TIDIR='F'
```
|COUNT(NUMDE)|AVG(PRESU)|
|---|---|
|2|1505.5|

  
&nbsp;


28.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar la masa salarial anual, salario + comisión suponiendo que ofrecemos 14 pagas anuales.
```SQL
SELECT SUM((SALAR+NVL(COMIS,0))*14) MASA_SALARIAL_ANUAL
FROM TEMPLE
```
|MASA_SALARIAL_ANUAL|
|---|
|1271186|
  
&nbsp;


29.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar la diferencia entre el salario más alto y el salario más bajo.
```SQL
SELECT MAX(SALAR)-MIN(SALAR) DIFERENCIA
FROM TEMPLE
```
|DIFERENCIA|
|---|
|9619|
  
&nbsp;


30.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para los empleados que no tienen comisión, obtener por orden alfabético el nombre y el cociente entre su salario y el número de hijos, siempre y cuando supere al salario mínimo en 100€.
```SQL
SELECT NOMEM, SALAR/NUMHI COCIENTE
FROM TEMPLE
WHERE COMIS IS NULL AND NUMHI>0 AND SALAR/NUMHI>(SELECT MIN(SALAR) FROM TEMPLE)+100
```
|NOMEM|COCIENTE|
|---|---|
|"CAMPOS,ROMULO"|2000|
|"CAMPS,AURELIO"|4050|
|"FLOR,DOROTEA"|580|
|"GALVEZ,PILAR"|1900|
|"GIL,GLORIA"|690|
|"MORA,VALERIANA"|2100|
|"MORAN,CARMEN"|2015|
|"RUIZ,FABIOLA"|1090|
|"SANZ,CORNELIO"|2002.5|
|"VEIGA,JULIANA"|750|


  
&nbsp;


31.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar el número medio de hijos por empleado, para todos los empleados que no tienen más de dos hijos.
```SQL
SELECT AVG(NUMHI) MEDIA_HIJOS
FROM TEMPLE
WHERE NUMHI<=2
```
|MEDIA_HIJOS|
|---|
|.730769230769230769230769230769230769231|
  
&nbsp;


32.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo salario esté comprendido entre 250 y 300.
```sql
SELECT NOMEM
FROM TEMPLE
WHERE SALAR BETWEEN 250 AND 300
ORDER BY NOMEM
```
|NOMEM|
|---|
|"TORRES,LUCIANO"|
  
&nbsp;


33.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener  por orden alfabético los nombres de los empleados que trabajan en el mismo departamento que Gálvez, Pilar o Flor, Dorotea.
```SQL
SELECT NOMEM, NUMDE
FROM TEMPLE
WHERE NUMDE IN (SELECT NUMDE FROM TEMPLE WHERE NOMEM LIKE '%G_LVEZ,PILAR%' OR NOMEM LIKE '%FLOR,DOROTEA%')
ORDER BY 1
```
|NOMEM|NUMDE|
|---|---|
|"ALBA,ADRIANA"|100|
|"FIERRO,CLAUDIA"|130|
|"FLOR,DOROTEA"|130|
|"GALVEZ,PILAR"|100|
|"GARCIA,AUGUSTO"|130|
|"LOPEZ,ANTONIO"|100|


  
&nbsp;


34.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar el salario medio de los empleados cuyo salario no supera en más de un 20% al salario mínimo de los empleados que tienen algún hijo siendo el salario por hijo mayor que 100€.
```SQL
SELECT AVG(SALAR)
FROM TEMPLE
WHERE SALAR<=(SELECT MIN(SALAR) FROM TEMPLE WHERE NUMHI>0 AND SALAR/NUMHI>100)*1.2
```
|AVG(SALAR)|
|---|
|303.333333333333333333333333333333333333|
  
&nbsp;


35.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para los departamentos cuyo director lo sea en funciones hallar el número de empleados y la suma de sus salarios, comisiones y número de hijos.
```SQL
SELECT COUNT(NUMEM), SUM(SALAR) SUMA_SALARIOS, SUM(COMIS) SUMA_COMISIONES, SUM(NUMHI) SUMA_HIJOS
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND TIDIR='F'
```
|COUNT(NUMEM)|SUMA_SALARIOS|SUMA_COMISIONES|SUMA_HIJOS|
|---|---|---|---|
|9|16145|6310|15|

  
&nbsp;


36.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hallar por orden alfabéticos los nombres de los empleados que son directores en funciones.
```SQL
SELECT NOMEM
FROM TEMPLE
WHERE NUMEM IN (SELECT DIREC FROM TDEPTO WHERE TIDIR='F')
ORDER BY 1
```
|NOMEM|
|---|
|"PEREZ,JULIO"|
|"PEREZ,MARCOS"|
  
&nbsp;


37.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo primer apellido es mora o comienza por Mora.
```SQL
SELECT NOMEM
FROM TEMPLE
WHERE NOMEM LIKE '%MORA%%'
ORDER BY 1
```
|NOMEM|
|---|
|"MORA,VALERIANA"|
|"MORAN,CARMEN"|
  
&nbsp;


38.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados que tengan un apellido de 7 letras
```SQL
SELECT NOMEM
FROM TEMPLE
WHERE NOMEM LIKE'________,%'
ORDER BY 1
```
|NOMEM|
|---|
|"AGUIRRE,AUREO"|
|"VAZQUEZ,HONORIA"|  

&nbsp;


39.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo apellido sea de 6 o más letras.
```SQL
SELECT NOMEM
FROM TEMPLE
WHERE NOMEM LIKE'_______%,%'
ORDER BY 1
```
|NOMEM|
|---|
|"AGUIRRE,AUREO"|
|"CAMPOS,ROMULO"|
|"FIERRO,CLAUDIA"|
|"GALVEZ,PILAR"|
|"GARCIA,AUGUSTO"|
|"GARCIA,OCTAVIO"|
|"MARTIN,MICAELA"|
|"SANTOS,SANCHO"|
|"TORRES,HORACIO"|
|"TORRES,LUCIANO"|
|"VAZQUEZ,HONORIA"|

  
&nbsp;


40.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados cuyo apellido termina en “ez” su nombre termina en o y este último tiene al menos 3 letras.

```sql
SELECT NOMEM
FROM TEMPLE
WHERE NOMEM LIKE '%EZ,%___%O_'
ORDER BY 1
``` 
|NOMEM|
|---|
|"LOPEZ,ANTONIO"|
|"PEREZ,JULIO"|  

  
&nbsp;


41.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obtener por orden alfabético los nombres de los empleados que comenzaron a trabajar en el año 66.
```SQL
SELECT NOMEM 
FROM TEMPLE
WHERE FECIN LIKE '%66'
ORDER BY 1
--no data found
--Para comprobar que funciona cambio la fecha al 86
SELECT NOMEM 
FROM TEMPLE
WHERE FECIN LIKE '%86'
ORDER BY 1
```
Resultado comprobación:
|NOMEM|
|---|
|"CAMPOS,ROMULO"|
|"DURAN,LIVIA"|
|"PEREZ,SABINA"|
|"PINO,DIANA"|


  
&nbsp;


42.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Se desea hacer un regalo de un 1% del salario a los empleados en el día de su onomástica. Hallar por ordena alfabético los nombres de los empleados y la cuantía de los regalos en € para los que celebren su santo en el día de San Honorio.
```sql
SELECT NOMEM, SALAR*0.1
FROM TEMPLE
WHERE NOMEM LIKE '%,HONOR%'
ORDER BY NOMEM
```
|NOMEM|SALAR*0.1|
|---|---|
|"VAZQUEZ,HONORIA"|200|

  
&nbsp;


43.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el número de empleados que hay por cada departamento.
```sql
SELECT COUNT(*) NÚMERO_EMPLEADOS, NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
```
|NÚMERO_EMPLEADOS|DEPARTAMENTO|
|---|---|
|3|100|
|1|120|
|4|121|
|7|112|
|3|110|
|3|130|
|8|111|
|5|122|


  
&nbsp;


44.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular los departamentos que tengan 3 o más empleados trabajando.
```SQL
SELECT NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
HAVING COUNT(*)>=3
```
|DEPARTAMENTO|
|---|
|100|
|121|
|112|
|110|
|130|
|111|
|122|



  
&nbsp;


## Consultas improvisadas en clase:  

1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nombre de los empleados que trabajan en el centro 10

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TDEPTO.NUMCE = 10 AND TEMPLE.NUMDE=TDEPTO.NUMDE
```  
|NOMEM|
|---|
|"GALVEZ,PILAR"|
|"LOPEZ,ANTONIO"|
|"ALBA,ADRIANA"|
|"GIL,GLORIA"|
|"PEREZ,JULIO"|
|"PONS,CESAR"|
|"RUIZ,FABIOLA"|
|"VEIGA,JULIANA"|
|"MU�Z,AZUCENA"|
|"CAMPS,AURELIO"|
|"POLO,OTILIA"|
|"MORA,VALERIANA"|
|"SANZ,CORNELIO"|
|"GARCIA,AUGUSTO"|
|"FLOR,DOROTEA"|
|"FIERRO,CLAUDIA"|
  
&nbsp;



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
##### **OUTPUT 1**
|(SALAR+COMIS)*12|
|---|
|34800|
|48240|
|118908| 
 
---  

##### **OUTPUT 2**
|(SALAR+NVL(COMIS,0))*12|
|---|
|118908|
|34800|
|48240|  

  
&nbsp;


3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NOMBRE DEL DIRECTOR QUE TRABAJA EN EL DEPARTAMENTO 100
```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMEM = TDEPTO.DIREC AND TEMPLE.NUMDE = 100

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE NUMEM = DIREC AND TEMPLE.NUMDE=100 AND TDEPTO.NUMDE = 100

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE
WHERE NUMEM = (SELECT DIREC FROM TDEPTO WHERE NUMDE =100)
```
|NOMEM|
|---|
|"LOPEZ,ANTONIO"|
  
&nbsp;


4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DIRECTOR DEL DEPARTAMENTO DE FLOR DOROTEA

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMEM = TDEPTO.DIREC AND TEMPLE.NUMDE = (SELECT NUMDE FROM TEMPLE WHERE NOMEM LIKE '_FLOR,DOROTEA_')
```
|NOMEM|
|---|
|"GARCIA,AUGUSTO"|

  
&nbsp;


5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NOMBRE DE LA PERSONA QUE MAS COBRA DE TODOS

```sql
SELECT NOMEM
FROM TEMPLE
WHERE SALAR >= ALL(SELECT SALAR FROM TEMPLE)

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE
WHERE SALAR=(SELECT MAX(SALAR) FROM TEMPLE)
```
|NOMEM|
|---|
|"FIERRO,CLAUDIA"|
  
&nbsp;


6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OBTENER LOS EMPLEADOS QUE COMPARTEN DEPARTAMENTO CON FLOR DOROTEA Y CLAUDIA FIERRO
```sql
SELECT NOMEM
FROM TEMPLE
WHERE NUMDE = SOME(SELECT NUMDE FROM TEMPLE WHERE NOMEM ='"FLOR,DOROTEA"' OR NOMEM ='"FIERRO,CLAUDIA"')

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE
WHERE NUMDE = ALL(SELECT NUMDE FROM TEMPLE WHERE NOMEM ='"FLOR,DOROTEA"' OR NOMEM ='"FIERRO,CLAUDIA"')

--Otra forma de hacerlo:

SELECT NOMEM
FROM TEMPLE
WHERE NUMDE IN (SELECT NUMDE FROM TEMPLE WHERE NOMEM ='"FLOR,DOROTEA"' OR NOMEM ='"FIERRO,CLAUDIA"')
```
|NOMEM|
|---|
|"GARCIA,AUGUSTO"|
|"FLOR,DOROTEA"|
|"FIERRO,CLAUDIA"|

  
&nbsp;


7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre del departamento cuyo presupuesto sea superior a la media de presupuestos de la empresa

```sql
SELECT NOMDE
FROM TDEPTO
WHERE (SELECT AVG(PRESU) FROM TDEPTO) < PRESU
```
|NOMDE|
|---|
|DIRECCION GENERAL|
|DIRECCION COMERCIAL|
|SECTOR SERVICIOS|

  
&nbsp;


8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcular el nombre del departamento cuyo presupuesto sea superior a todos los presupuestos de la empresa
```sql
SELECT NOMDE
FROM TDEPTO
WHERE PRESU IN (SELECT MAX(PRESU) FROM TDEPTO) 
```
|NOMDE|
|---|
|DIRECCION COMERCIAL|
  
&nbsp;


9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR EL NOMBRE DE LOS EMPLEADOS QUE COMPARTEN EXTENSION TELEFONICA (APODO A UNA COLUMNA )

```sql
SELECT NOMEM, EXTEL
FROM TEMPLE A
WHERE EXTEL IN (SELECT EXTEL FROM TEMPLE WHERE A.NOMEM <> TEMPLE.NOMEM)
```
|NOMEM|EXTEL|
|---|---|
|"SANZ,LAVINIA"|760|
|"PINO,DIANA"|760|
|"VAZQUEZ,HONORIA"|750|
|"SANTOS,SANCHO"|780|
|"TORRES,HORACIO"|880|
|"PEREZ,SABINA"|880|
|"MARTIN,MICAELA"|880|
|"DURAN,LIVIA"|760|
|"SANZ,CORNELIO"|620|
|"VEIGA,JULIANA"|350|
|"LARA,LUCRECIA"|780|
|"POLO,OTILIA"|620|
|"LARA,DORINDA"|750|
|"PONS,CESAR"|350|

  
&nbsp;


10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SALARIO MEDIO POR DEPARTAMENTO

```sql
SELECT AVG(SALAR) SALARIO_MEDIO, NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
```
|SALARIO_MEDIO|DEPARTAMENTO|
|---|---|
|4433.33333333333333333333333333333333333|100|
|2070|120|
|1210|121|
|1424.28571428571428571428571428571428571|112|
|1498.33333333333333333333333333333333333|110|
|5609.66666666666666666666666666666666667|130|
|1759.375|111|
|2988|122|

  
&nbsp;


11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NÚMERO DE PERSONAS EN CADA DEPARTAMENTO

```sql
SELECT COUNT(*) Nº_PERSONAS, NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
```
|Nº_PERSONAS|DEPARTAMENTO|
|---|---|
|3|100|
|1|120|
|4|121|
|7|112|
|3|110|
|3|130|
|8|111|
|5|122|


  
&nbsp;


12.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMPLEADOS POR DEPARTAMENTO QUE NO SON EL DIRECTOR Y QUE SEA MAYOR QUE 1 Y SALARIO MAYOR QUE 2000
```sql
---Este ejercicio, durante su resolución, fue ampliado más allá del enunciado. 
SELECT COUNT(NOMEM), NUMDE, AVG(SALAR)
FROM TEMPLE
WHERE COMIS IS NULL AND NUMEM NOT IN (SELECT DIREC FROM TDEPTO) AND NUMHI > 0
GROUP BY NUMDE
HAVING COUNT(NUMEM) > 1 AND AVG(SALAR) > 2000
```
|COUNT(NOMEM)|NUMDE|AVG(SALAR)|
|---|---|---|
|2|110|2007.5|
|2|122|3052.5|

  
&nbsp;


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
|NOMEM|
|---|
|"LOPEZ,ANTONIO"|
  
&nbsp;


14.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CALCULAR EL SALARIO MEDIO POR DEPARTAMENTO PARA AQUELLOS DEPARTAMENTOS QUE TENGAN MÁS DE 3 EMPLEADOS Y CUYA SUMA DE LAS COMISIONES SEA MAYOR A LA MEDIA DE LAS COMISIONES DE SU DEPARTAMENTO

```sql
SELECT AVG(SALAR) SALARIOMEDIO, NUMDE DEPARTAMENTO
FROM TEMPLE
GROUP BY NUMDE
HAVING COUNT(*)>3 AND SUM(COMIS)>AVG(COMIS)
```
|SALARIOMEDIO|DEPARTAMENTO|
|---|---|
|1424.28571428571428571428571428571428571|112|
|1759.375|111|

  
&nbsp;

15.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR EL NOMBRE Y NÚMERO DE HIJOS DEL EMPLEAD MÁS JOVEN QUE NO SEA DIRECTOR Y CUYO DEPARTAMENTO TENGA LA MAYOR COMISIÓN MEDIA  

```sql
SELECT NOMEM NOMBRE, NUMHI HIJOS
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND TEMPLE.NUMEM<>TDEPTO.DIREC AND TEMPLE.NUMDE=(SELECT NUMDE FROM TEMPLE GROUP BY NUMDE HAVING AVG(COMIS)=(SELECT MAX(AVG(COMIS)) FROM TEMPLE GROUP BY NUMDE)) AND FECNA IN (SELECT MAX(FECNA) FROM TEMPLE GROUP BY NUMDE)
```
|NOMBRE|HIJOS|
|---|---|
|"AGUIRRE,AUREO"|2|

  
&nbsp;

16.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PARA CADA DEPARTAMENTO CON PRESUPUESTO INFERIOR A 60000 HALLAR EL NOMBRE DEL CENTRO DONDE ESTÁ UBICADO Y EL MÁXIMO SALARIO DE SUS EMPLEADOS, SI ESTE ES SUPERIOR A 2000 EUROS Y ORDENAR ALFABÉTICAMENTE POR ORDEN DE DEPARTAMENTO.

```sql
SELECT DISTINCT SEÑAS, NOMCE
FROM TCENTR, TDEPTO, TEMPLE
WHERE TCENTR.NUMCE=TDEPTO.NUMCE AND PRESU<60000 AND SALAR=(SELECT MAX(SALAR) FROM TEMPLE A WHERE A.NUMDE=TEMPLE.NUMDE) AND SALAR>2000
```
|SEÑAS|NOMCE|
|---|---|
|"C.ALCALA, 820 MADRID"|SEDE CENTRAL|
|"C.ATOCHA, 405, MADRID"|RELACION CON CLIENTES|

  
&nbsp;

17.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR EL NOMBRE Y FECHA DE NACIMIENTO DE TODOS LOS EMPLEADOS CUYO SALARIO SEA MENOR A LA MEDIA DE TODOS LOS SALARIOS Y PERTENEZCA AL DEPARTAMENTO CON MAYOR COMISIÓN O A UN DEPARTAMENTO QUE NO DEPENDA DE OTRO Y ORDENAR POR EDAD DESCENDENTE.
```sql
SELECT NOMEM NOMBRE, FECNA FECHA_NACIMIENTO
FROM TEMPLE, TDEPTO 
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND SALAR<(SELECT AVG(SALAR) FROM TEMPLE) AND (TEMPLE.NUMDE=(SELECT NUMDE FROM TEMPLE WHERE COMIS=(SELECT MAX(COMIS) FROM TEMPLE)) OR TDEPTO.DEPDE=0)
ORDER BY FECNA DESC

-- Otra forma de hacerlo:

SELECT NOMEM NOMBRE, FECNA FECHA_NACIMIENTO
FROM TEMPLE, TDEPTO 
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND SALAR<(SELECT AVG(SALAR) FROM TEMPLE) AND TEMPLE.NUMDE=(SELECT NUMDE FROM TEMPLE WHERE COMIS=(SELECT MAX(COMIS) FROM TEMPLE)) OR TDEPTO.DEPDE=0
ORDER BY FECNA DESC

-- Otra forma de hacerlo:

SELECT DISTINCT NOMEM, FECNA
FROM TEMPLE, TDEPTO
WHERE (SALAR < ALL(SELECT AVG(SALAR) FROM TEMPLE) AND TEMPLE.NUMDE = (SELECT NUMDE FROM TEMPLE GROUP BY NUMDE HAVING MAX(COMIS) = (SELECT MAX(COMIS) FROM TEMPLE))) OR DEPDE = 0 AND TEMPLE.NUMDE = TDEPTO.NUMDE
ORDER BY FECNA DESC
```
|NOMBRE|FECHA_NACIMIENTO|
|---|---|
|"LASA,MARIO"|06/09/1977|
|"DIEZ,AMELIA"|08/19/1968|
|"MARTIN,MICAELA"|03/30/1968|
|"PEREZ,SABINA"|10/21/1966|
|"TORRES,HORACIO"|06/06/1964|
|"TORRES,LUCIANO"|09/09/1955|


  
&nbsp;

18.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR EL NOMBRE Y EL NÚMERO DE HIJOS DEL EMPLEADO MÁS JOVEN QUE NO SEA DIRECTOR Y CUYO DEPARTAMENTO TENGA LA MAYOR COMISIÓN MEDIA.
```sql
SELECT NOMEM, NUMHI
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND DIREC<>NUMEM AND TEMPLE.NUMDE= (SELECT TEMPLE.NUMDE
                                                                    FROM TEMPLE, TDEPTO
                                                                    WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND DIREC<>NUMEM 
                                                                    GROUP BY TEMPLE.NUMDE
                                                                    HAVING AVG(NVL(COMIS,0)) >= ALL(SELECT MAX(AVG(NVL(COMIS,0))) 
                                                                                                    FROM TEMPLE 
                                                                                                    GROUP BY NUMDE)) AND FECNA=(SELECT MAX(FECNA)
                                                                                                                                FROM TEMPLE, TDEPTO
                                                                                                                                WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND DIREC<>NUMEM AND TEMPLE.NUMDE= (SELECT TEMPLE.NUMDE
                                                                                                                                                                                                    FROM TEMPLE, TDEPTO
                                                                                                                                                                                                    WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND DIREC<>NUMEM 
                                                                                                                                                                                                    GROUP BY TEMPLE.NUMDE
                                                                                                                                                                                                    HAVING AVG(NVL(COMIS,0))>= ALL(SELECT MAX(AVG(NVL(COMIS,0))) FROM TEMPLE GROUP BY NUMDE)))
```
|NOMEM|NUMHI|
|---|---|
|"AGUIRRE,AUREO"|2|

 
  
&nbsp;

# falta añadir el del asesinato


19.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR POR ORDEN ALFABÉTICO LOS NOMBRES DE LOS EMPLEADOS QUE SON DIRECTORES EN FUNCIONES.

```sql
SELECT NOMEM
FROM TEMPLE, TDEPTO
WHERE TDEPTO.DIREC=TEMPLE.NUMEM AND TIDIR='F'
ORDER BY NOMEM
```
|NOMEM|
|---|
|"PEREZ,JULIO"|
|"PEREZ,MARCOS"|

 
  
&nbsp;


20.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OBTENER POR ORDEN ALFABÉTICO LOS EMPLEADOS CON UNN APELLIDO DE 7 LETRAS
```sql
SELECT * FROM TEMPLE
WHERE NOMEM LIKE '"_______,%'
ORDER BY NOMEM
```
|NUMEM|NUMDE|EXTEL|FECNA|FECIN|SALAR|COMIS|NUMHI|NOMEM|
|---|---|---|---|---|---|---|---|---|
|160|111|740|07/09/1979|11/11/1999|310|110|2|"AGUIRRE,AUREO"|
|500|111|750|10/08/1965|01/01/1987|2000|1000|4|"VAZQUEZ,HONORIA"|


 
  
&nbsp;


21.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HALLAR EL DEPARTAMENTO EN EL QUE TRABAJA EL EMPLEADO CON MAYOR ANTIGUEDAD SIENDO SU SALARIO EL SALARIO MÁS BAJO
```sql
SELECT DISTINCT NUMDE
FROM TEMPLE
WHERE SALAR =(SELECT MIN(SALAR)
              FROM TEMPLE
              WHERE FECIN IN (SELECT MIN(FECIN)
                              FROM TEMPLE
                              GROUP BY NUMDE))
```
|NUMDE|
|---|
|112|
 
  
&nbsp;


22.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CALCULA EL SALARIO MÁXIMO DEL DEPARTAMENTO DEL DEPARTAMENTO EN EL QUE HAYA MÁS EMPLEADOS CON HIJOS DESCARTANDO A LOS DIRECTORES  
```SQL
SELECT TEMPLE.NUMDE, COUNT(*),(MAX(SALAR)) 
FROM TEMPLE, TDEPTO 
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND NUMHI>0 AND DIREC<>NUMEM GROUP BY TEMPLE.NUMDE HAVING COUNT(*)=(SELECT MAX(COUNT(*)) 
                                                                                                    FROM TEMPLE,TDEPTO 
                                                                                                    WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND NUMHI >0 AND DIREC<>NUMEM 
                                                                                                    GROUP BY TEMPLE.NUMDE)
```
|NUMDE|COUNT(*)|(MAX(SALAR))|
|---|---|---|
|111|5|2800|
  

&nbsp;  
  

23.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EL NOMBRE DEL DEPARTAMENTO CON EL MENOR SALARIO MÁXIMO  
```SQL
SELECT NOMDE
FROM TEMPLE, TDEPTO
WHERE TEMPLE.NUMDE=TDEPTO.NUMDE
GROUP BY NOMDE
HAVING MAX(SALAR)<=ALL(SELECT MAX(SALAR)
                        FROM TEMPLE
                        GROUP BY NUMDE)
```  
|NOMDE|
|---|
|DIRECCION COMERCIAL|

&nbsp;  


24.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EL NOMBRE DEL DEPARTAMENTO UBICADO EN EL CENTRO CON MÁS EMPLEADOS SIN COMISIÓN
```SQL
SELECT NOMDE
FROM TDEPTO
WHERE TDEPTO.NUMCE=(SELECT NUMCE
                    FROM TEMPLE, TDEPTO
                    WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND COMIS IS NULL
                    GROUP BY NUMCE
                    HAVING COUNT(*)=(SELECT MAX(COUNT(*)) 
                                     FROM TEMPLE, TDEPTO 
                                     WHERE TEMPLE.NUMDE=TDEPTO.NUMDE AND COMIS IS NULL 
                                     GROUP BY NUMCE))
```
|NOMDE|
|---|
|DIRECCION GENERAL|
|ORGANIZACION|
|PERSONAL|
|PROCESO DE DATOS|
|FINANZAS|

  

&nbsp;  
  


###### Andrés de la Hoz Camiroaga© - Gestión de la Ciberseguridad - UFV
