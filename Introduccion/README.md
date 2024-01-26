# Bitácora de aprendizaje


*----------------------------------------------------------------------------------------------------*
Clase 1
*----------------------------------------------------------------------------------------------------*
![sfi](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/3da810b6-3078-431b-8cd7-832cc0f26004)
![concert](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/2604172e-588f-4b3c-b7de-be5b20e5218a)

Por motivos de salud, no pude asistir a la primera clase.

Me puse a consultar información relacionada con el nombre de la materia.

Conclusion:
*----------------------------------------------------------------------------------------------------*
Sesion Externa 1
*----------------------------------------------------------------------------------------------------*
![arduino](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/80af048f-11d1-4e5b-a77b-acc8ac8a0c1e)
![microbit](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/cfee54b7-3cf2-4214-b718-dace858675a0)
![rpi](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/bc3cf74c-8183-4dc8-b0ac-1d7ae835776c)
![dcpu](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/bde2b88d-75b7-415e-a134-93441a1c26da)
![gamingpc](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/71e5e4b1-08f8-4941-95f3-a614699040a2)
![Sierra_Supercomputer_(48002385338)](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/d1465ada-a963-4698-934c-4a1073350030)

*----------------------------------------------------------------------------------------------------*
Clase 2
*----------------------------------------------------------------------------------------------------*
REFERENCIAS/RECURSOS:

Moment Factory
https://momentfactory.com/home

micro:bit
cable micro USB/USB




HERRAMIENTAS:

Hardware =>
micro:bit
Computador (PC)

Software =>
Micro:bit
https://python.microbit.org/v/3


El dia de hoy vamos a trabajar por primera vez con la placa de desarrollo micro:bit, utilizando herramientas online, se va a flashear funcionalidad a la board para familiarizarnos con ella.


NOTA: Cuando la board no tiene protección (caja), mantenerla sobre una superficie eléctricamente aislada



-------------------------------------------------
Actividad 1:
Vamos a utilizar por primera vez el sistema micro:bit,
1.	Conexión
2.	Conectar software (web)
3.	Flashear memoria

-------------------------------------------------
Actividad 2:
Sistemas usados:
1.	Acelerómetro
2.	Botones
NOTA: desconectar la conexión al terminar para liberar el BUS

-------------------------------------------------
Actividad 3:
Software =>
Visualizador de código online
 https://editor.p5js.org/

Conclusiones: Se pueden conectar múltiples computadores de limitados recursos para crear un sistema mas potente y eficiente sin incrementar los costos equiparables a un solo computador que ejecute todo el sistema
NOTA: conceptos de cohesión y acoplamiento

-------------------------------------------------
Actividad 4

-------------------------------------------------
Actividad 5

Responder preguntas
  1.	Explica e implementa ¿Cómo puedes hacer para que el círculo use colores diferentes?
  2.	Explica e implementa ¿Cómo puedes cambiar el fondo del canvas?
  3.	Explica e implementa ¿Cómo puedes cambiar la figura que se pinta en pantalla?
  4.	Explica e implementa ¿Cómo puedes cambiar las imágenes que muestra el micro:bit?
  •	Muestras imágenes de los resultados de tus experimentos en la bitácora.
  •	Realiza commits nuevos en el repositorio con los cambios al código en p5.js y para el micro:bit.


Respuestas

  1. Este framework utiliza la interface (methodo) "fill()", pasando como parametro el color en ingles "yellow"

   implementación:
   
        if(dataRx == 'A'){
            fill('yellow');
        }
        else if(dataRx == 'B'){
            fill('orange');
        }
        else{
            fill('purple');
        }

  2. "background(byte);" Es el comando para cambiar el color de fondo, utiliza escala 0-255 en escala de grises

      Implementación:
      
      byte color = 126;
      if(true){
          background(color);
      }
      return 0;
      
 3. El comando "display.show()" permite mostrar graficos de un banco predefinido, como "Image.HEART" e "Image.HAPPY"

    Implementación:

    if(port.availableBytes() > 0){
        let dataRx = port.read(1);
        if(dataRx == 'A'){
            display.show(Image.HEART);
        }
        else if(dataRx == 'B'){
            display.show(Image.HAPPY);
        }
        else{
            printf("NO input!");
        }

4.  Una forma facil, eficiente y practica, aunque un poco limitada, seria utilizar ASCII. Letras que parescan o se asemejen a formas e imprimirlas con el comando scroll "display.scroll(':)', wait=False, loop=True). Como nota extra incluso se podrian hacer secuencias de caracteres que cuenten una historia ...

   Implementación:

   std::string imagen1 = ":)";
   char[] imagen2 = { ´:´, ´(´ };

   
   if(dataRx == ´A´) {
   display.scroll(imagen1, wait=False, loop=True);

   else display.scroll(imagen2, wait =False, loop=False);
   }
   return 0;


![Captura de pantalla 2024-01-26 113119](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/f858deee-a451-4898-80aa-e6e54368cbdd)



TAREA:
Viernes a las 12 del dia

3 momentos en la bitacora, repo codigo
*----------------------------------------------------------------------------------------------------*
Sesion Externa 2
*----------------------------------------------------------------------------------------------------*

*----------------------------------------------------------------------------------------------------*

*----------------------------------------------------------------------------------------------------*
Clase 3
*----------------------------------------------------------------------------------------------------*

*----------------------------------------------------------------------------------------------------*
Sesion Externa 3
*----------------------------------------------------------------------------------------------------*

*----------------------------------------------------------------------------------------------------*
