# REFERENCIAS:

[WEB del curso](https://sistemasfisicosinteractivos1.readthedocs.io/)

[p5.js](https://p5js.org/)

[Web Serial](https://capuf.in/web-serial-terminal/)

[IEEE-754 Floating Point Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html)


[PUML Online](https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)

[State Diagram](https://en.wikipedia.org/wiki/State_diagram)

[ELECTRONICOS FANTASTICOS](https://www.youtube.com/watch?v=IRityYw-IfI)

![ELECTRONICOS FANTASTICOS](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/0162e8f3-f966-458e-8bfd-297cef3bc075)

## [Musica & micro:bit](https://www.youtube.com/watch?v=3lZOkUlGsdQ)

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/1e98138b-8a07-4360-846b-3aec30270aca)

[speaker 1](https://microbit.org/projects/make-it-code-it/make-some-noise/)

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/71bbbf52-389e-48b9-aa31-73609260568a)

[speaker 2](https://microbit.org/projects/make-it-code-it/guitar-1-touch-tunes/)

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/9652aac3-4347-47c0-9471-47c3615368aa)

[speaker 3](https://microbit.org/projects/make-it-code-it/guitar-2-chords/)

---

# Bitácora de aprendizaje

## ¿Cómo voy?

- [ ] Tengo mi reto personalizado. 
- [ ] Terminé la actividad 1 de investigar. 
- [ ] Terminé la actividad 2 de investigar.
- [ ] Terminé la actividad 3 de investigar.
- [ ] Terminé la actividad 4 de investigar.
- [ ] Terminé la actividad 5 de investigar.
- [ ] Terminé la fase de aplicar.
- [ ] Terminé la documentación de cierre.

## Reto personalizado
> [!TIP]
> Escribe aquí tu reto personalizado. 

## Documentación de cierre de la unidad

### ¿En qué consiste la aplicación que diseñaste e implementaste?

### Explica el protocolo de integración entre p5.js y el micro:bit.

### Muestra las partes del código donde implementaste el protocolo.

### Enlace al video demostrativo




## Consejos para el uso efectivo de la bitácora

* Preparación al inicio de la micro-sesión 1: establece un objetivo claro de la sesión para maximizar el tiempo de trabajo efectivo.
* Concisión: sé breve pero significativo en tus respuestas para ajustarte al tiempo de reflexión de 4 minutos.
* Pausas activas: usa las pausas de 1 minutos para realmente desconectar, estirar y descansar los ojos; esto ayuda a mantener la energía y la concentración.
* Reflexión profunda al final de la mimcro-sesión 4: usa parte del tiempo para una reflexión más profunda y para planificar, asegurándote de cerrar la sesión
  con una nota productiva y prepararte para lo que sigue.

## Semana 10

### Sesión 1

#### Micro-sesión 1 (25 minutos)

**Planeación:**

1. ¿Qué voy a trabajar hoy?
   Voy a investigar informacion relacionada con el *Theremin*
3. ¿Cuál es mi objetivo principal para esta sesión?
   Conocer el instrumento, saber si es viable realizarlo como proyecto en el **micro:bit + p5.js**

**Trabajo en concentración**

**Meta-aprendizaje:**

3. ¿Qué he logrado en esta micro-sesión de trabajo
   He logrado hacerme una idea basica de como seria el proyecto, un esquema en la cabeza. Me parece muy sensillo.
   Se podria realizar con el *Acelerometro* del **micro:bit** tomando los 3 vectores (x, y, z) y dandole a cada dimension una propiedad en el instrumento, ej:
   - la *aceleracion* en **x** puede controlar: la frecuencia del sonido.
   - la *aceleracion* en **y** puede controlar: el volumen.
   - la *aceleracion* en **z** puede controlar: el tipo de sonido,efecto, "color".

   Esa es la idea basica principal e inicial.
   Leyendo mas sobre el instrumento, entendi que se usan las dos manos:
   - una para el **volumen**
   - y la otra para el **"color"**

   Asi que me gustaria realizar el ejercicio con **2 micro:bit**, para que el ejercicio sea mas fiel al instrumento original y tenga mas alcance, pero esta la idea simple de uno por facilidad (el problema esque el cambio en sonido es mas limitado porque solo se puede realizar pulsando 2 botones envez de un valor en     punto flotante dictado por una dimension del acelerometro).
   
5. ¿Con qué dificultades me encontré y cómo las abordé?
   Mis dificultades fueron desiciones de de complejidad y alcance del proyecto.
   Las aborde empujando (y limitando) todas mis opciones a dos extremos opuestos, elijiendo una y dejando la otra como **Plan B (emergencia)**
   
7. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
   Falta ver un video de como funciona el **Theremin**, ver una persona usarlo y desidir que tan adaptable es a los acelerometros.
   
9. ¿Qué he aprendido o reforzado en esta micro-sesión?
   Altamente los conceptos de **maquina de estados** y **programacion por eventos**

```python
   # Imports go at the top
from microbit import *
import music

# Variables ---------------------------------
uart.init(baudrate=115200)
theremin_mode = 0
state = 1;
# Variables ---------------------------------

# States ------------------------------------
def state_1():
    if button_a.was_pressed():
        theremin_mode = 1
    if button_b.was_pressed():
        theremin_mode = 2

def theremin_1():
    music.set_tempo(bpm=120)

    x_strength = accelerometer.get_x()
    # x_strength *= 10
    display.scroll(x_strength)
    print(x_strength)

def theremin_2():
    music.set_tempo(bpm=120)
# States ------------------------------------
    

# Setup -------------------------------------
display.show(Image.SILLY)
# Setup -------------------------------------


# loop repeats forever ----------------------
while True:
    if state == 1: 
        state_1()
        break
    elif state == 2:
        if theremin_mode == 1:
            theremin_1()
            break
        else:
            theremin_2()
            break
# loop repeats forever ----------------------
```

#GIGANOTA:
Algo a resaltar esque la matematica es el alfabeto en el que esta escrito el mundo...
Siento, que estoy en un punto donde conceptos tan altos como mover una mano para hacer sonar el instrumento, rapidamente, los llevo a un bajo nivel donde estan compuestos por vectores y luego es facilmente simularlo en un dispositivo de computo.

- Tambien a resaltar (y parte de lo mismo) es que conceptos de fisica como hondas de radio y frecuencia. para tomar como referencia el punto inicial donde se activo el **micro:theremin** y leyendo que tanto se aleja de ese punto, para simular la antena ... 🤯

Alexandra Stepanoff playing the theremin on NBC Radio, 1930

![Theramin-Alexandra-Stepanoff-1930](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/313b9973-4c05-407e-ab2e-943e78266656)

The components of a modern Moog theremin, in kit form

![Moog_Theremin_Bausatz](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/4effda4e-5de6-4aa3-947f-7981fb4535c7)


#### Micro-sesión 2 (25 minutos)

![2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/24807365-958b-42b6-b36c-a6b4e8b5110b)  ![3](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/ec58a13b-cca1-43f3-b367-7cc81a9fa177)

Posibles ejes de movimiento para utilizar como datos (punto flotante)

![Theramin-Alexandra-Stepanoff-1930 - diagram](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/bfac0a3e-c3a7-4923-9025-9d6c19b0f0de)



se puede expandir a 6 gestos + 3 (4 con touch) botones para mapear los controles del sonido...
NOTA: Me parece gran cantidad de de inputs, almenos a comparacion del **Theremin** original, que solo utiliza 2, una mano para el **pitch** y la otra para el **volumen**

- Inclusive se puede dar la posiblidad al usuario para elejir en que nota se quiere "afinar" el "instrumento", mostrando la nota (y puede ser los Hz) en la pantalla del **micro:"bit**.
```python
music.set_tempo(bpm=120)
```

tabla frecuencia (Hz) en relacion con la escala musical

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/7f88e2b3-4421-4913-b201-c82ffd7bbd5a)

Referencias:

https://en.wikipedia.org/wiki/State_diagram


Le e trabajado a la maquina de estados, aprendiendo un poco el lenguaje de diagramacion y estructurando (y re-estructurando) como podria ser la maquina de estados.

![state_machine_1](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/8b092149-3668-4494-809c-684fba7bae57)

![state_machine_2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/9685d5ee-9602-4305-9b19-674a03858bd9)

algoritmo: estado 1 - seleccionar octava: boton a & b ( seleccionar octava)


![algo state1 - button_a](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/b2324d7a-c441-46be-9385-4c3d748ed383) ![algo state1 - button_b](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/2ab4f03a-4eb1-4f2d-95e2-3214a1885441)

![algo state2 - button_a](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/46f5c158-c325-405a-8671-cc3e9da3a299) ![algo state2 - button_b](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/c0aa17c8-e441-494b-89ba-8f698dbe8fe9)


![state_machine_3](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/95b9ad93-9c2e-4076-8a3d-aca40e2a0837)

![state_machine_4](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/dec1d98d-6560-4e55-84ce-312b5e8cee89)


**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 3 (25 minutos)

voy a disenar como va a ser la sensada del movimiento

**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 4. (25 minutos)

Trabaje en el codigo del microbit.
NOTA:
- falta serializado.
- hay un error en el sonido (de como funciona en loop)

**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión?

**Cierre de sesión:**

5. ¿He alcanzado los objetivos planteados al inicio? Si no, ¿por qué y qué puedo mejorar?
6. ¿Cuáles fueron los desafíos más significativos de hoy y cómo los superé?
7. Basado en el trabajo de hoy, ¿qué insights importantes he ganado?
8. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

### Sesión 2

#### Micro-sesión 1 (25 minutos)

**Planeación:**

invetigue uno poco sobre un concepto que vi y me parecio interesante:

[Cyber–physical system](https://en.wikipedia.org/wiki/Cyber%E2%80%93physical_system)

1. ¿Qué voy a trabajar hoy?
2. ¿Cuál es mi objetivo principal para esta sesión?

**Trabajo en concentración**

**Meta-aprendizaje:**

3. ¿Qué he logrado en esta micro-sesión de trabajo?
4. ¿Con qué dificultades me encontré y cómo las abordé?
5. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
6. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 2 (25 minutos)

**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 3 (25 minutos)

**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 4. (25 minutos)

![state_machine_5](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/5c6341c2-86e0-4e02-a561-f0fb947b583c)

[Aprendiendo a usar p5.js](https://p5js.org/get-started/)

![1](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/6e0027ea-9d43-4e38-a17f-da567e19dee9) ![2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/c3a8a1a1-c2e5-4ec0-9d8f-bdf6bd41aa81)

Algoritmo para cambiar el color segun la posicion del cursor

![algo cursor_color](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/765d132f-1b58-470d-a52e-20d9e37b19c2)

![regla de tres](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/b6e3a5eb-45d3-4476-bada-d0d47ddab29d)

![10](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/b096ef94-1978-4af0-ad22-9417e3813954)

![11](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/44d8e351-3c5b-4a6d-900a-01c62970c704)

![12](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/f5fb4e31-356a-4e1e-bc08-9239c70992dc)

![13](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/9c392d34-449d-41af-b12b-deb08e701113)


Estaba investigando un poco sobre los cursores

[Cursor (user interface](https://en.wikipedia.org/wiki/Cursor_(user_interface)

![Windows_Command_Prompt](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/2a1f2680-e98b-4799-813c-f5498e0b4eb4)

![CursorListHorizontal](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/c18b8bf2-1d9c-41b9-857d-f514ba59d34c)


![Text_cursor_blinking](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/4fc5c155-b02e-46ed-b765-4e2f6a3fd0ab)
![Slide_rule_cursor](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/369bdd49-1964-47de-89ab-a5d7864408a8)
![PointerTrails](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/623989b5-93f4-483b-87bd-ac9874932da6)

![Blender3DCursor](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/f6989d9e-9467-47fb-86f0-b2f5f4c5fbb1)


**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión?

**Cierre de sesión:**

5. ¿He alcanzado los objetivos planteados al inicio? Si no, ¿por qué y qué puedo mejorar?
6. ¿Cuáles fueron los desafíos más significativos de hoy y cómo los superé?
7. Basado en el trabajo de hoy, ¿qué insights importantes he ganado?
8. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

### Sesión 3

#### Micro-sesión 1 (25 minutos)

**Planeación:**

1. ¿Qué voy a trabajar hoy?
2. ¿Cuál es mi objetivo principal para esta sesión?

**Trabajo en concentración**

**Meta-aprendizaje:**

3. ¿Qué he logrado en esta micro-sesión de trabajo?
4. ¿Con qué dificultades me encontré y cómo las abordé?
5. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
6. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 2 (25 minutos)

**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 3 (25 minutos)

**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 4. (25 minutos)

**Trabajo en concentración**

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión?

**Cierre de sesión:**

5. ¿He alcanzado los objetivos planteados al inicio? Si no, ¿por qué y qué puedo mejorar?
6. ¿Cuáles fueron los desafíos más significativos de hoy y cómo los superé?
7. Basado en el trabajo de hoy, ¿qué insights importantes he ganado?
8. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

## Semana 11

### Sesión 1

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí

### Sesión 2 (Miercoles 10)

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí

### Sesión 3

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí


## Semana 12

### Sesión 1

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí

### Sesión 2

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí

### Sesión 3

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí

## Semana 13

### Sesión 1

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí

### Sesión 2

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí

### Sesión 3

1. ¿Cuál será el propósito de la sesión de hoy?

> Escribe aquí
 
2. ¿Cuáles fueron los desafíos más significativos de la sesión y cómo los superé?

> Escribe aquí

3. Basado en el trabajo de la sesión, ¿Qué aprendí o qué conclusión saco o cuál es la síntesis?

> Escribe aquí

4. ¿Cuáles son los pasos siguientes para continuar avanzando en el proyecto?

> Escribe aquí



# Abril 17 Miercoles

El profesor dio una completa explicacion sonbre el serializado en binario, temas a tener en cuenta y otros temas relacionados con el curso.

