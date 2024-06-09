import subprocess

def Ping_func(IpAddress_str):
    ping_reply = subprocess.Popen(['ping', IpAddress_str, '-n', '1','-w','100'], stdout=subprocess.PIPE).stdout.read()

    if str(ping_reply).find('TTL') > 0:
        Status_str = 'OK'
    else:
        Status_str = 'NG'
        
    print(IpAddress_str + ' ' + Status_str)

i = 0
j = 0

for i in range(0,254):

	for j in range(0,254):

		
		Ping_func('192.168.' + str(i) + '.' + str(j))