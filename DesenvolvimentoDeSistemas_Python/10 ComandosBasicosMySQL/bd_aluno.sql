drop database bd_escola;

create database bd_escola;

use bd_escola;

create table if not exists aluno (
	idaluno int not null auto_increment,
    nome varchar(100) not null,
    dtnasc date not null,
    endereco varchar(100) not null,
    numero int not null,
    cidade varchar(45) not null,
    estado varchar(2) not null,
    email varchar(100) not null,
    primary key (idaluno));
    
insert into aluno values(default, "Paulo Henrique Santana", "2000-03-05", "Rua A", 25, "Osasco", "SP", "phsantana@gmail.com"),
							(default, "Marcos Qualquer Coisa", "2001-08-04", "Avenida Joao XXIII", 89, "São Paulo", "SP", "qqcoisa@gmail.com"),
                            (default, "Paulo Afonso da Souza", "1980-12-25", "Rua Carlos Marighella", 50, "Rio de Janeiro", "RJ", "paulo_afonso_souza@gmail.com"),
                            (default, "Lucifer da Silva", "0000-00-00", "Rua dos Infernos", 666, "Inferno", "XX", "lucifer@gmail.com"),
                            (default, "Cleyton Aparecido Pinto", "1998-11-28", "Rua Andrade", 74, "Juquitiba", "SP", "cleyton_aparecido_membro@gmail.com");