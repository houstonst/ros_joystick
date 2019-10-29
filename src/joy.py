from Tkinter import *
from std_msgs.msg import String
import pygame, rospy

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
	rospy.init_node('listener', anonymous = True)
	rospy.Subscriber("joynode", String, callback)
	rospy.spin()


class Find_Joystick:
	def __init__(self, root, wndw, up, right, left, down, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt10, bt11):
		self.root = root
		self.wndw = wndw
		self.up = up
		self.right = right
		self.left = left
		self.down = down
		self.bt1 = bt1
		self.bt2 = bt2
		self.bt3 = bt3
		self.bt4 = bt4
		self.bt5 = bt5
		self.bt6 = bt6
		self.bt7 = bt7
		self.bt8 = bt8
		self.bt9 = bt9
		self.bt10 = bt10
		self.bt11 = bt11


		## initialize pygame and joystick
		pygame.init()
		if(pygame.joystick.get_count() < 1):
			# no joysticks found
			print("Please connect a joystick.\n")
			self.quit()
		else:
			# create a new joystick object from
			# ---the first joystick in the list of joysticks
			self.jStick = pygame.joystick.Joystick(0)
			# tell pygame to record joystick events
			self.jStick.init()

		## bind the event I'm defining to a callback function
		self.root.bind("<<Right>>", self.eventRight)
		self.root.bind("<<Left>>", self.eventLeft)
		self.root.bind("<<Up>>", self.eventUp)
		self.root.bind("<<Down>>", self.eventDown)

		self.root.bind("<<0Rel>>", self.rel0)
		self.root.bind("<<1Rel>>", self.rel1)

		self.root.bind("<<Button 1>>", self.butt1)
		self.root.bind("<<Button 2>>", self.butt2)
		self.root.bind("<<Button 3>>", self.butt3)
		self.root.bind("<<Button 4>>", self.butt4)
		self.root.bind("<<Button 5>>", self.butt5)
		self.root.bind("<<Button 6>>", self.butt6)
		self.root.bind("<<Button 7>>", self.butt7)
		self.root.bind("<<Button 8>>", self.butt8)
		self.root.bind("<<Button 9>>", self.butt9)
		self.root.bind("<<Button 10>>", self.butt10)
		self.root.bind("<<Button 11>>", self.butt11)

		self.root.bind("<<Button 1 Rel>>", self.butt1Rel)
		self.root.bind("<<Button 2 Rel>>", self.butt2Rel)
		self.root.bind("<<Button 3 Rel>>", self.butt3Rel)
		self.root.bind("<<Button 4 Rel>>", self.butt4Rel)
		self.root.bind("<<Button 5 Rel>>", self.butt5Rel)
		self.root.bind("<<Button 6 Rel>>", self.butt6Rel)
		self.root.bind("<<Button 7 Rel>>", self.butt7Rel)
		self.root.bind("<<Button 8 Rel>>", self.butt8Rel)
		self.root.bind("<<Button 9 Rel>>", self.butt9Rel)
		self.root.bind("<<Button 10 Rel>>", self.butt10Rel)
		self.root.bind("<<Button 11 Rel>>", self.butt11Rel)


		## start looking for events
		self.root.after(0, self.find_events)

	def find_events(self):
		## check everything in the queue of pygame events
		events = pygame.event.get()
		for event in events:
			axis0 = self.jStick.get_axis(0)
			axis1 = self.jStick.get_axis(1)
			axis2 = self.jStick.get_axis(2)

			b1 = self.jStick.get_button(0)
			b2 = self.jStick.get_button(1)
			b3 = self.jStick.get_button(2)
			b4 = self.jStick.get_button(3)
			b5 = self.jStick.get_button(4)
			b6 = self.jStick.get_button(5)
			b7 = self.jStick.get_button(6)
			b8 = self.jStick.get_button(7)
			b9 = self.jStick.get_button(8)
			b10 = self.jStick.get_button(9)
			b11 = self.jStick.get_button(10)
			print("""Axes - Axis 0: {}, Axis 1: {}, Axis 2: {},
Buttons - Trigger: {}, #2: {}, #3: {}, #4: {}, #5: {}, #6: {}, #7: {}, #8: {}, #9: {}, #10: {}, #11: {}\n"""
.format(round(axis0, 2), round(axis1, 2), round(axis2, 2), b1,b2,b3,
	b4,b5,b6,b7,b8,b9,b10,b11))
			# event type for pressing any of the joystick buttons down
			if axis0 > 0.2:
				self.root.event_generate("<<Right>>")
			if axis0 < -0.2: 
				self.root.event_generate("<<Left>>")
			if axis1 < -0.2:
				self.root.event_generate("<<Up>>")
			if axis1 > 0.2: 
				self.root.event_generate("<<Down>>")
			if axis0 > -0.2 and axis0 < 0.2:
				self.root.event_generate("<<0Rel>>")
			if axis1 > -0.2 and axis1 < 0.2: 
				self.root.event_generate("<<1Rel>>")
			if b1:
				self.root.event_generate("<<Button 1>>")
			if (b1 == 0):
				self.root.event_generate("<<Button 1 Rel>>")
			if b2:
				self.root.event_generate("<<Button 2>>")
			if (b2 == 0):
				self.root.event_generate("<<Button 2 Rel>>")  
			if b3:
				self.root.event_generate("<<Button 3>>")
			if (b3 == 0):
				self.root.event_generate("<<Button 3 Rel>>")
			if b4:
				self.root.event_generate("<<Button 4>>")
			if (b4 == 0):
				self.root.event_generate("<<Button 4 Rel>>")
			if b5:
				self.root.event_generate("<<Button 5>>")
			if (b5 == 0):
				self.root.event_generate("<<Button 5 Rel>>")
			if b6:
				self.root.event_generate("<<Button 6>>")
			if (b6 == 0):
				self.root.event_generate("<<Button 6 Rel>>")
			if b7:
				self.root.event_generate("<<Button 7>>")
			if (b7 == 0):
				self.root.event_generate("<<Button 7 Rel>>")
			if b8:
				self.root.event_generate("<<Button 8>>")
			if (b8 == 0):
				self.root.event_generate("<<Button 8 Rel>>")
			if b9:
				self.root.event_generate("<<Button 9>>")
			if (b9 == 0):
				self.root.event_generate("<<Button 9 Rel>>")
			if b10:
				self.root.event_generate("<<Button 10>>")
			if (b10 == 0):
				self.root.event_generate("<<Button 10 Rel>>")
			if b11:
				self.root.event_generate("<<Button 11>>")
			if (b11 == 0):
				self.root.event_generate("<<Button 11 Rel>>")
		self.root.after(20, self.find_events)

	def eventRight(self, event):
		self.wndw.itemconfig(self.right, fill ="red")
	def eventLeft(self, event):
		self.wndw.itemconfig(self.left, fill ="red")
	def eventUp(self, event):
		self.wndw.itemconfig(self.up, fill ="red")
	def eventDown(self, event):
		self.wndw.itemconfig(self.down, fill ="red")
	def rel1(self, event):
		self.wndw.itemconfig(self.up, fill ="white")
		self.wndw.itemconfig(self.down, fill = "white")
	def rel0(self, event):
		self.wndw.itemconfig(self.right, fill ="white")
		self.wndw.itemconfig(self.left, fill = "white")
	def butt1(self, event):
		self.wndw.itemconfig(self.bt1, fill ="red")
	def butt2(self, event):
		self.wndw.itemconfig(self.bt2, fill ="red")
	def butt3(self, event):
		self.wndw.itemconfig(self.bt3, fill ="red")
	def butt4(self, event):
		self.wndw.itemconfig(self.bt4, fill ="red")
	def butt5(self, event):
		self.wndw.itemconfig(self.bt5, fill ="red")
	def butt6(self, event):
		self.wndw.itemconfig(self.bt6, fill ="red")
	def butt7(self, event):
		self.wndw.itemconfig(self.bt7, fill ="red")
	def butt8(self, event):
		self.wndw.itemconfig(self.bt8, fill ="red")
	def butt9(self, event):
		self.wndw.itemconfig(self.bt9, fill ="red")
	def butt10(self, event):
		self.wndw.itemconfig(self.bt10, fill ="red")
	def butt11(self, event):
		self.wndw.itemconfig(self.bt11, fill ="red")

	def butt1Rel(self, event):
		self.wndw.itemconfig(self.bt1, fill ="white")
	def butt2Rel(self, event):
		self.wndw.itemconfig(self.bt2, fill ="white")
	def butt3Rel(self, event):
		self.wndw.itemconfig(self.bt3, fill ="white")
	def butt4Rel(self, event):
		self.wndw.itemconfig(self.bt4, fill ="white")
	def butt5Rel(self, event):
		self.wndw.itemconfig(self.bt5, fill ="white")
	def butt6Rel(self, event):
		self.wndw.itemconfig(self.bt6, fill ="white")
	def butt7Rel(self, event):
		self.wndw.itemconfig(self.bt7, fill ="white")
	def butt8Rel(self, event):
		self.wndw.itemconfig(self.bt8, fill ="white")
	def butt9Rel(self, event):
		self.wndw.itemconfig(self.bt9, fill ="white")
	def butt10Rel(self, event):
		self.wndw.itemconfig(self.bt10, fill ="white")
	def butt11Rel(self, event):
		self.wndw.itemconfig(self.bt11, fill ="white")


	def quit(self):
		import sys
		sys.exit()

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

	app = Find_Joystick(root, wndw, up, right, left, down, b1Fill, b2Fill, b3Fill, b4Fill, b5Fill, b6Fill, b7Fill, b8Fill, b9Fill, b10Fill, b11Fill)
	root.protocol('WM_DELETE_WINDOW', app.quit)
	root.bind('<Control-q>', app.quit)
	root.bind('<Control-Q>', app.quit)
	root.mainloop()

if __name__ == "__main__":
	main()
	listener()
