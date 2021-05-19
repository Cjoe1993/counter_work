from dearpygui import core
from dearpygui.core import *
from dearpygui.simple import *
from datetime import datetime
import sys
import os
import keyboard
from pathlib import Path

"""
Created by https://github.com/Cjoe1993
Sound menu disabled
"""

###################################################################
#Load data, create files
# t1, t2, qc tickets
if not os.path.exists('t1_ticket.txt'):
	Path('t1_ticket.txt').touch()
	with open('t1_ticket.txt', 'w') as t:
		string = '0'
		t.write(string)
	with open('t1_ticket.txt', 'r') as r:
		line = r.readlines()
		t1 = int(line[0].rstrip())
else:
	with open('t1_ticket.txt') as checker:
		reading = checker.readlines()
		for line in reading:
			t1=int(line.rstrip())

if not os.path.exists('t2_ticket.txt'):
	Path('t2_ticket.txt').touch()
	with open('t2_ticket.txt', 'w') as t:
		string = '0'
		t.write(string)
	with open('t2_ticket.txt', 'r') as r:
		line = r.readlines()
		t2 = int(line[0].rstrip())
else:
	with open('t2_ticket.txt') as checker:
		reading = checker.readlines()
		for line in reading:
			t2=int(line.rstrip())

if not os.path.exists('qc_ticket.txt'):
	Path('qc_ticket.txt').touch()
	with open('qc_ticket.txt', 'w') as t:
		string = '0'
		t.write(string)
	with open('qc_ticket.txt', 'r') as r:
		line = r.readlines()
		qc = int(line[0].rstrip())
else:
	with open('qc_ticket.txt') as checker:
		reading = checker.readlines()
		for line in reading:
			qc=int(line.rstrip())



# Totalus
if not os.path.exists('totalus.txt'):
	Path('totalus.txt').touch()
	with open('totalus.txt', 'w') as tot:
		string = '0'
		tot.write(string)
	totalus = 0
else:
	with open('totalus.txt') as history:
		reading = history.readlines()
		for line in reading:
			totalus=int(line.rstrip())


# hotkeys
if not os.path.exists('hotkeys.txt'):
	Path('hotkeys.txt').touch()
	hold_binding = 'Nil'
	t1_binding = 'Nil'
	t2_binding = 'Nil'
	qc_binding = 'Nil'
	with open('hotkeys.txt', 'w') as hot:
		string = '0\n0\n0\n0'.rstrip()
		hot.write(string)

else:
	with open('hotkeys.txt') as hotkey:
		reading = hotkey.readlines()
		if '0' in reading[0]:
			hold_binding = 'Nil'
		if '1' in reading[0]:
			hold_binding = 'shift'
		if '2' in reading[0]:
			hold_binding = 'ctrl'
		if '3' in reading[0]:
			hold_binding = 'alt'
		
		if '0' in reading[1]:
			t1_binding = 'Nil'
		else:
		# elif '0' not in reading[1]:
			t1_binding = reading[1].rstrip('\n')
		if '0' in reading[2]:
			t2_binding = 'Nil'
		else:
			t2_binding = reading[2].strip('\n')
		if '0' in reading[3]:
			qc_binding = 'Nil'
		else:
			qc_binding = reading[3].strip('\n')


# month file
month = datetime.now().strftime('%B')
if not os.path.exists(month):
	os.mkdir(month)
	Path(f'{month}/week_1.txt').touch()
	Path(f'{month}/week_2.txt').touch()
	Path(f'{month}/week_3.txt').touch()
	Path(f'{month}/week_4.txt').touch()
	Path(f'{month}/week_5.txt').touch()
	files = ['week_1.txt','week_2.txt','week_3.txt','week_4.txt','week_5.txt']
	for file in files:
		with open(f'{month}/{file}', 'w')as f:
			string = "Monday 0\nTuesday 0\nWednesday 0\nThursday 0\nFriday 0\nSaturday 0\nSunday 0"
			f.write(string)
	print('Please restart app to load proper chart data')


def t1_tick():
	global t1, total
	# if sound_mp3 != None:
	# 	play(sound_mp3)
	delete_item(f'T1 tickets: {str(t1)}')
	delete_item(f'Total: {str(total)}')
	t1 += 1
	total += 1
	add_text(f'T1 tickets: {str(t1)}', before=' \n\n')
	add_text(f'Total: {str(total)}', before='                                ', color=[255,215,0])
	with open('t1_ticket.txt', 'w') as f:
		f.write(str(t1))

def t2_tick():
	global t2, total
	# if sound_mp3 != None:
	# 	play(sound_mp3)
	delete_item(f'T2 tickets: {str(t2)}')
	delete_item(f'Total: {str(total)}')
	t2 += 1
	total += 2
	add_text(f'T2 tickets: {str(t2)}', before='   \n\n')
	add_text(f'Total: {str(total)}', before='                                ', color=[255,215,0])
	with open('t2_ticket.txt', 'w') as f:
		f.write(str(t2))

def qc_tick():
	global qc, total
	# if sound_mp3 != None:
		# play(sound_mp3)
	delete_item(f'Total: {str(total)}')
	delete_item(f'QC tickets: {str(qc)}')
	qc += 1
	total += 1
	add_text(f'QC tickets: {str(qc)}', before='     \n\n')
	add_text(f'Total: {str(total)}', before='                                ', color=[255,215,0])
	with open('qc_ticket.txt', 'w') as f:
		f.write(str(qc))

# add hotkey
if hold_binding != 'Nil' and t1_binding != 'Nil':
	keyboard.add_hotkey(f'{hold_binding}+{t1_binding}', t1_tick)
elif hold_binding == 'Nil' and t1_binding != 'Nil':
	keyboard.add_hotkey(t1_binding, t1_tick)
else:
	pass

if hold_binding != 'Nil' and t2_binding != 'Nil':
	keyboard.add_hotkey(f'{hold_binding}+{t2_binding}', t2_tick)
elif hold_binding == 'Nil' and t2_binding != 'Nil':
	keyboard.add_hotkey(t2_binding, t2_tick)
else:
	pass

if hold_binding != 'Nil' and qc_binding != 'Nil':
	keyboard.add_hotkey(f'{hold_binding}+{qc_binding}', qc_tick)
elif hold_binding == 'Nil' and qc_binding != 'Nil':
	keyboard.add_hotkey(qc_binding, qc_tick)
else:
	pass



#######################################
# ticket values

a=t1
b=t2*2
c=qc
total = int(a+b+c)

#######################################
# Save function

month = datetime.now().strftime('%B')
date_numeric = datetime.now().strftime('%d')


# Assigning correct file to open based on day of month

if int(date_numeric) <= 7:

	current_week = 'week_1.txt'

elif int(date_numeric) >= 8 and int(datetime.now().strftime('%d')) <= 14:
				
	current_week = 'week_2.txt'

elif int(date_numeric) >= 15 and int(datetime.now().strftime('%d')) <= 21:

	current_week = 'week_3.txt'

elif int(date_numeric) >= 22 and int(datetime.now().strftime('%d')) <= 28:

	current_week = 'week_4.txt'

else:

	current_week = 'week_5.txt'

def disableCheckBox():
	# Delete checkboxes and replace so user cannot select multiple sounds
	group = ['Click##','Splat##','Zombie##']
	masterBox = 'None##'
	for checkbox in group:
		if get_value(masterBox) == 1 and get_value(checkbox) != 0:
			delete_item(checkbox)
			if checkbox == group[0]:
				add_checkbox(checkbox,
					before='			')
			if checkbox == group[1]:
				add_checkbox(checkbox,
					before='				')
			if checkbox == group[2]:
				add_checkbox(checkbox,
					before='					')


def save():
	"""

	'%B' == Month
	'%d' == 15
	'%A' == Day

	"""

	save_format = """
Monday 0
Tuesday 0
Wednesday 0
Thursday 0
Friday 0
Saturday 0
Sunday 0
  """

	day = datetime.now().strftime('%A')

	

	# Assigning an integer that can be used as list indices

	if day == 'Monday':
		day_value = 0
	elif day == 'Tuesday':
		day_value = 1
	elif day == 'Wednesday':
		day_value = 2
	elif day == 'Thursday':
		day_value = 3
	elif day == 'Friday':
		day_value = 4
	elif day == 'Saturday':
		day_value = 5
	else: 
		day_value = 6

	# Rewriting text file with saved data	

	new_document = ''

	with open(f'{month}/{current_week}', 'r') as f:
		lines = f.readlines()

	with open(f'{month}/{current_week}', 'w') as f:
		lines[day_value] = f'{day} {total}\n'
		for line in lines:
			new_document+=line
		f.write(str(new_document))

def reinit_hotkeys():
	# reinitialize hotkeys if language pack interupts them
	keyboard.unhook_all_hotkeys()
	if hold_binding != 'Nil' and t1_binding != 'Nil':
		keyboard.add_hotkey(f'{hold_binding}+{t1_binding}', t1_tick)
	elif hold_binding == 'Nil' and t1_binding != 'Nil':
		keyboard.add_hotkey(t1_binding, t1_tick)
	else:
		pass

	if hold_binding != 'Nil' and t2_binding != 'Nil':
		keyboard.add_hotkey(f'{hold_binding}+{t2_binding}', t2_tick)
	elif hold_binding == 'Nil' and t2_binding != 'Nil':
		keyboard.add_hotkey(t2_binding, t2_tick)
	else:
		pass

	if hold_binding != 'Nil' and qc_binding != 'Nil':
		keyboard.add_hotkey(f'{hold_binding}+{qc_binding}', qc_tick)
	elif hold_binding == 'Nil' and qc_binding != 'Nil':
		keyboard.add_hotkey(qc_binding, qc_tick)
	else:
		pass

		
class ConstructGui:

	def __init__(self, width, height):
		self.width = width
		self.height = height


	def builder(self):
		set_main_window_title('Ticket Counter')
		set_main_window_size(self.width,self.height)
		set_theme('Classic')
		LoginScreen()

	@staticmethod
	def run_app():
		start_dearpygui(primary_window='Jake counter')


class Tab:
	def __init__(self, tab_name, parent):
		self.tab_name = tab_name
		self.parent = parent

	def generate(self, yes):

		add_tab(name=self.tab_name, parent=self.parent, show=yes)

class Column:
	def __init__(self, table,name,column):
		self.table = table
		self.name = name
		self.column = column

	def generate(self):
		add_column(table=self.table,name=self.name,column=self.column)


class LoginScreen:

	def __init__(self):
		set_render_callback(self.auto_center)
		#this is to remove style borders, padding and spacings from the main window which mess up spacing calculation
		set_item_style_var('Jake counter', mvGuiStyleVar_WindowPadding, [0,0])
		set_item_style_var('Jake counter', mvGuiStyleVar_ItemSpacing, [0,0])
		set_item_style_var('Jake counter', mvGuiStyleVar_ItemInnerSpacing, [0,0])
		set_item_style_var('Jake counter', mvGuiStyleVar_WindowBorderSize, [0])
		self.t2_counter = 0


	def auto_center(self, sender, data):
		#getting the window sizes
		main_width = get_item_width('Jake counter')
		main_height = get_item_height('Jake counter')


	def theme_setting(sender, data):
		set_theme(data)	

	def save_hotkey(sender, data):


		
		"""
		Save values of radio buttons to text file. get_value() returns index number
		data[0] = hold
		data[1] = t1
		data[2] = t2
		data[3] = qc

		-------------

		Write line to file depending on these returned integers

		get_value returns:
		HOLD:
		0 = none
		1 = shift
		2 = ctrl
		3 = mod
		4 = alt

		PRESS T1:
		0 = none
		1 = 1
		2 = /

		PRESS T2:
		0 = none
		1 = 2
		2 = *

		PRESS QC:
		0 = none
		1 = q
		2 = -

		"""


		# with open('config.txt', 'w') as config:

		# 	bools = [get_value(data[0]),get_value(data[1]),get_value(data[2]),get_value(data[3])]
		# 	string = f"None={bools[0]}\nClick={bools[1]}\nSplat={bools[2]}\nZombie={bools[3]}\n"
		# 	# string = f"sound={get_value(data)}"
		# 	print(string)
		# 	config.write(string)
		pass


	def saveHotkeys(sender, data):

		with open('hotkeys.txt', 'w') as hotkey:

			bools = [get_value(data[0]),get_value(data[1]),get_value(data[2]),get_value(data[3])]
			if bools[1] == '':
				bools[1] = 0
			if bools[2] == '':
				bools[2] = 0
			if bools[3] == '':
				bools[3] = 0
			string = f"{bools[0]}\n{bools[1]}\n{bools[2]}\n{bools[3]}\n"
			hotkey.write(string)

	# Initializing main window	

	with window('Jake counter'):

		with child(name='chi', border=False, autosize_x=True, autosize_y=True):
			add_separator()

			with menu_bar(name='menu '):

				with menu(name=' themes '):
					add_menu_item(parent=' themes ', name='Classic', callback=theme_setting, callback_data='Classic')
					add_menu_item(parent=' themes ', name='Light', callback=theme_setting, callback_data='Light')
					add_menu_item(parent=' themes ', name='Dark', callback=theme_setting, callback_data='Dark')
					add_menu_item(parent=' themes ', name='Dark 2', callback=theme_setting, callback_data='Dark 2')
					add_menu_item(parent=' themes ', name='Cherry', callback=theme_setting, callback_data='Red')

				with menu(name=' options ', parent='menu '):
					add_menu_item(parent=' options ', name='style editor', callback=show_style_editor)
					end()

				with menu(" sounds ", parent='menu '):

					with collapsing_header("Sound Effects         "):

						# add_text(' \nSelecting a sound will add it to\nall buttons/hotkeys\n')
						add_text('Feature not available')


						with tree_node("\nSounds\n"):
							
							add_text('\nAdd a sound effect\n')
							add_checkbox('None##',
								default_value=0,
								callback=disableCheckBox)
							add_text('								')
							add_checkbox('Click##',
								default_value=0)
							add_text('			')
							add_checkbox('Splat##',
								default_value=0)
							add_text('				')
							add_checkbox('Zombie##',
								default_value=0)
							add_text('					')
							
						add_separator()
						add_text('\n')
						add_text(' ')
						add_same_line()
						add_button('Save Sound', callback=None, callback_data=None)
						with popup('Save Sound', 'Exit', mousebutton=0):
							add_text('\n\nExit and reopen counter to load new sound effect\n\n\n', color=[200,0,100])
							add_button('Close App', callback=lambda: sys.exit())
							add_text('')

						add_same_line()
						add_text(' ')
						add_text('\n')
						add_separator()
						add_text('')
						add_text(f'Current sound:\n'
								 f'----------------------------------\n'
								 f'None'
								 , color=[0,200,0])

						add_text('')

				with menu(' hotkeys ', parent='menu '):

					with collapsing_header(' Hotkeys '):

						with tree_node(' set hotkeys '):

							add_text(' \nPlease add a hold key,\nthen a press key for\neach ticket type\n ')

							#hold key
							add_radio_button('hold##',
								items=['none','shift','ctrl','alt',],
								horizontal=True)
							add_text('')
							#t1
							add_input_text('##inp1',
								hint='T1 tickets')
							add_text('')
							#t2
							add_input_text('##inp2',
								hint='T2 tickets')
							add_text('')
							#qc
							add_input_text('##inp3',
								hint='QC tickets')
							add_text('')

						add_separator()
						add_text('\n')
						add_text('')
						add_same_line()
						add_button('Save hotkeys',
							callback=saveHotkeys,
							callback_data=('hold##','##inp1','##inp2','##inp3'))
						with popup('Save hotkeys', 'Close', mousebutton=0):
							add_text('\n\nExit and reopen counter to load new hotkeys\n\n\n', color=[200,0,100])
							add_button('Close App ', callback=lambda: sys.exit())
							add_text('')

						add_same_line()
						add_text('')
						add_text('\n')
						add_separator()
						add_text(f'Current Hotkeys:\n'
								 f'----------------------------------\n'
								 f'HOLD= {hold_binding} \tPRESS= {t1_binding}, {t2_binding}, {qc_binding}'
								 , color=[0,200,0])

						add_text('')



				with tab_bar(name='tab_bar_1', parent='chi'):  # Parent tab bar - contains all the respective tabs
					Tab('Tickets', 'tab_bar_1').generate(True)



					add_text('\n\n')
					add_text(f'T1 tickets: {str(t1)}')

					
					def t1_downtick():
						global t1, total
						delete_item(f'T1 tickets: {str(t1)}')
						delete_item(f'Total: {str(total)}')
						t1 -= 1
						total -= 1
						add_text(f'T1 tickets: {str(t1)}', before=' \n\n')
						add_text(f'Total: {str(total)}', before='                                ', color=[255,215,0])
						with open('t1_ticket.txt', 'w') as f:
							f.write(str(t1))
					
					add_text(' \n\n')
					add_button(name='Add T1', width=60, height=40, callback=t1_tick)
					add_same_line(spacing=10)
					add_button(name='Reduce T1', height=40, callback=t1_downtick)
					add_separator()

					add_text('  \n\n')
					add_text(f'T2 tickets: {str(t2)}')

					

					def t2_downtick():
						global t2, total
						delete_item(f'Total: {str(total)}')
						delete_item(f'T2 tickets: {str(t2)}')
						t2 -= 1
						total -= 2
						add_text(f'T2 tickets: {str(t2)}', before='   \n\n')
						add_text(f'Total: {str(total)}', before='                                ', color=[255,215,0])
						with open('t2_ticket.txt', 'w') as f:
							f.write(str(t2))

						
					add_text('   \n\n')
					add_button(name='Add T2', width=60, height=40, callback=t2_tick)
					add_same_line(spacing=10)
					add_button(name='Reduce T2', height=40, callback=t2_downtick)
					add_separator()


					add_text('    \n\n')
					qc_text = add_text(f'QC tickets: {str(qc)}')

					def qc_downtick():
						global qc, total
						delete_item(f'Total: {str(total)}')
						delete_item(f'QC tickets: {str(qc)}')
						qc -= 1
						total -= 1
						add_text(f'QC tickets: {str(qc)}', before='     \n\n')
						add_text(f'Total: {str(total)}', before='                                ', color=[255,215,0])
						with open('qc_ticket.txt', 'w') as f:
							f.write(str(qc))

						
					add_text('     \n\n')
					add_button(name='Add QC', width=60, height=40, callback=qc_tick)
					add_same_line(spacing=10)
					add_button(name='Reduce QC', height=40, callback=qc_downtick)
					add_separator()

					add_text('                            \n\n\n')

					def reset():
						global t1,t2,qc, total
						delete_item(f'T1 tickets: {str(t1)}')
						delete_item(f'T2 tickets: {str(t2)}')
						delete_item(f'QC tickets: {str(qc)}')
						delete_item(f'Total: {str(total)}')
						t1 = 0
						t2 = 0
						qc = 0
						total = 0
						add_text(f'T1 tickets: {str(t1)}', before=' \n\n')
						add_text(f'T2 tickets: {str(t2)}', before='   \n\n')
						add_text(f'QC tickets: {str(qc)}', before='     \n\n')
						add_text(f'Total: {str(total)}', before='                                ', color=[255,215,0])
						with open('t1_ticket.txt', 'w') as f:
							f.write(str(t1))
						with open('t2_ticket.txt', 'w') as f2:
							f.write(str(t2))
						with open('qc_ticket.txt', 'w') as f3:
							f.write(str(qc))

					

					add_text(f'Total: {str(total)}', color=[255,215,0])
					add_text('                                ')
					
					add_button('Save', callback=save)

					add_text('                             ')

					# add_same_line()
					add_button('Reset All', small=True, callback=reset)
					add_same_line()
					add_text('  ')
					add_same_line()
					add_button('Restart Hotkeys',
					small=True, 
					callback=reinit_hotkeys)


					

					add_text('\n\n\n')

					################### Stats #####################

					end()

					# Tab 2

					Tab('Stats', 'tab_bar_1').generate(True)

					add_text('                                                   ')

					if int(datetime.now().strftime('%d')) <= 7:

						add_text(f'Current week: 1   |   {datetime.now().strftime("%B %d, %Y")}')

					elif int(datetime.now().strftime('%d')) >= 8 and int(datetime.now().strftime('%d')) <= 14:
					
						add_text(f'Current week: 2   |   {datetime.now().strftime("%B %d, %Y")}')

					elif int(datetime.now().strftime('%d')) >= 15 and int(datetime.now().strftime('%d')) <= 21:

						add_text(f'Current week: 3   |   {datetime.now().strftime("%B %d, %Y")}')

					elif int(datetime.now().strftime('%d')) >= 22 and int(datetime.now().strftime('%d')) <= 28:

						add_text(f'Current week: 4   |   {datetime.now().strftime("%B %d, %Y")}')

					else:

						add_text(f'Current week: 5   |   {datetime.now().strftime("%B %d, %Y")}')


					add_text('                                                           ')

					with tab_bar(name='tab_bar_2', parent='Stats'):  # Parent tab bar - contains all the respective tabs

						def color_check(x):

							if float(x) < 8:
								add_text(
									f'{x}', 
									bullet=True, 
									color=[255,0,0])
							else:
								add_text(
									f'{x}', 
									bullet=True, 
									color=[0,255,0])

						def color_check_2(x,minimum):
							"""
							Because I cannot be bothered to change 
							params for every single instance of color_checker...
							"""
							if float(x) < minimum:
								add_text(
									f'\t\t{x}', 
									bullet=False, 
									color=[255,0,0])
							else:
								add_text(
									f'\t\t{x}', 
									bullet=False, 
									color=[0,255,0])

						try:

							Tab('Week 1', 'tab_bar_2').generate(True)
								
							with open(f'{month}/week_1.txt', 'r') as f:
								days = [
								'Monday',
								'Tuesday',
								'Wednesday',
								'Thursday',
								'Friday',
								'Saturday',
								'Sunday'
								]
								lines = f.readlines()
								for line in lines:

									if days[5] in line:
										sat = line.replace('Saturday'+' ','')
										sat_avg = float(sat)/8
										sat_avg = "{:.3f}".format(sat_avg)
									if days[6] in line:
										sun = line.replace('Sunday'+' ','')
										sun_avg = float(sun)/8
										sun_avg = "{:.3f}".format(sun_avg)
									if days[0] in line:
										mon = line.replace('Monday'+' ','')
										mon_avg = float(mon)/8
										mon_avg = "{:.3f}".format(mon_avg)
									if days[1] in line:
										tue = line.replace('Tuesday'+' ','')
										tue_avg = float(tue)/8
										tue_avg = "{:.3f}".format(tue_avg)
									if days[2] in line:
										wed = line.replace('Wednesday'+' ','')
										wed_avg = float(wed)/8
										wed_avg = "{:.3f}".format(wed_avg)

								# Grab averages each week

								week_total = float(sat)+float(sun)+float(mon)+float(tue)+float(wed)
								week_avg = week_total/40
								daily_avg = week_total/5
							
								with managed_columns('row1', 5):
									add_text('Saturday')
									add_text('Sunday')
									add_text('Monday')
									add_text('Tuesday')
									add_text('Wednesday')
								add_separator()
								with managed_columns('blank1',5):
									add_text('')
								with managed_columns('row2', 5):
									add_text('Total')
									add_text('Total')
									add_text('Total')
									add_text('Total')
									add_text('Total')
							
								with managed_columns('row3', 5):
									add_text(f'{sat}', bullet=True)
									add_text(f'{sun}', bullet=True)
									add_text(f'{mon}', bullet=True)
									add_text(f'{tue}', bullet=True)
									add_text(f'{wed}', bullet=True)
								with managed_columns('blank2', 5):
									add_text('')

								add_separator()

								with managed_columns('blank3', 5):
									add_text('')

								with managed_columns('row4', 5):
									add_text('Hourly Avg')
									add_text('Hourly Avg')
									add_text('Hourly Avg')
									add_text('Hourly Avg')
									add_text('Hourly Avg')
								
								with managed_columns('row5', 5):
									color_check(sat_avg)
									color_check(sun_avg)
									color_check(mon_avg)
									color_check(tue_avg)
									color_check(wed_avg)
								with managed_columns('blank4',5):
									add_text('')

								add_separator()
								add_text('')
								add_text('')
								add_text('')
								add_text('Total tickets week 1')
								add_text('')
								color_check_2(week_total, 400)
								add_text('')
								add_text('Average tickets per hour week 1')
								add_text('')
								color_check_2(week_avg, 10)
								add_text('')
								add_text('Average tickets per day week 1')
								add_text('')
								color_check_2(daily_avg, 80)
								end()




							Tab('Week 2', 'tab_bar_2').generate(True)

							with open(f'{month}/week_2.txt', 'r') as f:
								days = [
								'Monday',
								'Tuesday',
								'Wednesday',
								'Thursday',
								'Friday',
								'Saturday',
								'Sunday'
								]
								lines = f.readlines()
								for line in lines:

									if days[5] in line:
										sat = line.replace('Saturday'+' ','')
										sat_avg = float(sat)/8
										sat_avg = "{:.3f}".format(sat_avg)
									if days[6] in line:
										sun = line.replace('Sunday'+' ','')
										sun_avg = float(sun)/8
										sun_avg = "{:.3f}".format(sun_avg)
									if days[0] in line:
										mon = line.replace('Monday'+' ','')
										mon_avg = float(mon)/8
										mon_avg = "{:.3f}".format(mon_avg)
									if days[1] in line:
										tue = line.replace('Tuesday'+' ','')
										tue_avg = float(tue)/8
										tue_avg = "{:.3f}".format(tue_avg)
									if days[2] in line:
										wed = line.replace('Wednesday'+' ','')
										wed_avg = float(wed)/8
										wed_avg = "{:.3f}".format(wed_avg)

								week_total = float(sat)+float(sun)+float(mon)+float(tue)+float(wed)
								week_avg = week_total/40
								daily_avg = week_total/5

							add_separator()

						

							with managed_columns('row 1', 5):
								add_text('Saturday')
								add_text('Sunday')
								add_text('Monday')
								add_text('Tuesday')
								add_text('Wednesday')
							add_separator()
							with managed_columns('blank 1',5):
								add_text('')
							with managed_columns('row 2', 5):
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
						
							with managed_columns('row 3', 5):
								add_text(f'{sat}', bullet=True)
								add_text(f'{sun}', bullet=True)
								add_text(f'{mon}', bullet=True)
								add_text(f'{tue}', bullet=True)
								add_text(f'{wed}', bullet=True)
							with managed_columns('blank 2', 5):
								add_text('')

							add_separator()

							with managed_columns('blank 3', 5):
								add_text('')

							with managed_columns('row 4', 5):
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
							
							with managed_columns('row 5', 5):
								color_check(sat_avg)
								color_check(sun_avg)
								color_check(mon_avg)
								color_check(tue_avg)
								color_check(wed_avg)
							with managed_columns('blank 4',5):
								add_text('')

							add_separator()
							add_text('')
							add_text('')
							add_text('')
							add_text('Total tickets week 2')
							add_text('')
							color_check_2(week_total, 400)
							add_text('')
							add_text('Average tickets per hour week 2')
							add_text('')
							color_check_2(week_avg, 10)
							add_text('')
							add_text('Average tickets per day week 2')
							add_text('')
							color_check_2(daily_avg, 80)

							end()

							Tab('Week 3', 'tab_bar_2').generate(True)
							with open(f'{month}/week_3.txt', 'r') as f:
								days = [
								'Monday',
								'Tuesday',
								'Wednesday',
								'Thursday',
								'Friday',
								'Saturday',
								'Sunday'
								]
								lines = f.readlines()
								for line in lines:

									if days[5] in line:
										sat = line.replace('Saturday'+' ','')
										sat_avg = float(sat)/8
										sat_avg = "{:.3f}".format(sat_avg)
									if days[6] in line:
										sun = line.replace('Sunday'+' ','')
										sun_avg = float(sun)/8
										sun_avg = "{:.3f}".format(sun_avg)
									if days[0] in line:
										mon = line.replace('Monday'+' ','')
										mon_avg = float(mon)/8
										mon_avg = "{:.3f}".format(mon_avg)
									if days[1] in line:
										tue = line.replace('Tuesday'+' ','')
										tue_avg = float(tue)/8
										tue_avg = "{:.3f}".format(tue_avg)
									if days[2] in line:
										wed = line.replace('Wednesday'+' ','')
										wed_avg = float(wed)/8
										wed_avg = "{:.3f}".format(wed_avg)

								week_total = float(sat)+float(sun)+float(mon)+float(tue)+float(wed)
								week_avg = week_total/40
								daily_avg = week_total/5

							add_separator()
							with managed_columns('row 11', 5):
								add_text('Saturday')
								add_text('Sunday')
								add_text('Monday')
								add_text('Tuesday')
								add_text('Wednesday')
							add_separator()
							with managed_columns('blank 11',5):
								add_text('')
							with managed_columns('row 22', 5):
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
						
							with managed_columns('row 33', 5):
								add_text(f'{sat}', bullet=True)
								add_text(f'{sun}', bullet=True)
								add_text(f'{mon}', bullet=True)
								add_text(f'{tue}', bullet=True)
								add_text(f'{wed}', bullet=True)
							with managed_columns('blank 22', 5):
								add_text('')

							add_separator()

							with managed_columns('blank 33', 5):
								add_text('')

							with managed_columns('row 44', 5):
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
							
							with managed_columns('row 55', 5):
								color_check(sat_avg)
								color_check(sun_avg)
								color_check(mon_avg)
								color_check(tue_avg)
								color_check(wed_avg)
							with managed_columns('blank 44',5):
								add_text('')

							add_separator()
							add_text('')
							add_text('')
							add_text('')
							add_text('Total tickets week 3')
							add_text('')
							color_check_2(week_total, 400)
							add_text('')
							add_text('Average tickets per hour week 3')
							add_text('')
							color_check_2(week_avg, 10)
							add_text('')
							add_text('Average tickets per day week 3')
							add_text('')
							color_check_2(daily_avg, 80)

							end()

							Tab('Week 4', 'tab_bar_2').generate(True)
							with open(f'{month}/week_4.txt', 'r') as f:
								days = [
								'Monday',
								'Tuesday',
								'Wednesday',
								'Thursday',
								'Friday',
								'Saturday',
								'Sunday'
								]
								lines = f.readlines()
								for line in lines:

									if days[5] in line:
										sat = line.replace('Saturday'+' ','')
										sat_avg = float(sat)/8
										sat_avg = "{:.3f}".format(sat_avg)
									if days[6] in line:
										sun = line.replace('Sunday'+' ','')
										sun_avg = float(sun)/8
										sun_avg = "{:.3f}".format(sun_avg)
									if days[0] in line:
										mon = line.replace('Monday'+' ','')
										mon_avg = float(mon)/8
										mon_avg = "{:.3f}".format(mon_avg)
									if days[1] in line:
										tue = line.replace('Tuesday'+' ','')
										tue_avg = float(tue)/8
										tue_avg = "{:.3f}".format(tue_avg)
									if days[2] in line:
										wed = line.replace('Wednesday'+' ','')
										wed_avg = float(wed)/8
										wed_avg = "{:.3f}".format(wed_avg)

								week_total = float(sat)+float(sun)+float(mon)+float(tue)+float(wed)
								week_avg = week_total/40
								daily_avg = week_total/5

							add_separator()
							with managed_columns('row 111', 5):
								add_text('Saturday')
								add_text('Sunday')
								add_text('Monday')
								add_text('Tuesday')
								add_text('Wednesday')
							add_separator()
							with managed_columns('blank 111',5):
								add_text('')
							with managed_columns('row 222', 5):
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
						
							with managed_columns('row 333', 5):
								add_text(f'{sat}', bullet=True)
								add_text(f'{sun}', bullet=True)
								add_text(f'{mon}', bullet=True)
								add_text(f'{tue}', bullet=True)
								add_text(f'{wed}', bullet=True)
							with managed_columns('blank 222', 5):
								add_text('')

							add_separator()

							with managed_columns('blank 333', 5):
								add_text('')

							with managed_columns('row 444', 5):
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
							
							with managed_columns('row 555', 5):
								color_check(sat_avg)
								color_check(sun_avg)
								color_check(mon_avg)
								color_check(tue_avg)
								color_check(wed_avg)
							with managed_columns('blank 444',5):
								add_text('')

							add_separator()
							add_text('')
							add_text('')
							add_text('')
							add_text('Total tickets week 4')
							add_text('')
							color_check_2(week_total, 400)
							add_text('')
							add_text('Average tickets per hour week 4')
							add_text('')
							color_check_2(week_avg, 10)
							add_text('')
							add_text('Average tickets per day week 4')
							add_text('')
							color_check_2(daily_avg, 80)

							end()

							Tab('Week 5', 'tab_bar_2').generate(True)
							with open(f'{month}/week_5.txt', 'r') as f:
								days = [
								'Monday',
								'Tuesday',
								'Wednesday',
								'Thursday',
								'Friday',
								'Saturday',
								'Sunday'
								]
								lines = f.readlines()
								for line in lines:

									if days[5] in line:
										sat = line.replace('Saturday'+' ','')
										sat_avg = float(sat)/8
										sat_avg = "{:.3f}".format(sat_avg)
									if days[6] in line:
										sun = line.replace('Sunday'+' ','')
										sun_avg = float(sun)/8
										sun_avg = "{:.3f}".format(sun_avg)
									if days[0] in line:
										mon = line.replace('Monday'+' ','')
										mon_avg = float(mon)/8
										mon_avg = "{:.3f}".format(mon_avg)
									if days[1] in line:
										tue = line.replace('Tuesday'+' ','')
										tue_avg = float(tue)/8
										tue_avg = "{:.3f}".format(tue_avg)
									if days[2] in line:
										wed = line.replace('Wednesday'+' ','')
										wed_avg = float(wed)/8
										wed_avg = "{:.3f}".format(wed_avg)

								week_total = float(sat)+float(sun)+float(mon)+float(tue)+float(wed)
								week_avg = week_total/40
								daily_avg = week_total/5

							add_separator()
							with managed_columns('row 1111', 5):
								add_text('Saturday')
								add_text('Sunday')
								add_text('Monday')
								add_text('Tuesday')
								add_text('Wednesday')
							add_separator()
							with managed_columns('blank 1111',5):
								add_text('')
							with managed_columns('row 2222', 5):
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
								add_text('Total')
						
							with managed_columns('row 3333', 5):
								add_text(f'{sat}', bullet=True)
								add_text(f'{sun}', bullet=True)
								add_text(f'{mon}', bullet=True)
								add_text(f'{tue}', bullet=True)
								add_text(f'{wed}', bullet=True)
							with managed_columns('blank 2222', 5):
								add_text('')

							add_separator()

							with managed_columns('blank 3333', 5):
								add_text('')

							with managed_columns('row 4444', 5):
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
								add_text('Hourly Avg')
							
							with managed_columns('row 5555', 5):
								color_check(sat_avg)
								color_check(sun_avg)
								color_check(mon_avg)
								color_check(tue_avg)
								color_check(wed_avg)
							with managed_columns('blank 4444',5):
								add_text('')

							add_separator()
							add_text('')
							add_text('')
							add_text('')
							add_text('Total tickets week 5')
							add_text('')
							color_check_2(week_total, 400)
							add_text('')
							add_text('Average tickets per hour week 5')
							add_text('')
							color_check_2(week_avg, 10)
							add_text('')
							add_text('Average tickets per day week 5')
							add_text('')
							color_check_2(daily_avg, 80)

							end()							

							Tab('All Time', 'tab_bar_1').generate(True)
							add_text('')
							add_text('')
							add_text('\t\tBarring todays unsaved tickets,')
							add_text('')
							add_text(f'\t\tyou have done - {totalus} - tickets since\n\n\t\tWednesday, May 19th, 2021')


							end()

						except:
							print('Please save and re-open to create new database')

					
				

if __name__ == '__main__':
	base = ConstructGui(500, 510)
	base.builder()
	base.run_app()


#################################################################
#Save data

with open('t1_ticket.txt', 'w') as f:
	f.write(str(t1))

with open('t2_ticket.txt', 'w') as f:
	f.write(str(t2))

with open('qc_ticket.txt', 'w') as f:
	f.write(str(qc))

with open('totalus.txt', 'w') as t:
	totalus += total
	t.write(str(totalus))

#################################################################


