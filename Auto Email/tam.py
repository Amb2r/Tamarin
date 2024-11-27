import pyautogui as pag
from time import sleep

#copy code
pag.click(469,174)
pag.hotkey('ctrl', 'a')
pag.hotkey('ctrl', 'c')
#open opera
pag.moveTo(747 , 743 , 2)
pag.click(747 , 743) 
sleep (2)
pag.typewrite('gmail.com')
pag.press('enter')
sleep (3)
#choose accuont & enter password
pag.moveTo(791,300 , 2)
pag.click(791,300)
sleep (2)
pag.click(843,360)
pag.typewrite('R.s9910&')
pag.moveTo(1100, 512 , 2)
pag.click(1100, 512)

#click compose
sleep(3)
pag.moveTo(129,195, 2)
pag.click(129,195) 
#click new Emaile
sleep (2)
pag.moveTo(875,302, 2)
pag.click(875,302)
pag.typewrite('amb2rch@gmail.com')
pag.press('enter')
pag.click(925,354)
pag.typewrite('PYTHON27')
pag.click(999,460)
pag.hotkey('ctrl', 'v')
pag.moveTo(838,679, 2)
pag.click(838,679)

