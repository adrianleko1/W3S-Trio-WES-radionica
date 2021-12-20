import serial
port = serial.Serial('COM3')
from pynput.keyboard import Key, Listener
keys = ['y','x']

def on_press(key):
    keys.append(key)
    if (keys[-1] != keys[-2]):
        port.write(('p{0}'.format(key.char))
        
def on_release(key):				
    port.write(('r{0}'.format(key.char))
	if key == Key.esc:
		return False

with Listener(on_press = on_press, on_release = on_release) as listener:		
	listener.join()
