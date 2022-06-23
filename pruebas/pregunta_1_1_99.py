{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8f563398",
   "metadata": {},
   "source": [
    "# Examen práctica 1 Python Bioestadística Medicina UMH 2021-2022"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16b4c693",
   "metadata": {},
   "source": [
    "Ejecuta todas las celdas en orden secuencial. En caso de enviar dos veces la misma pregunta se considerará nula"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c26600f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import datetime\n",
    "import time\n",
    "import sys\n",
    "from time import gmtime\n",
    "import random\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "nombre=\"99\"\n",
    "codigo_examen=\"PYTHON1\"\n",
    "\n",
    "url = 'https://docs.google.com/forms/d/e/1FAIpQLScxikMrmQZx4GxrMa6AXHB2-HpnSyXaoFa6RQ-RQ2JWRo0SKA/formResponse'\n",
    "\n",
    "def on_button_clicked(b):\n",
    "  with output:\n",
    "    enviar_respuesta(url, crear_diccionario(nombre,codigo_examen,num_pregunta,respuesta))\n",
    "    #print(\"Has enviado la respuesta.\")\n",
    "\n",
    "def enviar_respuesta(url, diccionario):\n",
    "    try:\n",
    "        requests.post(url, data=diccionario)\n",
    "        print(\"Pregunta \"+ diccionario[\"entry.1809683194\"]+\" con respuesta \"+ diccionario[\"entry.1838103206\"]+ \" enviada correctamente al sistema\")\n",
    "        time.sleep(1)\n",
    "    except:\n",
    "        print(\"Error Occurrido al intentar enviar la respuesta!\")\n",
    "\n",
    "def crear_diccionario(nombre,codigo_examen, num_pregunta,respuesta):\n",
    "    segundos=time.time()+7200\n",
    "    fecha=gmtime(segundos)\n",
    "    hora=fecha.tm_hour\n",
    "    minutos=fecha.tm_min\n",
    "    diccionario = {\"entry.278655193\":nombre,\n",
    "                   \"entry.1822067037\":codigo_examen,\n",
    "                   \"entry.1809683194\":num_pregunta,\n",
    "                   \"entry.1838103206\":respuesta,\n",
    "                   \"entry.736634225_hour\":hora,\n",
    "                   \"entry.736634225_minute\":minutos}\n",
    "    return diccionario \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e445f23",
   "metadata": {},
   "source": [
    "#Enunciado pregunta 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e92f496b",
   "metadata": {},
   "source": [
    "Calcular la cantidad almacenada en valor, responde con los 4 primeros caracteres de la solución"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7c52833",
   "metadata": {},
   "outputs": [],
   "source": [
    "valor=27\n",
    " valor/=34\n",
    " valor+=32\n",
    " valor-=30\n",
    " valor/=47"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61c527cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#@title Contestacion Pregunta 1 { display-mode: \"form\" }\n",
    "#@markdown Rellena la respuesta y al ejectuar la celda se envia automáticamente la contestación al sistema.\n",
    "respuesta = ''  #@param {type: \"string\"}\n",
    "#@markdown ---\n",
    "num_pregunta=\"1\"\n",
    "button = widgets.Button(description=\"Envia respuesta\")\n",
    "output = widgets.Output()\n",
    "button.on_click(on_button_clicked)\n",
    "display(button, output)\n",
    "    "
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
