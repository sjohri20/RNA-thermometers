from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from BeautifulSoup import BeautifulSoup as BS
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import urllib, urllib2
import html2text
import httplib
import time


file = open("data.txt", "w")
file_seq = open("sequences.txt", "r")
while (file):
	driver = webdriver.Firefox()
	driver.get("http://nupack.org/partition/new")

	driver.find_element_by_id('partition_job_is_melt').click()
	min_temp = driver.find_element_by_id('partition_job_min_melt_temperature')
	min_temp.clear()
	min_temp.send_keys("10")



	increment = driver.find_element_by_id('partition_job_melt_temperature_increment')
	increment.clear()
	increment.send_keys("2")



	max_temp = driver.find_element_by_id('partition_job_max_melt_temperature')
	max_temp.clear()
	max_temp.send_keys("70")

	#i=0
	#while (i<=130):
	sequence_no = driver.find_element_by_id('partition_sequence_0_name')
	sequence_no.clear()
	sequence_no.send_keys("seq 1")
	# sequence_no.send_keys(Keys.RETURN)

	sequence = driver.find_element_by_id('partition_sequence_0_contents')
	sequence.clear()
	line = file_seq.readline()
	sequence.send_keys(line)
	# sequence.send_keys(Keys.RETURN)

	# driver.quit()

	driver.find_element_by_name('commit').click() 			#button click

	element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "melt_curve")))

	new_url = driver.current_url; 
	#new_url = new_url[:new_url.index('&')
	print new_url
	html = urllib.urlopen(new_url)
	soup = BS(html)

	driver.find_element_by_id('melt_curve').click()

	driver.find_element_by_id('svg_link_melt_2').click()

	new_url = driver.current_url;
	html2 = urllib.urlopen(new_url)

	webContent = html2.read()
	file.write(line)
	file.write(webContent[0:])
	file.write('\n')

file_seq.close()
file.close()

#assert "No results found." not in driver.page_source
