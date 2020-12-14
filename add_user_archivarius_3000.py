import pyautogui
import pyperclip
import win32com.client


def write_network_resource():
    shell = win32com.client.Dispatch('WScript.Shell')

    # click "Add network disk (double click)..."
    #pyautogui.sleep(1)
    pyautogui.moveTo(195, 195)
    pyautogui.click()
    pyautogui.click()

    # write network resource
    #pyautogui.sleep(1)
    pyautogui.moveTo(850, 650)
    pyautogui.click()
    shell.SendKeys('^v')
    # keyboard.press_and_release('ctrl + v')

    # click "oK"
    #pyautogui.sleep(1)
    pyautogui.moveTo(980, 690)
    pyautogui.click()


print('Введите путь до файла с путями сетевых ресурсов:')
path = input()

with open(r'' + path, 'r') as f:
    paths = f.read().splitlines()

screenWidth, screenHeight = pyautogui.size()

print('Ширина экрана - ' + str(screenWidth) + '\n' + 'Высота экрана - ' + str(screenHeight))

pyautogui.sleep(4)
# click "Local area network"
pyautogui.moveTo(185, 180)
pyautogui.click()
pyautogui.click()

i = 0
for path in paths:
    if i < 10:
        pyautogui.sleep(1)
        pyperclip.copy(path)
        write_network_resource()
    else:
        break
    i += 1
