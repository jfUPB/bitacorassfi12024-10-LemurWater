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

[Cursor user interface](https://en.wikipedia.org/wiki/Cursor_(user_interface)


![Text_cursor_blinking](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/4fc5c155-b02e-46ed-b765-4e2f6a3fd0ab)

![Windows_Command_Prompt](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/2a1f2680-e98b-4799-813c-f5498e0b4eb4)

![PointerTrails](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/623989b5-93f4-483b-87bd-ac9874932da6)

![CursorListHorizontal](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/c18b8bf2-1d9c-41b9-857d-f514ba59d34c)

![Slide_rule_cursor](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/369bdd49-1964-47de-89ab-a5d7864408a8)

![Blender3DCursor](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/f6989d9e-9467-47fb-86f0-b2f5f4c5fbb1)


NOTA: E estado aprendiendo como usar el sistema de renderizado de __p5.js__ , diferentes formas y colores.

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

con los conocimientos obtenidos hasta el momento, de otras materias (sistemas computacionales); e logrado hacer un alto y pensar con cabeza fria...

Al intentar conectar el __micro:bit__ al __PC__ me salio el error:
```error
Serial Connection FailedNetworkError: Failed to execute 'open' on 'SerialPort': Failed to open serial port.
```
Y muy sagazmente le antepuse _arch_ como usualmente ago y lo puse en el buscador:

```
arch Serial Connection FailedNetworkError: Failed to execute 'open' on 'SerialPort': Failed to open serial port.
```
llevandome al siempre confiale foro de __Arch__ Linux (Wikipedia 2.0); donde alguien responde muy amablemente:

```
IIRC, serial ports belong to group uucp in Arch Linux.
```
...y fue hay cuando se me abrio el tercer ojo ...

__recorde__ (platonicamente) que los usuarios pertenecen a grupos y estos les dan los permisos, entonces (como siempre) _clickee_ el link a la __Wikipedia__ de __Arch__ Linux, a leer un poco sobre _users_.

y asi fue como logre __NO__ usar _Windows_.


[serial connection __micro:bit__ in GNU/Linux](https://youtu.be/n12hKIMMhLA)


Referencias:

![Arch Linux forums](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/299a46c1-c3d7-448a-93c2-1498659ea861)

[Newbie Corner» SOLVED How to set non-root access to serial ports?](https://bbs.archlinux.org/viewtopic.php?id=178552)

![uucp](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/e19663fb-813c-4afa-87e4-fd7e680198a6)

[Arch Wiki - users and groups](https://wiki.archlinux.org/title/users_and_groups)

![linux WebUSB](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/5d402633-dad4-4b1a-8c15-c7ec209ccc61)


😃👍

**Planeación:**

1. ¿Qué voy a trabajar hoy?

   Repaso de JavaScript
   
3. ¿Cuál es mi objetivo principal para esta sesión?
     aprender un poco de *javaScript* en general y muy __muy importante__, como separar el proyecto en varios archivos

**Trabajo en concentración**

**Meta-aprendizaje:**

3. ¿Qué he logrado en esta micro-sesión de trabajo?
4. ¿Con qué dificultades me encontré y cómo las abordé?
5. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
6. ¿Qué he aprendido o reforzado en esta micro-sesión? 

#### Micro-sesión 2 (25 minutos)

**Trabajo en concentración**



[How to Connect Godot to an Arduino](https://www.youtube.com/watch?v=nOKno82_gd0)

PC/Godot script:

```cs
using Godot;
using System;
using Sytem.IO.Ports;

public partial class Arduino : Node2D
{
  SerialPort serialPort;
  RichTextLabel text;
  
  public override void _Ready()
  {
    text = GetNode<RichTextLabel>("RichTextLabel");
    serialPort = new SerialPort();
    serialPort.PortName = "COM3";
    serialPort.Baurate = 9600;
    serialPort.Open();
  }
  public override void _Process(double delta)
  {
    if(!serialPort.IsOpen) return;
  
    string serialMessage = serialPort.ReadExisting();

    if(serialMessage = "Hey Godot"){
      text.Text = "Hello Arduino, I hear you :)";
      hasHeadFromArduino = true;
      timer = Time.GetThicksMsec();
    }

    if(hasHeadFromArduino && Time.GetThicksMsec() - timer > 3000){
      text.Text = "\n Turning on the Light for your :D";
      serialPort.Write("1");
      hasHeardFromArduino = false;
    }
  }
}
```

Arduino script:

```c
const int buttonPin = 4;
const int ledPin = 10;

int buttonState = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if(buttonState == HIGH) {
    Serial.println("Hello Godot");
  }

  if(Serial.read() == '1') {
    digitalWrite(ledPin, HIGH);
  }
}
```
Con los conceptos aprendidos en la materia, puedo entender facilmente (e inclusive entender en codigo de lenguaje que no uso recientemente), cuales son las partes del codigo que intervienen en la serializacion, sus componentes y como sucede el intercambio de datos, el tipo de serializacion (sensilla en el ejemplo), __pero con los conocimientos aprendidos en el curso, me siento en la capacidad de integrar protocolos ascii, binarios y modelo de cliente-servidor que pregunta antes de enviar los datos.__

![code arduino godot](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/20718381-ff97-4027-8cf3-9242a97d81b1)

__CONCLUSION:__ Puedo conectar _lo que sea*_ con __lo que sea__*

por que las cosas son conectables _(todo?)_, y todo habla un lenguaje, es como los seres vivos entendemos la realidad (y los PC) y debe haber un punto medio de comunicacion, un _canal mediador_ que conecte los 2 <*> ...


... y el por que? bueno, eso ya lo sabemos:

```
“Cuatro manos trabajan mejor que dos”
```

[3 Body problem - X86 Needs To Die](https://youtu.be/xCBrtopAG80?t=857)

[The Stilwell Brain](https://youtu.be/rA5qnZUXcqo?t=830)


##### MOCAP

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/b4e3b293-4ce6-40b7-ace0-21f89ccd366b)

[https://www.aliexpress.com/w/wholesale-MPU%2525252d9250.html?g=y&SearchText=MPU-9250&sortType=total_tranpro_desc]

![Screenshot from 2024-04-23 04-05-02](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/daaa6cb8-c4b8-43f7-bba4-251b4128ce9a)

![MPU-6050](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/2e19fb59-b1b1-436d-9c82-97f893c30d44)

[CHALLENGE 25 MPU 6050 working well mocap suite](https://forum.arduino.cc/t/challenge-25-mpu-6050-working-well-mocap-suite/659042/4)

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/8464d44d-9c2a-431c-a776-c1f15b3c8349)


```
jremington Jun 2020post #6
You really haven't described your project well enough for anyone to advise you.

If "track 25 points on the body" means to track the (x,y,z) position of each point independently, then your current proposal won't work at all, especially with just the gyro terms.

That is why I suggested that you learn how to track one point, before thinking seriously about the rest of the project. This is really difficult to do! The question comes up every couple of days on the forum, and there is no cheap solution.
```
```
jremington:
"Belief" is not enough. You need to make absolutely certain what it is you want to measure, and get all data collection and analysis working perfectly with just one or two sensors, before you commit to putting 25 modules together.

Protoboards cannot be used on moving objects as the connections will be unreliable and fail.

I agree with Koepel: there are terrible logistics involved in getting data from N MPU-6050 modules mounted at N different points on a moving body. I am quite certain that you will need N sturdily constructed nodes, each with one sensor and one processor on a small PCB, which will somehow funnel the data back to a central point. That funneling will be quite a challenge as well.
That is a reasonable price, if the system is reliable and does what you want.

**Meta-aprendizaje:**

1. ¿Qué he logrado en esta micro-sesión de trabajo?
2. ¿Con qué dificultades me encontré y cómo las abordé?
3. ¿Estoy más cerca de alcanzar el objetivo de la sesión? ¿Qué falta por hacer?
4. ¿Qué he aprendido o reforzado en esta micro-sesión? 
```
```
Koepel Jun 2020post #2
Hi. I'm afraid it is not going to work.

There is a way to have more than one MPU-6050 on the I2C bus with the adress selection pin AD0. Keep all AD0 of all the sensors high (they will have address 0x69) and bring only one down to 0x68 by making AD0 low. When that sensor is done, then select another one. You need a 3.3V Arduino board to do that.

You would have to remove all the pullup resistors from the modules.

So far so good, but the problems are:

A Arduino Uno can get data from a MPU-6050 at a rate of 100Hz and do some calculations as well. For 25 sensors you need a faster Arduino board, but the I2C bus will still be slow. It will take a long time before all the data from all sensors is collected.

The I2C bus can not have long wires. Using a cable makes it worse and SDA and SCL next to each other in a flat ribbon cable is the worst because the I2C bus can not handle crosstalk between SDA and SCL.

What library will you be using for the calculations ?

Some IMU modules have a sensor with a processor inside the sensor chip. They can do the calculations in the sensor chip: SparkFun VR IMU Breakout - BNO080 (Qwiic) - SEN-14686 - SparkFun Electronics 18.
35 * 25 = 875 dollars.

Breadboards are only for testing and they are not even good at that because they can have bad contacts.

What will you do with that data ? Where will it go and how ?
Would it be possible to have a few Arduino boards, each with 8 or 9 sensors ?
```

```
So far I understand that it is difficult to make the arduino read more than one MPU 6050 sensor and make it work, but I need to make it work and respond with minimum response time.
I am listing the items I need to buy by the logic I was in before reading the forum:

1x arduino
1x 400 dots protoboard
4x mini protoboards 170 dots
25x mpu 6050 sensor
```




##### Motion Capture system that you can build yourself

[Motion Capture system that you can build yourself](https://hackaday.io/project/27519-motion-capture-system-that-you-can-build-yourself)

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/2d6cbbb0-2d02-4281-b64d-528a77f54220)

```
Why Chordata was created
The origin of Chordata was a basic need. Bruno, our tech lead, wanted a way to register dance moves for a performance piece, but none of the tools available matched his needs (nor his budget). A lot has happened since then: now the system is publicly available (as a BETA release), and lots of documentation can be found on the sites described above.

This project consists on three parts:

Hardware (K-Ceptor):
Motion capture is about getting the orientation of every body limb or part at real time as accurate as possible. A simple MEMS IMU device*, and freely available sensor fusion algorithms are enough to get a decent result. The problem starts when you want to get the data of several devices. Most of this devices came with an i2c interface, but their address is fixed in the hardware. So one of the building blocks of Chordata is the sensing unit capable of coexisting with several “siblings” on the same bus: the “K-Ceptor” It consists of a LSM9DS1 IMU, and a LTC4316 i2c address translator.

```
![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/fdba4049-109e-4f1c-922e-7e3529840344)


[](https://medium.com/@fasateaniket5/motion-sensors-mpu-6050-and-mpu9250-e86467e9a237)

```
Software (Notochord):
Getting the data of a lot of sensors on real time, processing it, and send it in an easy-to-read format to some client is not a simple job, so I’m developing a software from scratch to deal with it.

It is responsible for:

Building a digital model of the physical hierarchy of sensors. Initializing the i2c communication on the Hub, and running the configuration routine on each of the sensors.
Performing a reading on each of the sensors at the specified refresh rate.
Correcting each sensor reading with the deviation obtained on a previous calibration process.
Performing a sensor fusion on the corrected sensor reading, obtaining absolute orientation information in form of a quaternion.
Sending the orientation data, together with the sensor_id and a timestamp to the client using an open protocol (such as OSC)
After several testing I discovered that using an Single Board Computer running linux was the best choice to host such a program, so all of the development of this part of the software has been done on C++, using a Raspberry Pi 3 as the hub. Some of the advantages of this type of hub, in comparison with simpler microcontrollers are:

It’s not an expensive component.
Programming and debugging is enormously simplified.
Some of them, like the rPi3, came out of the box with all the communication peripherals needed to perform a confortable capture, with the remarkable example of the Wifi adapter.


Software (Client):
Since the protocol with which the data is transmitted is clear, the client can be anything that is capable of displaying a 3D skeleton.  

Most of the time I'm using a python script running in Blender that grabs the quaternion data from OSC, and rotates the bones of a 3D armature.

The idea would be releasing a basic client in the form of a Blender add-on responsible for:

Establishing some handshake communication with the hub, checking compatibility and status.
Communicate the status to the user (the human in front of the computer).
Act as a GUI to run the on-pose calibration procedures and start the capture.
Display the preview of the capture on real time, and allow the user to register part of it.
Allow an user with a basic experience on Blender to create a custom distribution of the sensors on a virtual model of the human body, export it on an structured data format (like xml) and send it to the hub.
*For the sake of simplicity here I refer to IMU device, but to be correct I should say IMU (gyroscope and accelerometer) + magnetometer

```


##### “Mastering Motion Sensing: A Comprehensive Guide to the MPU6050 and MPU9250”

When the object goes from idle state to any velocity, to measure that non-gravitational acceleration a compact device used is accelerometer. 

1. Capacitive MEMS accelerometer:
   These type of accelerometer uses a microelectromechanical system to measure the changes in capacitance caused by the acceleration.

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/a16d1fbe-f758-4720-befa-3db88cecaeaf)


2. Piezoresistive accelerometer:
   these types of accelerometers use a strain gauge to measure the change in resistance caused by acceleration. These sensors are not the best for measuring low-frequency impacts.

(![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/baf7c3b5-06ef-4f93-ae49-6d18a3bbf385)
)

3. Piezoelectric accelerometer:
   These type of sensor uses a piezoelectric crystal to generate an electric charge proportional to acceleration. These types of accelerometers are highly effective at measuring shocks and vibrations. Piezoelectric accelerometers are better than piezoresistive accelerometers because of able to measure low-frequency impacts.

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/a38192fb-4b03-4eb3-a490-86864f5583ef)



###### Gyroscope

Gyroscope uses the principle of angular momentum, in which we detect the rotation of the object around an axis will tend to resist any change in the orientation of that axis. It is mainely used for measuring or maintaining orientation and angular velocity. It is commonly used in various applications such as navigation, robotics, aviation and electronics.
 
Aviation and aerospace: In aircraft and spacecraft gyroscopes are used to maintain orientation and stability and to control autopilot. In aircraft to help the pilot maintain orientation and stability, even in turbulent conditions.

```
Robotics: In robots' gyroscope is to provide directional cues, maintain position and navigation system. In drones Gyroscope ae used to help them maintain their orientation and stability while flying.

Consumer Electronics: In consumer electronics gyroscopes are mostly used in smartphones and other consumer electronics devices to detect orientation and movement. Gyroscopes are responsible for some smart features that are available in electronic devices such as automatic screen rotation, motion control in games, and augmented reality.
Industrial Applications: In industry Self-driving cars are popular and gyroscopes are used in self-driving cars to help them maintain their orientation and stability. This is essential for cars to be able to navigate safely and avoid obstacles.
```
Navigation: Gyroscope are used in navigation systems to track and balance and to provide directional cues. For the navigation and stabilization of large boats and satellites gyroscopes are used.

There are different types of gyroscopes, but the most common ones include

Mechanical gyroscopes: This type of gyroscope consists of a spinning wheel or disk mounted on a set of gimbals, which allows it to rotate freely in multiple axes. 

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/462c86d5-4e87-4981-b1ec-03f263331fcb)

Optical gyroscope: optical gyroscopes are used light to measure rotational motion.

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/ab98c105-9253-4321-9fd5-2720b838e286)


```
Micro-electromechanical systems (MEMS): MEMS gyroscopes are very small and lightweight gyroscopes that are made using microfabrication techniques. They use a variety of different operating principles, but they all work by measuring the Coriolis force, which is a force that acts on a moving object in a rotating reference frame. MEMS gyroscopes are relatively inexpensive and are becoming increasingly common in consumer electronics devices. However, they are not as accurate as optical gyroscopes. Which type of gyroscope is best for a particular application depends on the specific requirements of the application. For example, if the application requires high accuracy and reliability, then an optical gyroscope would be the best choice. If the application requires a small and lightweight gyroscope, then a MEMS gyroscope would be the best choice.
```

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/5b5dd750-6a3a-48d5-ba5e-7a1c82ac2e51)


##### MPU-6050
The MPU 6050 is an Inertial Measurement unit (IMU) is a 3- axis accelerometer and 3 -axis gyroscope. Additionally, this module also measures chip ambient temperature. The MPU-6050 is a very popular IMU due to its small size, low power consumption, high accuracy, and reliability. It is also very affordable, making it a good choice for a wide range of applications like Robotics, Wearable Devices, Consumer electronics, Virtual reality, Industrial automation and many more.

Accelerometer
The accelerometer in the MPU-6050 is a 3-axis MEMS accelerometer that can measure acceleration in the X, Y, and Z directions. It has a full-scale range of ±2g, ±4g, ±8g, or ±16g. The accelerometer uses a capacitive sensing element to measure acceleration. The sensing element consists of a movable mass that is suspended between two fixed plates. When the accelerometer is accelerated, the movable mass displaces, which changes the capacitance between the plates. This change in capacitance is converted to an electrical signal, which is then digitized by the MPU-6050’s ADC.

The MPU-6050 accelerometer has a number of features that make it a good choice for a wide range of applications. It is very small and lightweight, measuring just 4x4x0.9mm. It is also very low power, consuming just 3mA. The MPU-6050 accelerometer is also very accurate and reliable, with a typical acceleration error of just 2%.

Gyroscope
The gyroscope in the MPU-6050 is a 3-axis MEMS gyroscope that measures the rotational velocity of the device around the X, Y, and Z axes. It has a programmable full-scale range of ±250°/s, ±500°/s, ±1000°/s, and ±2000°/s. The output data is in the form of 16-bit digital values.


Source Google.com
MPU-6050 Pinout
Vin — this is the power pin. Since the sensor chip uses 3 VDC, we have included a voltage regulator on board that will take 3–5VDC and safely convert it down. To power the board, give it the same power as the logic level of your microcontroller — e.g. for a 5V microcontroller like Arduino, use 5V
GND — common ground for power and logic
SCL — I2C clock pin, connect to your microcontroller’s I2C clock line. This pin is level shifted so you can use 3–5V logic, and there’s a 10K pullup on this pin.
SDA -I2C data pin, connect to your microcontroller’s I2C data line. This pin is level shifted so you can use 3–5V logic, and there’s a 10K pullup on this pin.
INT -This is the interrupt pin. You can set up the MPU-6050 to pull this low when certain conditions are met such as new measurement data being available.
AD0 — I2C Address pin. Pulling this pin high or bridging the solder jumper on the back will change the I2C address from 0x68 to 0x69
FS, SCE, SDE, CLKIN — Pins for advanced users to connect the MPU-6050 to another sensor.

Source: google.com
Block Diagram


Source: google.com
MPU-6050 Key Features
Built-in I2C sensor bus which is used to provide gyroscope, accelerometer, and temperature sensor data to other devices such as microcontrollers.
Onboard pull-up resistor so we do not need to connect external pull resistors which are a requirement for the I2C bus interface.
User Programmable gyroscope and accelerometer with the help of 16-bit analog to digital converter.
1024 Byte FIFO buffer to provide data to the connected microcontroller in high speed and enters the low power mode afterwards.
Built-in temperature sensor.
How access MPU-6050 using ESP32
We have already seen the pin configuration of the MPU 6050. Now we will see how we can gather 6 axis data using ESP32 and MPU6050.

Communication between ESP32 and MPU6050 is happen using I2C protocol. It is half duplex communication protocol. In which poly two wires are involved for the exchange of the data. I2C protocol is mostly used for the short range of communication.

Serial Data (SDA) — Transfer of data takes place through this pin.
Serial Clock (SCL) — It carries the clock signal

For more information about I2C protocols you can go through my communication protocols blog.

The I2C protocol has a number of advantages, including:

It is a simple and easy-to-implement protocol.
It is a low-cost protocol, requiring only two wires to communicate.
It is a versatile protocol that can be used to communicate with a wide variety of devices.
It is a scalable protocol that can support up to 127 devices on a single bus.
Circuit Diagram

Source: google.com
Pin Connection

Programming for MPU-6050
Programming the MPU 6050 using esp32 there are two ways. In which we can use the Adafruit library and other using raw code. So, if you want to use adafruit library then I am sharing the link with in which you will find the step process.

ESP32 MPU-6050 Accelerometer and Gyroscope (Arduino) | Random Nerd Tutorials

I prefer another way which is by using the raw code. In which we will get the raw data rather than process data. On raw data you can do any data process.

#include<Wire.h>

const int MPU_ADDR = 0x68; // I2C address of the MPU-6050
int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;

void setup() {
   Serial.begin(115200);
   Wire.begin(21, 22, 100000); // sda, scl, clock speed
   Wire.beginTransmission(MPU_ADDR);
   Wire.write(0x6B);  // PWR_MGMT_1 register
   Wire.write(0);     // set to zero (wakes up the MPU−6050)
   Wire.endTransmission(true);
   Serial.println("Setup complete");
}

void loop() {
   Wire.beginTransmission(MPU_ADDR);
   Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
   Wire.endTransmission(true);
   Wire.beginTransmission(MPU_ADDR);
   Wire.requestFrom(MPU_ADDR, 14, true); // request a total of 14 registers
   AcX = Wire.read() −− 8 | Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
   AcY = Wire.read() −− 8 | Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
   AcZ = Wire.read() −− 8 | Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
   Tmp = Wire.read() −− 8 | Wire.read(); // 0x41 (TEMP_OUT_H) &  0x42 (TEMP_OUT_L)
   GyX = Wire.read() −− 8 | Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
   GyY = Wire.read() −− 8 | Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
   GyZ = Wire.read() −− 8 | Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)


   Serial.print(AcX); Serial.print(" , ");
   Serial.print(AcY); Serial.print(" , ");
   Serial.print(AcZ); Serial.print(" , ");
   Serial.print(GyX); Serial.print(" , ");
   Serial.print(GyY); Serial.print(" , ");
   Serial.print(GyZ); Serial.print("\n");
}
These code for the 6- axis data gather using MPU6050. I have done multiple operations using this code and found some interesting results.

Only with a 3-axis accelerometer will you get 1 kHz of frequency. For a single channel you will get 2.4 kHz of frequency. Above this frequency you will get the data but the data with repeated values. One more thing I would like to add, if the length of the connecting wires is above 1m then the results will be different.
Only with a 3- axis gyroscope will you get 4 kHz of frequency. For a single channel you will get 7.2kHz of frequency. Above this frequency you will get the data but the data with repeated values. One more thing I would like to add, if the length of the connecting wires is above 1m then the results will be different.
If you gather all 6-axis channel data together then the frequency you will get is 1kHz. Here also connecting wires length not more than 1 m condition is applied.
For more information you can go through the data sheet. Here I am sharing the link of the data sheet.

([MPU-6000-Datasheet1.pdf (tdk.com](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf))


Application

```
Gyroscope and Accelerometer: The MPU-6050 can be used to measure angular velocity and acceleration. It’s commonly employed in applications that require motion detection, such as gaming controllers and virtual reality devices.
```
Inertial Measurement Units (IMUs): IMUs that consist of a combination of accelerometers and gyroscopes like the MPU-6050 are used in robotics, drones, and other autonomous systems to estimate orientation, track movement, and stabilize the device.
```
Motion Tracking: The MPU-6050 can be used for motion tracking and gesture recognition in applications like wearable devices and sports activity trackers.
```
Digital Pedometers: The accelerometer in the MPU-6050 can be used to count steps and track physical activity, making it suitable for fitness and health monitoring applications.
```
Quadcopters and Drones: MPU-6050 is used in quadcopters and drones for stabilization and attitude estimation. It helps keep the aircraft level and steady during flight.
Virtual Reality (VR) and Augmented Reality (AR): MPU-6050 can be used in VR and AR headsets to track the movement of the user’s head and provide a more immersive experience.
Gesture Control: It is employed in gesture control applications, such as controlling a computer or home automation devices with hand movements.
```
Electronic Compass: By combining the accelerometer and gyroscope data, the MPU-6050 can serve as an electronic compass, providing heading and orientation information for navigation systems.
Telemetry in Sports: It is used in sports equipment, such as golf clubs and tennis rackets, to measure and analyze performance data, including swing speed and motion patterns.
Vibration Monitoring: The accelerometer in the MPU-6050 can be used to monitor and analyze vibrations in industrial machinery, vehicles, and buildings for predictive maintenance and safety purposes.
```
Human-Machine Interfaces: The MPU-6050 can be used to create innovative human-machine interfaces, enabling control of machines or devices through body movements or gestures.
Research and Development: Researchers and hobbyists use the MPU-6050 for various projects, from robotics and autonomous vehicles to experiments in physics and biomechanics.
```



####### MPU 9250
MPU-9250 is a multi-chip module (MCM) consisting of two dies integrated into a single QFN package. One die houses the 3-Axis gyroscope and the 3-Axis accelerometer. The other die houses the AK8963 3-Axis magnetometer from Asahi Kasei Microdevices Corporation. Hence, the MPU-9250 is a 9-axis Motion Tracking device that combines a 3-axis gyroscope, 3-axis accelerometer, 3-axis magnetometer and a Digital Motion Processor™ (DMP) all in a small 3x3x1mm package available as a pin-compatible upgrade from the MPU6515. 

![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/5931b036-6190-4918-aacd-61993ce461a5)


![image](https://github.com/jfUPB/bitacorassfi12024-10-LemurWater/assets/38868316/9dba1b9e-7766-41f3-84ca-ef75b540ea4e)



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

#### Micro-sesion 1 Apertura:

Voy a avanzar lo mas posible en enviar la coneccion BINARIA, un prototipo enviando desde el __micro:bit__, y recbiendo la inforamcion en el __PC__.


#### Micro-sesion 2:

El _algoritmo_ de la __maquina de estados__ estaba un poco incorrecto, lo modifique para, en ves de ser una maquina pensada para un sistema __NO__ distribuido como un juego local; pero facilmente lo modifique para esta funcionalidad quedara en un solo bloque y se le agrega un bloque de algoritmo al _principio_ para __SOLO funcionar cuando se le pide (pregunta)__, tambien para que el proceso se realize cada cierta cantidad de frames (20) envez de enviar la informacion cada ciclo.

1. ¿Cuál será el propósito de la sesión de hoy?

>  Avanzar lo mayor posible en el serializado _binario_. Ya entiendo bien el _ASCII_ y comprendo los conceptos de enviar binario en orden de _derecha a iz_ o _iz a derecha_ para saber en que __tipo__ de orden se enviaron los datos.
 
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

