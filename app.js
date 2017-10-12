
var reqUrl = "http://mvwin10julian.eastus.cloudapp.azure.com:8784/uvradiation/raspberrycontroller/insertarTracks"; //direccion servidor
var request = require('request');//obtener librerria request
setInterval(function(){



//LEER SENSOR

  request.post(
    reqUrl,
    { 
     json: 
		   [{
			"id":1,
			"idUsuario":1,
			"nombreUsuario":"Julian",
			"estado":"activo",
			 "fechaServidor":null,
			 "fechaMovil":null,
			 "fechaCapturaGps":null,
			 "ubicacion":null,
			 "frecuencia":"1000",
			"latitudPosicion":2.4486807,
			"longitudPosicion":76.61804479999999
		}
		]
    },
    function (error, response, body) {
        if (!error && response.statusCode == 200) {//CODIGO DE RESPUESTA 200
            console.log(body)
        }else{
	     console.log(error);
	    }
    console.log(response.statusCode);
    });
},1000);
