#--------------------------------------------------------------------------
#------- TOP RACER --------------------------------------------------------
#------- Por: Manuela Restrepo  manuela.restrepoc@udea.edu.co -------------
#-------      CC 1152704892, Tel 3194707181,  Wpp 3194707181  -------------
#-------      David Vargas Bonett  odavid.vargas@udea.edu.co  -------------
#-------      CC 1036685469, Tel 3122505311,  Wpp 3122505311  -------------
#------- Curso Básico de Procesamiento de Imágenes y Visión Artificial-----
#------- V1 Octubre de 2020------------------------------------------------
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#--1. Importando las librerias  -------------------------------------------
#--------------------------------------------------------------------------

import pygame          #importamos la libreria de juegos de python
import time            #libreria de tiempo de python
import random        #modulo de funciones de generacion de valores aleatorios
import cv2 as cv    #Opencv-python

#--------------------------------------------------------------------------
#-- 2. Definición de Variables Globales del juego   -----------------------
#--------------------------------------------------------------------------

#----  Pygame Window  -----------------------------------------------------
pygame.init()                                                              #Iniciamos Pygame
display_width = 640                                                        #Definimos el ancho de la ventana de pygame
display_height = 480                                                    #Definimos el alto de la ventana de pygame
gameDisplay = pygame.display.set_mode((display_width,display_height))   #Inicializamos la ventana del juego
pygame.display.set_caption("Top Racer")     #Nombre del Juego en pantalla

#----  Colors  ------------------------------------------------------------
black = (0,0,0)         #Definimos el color negro en una tupla RGB
white = (255,255,255)   #Definimos el color blanco en una tupla RGB
green = (0,255,0)       #Definimos el color verde en una tupla RGB
red = (255,0,0)         #Definimos el color rojo en una tupla RGB
blue = (171, 187, 148)  #Definimos el color Verde oscuro en una tupla RGB

#----  Tamaño de los carros en el juego -----------------------------------
car_width = 50          #Ancho del carro
car_height = 100        #Alto del carro

#----  Cargamos la musica, background y los sprites del juego  ------------
pygame.mixer.music.load("soundtrack.mp3")           #Musica del juego
bg_img = pygame.image.load("retro1.png")            #Imagen background de la introducción
bg_img_sc = pygame.transform.scale(bg_img,(640,480))#Imagen de fondo escalada 
carImg = pygame.image.load("car1.png")              #Imagen del carro del jugador
car2Img = pygame.image.load("car2.png")             #Imagen del carro del NPC
bgImg = pygame.image.load("road.jpg")               #Imagen del Background del juego
crash_img = pygame.image.load("explossion.png")     #Imagen del choque del carro

clock = pygame.time.Clock()                     #tiempo

#--------------------------------------------------------------------------
#-- 3. Definición de funciones del juego   --------------------------------
#--------------------------------------------------------------------------

#---- Funcion de Intro  ---------------------------------------------------
def intro():
    
    #--- Definición de variables de la funcion
    intro = True       #Booleano para el ciclo while
    menu1_x = 80       #posición en x del menu de start
    menu1_y = 250      #posición en y del menu de start
    menu2_x = 400      #posición en x del menu exit
    menu2_y = 250      #posición en y del menu exit
    menu_width = 150   #Ancho de los menu
    menu_height = 50   #alto de los menu
    
    #--- Inicio del loop de Intro
    while intro:
        
        #--- Cada vez que ocurre un evento pygame
        for event in pygame.event.get():      #recorre los eventos pygame
            if event.type == pygame.QUIT:     #Si ocurre el evento quit    
                pygame.quit()                 #Cierre pygame
                quit()                        #Elimine las ventanas  
                
          
        pygame.display.set_icon(carImg)     #Agrega el icono a la ventana de intro
        gameDisplay.blit(bg_img_sc,(0,0))   #Agrega la imagen de fondo a la pantalla de carga

        pygame.draw.rect(gameDisplay,black,(105,250,100,50))  #dibuja un rectangulo negro
        pygame.draw.rect(gameDisplay,black,(425,250,100,50))  #dibuja un rectangulo negro
       
        message_display("TOP RACER",50,display_width/2,display_height/4)  #coloca el nombre del juego en el centro de la vantana 
        
        pygame.draw.rect(gameDisplay,blue,(105,250,100,50)) #Coloca un rectangulo verde oscuro para el menu1
        pygame.draw.rect(gameDisplay,blue,(425,250,100,50)) #Coloca un rectangulo verde oscuro para el menu2
        
        #--- Se determina la posición del mouse y se determina el evento click
        mouse = pygame.mouse.get_pos()        #Obtiene la posición (x,y) del cursor
        click = pygame.mouse.get_pressed()    #Determina si se hizo click

        
        #--- Elecciones del usuario
        if menu1_x < mouse[0] < menu1_x+menu_width and menu1_y < mouse[1] < menu1_y+menu_height: #Si la posición del mause se encuentra en el recuadro de menu1
            pygame.draw.rect(gameDisplay,green,(105,250,100,50))                                 #Dibuja el Recuadro Verde para indicar que el mause esta en esa posición
            if click[0] == 1:                                                                    #Si realizo click sobre el recuadro
                intro = False                                                                    #Coloque Intro en False para terminar el intro del juego   
        if menu2_x < mouse[0] < menu2_x+menu_width and menu2_y < mouse[1] < menu2_y+menu_height: #Si la posición del mause se encuentra en el recuadro de menu2
            pygame.draw.rect(gameDisplay,red,(425,250,100,50))                                   #Dibuja el Recuadro Rojo para indicar que el mause esta en esa posición
            if click[0] == 1:                                                                    #Si realizo click sobre el recuadro        
                pygame.quit()                                                                    #Cierre pygame       
                quit()                                                                           #quite las ventanas   
        
        #--- Coloca un mensaje sobre las Casillas de los rectangulos del menu
        message_display("START",20,menu1_x+menu_width/2,menu1_y+menu_height/2)
        message_display("EXIT",20,menu2_x+menu_width/2,menu2_y+menu_height/2)
        
        #--- Actualiza la ventana
        pygame.display.update()
        clock.tick(50)

#---- Funcion de puntuacion  ---------------------------------------------
def highscore(count):                       #recibe una puntuacion y la dibuja en pantalla
    
    font = pygame.font.SysFont("Calibri",35)               #Se define un objeto de la clase font
    text = font.render("Score : "+str(count),True,white)   #Se agrega el valor de la puntuación al objeto
    gameDisplay.blit(text,(0,0))                           #Se agrega la puntuación a la ventana

#---- Funcion Para dibujar en pantalla  ----------------------------------
def draw_things(thingx,thingy,thing):       #Recibe el sprite y la posición en x y y, donde se va dibujar

    gameDisplay.blit(thing,(thingx,thingy)) #Dibuja el sprite en la posicion correspondiente

#---- Funcion Para dibujar en pantalla el carro del jugador  -------------
def car(x,y):                               #Recibe la posición del jugador

    gameDisplay.blit(carImg,(x,y))  #Dibuja en pantalla el carro del jugador

#---- Funcion Crear una superficie de tipo texto renderizado -------------
def text_objects(text,font):                #recibe el texto y el obejto tipo fuente
    
    textSurface = font.render(text,True,black) #Crea una nueva superficie con el texto especificado
    return textSurface,textSurface.get_rect()  # retorna la superficie y el area rectangular de la misma

#---- Funcion para escribir un mensaje en pantalla  ----------------------
def message_display(text,size,x,y):         #Recibe el texto, el tamaño y el lugar donde se debe colocar
    
    font = pygame.font.SysFont("Haettenschweiler", size, italic=1) #crea una fuente 
    text_surface , text_rectangle = text_objects(text,font)        #utiliza la funcion text_objects para obtener el texto renderizado y su area
    text_rectangle.center =(x,y)                                   #Coloca el cuadro de texto en la posición especificada
    gameDisplay.blit(text_surface,text_rectangle)                  #Dibuja el mensaje en pantalla

#---- Funcion para cuando el carro choca  -------------------------------
def crash(x,y):                             #Recibe la posición donde ocurrio el choque
    
    gameDisplay.blit(crash_img,(x,y))                                      #Dibuja el choque en pantalla
    message_display("YOU CRASHED",40,display_width/2,display_height/2)     #Coloca el mensaje de choque en el centro de la pantalla de juego
    pygame.display.update()                                                #Actualiza la imagen
    time.sleep(2)                                                          #Coloca el juego en espera  2 segundos
    gameloop()                                                             #Reinicia el juego despues del choque

#---- Funcion para jugar forever and ever  ------------------------------
def gameloop():
    
    pygame.mixer.music.play(-1)                                             #Inicio la música del juego
    bg_x1 = (display_width/2)-(360/2)                                       #posición en x de la carretera en pantalla
    bg_x2 = (display_width/2)-(360/2)                                       #posición final de x de la carretera en pantalla 
    bg_y1 = 0                                                               #posición inical en y de la carretera
    bg_y2 = -600                                                            #Posición final en y de la carretera
    bg_speed = 10                                                           #Velocidad de la carretera para dar sensación de movimiento
    car_x = ((display_width / 2) - (car_width / 2))                         #Posición inicial en x del carro del jugador
    car_y = (display_height - car_height)                                   #Posición inicial en y del carro del jugador
    #car_x_change = 0                                                        #Cambio a realzizar en la posición de x solo cuando se juega con teclado
    road_start_x =  (display_width/2)-112                                   #limites de la carretera
    road_end_x = (display_width/2)+112                                      #limites de la carretera

    thing_startx = random.randrange(road_start_x,road_end_x-car_width)      #Genera una posición aleatoria en x para el carro del npc
    thing_starty = -600                                                     #Posición en y donde se coloca el carro del Npc
    thingw = 50                                                             #ancho del carro del npc
    thingh = 100                                                            #alto del carro del npc
    thing_speed = 20                                                        #Cambio de velocidad
    count=0                                                                 #Contador de puntos
    gameExit = False                                                        #Bandera para el ciclo while de juego

    while not gameExit:
        
        #Captura de Imagen y procesado digital
        cap= cv.VideoCapture(0)                                         #captura de video
        fourcc = cv.VideoWriter_fourcc(*'XVID')                         # Define the codec and create VideoWriter object
        out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))   #definimos el tamaño de la imagen en 640x480 y guardamo el video

        while cap.isOpened():
            
            ret, frame = cap.read()                                     #Leemos las imagenes de la camara
            if not ret:                                                 #determina si se logro tomar imagen
                print("Can't receive frame (stream end?). Exiting ...")
                break                                                   #en caso de que no termina el juego
                
            img_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)                          #Pasamos la imagen al espacio de color HSV
            _, mask_hsv = cv.threshold(img_hsv[:,:,1], 150, 255, cv.THRESH_BINARY)  #deinimos una mascara binaria para la capa se saturación
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (19,19))            #obtenemos la funcion o kernel que describe la mascara    
            opened = cv.morphologyEx(mask_hsv, cv.MORPH_OPEN, kernel)               #aplicamos el filtro de eroción y dilatación
            
            cX = car_x  #posicion del centro de masa se iguala al del carro

            try:
                contours, hierarchy = cv.findContours(opened, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) #Se extraen los contornos de la mascara de la imagen
                contours = sorted(contours, key=cv.contourArea,reverse=True)                          
                con=cv.drawContours(frame,contours,-1,(102,5,192),4)                                  #Se dibujan los contornos de la mascara en la imagen original  

                M = cv.moments(contours[0])                 #Extraemos el momento de la imagen utilizando los contornos
                cX = abs(480 - int(M["m10"] / M["m00"]))    #Centro de masa de la imagen en x, conversion para abjustar a la pantalla de pygame
                #cY = int(M["m01"] / M["m00"])               #Centro de masa de la imagen en y

                # write the flipped frame
                frame = cv.flip(con, 1)     #Adecua la imagen para mostrarla                 
                out.write(frame)            #Guarda el video        
                cv.imshow('frame', frame)   #Muestra en tiempo real la imagen captada

            except:
                #En caso de que no se detecte el contorno
                print("Se pérdio el contorno")
                frame = cv.flip(frame, 1)    #Adecua la imagen para mostrarla 
                out.write(frame)             #Guarda el video
                cv.imshow('frame', frame)    #Muestra en tiempo real la imagen captada

            for event in pygame.event.get():     #Recorre los eventos de pygame
                
                if event.type == pygame.QUIT:    #Evento de cerrado de ventana de juego
                
                    gameExit = True              #termina el juego   
                    cap.release()                #Cierra la captura de imagen
                    out.release()                #Deja de escribir el archivo de grabación   
                    cv.destroyAllWindows()       #Destruye la ventana de cv inshow   
                    pygame.quit()                #Destruye pygame 
                    quit()                       #quita todo   


                if event.type == pygame.KEYDOWN:    #Evento de presion de tecla
                    if event.key == pygame.K_SPACE: #Tecla presionada barra espaciadora
                    
                         gameExit = True              #termina el juego   
                         cap.release()                #Cierra la captura de imagen
                         out.release()                #Deja de escribir el archivo de grabación   
                         cv.destroyAllWindows()       #Destruye la ventana de cv inshow   
                         pygame.quit()                #Destruye pygame 
                         quit()                       #quita todo  

               #Para jugar con teclado UwU                    
                    # if event.key == pygame.K_LEFT:
                    #     car_x_change = -5
                    # elif event.key == pygame.K_RIGHT:
                    #     car_x_change = 5


                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #         car_x_change = 0

            
            car_x = cX  #Asigna la posición de masa de la imagen a la del carro
            
            #Determina si el carro salio de los limites
            if car_x > road_end_x-car_width:
                crash(car_x,car_y)
            if car_x < road_start_x:
                crash(car_x-car_width,car_y)

            #determina si el carro choco con el carro del npc
            if car_y < thing_starty + thingh:
                if car_x >= thing_startx and car_x <= thing_startx+thingw:
                    crash(car_x-25,car_y-car_height/2)
                if car_x+car_width >= thing_startx and car_x+car_width <= thing_startx+thingw:
                    crash(car_x,car_y-car_height/2)



            gameDisplay.fill(blue)    #Coloca el backgrounde color verde oscuro

            gameDisplay.blit(bgImg,(bg_x1,bg_y1))           #Dibuja la carretera
            gameDisplay.blit(bgImg,(bg_x2,bg_y2))           #Dibuja la carretera
            car(car_x,car_y)                                #display car
            draw_things(thing_startx,thing_starty,car2Img)  #Dibuja el carro del npc
            highscore(count)                                #Muestra la puntuación en la imagen
            count+=1                                        #Aumenta el highscore
            thing_starty += thing_speed

            if thing_starty > display_height:               #Determina si el carro del npc salio de pantalla
                thing_startx = random.randrange(road_start_x,road_end_x-car_width)  #Genera una nueva posición en x para el npc
                thing_starty = -200

            bg_y1 += bg_speed
            bg_y2 += bg_speed

            if bg_y1 >= display_height:
                bg_y1 = -600

            if bg_y2 >= display_height:
                bg_y2 = -600



            pygame.display.update() # update the screen
            clock.tick(200)         # frame per sec
        break
    
    cap.release()                #Cierra la captura de imagen
    out.release()                #Deja de escribir el archivo de grabación   
    cv.destroyAllWindows()       #Destruye la ventana de cv inshow   
    pygame.quit()                #Destruye pygame 
    quit()                       #quita todo 

#--------------------------------------------------------------------------
#-- 3.Definición de funciones del juego   ---------------------------------
#--------------------------------------------------------------------------

intro()         #Inicia la ventana de introducción 
gameloop()      #Jugando

#--------------------------------------------------------------------------
#---------------------------  FIN DEL PROGRAMA ----------------------------
#--------------------------------------------------------------------------
