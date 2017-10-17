import requests #obtener librerria request

reqUrl = "http://mvwin10julian.eastus.cloudapp.azure.com:8784/uvradiation/raspberrycontroller/insertarTracks"; #direccion servidor
r=requests.post(
 reqUrl,
  json=[{
			"id":1,
			"idUsuario":1,
			"nombreUsuario":"Julian",
			"estado":"activo",
			 "fechaServidor":None,
			 "fechaMovil":None,
			 "fechaCapturaGps":None,
			 "ubicacion":None,
			 "frecuencia":"1000",
			"latitudPosicion":2.4486807,
			"longitudPosicion":76.61804479999999
		    }
		   ]
  )
print r.json()
    
