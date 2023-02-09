#Tutorial from https://www.youngwonks.com/blog/Remote-Controlled-Robot-Car-using-Raspberry-Pi

#PASO 1
#Importar los módulos
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import pygame, sys
from pygame.locals import *
pygame.init()

#PASO 2
#Crear pantalla pygame
SCREEN_SIZE = (500,500)
screen = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption('Robot Auto con Raspberry')

#PASO 3
#Elegir pins de la Raspberry

#Rueda izquierda
left_wheel_pin_1 = 22
left_wheel_pin_2 = 23

#Rueda derecha
right_wheel_pin_3 = 24
right_wheel_pin_4 = 25

#PASO 4
#Configurar pins
GPIO.setup(
   [left_wheel_pin_1,
   left_wheel_pin_2,
   right_wheel_pin_3,
   right_wheel_pin_4], GPIO.OUT
)

#PASO 5
#Crear variables de dirección
forward = False
reverse = False
turn_left = False
turn_right = False

#PASO 6
#Código mínimo requerido por pygame

#bucle principal de pygame
while True

    #Chequear evento
    for event in pygame.event.get():

        #Ventana cerrar evento
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        #PASO 7
        #Apretar tecla: Evento
        if event.type == KEYDOWN:
    
            #Adelante
            if event.key == K_w:
            forward = True

            #Retroceder
            if event.key == K_s:
            reverse = True
    
            #Izquierda
            if event.key == K_a:
            turn_left = True

            #Derecha
            if event.key == K_d:
            turn_right = True
        
        #PASO 8
        #Liberar tecla: Evento
        if event.type == KEYUP:
            forward = reverse = turn_left = turn_right = False
            GPIO.output(
                [left_wheel_pin_1,
                left_wheel_pin_2,
                right_wheel_pin_3,
                right_wheel_pin_4], GPIO.LOW
            )

    #PASO 9
    #Qué hacemos si ninguna variable de dirección
    #está puesta como verdadero (True)

    #Mover adelante
    if forward:
        GPIO.output([left_wheel_pin_1, right_wheel_pin_4], GPIO.LOW)
        GPIO.output([left_wheel_pin_2, right_wheel_pin_3], GPIO.HIGH)

    #Mover atrás
    if reverse:
        GPIO.output([left_wheel_pin_1, right_wheel_pin_4], GPIO.HIGH)
        GPIO.output([left_wheel_pin_2, right_wheel_pin_3], GPIO.LOW)
    
    #PASO 10

    #Mover izquierda
    if turn_left:
        GPIO.output([left_wheel_pin_1, left_wheel_pin_2, right_wheel_pin_4], GPIO.LOW)
        GPIO.output([right_wheel_pin_3], GPIO.HIGH)

    #Mover derecha
    if turn_right:
        GPIO.output([left_wheel_pin_1, right_wheel_pin_3, right_wheel_pin_4], GPIO.LOW)
        GPIO.output([left_wheel_pin_2], GPIO.HIGH)
    
    #Actualizar pantalla
    pygame.display.update()