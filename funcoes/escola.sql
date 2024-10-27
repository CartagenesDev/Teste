CREATE DATABASE ESCOLA;
USE ESCOLA;


CREATE TABLE PROFESSOR (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE CURSO (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES PROFESSOR(ID)
);

CREATE TABLE ALUNO (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    curso_id INT,
    FOREIGN KEY (curso_id) REFERENCES CURSO(ID)
);

-- Inserir dados na tabela PROFESSOR
INSERT INTO PROFESSOR (nome, email) VALUES ('Prof. João', 'joao@example.com');
INSERT INTO PROFESSOR (nome, email) VALUES ('Prof. Maria', 'maria@example.com');

-- Inserir dados na tabela CURSO
INSERT INTO CURSO (nome, professor_id) VALUES ('Matemática', 1);
INSERT INTO CURSO (nome, professor_id) VALUES ('História', 2);

-- Inserir dados na tabela ALUNO
INSERT INTO ALUNO (nome, email, curso_id) VALUES ('Ana', 'ana@example.com', 1);
INSERT INTO ALUNO (nome, email, curso_id) VALUES ('Pedro', 'pedro@example.com', 2);


-- Consulta simples para obter informações de alunos e seus cursos
SELECT ALUNO.nome AS aluno, CURSO.nome AS curso
FROM ALUNO
JOIN CURSO ON ALUNO.curso_id = CURSO.ID;

-- Consulta para obter informações detalhadas incluindo professores
SELECT ALUNO.nome AS aluno, CURSO.nome AS curso, PROFESSOR.nome AS professor
FROM ALUNO
JOIN CURSO ON ALUNO.curso_id = CURSO.ID
JOIN PROFESSOR ON CURSO.professor_id = PROFESSOR.ID;
