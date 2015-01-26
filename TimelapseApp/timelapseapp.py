import os
import subprocess
import Tkinter
import time
import pyscreenshot as screenshot

top = Tkinter.Tk()
top.title("Mith's screenshot app")
top.minsize(500,500);
delay = 1
num = 5
loop = False
curr_num = 0

def startScreenCapture():
	deleteOldFiles()
	global curr_num, loop, delay
	curr_num = 0
	loop = True
	if(is_number(delay)):
		delay = float(Input_delay.get())
	print("clicked start")


def stopScreenCapture():
	global curr_num, loop
	curr_num = 0
	loop = False
	print("clicked stop")

def main():
	global curr_num

	if loop:
		Button_quit.config(state='disabled')
		Button_startcapture.config(state='disabled')
		Button_stopcapture.config(state='normal')
		screenshot.grab_to_file('images/' + str(curr_num) + '.png')
		print(str(curr_num))
		Label_imageCount["text"] = str(curr_num)
		curr_num += 1
		time.sleep(delay)
	else:
		Button_quit.config(state='normal')
		Button_startcapture.config(state='normal')
		Button_stopcapture.config(state='disabled')

	
	top.after(100,main)

directory = 'images'


def deleteOldFiles():
	for the_file in os.listdir(directory):
		file_path = os.path.join(directory, the_file)
		try:
			os.unlink(file_path)
		except Exception, e:
			print e
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def openFolder():
	subprocess.check_call(['open', '--', directory])

Button_startcapture = Tkinter.Button(top, text="Start", command = startScreenCapture)
Button_stopcapture = Tkinter.Button(top, text="Stop", command = stopScreenCapture)
Button_quit = Tkinter.Button(top, text="Quit", command = quit)
Button_open = Tkinter.Button(top, text="Open", command = openFolder)

Input_delay = Tkinter.Entry(top)
Label_delay = Tkinter.Label(top, text = "Delay Amount")
Label_imageCount = Tkinter.Label(top, text = "0")

Label_delay.place(x = 10, y = 50) 
Label_imageCount.place(x = 90, y = 220) 

Input_delay.place(x = 130, y = 50)
Button_startcapture.place(x = 10, y = 80)
Button_stopcapture.place(x = 130, y = 80)
Button_open.place(x = 10, y = 120)
Button_quit.place(x = 130, y = 120)

top.after(100, main)
top.mainloop()
