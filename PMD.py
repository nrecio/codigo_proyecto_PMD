
from selenium import webdriver
from url_container import url_giver
import csv

#Aquí definimos el intervalo de fechas entre el que queremos buscar
date_min_list = ['3A9%2F1%2F2019', '3A10%2F1%2F2019', '3A11%2F1%2F2019', '3A12%2F1%2F2019', '3A1%2F1%2F2020','3A2%2F1%2F2020','3A3%2F1%2F2020','3A4%2F1%2F2020','3A5%2F1%2F2020','3A6%2F1%2F2020','3A7%2F1%2F2020','3A8%2F1%2F2020','3A9%2F1%2F2020','3A10%2F1%2F2020','3A11%2F1%2F2020','3A12%2F1%2F2020','3A1%2F1%2F2021','3A2%2F1%2F2021','3A3%2F1%2F2021','3A4%2F1%2F2021']
date_max_list = ['3A9%2F30%2F2019', '3A10%2F31%2F2019', '3A11%2F30%2F2019', '3A12%2F31%2F2019', '3A1%2F31%2F2020','3A2%2F29%2F2020','3A3%2F31%2F2020','3A4%2F30%2F2020','3A5%2F31%2F2020','3A6%2F30%2F2020','3A7%2F31%2F2020','3A8%2F31%2F2020','3A9%2F30%2F2020','3A10%2F31%2F2020','3A11%2F30%2F2020','3A12%2F31%2F2020','3A1%2F1%2F2021','3A2%2F1%2F2021','3A3%2F1%2F2021','3A4%2F1%2F2021']

#En esta lista definimos las enfermedades de interés
disease_list = ['covid','cardiopatia+isquemica', 'accidente+cerebrovascular', 'enfermedad+pulmonar+obstructica+cronica', 'infecciones+vias+respiratorias+inferiores', 'afecciones+neonatales', 'cancer+traquea', 'cancer+bronquios', 'cancer+pulmon', 'alzheimer', 'enfermedad+diarreica', 'diabetes+melitus', 'nefropatia']

#Llamamos a nuestra función para que nos cree un diccionario que devuelva las url de google con nuestras enfermedades
url_dict = url_giver(disease_list, date_min_list, date_max_list)


results_number_list = []

for disease in disease_list:

    concrete_disease_list = []

    for j in range(len(date_min_list)):
        start_url = url_dict[disease][j] #accedemos a la url que nos interesa

        driver = webdriver.Chrome('/home/sandra/Escritorio/PMD/chromedriver')  # Argumento opcional, si no se especifica se busca en el path por defecto.
        driver.get(start_url) #Hacemos que se inicialice el driver
        content = driver.find_elements_by_class_name("LHJvCe") #La clase a la que pertenece el número de resultados es la especificada

        codigos = [concrete_disease_list.append([element.get_attribute("innerText")]) for element in content] #guardamos cada número de resultados en una lista

        driver.quit()

    results_number_list.append(concrete_disease_list)

    #Guardamos los datos en un csv de manera que quede cada enfermedad en una columna nueva acompañado del número de resultados en diferentes filas.
    ''' Ahora mismo está comentado para que no cree un fichero nuevo cada vez que lo ejecutamos
    with open('url_info1.csv', 'a', newline='') as csvfile:

        writer = csv.writer(csvfile)
        writer.writerow(disease_list)

        for results in results_number_list:
            writer.writerows(results)
        '''
