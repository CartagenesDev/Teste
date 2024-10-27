CREATE DATABASE SUA_EMPRESA;
-- Usar o banco de dados
USE SUA_EMPRESA;

-- Criar a tabela PRODUTOS
CREATE TABLE PRODUTOS (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    preco DECIMAL(10, 2)
);

-- Criar a tabela COMPRAS
CREATE TABLE COMPRAS (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    produto_id INT,
    quantidade INT,
    data_compra DATE,
    FOREIGN KEY (produto_id) REFERENCES PRODUTOS(ID)
);

-- Inserir alguns dados para exemplo
INSERT INTO PRODUTOS (nome, preco) VALUES ('Produto A', 10.00), ('Produto B', 20.00);
INSERT INTO COMPRAS (produto_id, quantidade, data_compra) VALUES (1, 5, '2024-10-25'), (2, 3, '2024-10-25');

-- Criar a procedure para gerar o relatório diário
DELIMITER //
CREATE PROCEDURE gerar_relatorio_diario()
BEGIN
    SELECT 
        data_compra,
        produto_id,
        SUM(quantidade) AS total_quantidade
    FROM COMPRAS
    GROUP BY data_compra, produto_id;
END //
DELIMITER ;

-- Chamar a procedure para gerar o relatório
CALL gerar_relatorio_diario();
