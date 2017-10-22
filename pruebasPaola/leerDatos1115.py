import time
import Adafruit_ADS1x15
import requests

def outData(lectura):
    vol=lectura*0.0001875057222;
    reqUrl = "http://mvwin10julian.eastus.cloudapp.azure.com:8784/uvradiation/raspberrycontroller/insertarTracks"; #direccion servidor
    try:
        r=requests.post(
         reqUrl,
          json=[{
                    "id":None,
                    "idUsuario":1,
                    "nombreUsuario":"Paola y su cerveza",
                    "estado":"activo",
                     "fechaServidor":None,
                     "fechaMovil":None,
                     "fechaCapturaGps":None,
                     "ubicacion":None,
                     "frecuencia":"1000",
                    "latitudPosicion":2.4486807,
                    "longitudPosicion":76.61804479999999,
                    "lectura":vol
                    }
                   ]
          ,timeout = 10)
        print r.json()
        print(lectura)
    except requests.exceptions.ConnectTimeout:
        print "El servidor NO se encuentra disponible"
    except:
        print "Error de valor"

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0-3 for 3 seconds...')
start = time.time()
while (time.time() - start) <= 10:
    # Read the last ADC conversion value and print it out.
    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    #print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    print(values[0])
    outData(values[0])
    time.sleep(1)

# Stop continuous conversion.  After this point you can't get data from get_last_result!
adc.stop_adc()

