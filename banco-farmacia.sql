CREATE TABLE FARMACIA 
( 
 CNPJ_farmacia INT PRIMARY KEY,  
 end_farmacia INT,  
 nome_farmacia INT,  
 tel_farmacia INT,  
); 

CREATE TABLE PRODUTO 
( 
 qtd_produto INT,  
 valor_produto INT,  
 cod_produto INT PRIMARY KEY,  
 idFARMACIA INT,  
); 

CREATE TABLE farmaceutico 
( 
 nome_farmaceutico INT,  
 RG_farmaceutico INT PRIMARY KEY,  
 idFARMACIA INT,  
); 

ALTER TABLE PRODUTO ADD FOREIGN KEY(idFARMACIA) REFERENCES FARMACIA (idFARMACIA)
ALTER TABLE farmaceutico ADD FOREIGN KEY(idFARMACIA) REFERENCES FARMACIA (idFARMACIA)
