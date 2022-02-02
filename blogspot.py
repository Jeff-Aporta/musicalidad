import time
import pyautogui
import pyperclip
import json
import re

time.sleep(5)

file_json = open('lista-musica-acortadas.json', encoding='utf8')
texto_discografias_json = "".join(file_json.readlines())
discografias_json = json.loads(texto_discografias_json)

grabar = False
for e in discografias_json:
     if e["title"] == "Vice Squad":
       grabar = True
       continue

     if not grabar:
          continue

     time.sleep(5)

     pyautogui.moveTo(165, 334, duration=0.3)
     pyautogui.click()

     time.sleep(7)

     pyautogui.moveTo(470, 278, duration=0.3)
     pyautogui.click()

     pyperclip.copy(e["title"] + ' - Descargar discografía - MEGA')
     pyautogui.hotkey("ctrl", "v")

     pyautogui.moveTo(421, 409, duration=0.3)
     pyautogui.click()

     pyautogui.hotkey('ctrl', 'a')
     pyautogui.press('delete')

     _covers = ""

     for c in e["imagenes"]:
          _covers += f'''<img src='{c}' onerror='this.style.display = "none";' width="150">\n'''

     links = "<div style='text-align:center;padding:30px;'>\n"

     if e.get("contraseña"):
          links += f'''<h1>Contraseña: {e["contraseña"]}</h1>'''
     else:
          links += f'''<h1>Contraseña: No tiene</h1>'''

     links += "<br>\n"
     links += "<br>\n"

     links += "<div style='display:inline-block;text-align:left'>\n"
     for l in e["albums"]:
          t = l['album'].split("\n")[0]
          links += f"<h4>{t}</h4>\n"
          links += "<br>\n"
          for m in l["links"]:
               links += f"<h4><a href='{re.sub(r'CD [0-9]* -? ?', '', m )}' target='_blank'>{m}</a></h4>\n"
               links += "<br>\n"
     links += "</div>\n"
     links += "</div>\n"
     links += "<br>\n"
     links += "<br>\n"
     links += "<br>\n"
     links += '''
     Te invito a que conozcas las demás discografías que tengo en mi repertorio<br>
     <a href="https://jeff-aporta.github.io/musicalidad/">https://jeff-aporta.github.io/musicalidad/</a><br>
     <br>
     También te invito a que conozcas mi página de películas<br>
     <a href="https://jeff-aporta.github.io/cine-peliculas/">https://jeff-aporta.github.io/cine-peliculas/</a><br>
     '''
     links += "<br>\n"
     links += "<br>\n"
     links += "<br>\n"
     links += _covers+"\n"
     links += "<br>\n"
     links += "<br>\n"
     links += "<br>\n"
     
     pyperclip.copy(links)
     pyautogui.hotkey("ctrl", "v")

     pyautogui.moveTo(1823, 255, duration=0.3)
     pyautogui.click()

     time.sleep(1)

     pyautogui.moveTo(1093, 666, duration=0.3)
     pyautogui.click()

    # exit()
