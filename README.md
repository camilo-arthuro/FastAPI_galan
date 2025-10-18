# Activitat RA2_RA3_RA6 - FASTAPI BASICS 

## NOM I COGNOMS: Carlos Alberto Galan Delgado 

### 1. Crear - Afegir a la list
* Endpoint: /api/users  
* Mètode: POST  
* Funcionalitat: Crear un nou objecte nou i afegir-lo a la list de nom users.  
* Return: Retorna, en format diccionari, informació de tota la llista.  

![Crear_post](img/endpoint_crear_post.jpg)  
![Crear_repsonse](img/endpoint_crear_response.jpg)

### 2. Llegir - Consultar un usuari / objecte de la llista  
* Endpoint: /api/users/{id}
* Mètode: GET
* Funcionalitat: Haurà de buscar l’usuari o objecte de la list amb el que es passi per paràmetre {id}.
* Return: Retorna, en format diccionari, un usuari o un objecte consultat.  

![Consultar_get_id](img/endpoint_consultar_get_id.jpg)
![Consultar_response_id](img/endpoint_consultar_response_id.jpg) 

### 3. Llegir - Consultar tots els usuaris  
* Endpoint: /api/users
* Mètode: GET
* Funcionalitat: Haurà de buscar tots els usuaris o objectes de la llista.
* Return: Retorna, en format diccionari, totes les dades de la llista.  

![Consultar_get_all](img/endpoint_consultar_get_all.jpg)
![Consultar_response_all](img/endpoint_consultar_response_all.jpg)  

### 4. Actualitzar - Actualització completa
* Endpoint: /api/users/{id}
* Mètode: PUT
* Funcionalitat: Actualitzar un objecte (sigui una lletra o canvi sencer) de la list.
* Return: Retorna, en format diccionari, totes les dades de la list.  

![Actualitzacio_put](img/endpoint_actualitzacio_put.jpg)
![Actualitzacio_response](img/endpoint_actualitzacio_response.jpg)
![Actualitzacio_response_get_all](img/endpoint_actualitzacio_response_get_all.jpg)  

### 5. Eliminar - Esborrar usuari
* Endpoint: /api/usuaris/{id}
* Mètode: DELETE
* Funcionalitat: Eliminar un usuari / objecte de la list.
* Return: Retorna, en format diccionari, tota la llista.  

![Esborrar_delete](img/endpoint_esborrar_delete.jpg)
![Esborrar_response](img/endpoint_esborrar_response.jpg)
![Esborrar_response_get_all](img/endpoint_esborrar_response_get_all.jpg)  
