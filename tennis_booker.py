from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import traceback
import sys
import csv # maybe use a different way of storing information later.


# are constants supposed to be here?
HUMAN_CLICK_DELAY = 2 # in seconds

########### Import user/website-specific data from a .csv file ##############
def get_user_data():
	import csv

	with open('data/user_data.csv', 'r') as f:
		reader = csv.reader(f)
		user_data_list = list(reader)

	# for loop it?
	return user_data_list[2][0], user_data_list[2][1], user_data_list[2][2], user_data_list[2][3], user_data_list[2][4], user_data_list[2][5], user_data_list[2][6]

########### Chrome webdriver set up #########

def adjust_window(location): # will need to modify to make it work with python 3.
	'''
	print ("    Adjusting window size")

	# Resize/position the window to the user/tester's preference 
	# --> (left half of the screen, with some buffer on 3 sides)
	driver.maximize_window()

	max_window_width = driver.get_window_size().items()[0][1] # get screen width (values were stored in a dict)
	max_window_height = driver.get_window_size().items()[1][1] # get screen height
	driver.set_window_size((max_window_width/2)-10, max_window_height-20)

	if location == "left":
		driver.set_window_position(0, 5)
	elif location == "right":
		driver.set_window_position((max_window_width/2)-5, 5)
	'''

########### Testing functions ###########		

def log_in(username, password):
	print ("    Logging in with user name: " + username)

	# log out first, to "reset" the user/browsing session state.
	driver.get(login_url)
	time.sleep(HUMAN_CLICK_DELAY)
	driver.find_element_by_name("username").send_keys(username)
	time.sleep(HUMAN_CLICK_DELAY)
	driver.find_element_by_name("password").send_keys(password)
	time.sleep(HUMAN_CLICK_DELAY)

	# original: driver.find_element_by_xpath("//*[contains(text(), 'Sign In')]").click()
	driver.find_element_by_xpath(login_button_xpath).click()

def check_court_schedule(date):
	driver.get(court_url_pt1 + date + court_url_pt1)

def log_out():
	print ("    Logging out...")
	driver.get("http://qbtest-staging-linode.instaff.org/logout")

def close_test_window():
	print ("quitting in 3..",)
	time.sleep(1)
	print ("2...",)
	time.sleep(1)
	print ("1...")
	time.sleep(1)
	driver.quit()

######## Testing Profiles ########

# test all testing functionality
def all_systems_test():
	log_in(username, password) # more secure password reset
	check_court_schedule(date)
	#log_out()
	#close_test_window()

try:
	driver = webdriver.Chrome() # Create an instance of "Chrome Webdriver"
	

	''' Two concurrent selenium sessions? See P680-4
	#driver2 = webdriver.Chrome()
	#driver2.get("http://qbtest-staging-linode.instaff.org/logout")'''

	### Testing profiles ###
	username, password,date, login_url, login_button_xpath, court_url_pt1, court_url_pt2 = get_user_data()
	print (login_url)
	all_systems_test()
	#announcement_visibility_test()

#close window if there is an error

# is this applicable in this situation?

except Exception:
	print(traceback.format_exc())
	# or
	print(sys.exc_info()[0])
	#traceback.print_exc()
	driver.quit()
