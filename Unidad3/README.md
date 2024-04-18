REFERENCIAS:

[WEB del curso](https://sistemasfisicosinteractivos1.readthedocs.io/)

[p5.js](https://p5js.org/)

[Web Serial](https://capuf.in/web-serial-terminal/)

[IEEE-754 Floating Point Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

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

#### Micro-sesión 2 (25 minutos)

![3](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/ec58a13b-cca1-43f3-b367-7cc81a9fa177)

![2](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/24807365-958b-42b6-b36c-a6b4e8b5110b)


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

### Sesión 2

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

