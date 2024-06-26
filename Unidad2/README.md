# Bitácora de aprendizaje

![Screenshot from 2024-05-15 11-58-08](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/d0882411-bb0e-4161-a088-62afd9c9076c)

![Screenshot from 2024-05-15 11-58-13](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/aa449187-83d6-44ec-a86b-6979109e35de)



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

[MD](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

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

```javascript
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

#### Micro-sesión 2:

**PROBLEMA:** 

![Screenshot from 2024-03-22 04-15-11](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/4daf2fde-6eb0-4f66-a834-cdfa2d107789)

![Screenshot from 2024-03-22 04-14-45](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/c3253edb-f755-48be-8f9d-6269177feb9e)

No me es posible conectar **micro:bit** a *Web Serial Terminal*, me dice que ya esta conectado. Ya intente resolver el problema:
- terminando la coneccion en la otra ventana.
- re-conectando el dispositivo.
- reiniciando el computador.

----
### REPOSICION SEMANA 8: Sesión 2

#### Micro-sesión 1: Apertura

El sketch de ejemplo se conecta sin ningun problema, pero al modificarlo para el juego de la actividad, el systema no serializa. 
Voy a intentar resolver este problema.

#### Micro-sesión 2: Problemas

El codigo no funciona, la fusion del codigo de serializado base y el juego snake a sido un ***fracaso*** hasta el momento.

![Screenshot from 2024-04-01 10-36-12](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/e57535ee-8762-4b97-a486-a145413011cf)


----
### REPOSICION SEMANA 8: Sesion 3

#### Micro-sesión 1: Apertura

El plan es realizar modificaciones al codigo base; adaptarlo al proyecto. Que la *snake* se mueva con el movimiento de los botones **A** y **B** de **micro:bit**.

NOTA: se debe adaptar porque el input original es de 4 botones y se va a reducir a 2. En la logica del codigo se debe poner estas opciones.

#### Micro-sesión 2:

Se implemento:
- sistema de *pause* 
- cambio de direccion con tan solo 2 teclas
- maquina de estados rudimentaria (coneccion, y gameplay) 


#### Micro-sesión 3:

La coneccion entre el microbit y el sistema funciona. Los botones son presionados en el microbit y la informacion es enviada e interpretada por el codigo para modificar el movimiento de la culebra.

FALTA: Enviar informacion al **micro:bit**

![semana 8 sesion 3 ms 2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/0bdcdeea-eb61-497c-b485-ff82f6d02886)


#### Micro-sesión 4:

Agregado fundaciones del sistema de pausa.

NOTA: Al pausar, la coneccion de serializacion se dana y deja de funcionar el intercambio de datos.

#### Micro-sesión 5 (Cierre):

Se a pensado implementar como sensores: 
- 1 los botones
- 2 el accelerometro.

como actuadores:
- 1 sonido
- 2 pantalla (dot matrix) mostrando informacion como puntaje y otros.

Esta ese error pero voy a continuar e intentar correjirlo para el final, ya que el sistema de pausa no es necesario para el desarrollo del proyecto.
La proxima sesion se planea implementar la reception e interpretacion de datos en el *micro:bit*.

----

### REPOSICION SEMANA 9: Sesion 1

#### Micro-sesión 1:

El plan va a ser organizar el envio/recepcion de datos, que ya esta, pero falta empaquetarlos en un solo mensaje.

#### Micro-sesión 2:

Enviado de mensaje en un solo tajo

```python
while True:
    # Pause
    if pin_logo.is_touched(): uart_buffer = 'P'
    else : uart_buffer = 'p'
        
    # Accelerometer  
    if accelerometer.was_gesture('shake'): uart_buffer = uart_buffer + 'X'
    else: uart_buffer = uart_buffer + 'x'   
    
   
    # Button press
    if button_a.was_pressed(): uart_buffer = uart_buffer + 'A'
    else : uart_buffer = uart_buffer + 'a'
    
    if button_b.was_pressed(): uart_buffer = uart_buffer + 'D'
    else : uart_buffer = uart_buffer + 'd'


    
    # Send
    uart.write(uart_buffer)
    uart_buffer = ''
```

#### Micro-sesión 3:

leyendo mensaje en **p5.js**

```javascript
if (port.availableBytes() > 0) {
      let dataRx = port.read(4); //1

      if (pause == false) {
        if (port[0] == "P") {
          pause = true;
          return;
        } else {
          pause = false;
        }

        
        if (port[3] == "X") {
        }

        
        if (dataRx[1] == "A") {
          if (direction == "up") direction = "left";
          else if (direction == "down") direction = "right";
          else if (direction == "left") direction = "down";
          else direction = "up";
        } 
        
        else if (dataRx[2] == "D") {
          if (direction == "up") direction = "right";
          else if (direction == "down") direction = "left";
          else if (direction == "left") direction = "up";
          else direction = "down";
        }
      }
    }
```
#### Micro-sesión 4:

Estructura para la lectura de datos (un solo mensaje, se utilizan las potentes librerias de *js* para detectar los caracteres necesarios, a diferencia de deparar el string con un metodo mas tradicional y lento de escribir)

```javascript
if (dataRx.includes("A")) {
          if (direction == "up") direction = "left";
          else if (direction == "down") direction = "right";
          else if (direction == "left") direction = "down";
          else direction = "up";
        }
```

#### Micro-sesión 5 (Cierre):

![semana 8 sesion 3 ms 2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/0968d981-66e5-412f-b3cf-7182659cd6db)

![2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/cc7ae516-e0eb-491c-859d-e402a99eb547)

**NOTA:** 

- Considero el proyecto en gran medida terminado; se debe hablar con el profesor para evaluar el proyecto.
- Falta *preguntar por los datos*
----



# Continuacion

El profeson explico como hacer el serializado en ascii, con el sistema usando un modelo cliente servidor que pregunta antes de enviar los datos.

### micro:bit

Se hace la pregunta cada cierto tiempo:

```python
while True:
    questionCounter++
    if questionCounter == 20:
        uart.write("Q\n")
        questionCounter = 0
```
Si se a leido informacion por el puerto:

```python
    if uart.any():
        display.show(Image.HAPPY)
        data = uart.readline()
        if data:
```
Si se le pregunta al __micro:bit__, el responde:

```python
            if data[0] == ord('Q'):
                uart_buffer = ''
                if accelerometer.was_gesture('shake'):
                    uart_buffer = uart_buffer + 'P'
                    # send = True
                else: uart_buffer = uart_buffer + 'p' 
                    
                # Button press
                if button_a.was_pressed():
                    uart_buffer = uart_buffer + 'A'
                    send = True
                else : uart_buffer = uart_buffer + 'a'
                
                if button_b.was_pressed():
                    uart_buffer = uart_buffer + 'D'
                    send = True
                else : uart_buffer = uart_buffer + 'd'
                uart.write(uart_buffer)
            else:
                if data[0] == ord('M'):
                    music.play(['e'],wait=False)
                if data[1] == ord('F'):
                    display.scroll(data[2])
```

### JavaScript

__NOTA:__ La idea del sistema es _la misma, lo unico que cambia_ es el lenguaje (y lo que esto convella) ...

Se hace la pregunta cada cierto tiempo:

```javascript
if (pause == false) {
      counterQuestion++;
      if (counterQuestion == 5) {
        if (port.opened()) {
          port.write("Q\n");
        }
        counterQuestion = 0;
      }
```

Si se a leido informacion por el puerto:

```javascript
      if (port.availableBytes() > 0) {
        let dataRx = port.read(1); //1
        print("dataRx: " + dataRx);
```

Si se le pregunta al __PC__ (*_y no esta pausado_), el responde:

```javascript
        if (pause == false) {
          if (dataRx == "Q") {
            sendData();
          }

          if (dataRx.includes("P")) {
            pause = true;
          }

          if (dataRx == "A") {
            if (direction == "up") direction = "left";
            else if (direction == "down") direction = "right";
            else if (direction == "left") direction = "down";
            else direction = "up";
          }

          if (dataRx == "B") {
            if (direction == "up") direction = "right";
            else if (direction == "down") direction = "left";
            else if (direction == "left") direction = "up";
            else direction = "down";
          }
        }
      }
```
## Continuacion

### Objetivo

Finalizar el proyecto, integrando el engine construido y adaptado anteriormente a los otros proyectos y acabar lo que falta de serializado.

### Notas

Con un poco de dificultad, porque el proyecto era viejo y tenia problemas, se a ido adaptando al estandar del engine que estoy utilizando en los otros proyectos del curso.

Hasta el momento inicia y entra al juego pero tiene algunos botones y errores que no cuadran, tratando de buscar y creando objetos del otro juego pero se resuelven con facilidad.

Cuando el juego este integrado aceptablemente, el siguente paso sera trabajar en el serializado.
