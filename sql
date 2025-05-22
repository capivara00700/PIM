CREATE TABLE usuarios(
	id int not null AUTO_INCREMENT PRIMARY KEY,
    usuario varchar(50) not null,
    senha varchar(250) not null
)

CREATE TABLE pontos ( 
    id INT NOT NULL,
    TiposdeDadosF varchar(10),
    TiposdeDadosM varchar(10),
    EstruturasdeControleF varchar(10),
    EstruturasdeControleM varchar(10),
    VariáveiseOperadoresF varchar(10),
    VariáveiseOperadoresM varchar(10),
    ResoluçãodeProblemasF varchar(10),
    ResoluçãodeProblemasM varchar(10),
    FOREIGN KEY (id) REFERENCES usuarios(id)
);
