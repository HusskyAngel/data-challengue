CREATE TABLE IF NOT EXISTS  departamentos( 
	id_departamento SERIAL PRIMARY KEY,
	nombre_departamento varchar(30)
);

CREATE TABLE IF NOT EXISTS  provincias(
	id_provincia INTEGER UNIQUE PRIMARY KEY,
	nombre_provincia varchar(30) UNIQUE 
);

CREATE TABLE IF NOT EXISTS  localidades(
	id_localidad INTEGER UNIQUE PRIMARY KEY, 
	nombre_localidad varchar(30) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS  categorias(
	id_categoria SERIAL PRIMARY KEY ,
	nombre_categoria varchar(30)
);

CREATE TABLE IF NOT EXISTS  subcategorias(
	id_subcategoria SERIAL PRIMARY KEY NOT NULL,
	nombre_subcategoria varchar(30)
);


CREATE TABLE IF NOT EXISTS  codigos_postal(
	id_cod_postal SERIAL PRIMARY KEY,
	cod_postal varchar(15)
);

CREATE  TABLE IF NOT EXISTS establecimientos(
	id serial PRIMARY KEY,	
	nombre_establecimiento varchar(30), 
	direccion_establecimiento varchar(30),
	departamento_establecimiento INTEGER REFERENCES departamentos (id_departamento) ON UPDATE CASCADE,
	provincia_establecimiento INTEGER REFERENCES provincias (id_provincia) ON UPDATE CASCADE,
	localidad_establecimiento INTEGER REFERENCES localidades (id_localidad) ON UPDATE CASCADE, 
	categoria_establecimiento INTEGER REFERENCES categorias (id_categoria) ON UPDATE CASCADE,
	subcategoria_establecimiento INTEGER REFERENCES subcategorias (id_subcategoria) ON UPDATE CASCADE,
	codigo_postal_establecimiento INTEGER REFERENCES codigos_postal (id_cod_postal) ON UPDATE CASCADE,	
	fecha_actualización timestamp
);


CREATE OR REPLACE FUNCTION actualizacion_fecha_establecimientos()
	RETURNS TRIGGER AS $actualizacion_fecha_establecimientos$	
BEGIN 
	UPDATE establecimientos set fecha_actualización=NOW() where id=NEW.id;
END
	$actualizacion_fecha_establecimientos$ LANGUAGE plpgsql;



CREATE OR REPLACE TRIGGER actualizacion_fecha AFTER UPDATE OR INSERT  
		ON establecimientos
	FOR EACH STATEMENT
		EXECUTE PROCEDURE actualizacion_fecha_establecimientos();
