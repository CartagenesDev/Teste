CREATE DATABASE ESCOLA;
-- Usar o banco de dados ESCOLA
USE ESCOLA;

-- Criar a tabela de log para armazenar as inserções de alunos
CREATE TABLE log_alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    aluno_nome VARCHAR(100),
    curso_id INT,
    data_insercao TIMESTAMP
);

-- Criar um trigger para registrar quando um novo aluno é inserido
CREATE TRIGGER after_insert_aluno
AFTER INSERT ON ALUNO
FOR EACH ROW
BEGIN
    INSERT INTO log_alunos (aluno_nome, curso_id, data_insercao)
    VALUES (NEW.nome, NEW.curso_id, NOW());
END;
