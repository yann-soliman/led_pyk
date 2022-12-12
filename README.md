# Led Pyk
Script micro-python tout simple pour gérer les couleurs (et peut-être bientôt plus) d'une bande de LEDs (type WS2812B). Le script peut être installé sur un ESP32.

Le script se connecte à un point d'accès et expose une page HTML basique sur `http://ip:80/`.

A partir de cette page, il est possible de choisir la couleur des LEDs ainsi que le nombre de LEDs allumées (par défaut #FF00FF et 10)

Attention, le script est prévue pour des LEDs en RBG (RIP RGB)

# Installation
* Thonny IDE : https://thonny.org/ (pas terrible mais bon... fait le taff)
* Télécharger le bon firmaware de micro-python (ESP32 : https://micropython.org/download/esp32/)
* L'installer via Thonny IDE (Tools > Options > Interpreter > Install or update MicroPython)
* 

# TODO :
* Sauvegarder la couleur et le nombre de LEDs
* Arc-en-ciel de couleur (couleurs différentes par LED)
* ON/OFF
* Utiliser PyhtmlTemplate à la plage d'une String qui contient la page HTML (mais variable globale a priori)