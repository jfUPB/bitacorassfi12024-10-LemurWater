# Bitácora de aprendizaje

> [!IMPORTANT]  
> RETO PERSONALIZADO
> 
> Personaliza el reto cambiando los signos ¿? por tu personalización. ¿Qué interés vas a explorar? ¿En qué consiste la aplicación
> ¿Qué sensores y actuadores usarás
> 
> Diseñaré e implementaré una aplicación interactiva para explorar ¿? mediante la integración de los siguientes sensores: ¿? y estos actuadores ¿?. La integración se realizará mediante protocolos ASCII utilizando una
> arquitectura cliente-servidor.

DURACION: Semana 6-9

REFERENCIAS:

[WEB del curso](https://sistemasfisicosinteractivos1.readthedocs.io/)

[p5.js](https://p5js.org/)

[Web Serial](https://capuf.in/web-serial-terminal/)

----

## SEMANA 6


### Sesión 1: (lunes febrero 26)

#### Micro-sesión 1: apertura

Cierre Unidad 1, comienzo de unidad 2


Explicacion introductoria 
- GAME LOOPS function
- Maquina de estados y eventos

#### Micro-sesión 2:

Continuacion explicacion introductoria de la unidad, presentacion de algunos ejemplos y que sigue de ahora en adeltante en el curso


#### Micro-sesion 3:

Voy a consultar informacion sobre cliente-servidor, aplicacion distribuida y recursos compartidos

- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)

- [Distributed computing](https://en.wikipedia.org/wiki/Distributed_computing)

- [Shared resource](https://en.wikipedia.org/wiki/Shared_resource)

- [Protocolos de comunicacion](https://en.wikipedia.org/wiki/Communication_protocol)

- Se le pregunto al profesosr sobre serializacion


#### Micro-sesion 4: Cierre

A simple vista el proyecto no me parece dificil, pero, a simple vista, veo que se se deben tener fuertemenete los preconcetos de server-client y serializacion para no tener inconvenientes en el futuro.

Me gustaria hacer una implementacion sensilla de un videojuego controlado por el micro:bit. Debe ser implementado en la pagina p5js

----

### Sesión 2: Febrero 28

#### Micro-sesion 1: Apertura

Me acuerdo muy poco de lo propuesto para esta unidad, voy a comenzar haciendo un repaso


#### Micro-sesion 2: Entender

Aprender p5.js atravez de [videos](https://www.youtube.com/watch?v=MXs1cOlidWs&list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA&index=4)

#### Micro-sesion 2: Entender

Continuacion, voy a saltar algunos videos del playlist que hablan sobre fundamentos de programacion.

Voy en la implementacion de numeros aleatorios (para repasar)

#### Micro-sesion 2: Cierre

El aparendizaje de la plataforma debe ser rapido. Voy a buscar un juego ya echo envez de hacerlo, para ahorrar tiempo y concentrarme en el tema del curso (Serializado)

----

### Sesión 3: Marzo 1

#### Micro-sesion 1: Apertura

En este espacio se va  finalizar la etapa de comprometimiento, produciendo una idea global de lo que se va a hacer, de como va a ser el proyecto.

**NOTA:** Se debe consultar informacion hacerca del serializado ASCII

#### Micro-sesion 2: Investigación y elección

En este espacio voy a buscar y *decidir* cual juego se va a implementar en el ejercicio. E descidido un juego por que estoy familiarizado con este tipo de software y se pueden adaptar muy facilemnte los controles

- El juego seleccionado es [SNAKE](https://p5js.org/examples/interaction-snake-game.html)

#### Micro-sesion 3: Pre-conceptos

En este espacio voy a estudiar preconceptos necesarios para la realizacion del proyecto, empezando por:
- *Serializado ASCII*
- controlar videojuego en *p5.js* con *micro:bit*

#### Micro-sesion 4: Cierre

Me parece que el videojuego de snake encaja perfectamente con los controladores del micro bit, izq y derecha. La culebra siempre tiene movimiento en 3 direcciones:

- Al frente, automaticamente
- Al lado izquiero y derecho (2)

----

## SEMANA 7


### Sesión 1: (lunes marzo 04)

#### Micro-sesión 1: apertura

Retoma del proyecto.

El profesor dio una breve explicacion del proyecto con unas recomendaciones que pueden servir:

- Seguir el paso a paso del desarrollo del proyecto. No saltarse ningun paso para reducir los probleams que se puedan presentar y facilitar el desarrollo del proyecto.


PLANEACION:

- Investigar mas a fondo como se puede desarrollar el serializado

#### Micro-sesión 2:

Se le pidio orientacion al profesor hacerca de la serializacion, mas especificamente del codigo.

**NOTA:** TODAS las indicaciones para el serializado estan en la seccion: [Flujo de trabajo del curso](https://sistemasfisicosinteractivos1.readthedocs.io/es/latest/_intro/courseFlow.html#).
Se debe repasar y aprender esta informacion.

#### Micro-sesión 3:

Continuacion repaso/estudio sobre serializacion.

#### Micro-sesión 4: Cierre

Solo me falta un breve repaso al proceso de serializacion explicado en la pagina del curso.

----

## SEMANA 8


### Sesión 1: (lunes marzo 13)

#### Micro-sesión 1: Apertura

Estube enfermo la semana pasada y voy a retomar el trabajo.
En esta sesion voy a crear un sistema simple de serializado con el ejemplo del principio del semestre, como fundaciones del proyecto y sobre esto se ira mejorando.


#### Micro-sesión 2: 

El buscador de linux no tiene **WebSerial** ni **WebUSB**, e presentado problemas para conectar el *micro:bit*, y creo que me puede ahorrar tiempo instalar los componentes para realizar este serializado desde mi maquina, ya que es muy trabajoso utilizar otro sistema operativo solo para la serializacion...
 - Tambien pienso que solucionar esta barrera puede acortarme tiempo no solo para futuros proyectos de esta materia, sino en otras y para      mis trabajos profesionales/personales.

 - Pero tampoco quiero dedicarle mucho tiempo a esto. Si no logro hacer funcionar el serializado desde linux, voy a continuar, utilizando      otro PC como soporte.
 
 - Conocer como funciona, de forma basica, la interface USB puede ser una herramienta util para entender y facilitar los ejercicios de serializacion de la materia.

[USB](https://www.beyondlogic.org/usbnutshell/usb1.shtml)


#### Micro-sesión 3:

No pude solucionar el problema de serializacion en linux, voy a preguntarle al profesor si conoce alguna forma de solucionar esto.

#### Micro-sesión 4: Cierre

No e podido avanzar mucho en el proyecto. Estoy estancado en la serializacion y por lo mucho que e buscado, no hay facil/directa solucion a este problema.

----
### REPOSICION SEMANA 7: Sesión 2

#### Micro-sesión 1: Apertura

E pensado en como solucionar el inconveniente que no permite hacer la coneccion de ***micro:bit*** en **Linux**.
La ultima idea que me queda es intentar por medio de una maquina virtual. Con mis conocimientos previos creo que sera posible realizar este intento con destreza.

**PS:** El fin de semana estube sin internet, lo que me dificulto avanzar en la materia 😔.

#### Micro-sesión 2: Experimentación

Logre con satisfaccion realizar la coneccion serial sin necesidad de cambiar de sistema operativo.

**NOTA:** 
- En cierta forma siento que el aprendizaje del tiempo invertido en esta solucion, hace parte del aprendizaje de la materia; de como conectar varios sistemas (en este caso un sistema dentro de otro sistema), y a su vez la coneccion con el ***micro:bit***.

- Tambien me puede servir mas adelante para otros trabajos de la misma materia y para un futuro, eliminando la limitacion de un sistema operativo u otro.

- Tambien siento que hace parte del camino de aprendizaje personal. Otros companeros que utilicen otros SO pueden no presentar este problema, pero si esta es la forma en la que yo (...), debo aprender a solucionar mis problemas especificos.

![313549732-6d41a726-2d20-4eab-9341-6ffabbf789b5](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/b8d7ed8d-ce74-42ec-b7c5-a2bdda521976)

![313549734-984acc16-9aa4-4049-94a9-9247b4bc7607](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/d2dd5ce7-9f61-46f8-880b-678e0e862328)



#### Micro-sesión 3: Test

Debido a que los desarrolladores de ***Firefox*** no quieren implementar **WebSerial**, no me habia sido posible practicar este componente critico del curso; pero ya que solucioné este problema voy continuar con repasar el ejercicio de comienzo de semestre sobre serializacione (**Web Serial Terminal**).

#### Micro-sesión 4: Cierre

----

## SEMANA 9


### Sesión 1: (lunes marzo 18)

#### Micro-sesión 1: Apertura

El profesor me va a ayudar a solucionar el problema de serializado (**webUSB**).

![webSERIAL](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/ea2afb2e-60d8-4db1-a9e3-238c393a699b)

#### Micro-sesión 2:

Voy a realizar los ejercicios del curso relacionados con serializacion para entender como funciona.

#### Micro-sesión 3:

Debo repasar los conceptos de p5.js y como hacer para mostrar el juego; creo qua la coneccion serial sera mas facil ya que el tema en si lo entiendo muy bien.

#### Micro-sesión 4: Cierre

Siento que ya estoy mas centrado y puedo ver con claridad lo que debo hacer, ademas de poderlo practicar.

----

### Sesión 2: (miercoles marzo 20)

#### Micro-sesión 1: Apertura

Le consulte al profesor como realizar la coneccion serial hacia p5.js (no sabia donde poner la informacion de ***index.html***)

NOTA: Ya tengo todas las herramientas necesarias para realizar el proyecto.

#### Micro-sesión 2: Comprometerse

Pienso que la informacion que va a pasar sobre la serializacion puede ser los movimientos de la culebra y el puntaje, cada vez que uno de estos eventos se activa, mostrar la informacion en el **micro:bit**

#### Micro-sesión 3:

Se modificaron los controles del ***Player*** para facilitar la navegabilidad:

```
function keyPressed() {
  switch (keyCode) {
    case 65:
      if (direction !== 'right') {
        direction = 'left';
      }
      break;
    case 68:
      if (direction !== 'left') {
        direction = 'right'; 
      }
      break;
    case 87:
      if (direction !== 'down') {
        direction = 'up';
      }
      break;
    case 83:
      if (direction !== 'up') {
        direction = 'down';
      }
      break;
  }
}
```

#### Micro-sesión 4: Cierre

Siento que el proyecto va avanzando por buen camino, solo me faltan solucionar algunos incovenientes que impiden la serializacion.

----

### REPOSICION SEMANA 7: Sesión 3 (Martes 19)

### Sesión 1: (lunes marzo 18)

#### Micro-sesión 1: Apertura

Continuacion test serializacion, probar juego en ***p5.js**

#### Micro-sesión 1: Apertura

----
### REPOSICION SEMANA 8: Sesión 2


----
### REPOSICION SEMANA 8: Sesion 3

----
