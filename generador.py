import random
import requests
import os
import json

import re


def myfunc(e):
    return e["title"]


def ordenar_peliculas_alfabeticamente():
    with open('lista-musica.json', encoding='utf8') as f:
        txt = "".join(f.readlines())
        js = json.loads(txt)
        js.sort(key=myfunc)
        arr = []
        for j in js:
            arr.append(j)
        js = arr
        g = open("lista-musica-a-z.json", "w", encoding='utf-8')
        g.write(json.dumps(js, ensure_ascii=False))
        g.close()

#ordenar_peliculas_alfabeticamente()


def obtenerLinks():
    links = ""
    peliculas_a_z = open('lista-musica-a-z.json', encoding='utf8')
    txt = "\n".join(peliculas_a_z.readlines())
    js = json.loads(txt)
    for j in js:
        for k in j["albums"]:
            for l in k["links"]:
                links += l+"\n"
    g = open("links.txt", "w", encoding='utf-8')
    g.write(links)
    g.close()
    peliculas_a_z.close()

#obtenerLinks()


def intercambiarLinks():
    peliculas_a_z = open('lista-musica-a-z.json', encoding='utf8')
    links = open('links.txt', encoding='utf8')
    arr_links = links.readlines()
    links_acortados = open('links-acortados.txt', encoding='utf8')
    arr_links_acortados = links_acortados.readlines()
    txt = "".join(peliculas_a_z.readlines())
    for i in range(len(arr_links)):
        txt = txt.replace(arr_links[i].strip(),
                          arr_links_acortados[i].strip(), 1)
    g = open("lista-musica-acortadas.json", "w", encoding='utf-8')
    g.write(txt)
    g.close()
    peliculas_a_z.close()
    links.close()
    links_acortados.close()

#intercambiarLinks()


def portada(e):
    img = ""
    if(len(e["imagenes"]) == 1):
        img = f'''
                <table cellspacing="0" cellpadding="0" style="margin:auto" class="imgs1">
                    <tbody>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-1]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                    </tbody>
                </table>
                '''
    if(len(e["imagenes"]) == 2):
        img = f'''
                <table cellspacing="0" cellpadding="0" style="margin:auto" class="imgs2">
                    <tbody>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-1]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-2]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                    </tbody>
                </table>
                '''
    if(len(e["imagenes"]) == 3):
        img = f'''
                <table cellspacing="0" cellpadding="0" style="margin:auto" class="imgs3">
                    <tbody>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-1]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-2]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-3]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                    </tbody>
                </table>
                '''
    if(len(e["imagenes"]) >= 4):
        img = f'''
                <table cellspacing="0" cellpadding="0" style="margin:auto" class="imgs4">
                    <tbody>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-1]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                            <td>
                                <img src="{e["imagenes"][-2]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <img src="{e["imagenes"][-3]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                            <td>
                                <img src="{e["imagenes"][-4]}" onerror='this.src = "https://i.ibb.co/4mbzKjD/nf.jpg";'>
                            </td>
                        </tr>
                    </tbody>
                </table>
                '''
    return img


def crearDiscografia(e, peliculas_json, abrirTodo):
    _discografia = open('#discografia.html', encoding='utf8')
    texto_out_discografia = "".join(_discografia.readlines())
    _discografia.close()

    texto_out_discografia = texto_out_discografia.replace("#title", e["title"])
    texto_out_discografia = texto_out_discografia.replace("#BANDA", e["title"])
    texto_out_discografia = texto_out_discografia.replace(
        "#img", random.choice(e["imagenes"]))
    if e.get("contraseña"):
        texto_out_discografia = texto_out_discografia.replace(
            "#CONTRASEÑA", e["contraseña"]
        )
    else:
        texto_out_discografia = texto_out_discografia.replace(
            "#CONTRASEÑA", "No tiene"
        )

    _covers = ""

    for c in e["imagenes"]:
        _covers += f'''<a href='{c}' target='_blank'><img src='{c}' onerror='this.style.display = "none";'></a>'''

    texto_out_discografia = texto_out_discografia.replace("#COVERS", _covers)

    encabezado = open("#encabezado_discografia.html", "r", encoding='utf-8')
    txt_encabezado = "".join(encabezado.readlines())
    encabezado.close()

    texto_out_discografia = texto_out_discografia.replace(
        "#encabezado_discografia", txt_encabezado
    )

    links = "<div style='text-align:center;padding:30px;'>"
    links += "<br>"
    links += "Presiona el siguiente botón y abre todos los enlaces de descarga al tiempo"
    links += "<br>"
    links += "<br>"
    links += f'<div class="btn btn-light" onclick="{abrirTodo}"><h1>Descargar Todo</h1></div>'
    links += "<br>"
    links += "<br>"
    links += "<div style='display:inline-block;text-align:left'>"
    for l in e["albums"]:
        t = l['album'].split("\n")[0]
        links += f"<h4>{t}</h4>"
        links += "<br>"
        for m in l["links"]:
            links += f"<h6><a href='{re.sub(r'CD [0-9]* -? ?', '', m )}' target='_blank'>{m}</a></h6>"
            links += "<br>"
    links += "</div>"
    links += "<br>"
    links += "Presiona el siguiente botón y abre todos los enlaces de descarga al tiempo"
    links += "<br>"
    links += "<br>"
    links += f'<div class="btn btn-light" onclick="{abrirTodo}"><h1>Descargar Todo</h1></div>'
    links += "<br>"
    links += "</div>"

    texto_out_discografia = texto_out_discografia.replace("#LINKS", links)

    _recomendacion = "<div style='text-align:center;'>"

    for r in range(20):
        e2 = random.choice(peliculas_json)
        lbl = e2["title"].replace("(", "").replace(")", "").replace("-", "").replace("!", "").replace("?", "").replace(
            ".", " ").replace("¡", "").replace("¿", "").replace("#", "").replace("$", "").replace(":", "").replace("|", "").replace(" ", "")

        img = portada(e2)

        abrirTodo = ""
        for l in e2["albums"]:
            for m in l["links"]:
                abrirTodo += 'window.open(\'' + fr'{m}' + '\',\'_blank\');'

        _recomendacion += f'''
                <div class="contenedor" id="{lbl}">
                    <span style="font-weight:bolder;height:100px;padding:10px">{e2["title"]}</span>
                    <a href="{lbl}.html">
                    {img} 
                    </a>
                    <br>
                    { f'<div class="btn btn-light" onclick="{abrirTodo}">Descargar Todo</div>'}
                </div>
        '''

    _recomendacion += "</div>"
    texto_out_discografia = texto_out_discografia.replace(
        "#recomendaciones",
        _recomendacion
    )
    lbl = e["title"].replace("(", "").replace(")", "").replace("-", "").replace("!", "").replace("?", "").replace(".", " ").replace(
        "¡", "").replace("¿", "").replace("#", "").replace("$", "").replace(":", "").replace("|", "").replace(" ", "").replace("/", "")
    pelicula_out = open(f'discografia\\{lbl}.html', "w", encoding="utf-8")
    pelicula_out.write(texto_out_discografia)
    pelicula_out.close()


def crearIndex():
    index = open('#index.html', encoding='utf8')
    encabezado = open('#encabezado.html', encoding='utf8')
    texto_index = "".join(index.readlines())
    texto_encabezado = "".join(encabezado.readlines())

    texto_index = texto_index.replace("#encabezado", texto_encabezado)
    file_json = open('lista-musica-acortadas.json', encoding='utf8')

    texto_discografias_json = "".join(file_json.readlines())
    discografias_json = json.loads(texto_discografias_json)

    _contenido = "<div class='discografias' id='discografias'>"
    for e in discografias_json:

        e["title"] = e["title"].replace("&amp;","&")

        if(len(e["imagenes"])==0):
            e["imagenes"].append("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CD_autolev_crop.jpg/250px-CD_autolev_crop.jpg")

        lbl = e["title"].replace("(", "").replace(")", "").replace("-", "").replace("!", "").replace("?", "").replace(".", " ").replace(
            "¡", "").replace("¿", "").replace("#", "").replace("$", "").replace(":", "").replace("|", "").replace(" ", "").replace("/", "")

        abrirTodo = ""
        for l in e["albums"]:
            for m in l["links"]:
                abrirTodo += 'window.open(\'' + fr'{m}' + '\',\'_blank\');'

        crearDiscografia(e, discografias_json, abrirTodo)

        img = portada(e)
        _contenido += f'''
        <div class="contenedor" id="{lbl}">
            <span style="font-size:130%;font-weight:bolder;height:100px;padding:10px">{e["title"].title()}</span>
            <a href="discografia/{lbl}.html">
            {img} 
            </a>
            <br>
            <div class="btn btn-light" onclick="{abrirTodo}">Descargar Todo</div>
        </div>
        '''
    texto_index = texto_index.replace("#contenido", _contenido)

    index_out = open('index.html', "w", encoding="utf-8")
    index_out.write(texto_index)
    file_json.close()
    index_out.close()
    index.close()
    encabezado.close()


crearIndex()
