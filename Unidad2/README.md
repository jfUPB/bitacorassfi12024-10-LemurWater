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
