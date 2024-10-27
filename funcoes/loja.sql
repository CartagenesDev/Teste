-- Usar o banco de dados
CREATE DATABASE LOJA;
USE LOJA;

-- Criar a tabela CLIENTES
CREATE TABLE CLIENTES (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    data_cadastro DATE
);

-- Inserir dados na tabela CLIENTES
INSERT INTO CLIENTES (nome, email, data_cadastro) VALUES ('Ana', 'ana@example.com', '2024-10-26');
INSERT INTO CLIENTES (nome, email, data_cadastro) VALUES ('Pedro', 'pedro@example.com', '2024-10-26');
INSERT INTO CLIENTES (nome, email, data_cadastro) VALUES ('Carlos', 'carlos@example.com', '2024-10-25');


-- Criar a função
DELIMITER //
CREATE FUNCTION contar_clientes_por_dia(data DATE) 
RETURNS INT 
BEGIN 
    DECLARE total_clientes INT;
    SELECT COUNT(*) INTO total_clientes
    FROM CLIENTES
    WHERE data_cadastro = data;
    RETURN total_clientes;
END //
DELIMITER ;

-- Chamar a função
SELECT contar_clientes_por_dia('2024-10-26') AS total_clientes;
