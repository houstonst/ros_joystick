from Tkinter import *
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import pygame, rospy

def main():
	root = Tk()
	# Customize GUI #
	height = 800
	width = 1200
	root.title("Joystick Through ROS")
	wndw = Canvas(root,width = width, height = height)
	wndw.pack(expand = NO, fill = BOTH)
	wndw.configure(background = "black")

	down = wndw.create_oval((width/2-50, 450, width/2+50, 550), fill = "white")
	up = wndw.create_oval((width/2-50, 250, width/2+50, 350), fill = "white")
	left = wndw.create_oval((width/2-140, height/2-50, width/2-40, height/2+50), fill = "white")
	right = wndw.create_oval((width/2+50, height/2-50, width/2+150, height/2+50), fill = "white")

	##### LEFT SIDE #####
	b2Fill = wndw.create_oval((100, height/7, 175,  height/7+75), fill = "white")
	b3Fill = wndw.create_oval((100, 2*height/7, 175, 2*height/7+75), fill = "white")
	b4Fill = wndw.create_oval((100, 3*height/7, 175, 3*height/7+75), fill = "white")
	b5Fill = wndw.create_oval((100, 4*height/7, 175, 4*height/7+75), fill = "white")
	b6Fill = wndw.create_oval((100, 5*height/7, 175, 5*height/7+75), fill = "white")

	##### RIGHT SIDE #####
	b7Fill = wndw.create_oval((1000, height/7, 1075, height/7+75), fill = "white")
	b8Fill = wndw.create_oval((1000, 2*height/7, 1075, 2*height/7+75), fill = "white")
	b9Fill = wndw.create_oval((1000, 3*height/7, 1075, 3*height/7+75), fill = "white")
	b10Fill = wndw.create_oval((1000, 4*height/7, 1075, 4*height/7+75), fill = "white")
	b11Fill = wndw.create_oval((1000, 5*height/7, 1075, 5*height/7+75), fill = "white")

	##### TRIGGER #####
	b1Fill = wndw.create_oval((width/2-30, height/2-30,width/2+30,height/2+30), fill = "white")

	##### BUTTON LABELS #####
	b2Label = wndw.create_text(135, height/7 + 35, text = "Button 2", fill = "black")
	b3Label = wndw.create_text(135, 2*(height/7) + 35, text = "Button 3", fill = "black")
	b4Label = wndw.create_text(135, 3*(height/7) + 35, text = "Button 4", fill = "black")
	b5Label = wndw.create_text(135, 4*(height/7) + 35, text = "Button 5", fill = "black")
	b6Label = wndw.create_text(135, 5*(height/7) + 35, text = "Button 6", fill = "black")

	b7Label = wndw.create_text(1035, height/7 + 35, text = "Button 7", fill = "black")
	b8Label = wndw.create_text(1035, 2*(height/7) + 35, text = "Button 8", fill = "black")
	b9Label = wndw.create_text(1035, 3*(height/7) + 35, text = "Button 9", fill = "black")
	b10Label = wndw.create_text(1035, 4*(height/7) + 35, text = "Button 10", fill = "black")
	b11Label = wndw.create_text(1035, 5*(height/7) + 35, text = "Button 11", fill = "black")

	b1Label = wndw.create_text(width/2, height/2, text = "Trigger", fill = "black")

	upLabel = wndw.create_text(width/2, height/2-100, text = "Up", fill = "black")
	downLabel = wndw.create_text(width/2, height/2+100, text = "Down", fill = "black")
	leftLabel = wndw.create_text(width/2-100, height/2, text = "Left", fill = "black")
	rightLabel = wndw.create_text(width/2+100, height/2, text = "Right", fill = "black")



	def callback(data):
		### BUTTONS ###
		if data.buttons[0] == 1:
			wndw.itemconfig(b1Fill, fill = "red")
		else:
			wndw.itemconfig(b1Fill, fill = "white")

		if data.buttons[1] == 1:
			wndw.itemconfig(b2Fill, fill = "red")
		else:
			wndw.itemconfig(b2Fill, fill = "white")

		if data.buttons[2] == 1:
			wndw.itemconfig(b3Fill, fill = "red")
		else:
			wndw.itemconfig(b3Fill, fill = "white")

		if data.buttons[3] == 1:
			wndw.itemconfig(b4Fill, fill = "red")
		else:
			wndw.itemconfig(b4Fill, fill = "white")

		if data.buttons[4] == 1:
			wndw.itemconfig(b5Fill, fill = "red")
		else:
			wndw.itemconfig(b5Fill, fill = "white")

		if data.buttons[5] == 1:
			wndw.itemconfig(b6Fill, fill = "red")
		else:
			wndw.itemconfig(b6Fill, fill = "white")

		if data.buttons[6] == 1:
			wndw.itemconfig(b7Fill, fill = "red")
		else:
			wndw.itemconfig(b7Fill, fill = "white")

		if data.buttons[7] == 1:
			wndw.itemconfig(b8Fill, fill = "red")
		else:
			wndw.itemconfig(b8Fill, fill = "white")

		if data.buttons[8] == 1:
			wndw.itemconfig(b9Fill, fill = "red")
		else:
			wndw.itemconfig(b9Fill, fill = "white")

		if data.buttons[9] == 1:
			wndw.itemconfig(b10Fill, fill = "red")
		else:
			wndw.itemconfig(b10Fill, fill = "white")

		if data.buttons[10] == 1:
			wndw.itemconfig(b11Fill, fill = "red")
		else:
			wndw.itemconfig(b11Fill, fill = "white")
		###BUTTONS ###

		### AXES ###
		if data.axes[0] > 0.2:
			wndw.itemconfig(left, fill = "red")
			wndw.itemconfig(right, fill = "white")
		elif data.axes[0] < -0.2:
			wndw.itemconfig(right, fill = "red")
			wndw.itemconfig(left, fill = "white")
		else:
			wndw.itemconfig(right, fill = "white")
			wndw.itemconfig(left, fill = "white")

		if data.axes[1] > 0.2:
			wndw.itemconfig(up, fill = "red")
			wndw.itemconfig(down, fill = "white")
		elif data.axes[1] < -0.2:
			wndw.itemconfig(down, fill = "red")
			wndw.itemconfig(up, fill = "white")
		else:
			wndw.itemconfig(up, fill = "white")
			wndw.itemconfig(down, fill = "white")
		### AXES ###

	def listener():
		rospy.init_node('listener', anonymous = True)
		rospy.Subscriber("joy", Joy, callback)
		root.mainloop()


	listener()
if __name__ == "__main__":
	main()
