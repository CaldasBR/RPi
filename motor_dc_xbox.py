############ FAZ AS IMPORTACOES NECESSARIAS PARA ESTE CODIGO #########
import RPi.GPIO as GPIO
import time
import math
import curses #para controlar pelo teclado

#Este passo eh necessaio para poder importar um codigo de outro diretorio
import sys
sys.path.insert(0,'/home/pi/Documents/Arquivos/Raspberry_pi/DHT11_Python/')
import dht11
sys.path.insert(0,'/home/pi/Documents/Arquivos/Raspberry_pi/Xbox/')
import xbox

########## SETUP DE PORTAS #############
GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setwarnings(False)
GPIO.cleanup()

#Configura Outputs dos motores DC
DIR_ENABLE = 11
DIR_FRENTE = 13
DIR_RE = 15
ESQ_ENABLE = 33
ESQ_FRENTE = 35
ESQ_RE = 37

GPIO.setup(DIR_ENABLE, GPIO.OUT)
GPIO.setup(DIR_FRENTE, GPIO.OUT)
GPIO.setup(DIR_RE, GPIO.OUT)
GPIO.setup(ESQ_ENABLE, GPIO.OUT)
GPIO.setup(ESQ_FRENTE, GPIO.OUT)
GPIO.setup(ESQ_RE, GPIO.OUT)

#Configura Inputs do sensor de temperatura e humidade DHT11
sensor_dht11 = dht11.DHT11(pin = 29)

#Configura Outputs do Buzzer
buzzer = 12

GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,0)

####################### FUNCOES QUE CONTROLAM OS MOTORES DO CARRINHO ###############################
def sleep_para_andar():
    time.sleep(0.01) #I need the timesleep because if not the robot will get a -1 all the time

def fn_frente_soh_esq():
    GPIO.output(ESQ_FRENTE,1)
    GPIO.output(DIR_FRENTE,0)
    sleep_para_andar()

def fn_frente_soh_dir():
    GPIO.output(ESQ_FRENTE,0)
    GPIO.output(DIR_FRENTE,1)
    sleep_para_andar()

def fn_frente_all(sinal):
    GPIO.output(ESQ_FRENTE,sinal)
    GPIO.output(DIR_FRENTE,sinal)
    sleep_para_andar()

def fn_re_soh_esq():
    GPIO.output(ESQ_RE,1)
    GPIO.output(DIR_RE,0)
    sleep_para_andar()

def fn_re_soh_dir():
    GPIO.output(ESQ_RE,0)
    GPIO.output(DIR_RE,1)
    sleep_para_andar()

def fn_re_all(sinal):
    GPIO.output(ESQ_RE,sinal)
    GPIO.output(DIR_RE,sinal)
    sleep_para_andar()

def fn_stop_all():
    GPIO.output(ESQ_FRENTE,0)
    GPIO.output(ESQ_RE,0)
    GPIO.output(DIR_FRENTE,0)
    GPIO.output(DIR_RE,0)

############## FUNCOES DO SENSOR DE TEMPERATURA E HUMIDADE DHT11 ##############
def le_dht11():
    result_dht11 = sensor_dht11.read()
    if result_dht11.is_valid():
        print("Temperatura: %d C" % result_dht11.temperature)
        print("Humidade: %d %%" % result_dht11.humidity)
    else:
        print("Error: %d" % result_dht11.error_code)

############### FUNCOES DO BUZZER #################
def tocaBuzzer(repeticoes,delay):
    for _ in xrange(repeticoes):
        for value in [True, False]:
            GPIO.output(buzzer, value)
            time.sleep(delay)

############## PROGRAMA BASE DE EXECUCAO, ONDE AQUI SERA CHAMADO TODAS AS FUNCOES #################
if __name__ == '__main__':
    joy = xbox.Joystick()

    #Definido estados dos motores
    GPIO.output(ESQ_ENABLE,1)
    GPIO.output(DIR_ENABLE,1)


    while True:
    	ativa_frente = 0
    	ativa_re = 0
	soh_esq = 0
	soh_dir = 0

	#Bloco para ler controle
	if joy.connected():
            if joy.leftBumper():
		ativa_re = 1
            if joy.rightBumper():
		ativa_frente = 1
            if joy.dpadRight():
		soh_esq = 1
            if joy.dpadLeft():
		soh_dir = 1
            if joy.A():
                le_dht11()
            if joy.Y():
                tocaBuzzer(10,0.01)
                time.sleep(0.1)
                tocaBuzzer(10,0.01)
                time.sleep(0.5)

	#Bloco para ler teclado
	stdscr = curses.initscr()
	curses.cbreak()
	stdscr.keypad(1)

	stdscr.addstr(0,1,"Pressione 'x' para finalizar o programa: ")
	stdscr.nodelay(1) #nodelay(1) give us a -1 back when nothing is pressed
        tecla = ' '
	tecla = stdscr.getch() #Gets the key which is pressed
	stdscr.addch(20,25,tecla)
	if tecla != ' ':
   	    stdscr.refresh()
	    if tecla == ord('e'):
	        fn_stop_all()
	    if tecla == ord('a'):
	        soh_esq = 1
	    if tecla == ord('s'):
	        ativa_re = 1
	    if tecla == ord('d'):
	        soh_dir = 1
	    if tecla == ord('w'):
	        ativa_frente = 1
	    #if tecla == int('-1'):
	    #    fn_stop_all()
	    if tecla == ord('x'):
	        print "Programa finalizado"
	        break

	#Bloco para decidir qual motor ligar
        if ativa_frente == 1:
            if soh_esq == 1:
                fn_frente_soh_esq()
            else:
                if soh_dir == 1:
                    fn_frente_soh_dir()
                else:
                    fn_frente_all(1)
	else:
            fn_frente_all(0)

        if ativa_re == 1:
            if soh_esq == 1:
                fn_re_soh_esq()
            else:
                if soh_dir == 1:
                    fn_re_soh_dir()
                else:
                    fn_re_all(1)
	else:
            fn_re_all(0)

    fn_stop_all()

#Importante para voltar a tela ao normal quando o script acabar
curses.nocbreak()
stdscr.keypad(0)
curses.endwin()

#IMportante para encerrar as conexoes e resetar o GPIO
joy.close()
GPIO.cleanup()
