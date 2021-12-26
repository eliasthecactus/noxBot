from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from prettytable import PrettyTable
import time
import os
import re


noxusername = ""
noxpassword = ""
myjdownloaderusername = ""
myjdownloaderpassword = ""

linux = 0 #1 for on
headless = 1 #1 for on

if linux== 1:
  def clear(): return os.system('clear')
else:
  def clear(): return os.system('cls')

if headless == 1:
  options = Options()
  options.headless = True
  options.add_argument("--window-size=1920,1080")
  options.add_argument('--allow-running-insecure-content')
  options.add_argument('--log-level=3')
  options.add_experimental_option("excludeSwitches", ["enable-logging"])
  user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
  options.add_argument(f'user-agent={user_agent}')
  driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
  clear()
else:
  driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

driver.get("https://nox.to/")
driver.set_window_size(1920, 1080)
clear()
time.sleep(2)

#login
driver.find_element(By.XPATH, '/html/body/div[2]/div/nav/div/div[3]/ul/li[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(noxusername)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(noxpassword)
driver.find_element(By.XPATH, '/html/body/div[2]/div/nav/div/div[3]/ul/li[3]/ul/li/div/div[1]/form/div[3]/button').click()
time.sleep(2)


#search movie
while len(driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div/div/table/tbody[1]/tr[2]/td[2]/a')) < 1:
  clear()
  movienamesearch = input('filmname: ')
  driver.find_element(By.XPATH, '//*[@id="search_keyword"]').send_keys(movienamesearch)
  driver.find_element(By.XPATH, '/html/body/div[2]/div/nav/div/div[3]/div/form/div/div/button').click()

  time.sleep(2)
  clear()


  rawmoviecount = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div/table/tbody[1]/tr')
  moviecount = (len(rawmoviecount)) -1
  print(moviecount)


  #loop durch die filme
  i = 2
  t = PrettyTable(['Nummer', 'Film'])
  t.align["Film"] = "l"
  while i <= (1+moviecount):
    stri = str(i)
    showstri = int(i)-1
    movieelement = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div/table/tbody[1]/tr['+str(stri)+']/td[2]/a')
    moviename = movieelement.text
    movielink = movieelement.get_attribute('href')
    #print(stri + ": "+ moviename)
    t.add_row([str(showstri), moviename])
    i += 1

  clear()
  print(t)

#film auswählen
moviechoice = input('wähle den film: ')
rawmoviechoice = int(moviechoice)+1
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div/table/tbody[1]/tr['+str(rawmoviechoice)+']/td[2]/a').click()
clear()
time.sleep(7)

  


exitwhile = 0
while exitwhile == 0:
  if driver.find_elements(By.XPATH, '//*[@id="cf-browser-status"]'):
    driver.refresh()
    time.sleep(7)
  else:
    exitwhile = 1


#check site dom
try:
  driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/span/h2')
  trywith = "2"
except:
    trywith = "3"



#infos und versionen crawlen
end = None
imdburl = driver.find_element(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[2]/div[2]/div[2]/div/div/div/a').get_attribute('href')
imdbid = imdburl[26:end]
moreinfos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[1]/span/p').text
try:
  movieyear = re.findall('(\d{4})', moreinfos)[0]
except:
  movieyear = "Unbekannt"
noxmoviename = driver.find_element(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[1]/span/h2').text
imdbrating = driver.find_element(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[2]/div[2]/div[2]/div/div/div/a/span').text

t = PrettyTable(['Sache', 'Wert', 'Status'])
t.align["Wert"] = "l"
t.align["Sonstiges"] = "l"
t.add_row(['Filmname', noxmoviename, ''])
t.add_row(['Jahrgang', movieyear, ''])
t.add_row(['IMDB', imdbrating, ''])
t.add_row(['========', "", ''])


trywith = "3"
rawmoviecount = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[3]/div/table/tbody/tr')
moviecount = (len(rawmoviecount))
if moviecount < 1:
  trywith = "2"
  rawmoviecount = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[3]/div/table/tbody/tr')
  moviecount = (len(rawmoviecount))
print(moviecount)







#loop durch die filme
i = 1
while i <= (moviecount):
  stri = str(i)
  moviename = driver.find_element(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[3]/div/table/tbody/tr['+stri+']/td[2]/small').text
  #movielink = driver.find_element(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[3]/div/table/tbody/tr['+stri+']/td[5]/a').get_attribute('href')
  #print(stri + ": "+ moviename)
  if len(driver.find_elements(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[3]/div/table/tbody/tr['+stri+']/td[4]/img')) < 1:
    t.add_row([stri, moviename, "Online"])
  else:
    t.add_row([stri, moviename, "Offline"])
  i += 1

clear()
print(t)

moviechoice = input('wähle die version: ')
time.sleep(1)
linktomovie = driver.find_element(By.XPATH, '/html/body/div[2]/div/div['+trywith+']/div/div[3]/div/table/tbody/tr['+str(moviechoice)+']/td[5]/a').get_attribute('href')
clear()


#open my.jdownloader.com
driver.get("https://my.jdownloader.org/login.html#logout")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="usernameInput"]').send_keys(myjdownloaderusername)
driver.find_element(By.XPATH, '//*[@id="passwordInput"]').send_keys(myjdownloaderpassword)
driver.find_element(By.XPATH, '//*[@id="loginButton"]').click()
time.sleep(2)

#notification box wegklicken
try:
  driver.find_element(By.XPATH, '//*[@id="webuiContent"]/div[4]/div/div/div/div/div[1]/div[1]/a').click()
except:
    pass

time.sleep(1)

#select delltower
driver.find_element(By.XPATH, '//*[@id="gwtContent"]/div/div/div[2]/div[1]/div[2]/div').click()
time.sleep(2)

#add movie url
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/a[1]').click()
time.sleep(1)
#paste filer.net url
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/table/tbody/tr[1]/td[2]/div[1]/textarea').click()
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/table/tbody/tr[1]/td[2]/div[1]/textarea').send_keys(linktomovie)
#rename movie package
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/table/tbody/tr[5]/td[2]/input').click()
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/table/tbody/tr[5]/td[2]/input').send_keys(imdbid + "_" + noxmoviename)
#add
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/button[1]').click()
time.sleep(1)

driver.refresh()
time.sleep(3)

#start download
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[7]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/a[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/header/div/nav/div[1]/nav[1]/div/ul/li[4]/a').click()





time.sleep(1)

driver.close()
