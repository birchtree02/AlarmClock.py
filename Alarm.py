# alarm

from time import gmtime, strftime

def alarm():
	while True:
		if strftime("%H:%M", gmtime()) == alarmtime:
			print('wake up')
			print('\007')
			break

alarmtime = input('When would you like to be woken up? (hh:mm)
alarm()