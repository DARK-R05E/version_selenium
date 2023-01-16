from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.chrome.options import Options
from termcolor import colored
import warnings


def __one__():
    if __name__ == '__main__':
        warnings.filterwarnings('ignore')
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--auto-open-devtools-for-tabs')
        options.add_argument('log-level=3')
        options.add_argument('--headless')
        driver = uc.Chrome(options = options)
        crunch = input("URL please\n")
        url = driver.get(crunch)
        print ('target uri =', colored(crunch, 'green'))
        try:
            one = driver.execute_script('return jQuery().jquery')
            print("jQuery version is", one)
            time.sleep(1)
        except:
            print("")
            time.sleep(1)
        try:
            two = driver.execute_script('return jQuery.ui.version')
            print("jQuery UI version is", two)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            three = driver.execute_script('return moment.version')
            print("Moment version is", three)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            four = driver.execute_script('return jQuery.migrateVersion')
            print("Migrate version is", four)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            five = driver.execute_script('return core.version')
            print("Core version is", five)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            six = driver.execute_script('return d3.version')
            print("D3 version is", six)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            seven = driver.execute_script('return angular.version')
            print("AngularJS version is", seven)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            eight = driver.execute_script('return Modernizr._version')
            print("Modernizr version is", eight)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            nine = driver.execute_script('return $().dataTable.version')
            print("DataTables version is", nine)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            ten = driver.execute_script('return getAllAngularRootElements()[0].attributes["ng-version"]')
            print("Angular version is", ten)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            eleven = driver.execute_script('return lodash.version')
            print("Lodash version is", eleven)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            twelve = driver.execute_script('return Ko.version')
            print("Knockout version is", twelve)
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            thirteen = driver.execute_script('return $.fn.tooltip.Constructor.VERSION')
            print("Bootstrap version is", thirteen)
            time.sleep(1)
        except:
            time.sleep(1)


        driver.quit()
__one__()
