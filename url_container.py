
# Creamos una función que cree las url para google
#Sus parámetros son la enfermedad a buscar y el intervalo de tiempo en el que queremos buscarlo

def url_giver(disease_list, date_min_list, date_max_list):

    url_dict = {}

    for disease in disease_list:

        urls_list = []

        for date in range(len(date_max_list)):
            #creamos la url según el formato que pide google
            url_interval = 'https://www.google.com/search?q='+ disease +'&sxsrf=ALeKk03_0fdf4ktNw11l3PerFp3hTbXYYA%3A1621095350580&source=lnt&tbs=cdr%3A1%2Ccd_min%'+ date_min_list[date] +'%2Ccd_max%'+ date_max_list[date]+'&tbm='

            urls_list.append(url_interval)

        url_dict[disease] = urls_list #Guardamos las url en un diccionario con clave enfermedad

    return (url_dict)
