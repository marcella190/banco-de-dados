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
