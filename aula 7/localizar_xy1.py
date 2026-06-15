#importa a biblioteca(módulo) que controla o mouse e a tecla
import pyautogui

#localiza as coordenadas de um elemento na tela
#usando uma imagem

xy = pyautogui.locateCenterOnScreen('aula 7\\8.png', confidence=0.99)
print(xy)
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen('aula 7\\x.png', confidence=0.99)
print(xy)
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen('aula 7\\3.png', confidence=0.99)
print(xy)
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen('aula 7\\igual.png', confidence=0.99)
print(xy)
pyautogui.click(xy, duration=1)
