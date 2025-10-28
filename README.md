# Activitat RA2_RA3_RA6 - FASTAPI POSTGRES 

## NOM I COGNOMS: Carlos Alberto Galan Delgado 
### Crear 6 endpoints (create, read, read by id, update by id, update parcial i delete by id) per fer les consultes a la Base de Dades en postgreSQL i mostrar les respostes de l’APIREST amb docs de FastAPI o postman.  

### Endpoints CRUD amb Postgresql:  
### Ceate - Afegir un nou registre a la taula  
* Mètode: POST  
* Funcionalitat: Afegir un nou registre a la taula de la BD.  NO es demana gestionar els errors d’http.  
* Return: Retorna un missatge com a inserció correcta.  

![Create_post](img_postgres/create_post.jpg)
![Create_post_response](img_postgres/create_post_code.jpg)

### Read - Consultar totes les dades d’un registre a la taula.  
* Mètode: GET  
* Funcionalitat: Haurà de buscar un registre per id. NO es demana gestionar els errors d’http.  
* Return: Retorna en format sqlmodel adequat.  

![Read_by_id_get_by_id](img_postgres/read_by_id_get_by_id.jpg)
![Read_by_id_get_by_id_code](img_postgres/read_by_id_get_by_id_code.jpg)

### Read - Consultar totes les dades de tots els registres de la taula.  
Quan el client faci la consulta a /api/product caldrà una resposta per part del servidor amb les dades de tots els registres de la taula. S’han d’evitar enviar dades sensibles al client. indicar amb un comentari en el mateix endpoint les dades sensibles que heu escollit.  

![Read_All_get_all](img_postgres/read_all_get_all.jpg)
![Read_All_get_all_code_1](img_postgres/read_all_get_all_code_1.jpg) 
![Read_All_get_all_code_2](img_postgres/read_all_get_all_code_2.jpg)

### Read - Consultar les dades filtrant per un camp  
Quan el client faci la consulta a /api/product/{<nom_camp>} (cal substituir <nom-camp> pel nom del camp a filtrar) caldrà una resposta per part del servidor amb les dades d’aquells registres filtrats pel nom del camp.  

![Read_by_name](img_postgres/read_by_name.jpg)
![Read_by_name_code](img_postgres/read_by_name_code.jpg)

### Delete - Eliminar un registre per id  
Quan el client faci la consulta a /api/product/{id} caldrà tornar una resposta amb un missatge indicant que l’eliminació ha sigut exitosa.  

![Delete_by_id](img_postgres/delete_by_id.jpg)
![Delete_by_id_code](img_postgres/delete_by_id_code.jpg)
![Get_all_no_id_3](img_postgres/get_all_no_id_3.jpg)

### Read - Lectura parcial  
El client demana poder mostrar unes dades d’un producte. Les dades han de ser 3 camps (escollit per l’alumnat). Cal tenir en compte que 2 camps son sensibles i no es poden retornar en aquest endpoint.  

![Read_partially](img_postgres/read_partially.jpg)
![Read_partially_code](img_postgres/read_partially_code.jpg)  

### Update - Modificació total (PUT)  
El client vol tenir la opció de modificar totes les dades d’un producte. Cal pensar si l’id es pot modificar o no des del client.  

![Update_total](img_postgres/update_total.jpg)
![Update_total_code](img_postgres/update_total_code.jpg)  
* Abans  
![Update_total_before](img_postgres/update_total_before_id_5.jpg)  
* Després  
![Update_total_after](img_postgres/update_total_after_id_5.jpg)  

### Update - Modificació parcial un camp (PATCH)  
El client vol tenir la opció, també, de poder modificar només un camp d’un registre de la taula producte (podeu escollir vosaltres un).  

![Patch_one](img_postgres/patch_one.jpg)  
![Patch_one_code](img_postgres/patch_one_code.jpg)  
![Patch_one_get_id](img_postgres/patch_one_get_id.jpg)  

### Update - Modificació parcial dos camps  
El client vol tenir la opció, també, de poder modificar només dos camps d’un registre de la taula producte (podeu escollir vosaltres).  

![Patch_two](img_postgres/patch_two.jpg)
![Patch_two_code](img_postgres/patch_two_code.jpg)  
![Patch_two_get_id](img_postgres/patch_two_get_id.jpg)
