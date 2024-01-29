# Bitácora de aprendizaje

Lunes 29 de Enero

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

7. ¿Qué es una máquina de estados?

Maquina de estados finita:
Los estados se pueden definir como comportamientos que tienen los objetos. Los estados dan la impresion de que ses tienen varios objetos, o que un objeto cambia a ser otro.

Cierto estado requiere ciertas funciones y atributos especificos que pueden ser solo relevantes para ese estado.


