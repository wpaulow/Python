drop database if exists bd_pizzaria;

create database bd_pizzaria;

use bd_pizzaria;

CREATE USER 'PythonProjects'@'localhost' IDENTIFIED BY '12345678';
GRANT SELECT, DELETE, INSERT, UPDATE, EXECUTE ON bd_pizzaria.* TO 'PythonProjects'@'localhost';

CREATE TABLE IF NOT EXISTS bd_pizzaria.produtos (
		idProduto int not null,
		nome VARCHAR(35) NOT NULL,
		marca VARCHAR(35) NOT NULL,
		dtVal date NOT NULL,
		PRIMARY KEY (idProduto)
		);

insert into produtos (idProduto, nome, marca, dtVal) values 
	(1, "Molho de Tomate", "Pomarola", "2021-07-06"),
    (2, "Farinha de Trigo", "Dona Benta", "2021-12-07"),
    (3, "Mussarela", "Real", "2019-07-06"),
    (4, "Presunto", "Perdigão", "2020-05-06"),
    (5, "Calabresa", "Sadia", "2020-08-02");
    
select * from produtos;