# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# Configurar opciones para el navegador Chrome
options = Options()
options.add_argument('--headless')  # Ejecuta Chrome en modo headless
options.add_argument('--no-sandbox')  # Recomendado en entornos de CI como GitHub Actions
options.add_argument('--disable-dev-shm-usage')  # Ayuda a evitar algunos errores en contenedores

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(options=options)

	def test_video(self):
		browser = self.browser
		browser.get("https://www.youtube.com/")
		video = browser.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
		video.clear()
		video.send_keys('transformada z')
		time.sleep(3)
		buscar = browser.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/button/yt-icon/span')
		buscar.click()
		time.sleep(3)

	def test_leon(self):

		browser = self.browser
		browser.get("https://www.google.com")
		video = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
		video.clear()
		video.send_keys('leones')
		video.send_keys(Keys.RETURN)
		time.sleep(3)

		images_tab = browser.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div')
		images_tab.click()

		time.sleep(3)

		imagen = browser.find_element(By.XPATH, '//*[@id="rso"]/div/div/div[1]/div/div/div[1]/div[3]/a/div[2]/div')

		print("Nombre de la imagen:", imagen.text)

	def test_nit(self):
		browser = self.browser
		browser.get("https://www.unillanos.edu.co/")
		nit = browser.find_element(By.XPATH, '//*[@id="jm-copyrights"]/div/p[14]')
		self.assertEqual('Nit: 892.000.757-3', nit.text)

	def test_form(self):
		browser = self.browser
		browser.get("https://www.unillanos.edu.co/")
		time.sleep(8)
		boton1= browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[5]/div[1]/div/a/img')
		boton1.click()
		time.sleep(3)
		browser.switch_to.window(browser.window_handles[1]) 
		cedula = browser.find_element(By.XPATH, '//*[@id="codigoCedula"]')
		cedula.clear()
		cedula.send_keys('1006796802')
		cedula.send_keys(Keys.ENTER)
		time.sleep(5)
		doc = browser.find_element(By.XPATH, '/html/body/div/main/div/div/div/div[2]/table/tbody/tr/td[1]')
		print("DOC: ", doc.text)
		nom = browser.find_element(By.XPATH, '/html/body/div/main/div/div/div/div[2]/table/tbody/tr/td[2]')
		print("Nombre: ", nom.text)
		pro = browser.find_element(By.XPATH, '/html/body/div/main/div/div/div/div[2]/table/tbody/tr/td[3]')
		print("Programa: ", pro.text)
		acta = browser.find_element(By.XPATH, '/html/body/div/main/div/div/div/div[2]/table/tbody/tr/td[4]')
		print("ACTA: ", acta.text)

	def test_consultarusuario(self):
		browser = self.browser
		browser.get("https://www.unillanos.edu.co/")
		time.sleep(8)
		boton1= browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div/a')
		boton1.click()
		time.sleep(3)
		browser.switch_to.window(browser.window_handles[1]) 
		time.sleep(3)
		consulta = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/section/form/div[4]/div[2]/a/h2')
		consulta.click()
		time.sleep(3)
		docu = browser.find_element(By.XPATH, '//*[@id="documento"]')
		docu.clear()
		docu.send_keys('1006796802')
		botonconsu = browser.find_element(By.XPATH, '//*[@id="consultar"]')
		botonconsu.click()
		time.sleep(4)
		user = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/input')
		print("Usuario: ", user.get_attribute('value'))


	def tearDown(self):
		print()
		#self.browser.quit()
		

if __name__ == '__main__':
	unittest.main()