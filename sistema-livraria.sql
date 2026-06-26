-- Ativar suporte a chaves estrangeiras
PRAGMA foreign_keys = ON;

-- Criação da tabela Clientes
CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY,
    nomeCliente TEXT NOT NULL,
    emailCliente TEXT UNIQUE
);

-- Criação da tabela Compras
CREATE TABLE Compras (
    CompraID INTEGER PRIMARY KEY,
    ClienteID INTEGER,
    NomeLivro TEXT NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

SELECT * FROM Clientes; 

-- Inserção de dados na tabela Clientes
INSERT INTO Clientes (nomeCliente, emailCliente) VALUES
('Ana Silva', 'ana.silva@email.com'),
('Bruno Costa', 'bruno.costa@email.com'),
('Carla Souza', 'carla.souza@email.com');

-- Inserção de dados na tabela Compras
INSERT INTO Compras (ClienteID, NomeLivro) VALUES
(1, 'Dom Casmurro'),
(2, 'O Senhor dos Anéis'),
(3, '1984'),
(1, 'A Moreninha');

SELECT * FROM Clientes; 
SELECT * FROM Compras; 
