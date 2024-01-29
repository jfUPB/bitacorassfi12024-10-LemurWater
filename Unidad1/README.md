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

Se debe crear una coneccion entre micro:bit y el dispositivo, por medio de un cabl USB o coneccion Wi-Fi (mas complejo)

