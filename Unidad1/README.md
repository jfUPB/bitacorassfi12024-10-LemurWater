# Bitácora de aprendizaje

## SEMANA 2

WEB: https://sistemasfisicosinteractivos1.readthedocs.io/

Software para sistemas embebidos

Que es un sistema embebido?

Es un computador el cual envia, recibe y procesa informacion con otros computadores dentro de un sistema. normalmente cumple una funcion especifica.

Preguntas guía iniciales

1. ¿Cómo se leen los pulsadores A y B?

button_a.get_presses() y button_b.get_presses().
Los objectos "button_a" y "button_b" contienen la funcion "get_presses()" que actua cuando los botones A y B son presionados.

2. ¿Cómo se leen el botón virtual que está en el logo del micro:bit?

el objeto input tiene el methodo "logoIsPressed()" el cual debuelve un boolean indicando el estado del boton


3. ¿Cómo se lee información serial que llega al micro:bit?

Se debe crear una coneccion entre micro:bit y el dispositivo, por medio de un cable USB o coneccion Wi-Fi (mas complejo)

4. ¿Cómo se envía información serial desde el micro:bit?

Se debe establecer una coneccion entre el computador 1 (micro:bit) y el computador 2, este se puede configurar para enviar la senal, por cable USB y luego, transferir la informacion a una aplicacion web que interprete los datos enviados por el computador 1 (micro:bit)


5. ¿Cómo dibujar en la pantalla de LED?

micro:bit (al igual que el 99.9% de las pantallas) utiliza un sistema matricial; de 5x5 (25 LEDs)

la funcion plot(x,y) utiliza parejas ordenadas para la identificacion de los LEDs.


6. ¿Cómo hacer para producir sonidos con el speaker?

microbit.speaker.off()
El objecto speaker de microbit, tiene una funcion para activar el speaekr "on()" y desactivar "off()"

audio.play(Sound.HELLO) | audio.play(Sound.HELLO, speed=60, pitch=255)
El objecto audio tiene la funcion "play()", la cual recibe como parametro el sonido a producir; en este ejemplo se utilizan un banco de sonidos predefinidos.
NOTA: Tambien se puede definir variables como la velocidad y el pitch.

music.play() tambien tiene una biblioteca de sonidos chiptune predefinidos, mas melodicos y ritmicos.


7. ¿Qué es una máquina de estados?

Maquina de estados finita:
Los estados se pueden definir como comportamientos que tienen los objetos. Los estados dan la impresion de que ses tienen varios objetos, o que un objeto cambia a ser otro.

Cierto estado requiere ciertas funciones y atributos especificos que pueden ser solo relevantes para ese estado.
NOTA: El sistema solo puede estar en un (1) solo estado en todo momento (pero en cualquier momento puede cambiar de estado).


8. ¿Qué son eventos en una máquina de estados?

son sucesos o acciones disparados por un "trigger" que son relevantes solo para y dentro de la maquina, estos pueden ser IO streams, completar timers, condicionales, etc...
NOTA: pueden ocurrir varios al mismo tiempo.


--------
Continuacion

NOTA: No pude asistir a la clase pasada.



 
9. ¿Qué son las acciones?
Es una implementación adicional que trabaja con las funciones base del programa, la accion puede estar escrita en un lenguaje diferente al de la implementacion basica.
CONCEPTO INTERESANTE Y DISCUTIBLE: La unica manera de trabajar varias acciones al mismo tiempo es con Multithreading, pero inclusive asi, se puede argumentar que el sistema solo puede ejecutar una funcion al tiempo; a diferencia de las "acciones" en los seres vivos, podemos respirar y caminar al mismo tiempo (2 acciones a la vez).


11. ¿Cuáles son los estados, eventos y acciones en el reto propuesto?

ESTADO: Inicia en modo de configuración, es decir, sin hacer cuenta regresiva aún, la bomba está desarmada. El valor inicial del conteo regresivo es de 20 segundos.

https://app.diagrams.net/#G1o5ITmyDJ8qYDsCI7YrF0lJ_WU11ojUny




-----
Sesion individual



11. ¿Cómo es posible estructurar una aplicación usando una máquina de estados para poder atender varios eventos de manera concurrente?

Se empaquetan los eventos buscando tener una alta cohesion, la máquina irá secuencialmente de un estado a otro, utilizando los eventos que necesite pasando por sus etapas de funcionamiento. Habrán unos estados iniciales, finales. y unos intermedios los cuales el sistema usará convenientemente y concurrentemente en su uso habitual.



12. ¿Cuáles son los eventos que pueden ocurrir de manera simultánea en el problema planteado en el reto?

La serializacion es un evento que podriamos considerar siempre ocurre en paralelo con cualquier otro proceso.



13. Construye una aplicación que muestre en la pantalla de LED dos imágenes diferentes que se alternarán cada 2 segundos, pero sin usar la función bloqueante sleep(). Investiga las funciones ticks_ms() y ticks_diff() de la biblioteca utime. ¿Cómo puedes utilizar las dos funciones anteriores para resolver el problema de las imágenes que alternan?

REFERENCIAS: 
ticks_diff(a,b): devuelve la diferencia entre a y b
ticks_ms(): contador estandar que tiene un punto arbitrario como referencia

while True:
    now = int(utime.ticks_ms())
        while True:
           if int(utime.ticks_ms() / 1000) > now + 10:
           if ticks_diff(now + 2000, now) > 0:
               //display image
               return
return 0






1. ¿Cómo funciona este ejemplo?

se importan las librerias
se crea un objeto que representa un estado con una responsabilidad (guardar el tiempo actual)

se inicia la maquina

inicia en el estado que guarda el tiempo actual.
luego pasa al siguiente estado que es un timer el cual tiene un evento que se activa cuando la diferencia de tiempo es mayor a la establecida
luego tiene otro evento que ocurre dependiendo del estado de la variable self.pixelState




2. ¿Qué relación tiene este ejemplo con las preguntas guía?

Es un equema muy sensillo de una maquina de estados la cual contiene un estado que dispara algunos eventos y sus acciones serian configurar y decrementar el timer, mostrar imagenes en la pantalla y alterar variables



CONCLUSIONES:
Aveces tendemos a crear software como escribimos ... porque tenemos la habilidad, vamos escribiendo cualquier cosa que se nos va ocurriendo en la mente.

Pero si lo que se busca es la creacion de una obra literaria, se deben mantener siertas normas y reglas que faciliten tanto al creador como al lector, nadar por el mundo creado.

El software no es la excepcion (con ciertas diferencias, claro esta)


Sigiendo con los conceptos de OOP y similares, buscamos empaquetar la informacion y procesos, agrupando en "cosas" similares. Los estados son una manera muy util de entender claramente que hace que, cuando y donde.

-----

<span style="color:red">
Red Text test
</span>

<span style="color:red">Text content</span>sistemas-embebidos


## SEMANA 2

### Sesión 1 lunes febrero 5

#### Micro-sesión 1: apertura.
OBJETIVO: El proposito de la sesion sera implementar el codigo de la momba en el micro:bit.
Voy a empezar, en esta micro-sesion, por entender el algoritmo del ejemplo y transformarlo a UML.


#### Micro-sesión 2

NOTA: Me a tomado DEMASIADO tiempo crear el algoritmo (nisiquiera e empezado con el UML (50+ mins)) ... pero da una claridad visual hacerca del funcionamiento del sistema, asi que voy a continuar con la diagramacion.


#### Micro-sesión 3

![Bomba_8](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/bac70350-bb9c-4866-bf64-a588b538ddf3)


#### Micro-sesión 4: cierre 

CONCLUSIONES: El diagrama del algoritmo da gran claridad del funcionamiento del sistema y es muy facil verlo y referenciarse para analizar una parte especifica del funcionamiento del sistema. Tambien permite ver las conecciones entre los distinos bloques logicos.

### Sesión 2 miércoles febrero 7

#### Micro-sesión 1: apertura.

#### Micro-sesión 2

#### Micro-sesión 3

#### Micro-sesión 4: cierre 

### Sesión 3 fecha?

PROPOSITO: Darle realismo al proyecto con elementos faciles de implementar pero altamente creativos e interesantes que le agreguen valor al proyecto.


#### Micro-sesión 1: apertura.

PROPOSITO: Buscar componentes para armar el proyecto:
- tubos para los tacos de TNT.
- Cinta de teflon que los sostenga.
- Cables de decoracion y posible implementacion para desactivar la bomba quitando los cable en el orden especifico.

![5](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/925c9d75-ea83-49aa-a522-926d2cdd1e9b)
![4](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/706e99f6-9c17-4e87-a568-903d54aff396)
![unnamed](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/cff5b1dd-6432-41c3-b25e-6fdc0777c51d)


#### Micro-sesión 2

PROPOSITO: Aprender como funcionan los pines de entrada y salida de micro:bit, para agregarle elementos interactivos a la bomba.

![pins-v1-v2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/2697d436-fcb8-4db3-89a7-bd5502aa14e1)

https://makecode.microbit.org/device/pins

Los pines de cocodrilo pueden ser una buena opcion para el proyecto, se pueden desconectar facilmente a diferencia de los plugs banana de 4mm.

![Screenshot from 2024-02-06 23-00-59](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/675852f1-a218-4c62-9fbe-3fe932310140)

aliexpress.com






#### Micro-sesión 3

#### Micro-sesión 4

#### Micro-sesión 5: cierre 

