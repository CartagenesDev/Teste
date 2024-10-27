-- Criar o banco de dados
CREATE DATABASE ESCOLA;

-- Selecionar o banco de dados
USE ESCOLA;

-- Criar a tabela ALUNO
CREATE TABLE ALUNO (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    endereco VARCHAR(200)
);
