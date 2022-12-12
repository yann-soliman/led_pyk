from MicroWebSrv2  import *
from time          import sleep
from _thread       import allocate_lock
import network
import machine
from neopixel import NeoPixel

# pin = machine.Pin(4, machine.Pin.OUT)   # set GPIO0 to output to drive NeoPixels
# np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
# np[0] = (255, 255, 255) # set the first pixel to white
# np.write()  

def ApplyColor(color, nbLed):
    np = NeoPixel(machine.Pin(4, machine.Pin.OUT), nbLed)
    for i in range(0, nbLed):
        r = int(color[1:3], 16)
        b = int(color[3:5], 16)
        g = int(color[5:7], 16)
        np[i] = (r, g, b)
    np.write()


ApplyColor("#FF00FF", 10)            # write data to all pixels

def ConnectWifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.scan()                             # Scan for available access points
    station.connect("AP", "password") # Connect to an AP

    while station.isconnected() == False:
        print('.', end = " ")
        sleep(1)
    print("Connexion réussie")
    print ("ESP32 : Adresse IP, masque, passerelle et DNS", station.ifconfig())


ConnectWifi()

HTML_PAGE = """\
    <html lang=fr>

    <head>
        <meta charset="UTF-8" />
        <title>LED color picker</title>
    </head>

    <body style="padding: 0 70px;">
        <form action="/" method="post">
            <div>
                <label for="nbLed">Nb led</label>
                <input type="number" id="nbLed" name="nbLed" value="%s">
            </div>
            <br>
            <div>
                <label for="color">Color</label>
                <input type="color" id="color" name="color"
                       value="%s">
            </div>
            <br>
            <input type="submit" value="OK">
        </form>
    </body>

    </html>
    """

@WebRoute(GET, '/')
def Get(microWebSrv2, request) :
    try :
        nbLed = "10"
        color  = "#FF00FF"
        content   = HTML_PAGE % ( 
                MicroWebSrv2.HTMLEscape(nbLed),
                MicroWebSrv2.HTMLEscape(color) )
    except Exception as e:
        microWebSrv2.Log("ERREUR " + str(e), MicroWebSrv2.ERROR)
        request.Response.ReturnBadRequest()
        return
    request.Response.ReturnOk(content)

@WebRoute(POST, '/')
def Post(microWebSrv2, request) :
    data = request.GetPostedURLEncodedForm()
    try :
        nbLed = int(data['nbLed'])
        color  = data['color']
        ApplyColor(color, nbLed)
        content   = HTML_PAGE % ( 
                MicroWebSrv2.HTMLEscape(str(nbLed)),
                MicroWebSrv2.HTMLEscape(color) )
    except Exception as e:
        microWebSrv2.Log("ERREUR " + str(e), MicroWebSrv2.ERROR)
        request.Response.ReturnBadRequest()
        return
    request.Response.ReturnOk(content)


# # Loads the PyhtmlTemplate module globally and configure it,
# pyhtmlMod = MicroWebSrv2.LoadModule('PyhtmlTemplate')
# pyhtmlMod.ShowDebug = True
# pyhtmlMod.SetGlobalVar('TestVar', 12345)

# # Loads the WebSockets module globally and configure it,
# wsMod = MicroWebSrv2.LoadModule('WebSockets')
# wsMod.OnWebSocketAccepted = OnWebSocketAccepted

# Instanciates the MicroWebSrv2 class,
mws2 = MicroWebSrv2()

# SSL is not correctly supported on MicroPython.
# But you can uncomment the following for standard Python.
# mws2.EnableSSL( certFile = 'SSL-Cert/openhc2.crt',
#                 keyFile  = 'SSL-Cert/openhc2.key' )

# For embedded MicroPython, use a very light configuration,
mws2.SetEmbeddedConfig()

# All pages not found will be redirected to the home '/',
mws2.NotFoundURL = '/'

# Starts the server as easily as possible in managed mode,
mws2.StartManaged()

# Main program loop until keyboard interrupt,
try :
    while mws2.IsRunning :
        sleep(1)
except KeyboardInterrupt :
    pass

# End,
print()
mws2.Stop()
print('Bye')
print()

# ============================================================================
# ============================================================================
# ============================================================================


