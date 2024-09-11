import requests,json

def obtenerIpDesdeDominio(dominio):
    print("------Dominio ->" +str(dominio)+"---------")
    ResultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/"+str(dominio))
    if ResultadoBusqueda.json()['records'] !=None:
        for i in range(len(ResultadoBusqueda.json()['records']["A"])):
            ip = ResultadoBusqueda.json()['records']['A'][i]['address']
            resultadoRegion = requests.get("https://ipinfo.io/"+str(ip)+"?token=d32ef5c0f06747")
            print("La Region de la IP ->" +str(ip)+" es "+str(resultadoRegion.json()['region']))


dominios_empresas = [
    "grupoaval.com",
    "bancolombia.com",
    "epm.com.co",
    "gruposura.com",
    "cemexlatam.com",
    "ecopetrol.com.co",
    "grupoargos.com",
    "alpina.com",
    "exito.com",
    "postobon.com",
    "corferias.com",
    "colpatria.com",
    "grupocorona.com",
    "supertiendas.com.co",
    "alqueria.com",
    "jumbo.com.co",
    "sanandresito.com.co",
    "bavaria.com",
    "grupoempresaspublicas.com",
    "grupoexito.com",
    "bancamia.com",
    "unibio.com",
    "exito.com",
    "grupometrolina.com",
    "mercamena.com",
    "d1.com.co",
    "pizano.com",
    "soacha.com.co",
    "cadena.com",
    "grupoavanza.com",
    "ciudaddelamarina.com",
    "edufranc.com",
    "homcenter.com.co",
    "centrocomerciallosandinos.com",
    "hipermarcade.com",
    "edificioalhambra.com",
    "veltex.com.co",
    "azul.com.co",
    "perifericos.com.co",
    "coomuldesa.com",
    "plaza22.com",
    "tiendasd1.com.co",
    "elnacional.com",
    "eltiempo.com",
    "enlacolombia.com",
    "davidson.com.co",
    "intercontinental.com.co"
]

#for dominio in dominios_empresas:
  #  obtenerIpDesdeDominio(dominio)

def obtenerEmailsDesdeDominio(dominio):
    resultadoEmails = requests.get("https://api.hunter.io/v2/domain-search?domain="+str(dominio)+"stripe.com&api_key=bcecaa5ef1a6d1dccb0d56d908d0bce7cee9a7ce")
    print(json.dumps(resultadoEmails.json()['data']['emails'],indent=4))
    if resultadoEmails.json()['data']['emails'] != None:
        for correo in range (len(resultadoEmails.json()['data']['emails'])):
            print("correo: "+str(resultadoEmails.json()['data']['emails'][correo]['value']))

for dominio in dominios_empresas:
  obtenerIpDesdeDominio(dominio)
  obtenerEmailsDesdeDominio(dominio)

obtenerIpDesdeDominio("dersa.com.co")



