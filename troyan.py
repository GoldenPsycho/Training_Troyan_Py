import socket

from requests import get



hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

puplic_ip = get('https://api.ipify.org').text

print(f'Host: {hostname}')
print(f'Local IP: {local_ip}')
print(f'Public IP: {puplic_ip}')