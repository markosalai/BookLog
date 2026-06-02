CREATE TABLE korisnik(
	id int AUTO_INCREMENT PRIMARY KEY,
  	ime varchar(255) NOT NULL,
  	email varchar(255) UNIQUE,
  	lozinka_hash varchar(255) NOT NULL,
  	uloga ENUM('user', 'admin') DEFAULT 'user',
  	datum_registracije DATE
);

CREATE TABLE knjiga(
	id int AUTO_INCREMENT PRIMARY KEY,
  	naslov varchar(255) NOT NULL,
  	autor varchar(255) NOT NULL,
  	isbn varchar(17) UNIQUE NOT NULL,
  	zanr varchar(255),
  	opis varchar(255),
  	godina_izdanja YEAR,
  	korisnik_id int,
  	CONSTRAINT fk_korisnik FOREIGN KEY (korisnik_id) REFERENCES korisnik(id)
);

CREATE TABLE recenzija(
	id int AUTO_INCREMENT PRIMARY KEY,
  	tekst TEXT,
  	ocjena int NOT NULL,
  	vidljiva boolean DEFAULT TRUE,
  	datum_pisanja DATE,
  	korisnik_id int,
  	knjiga_id int,
  	CONSTRAINT fk_recenzija_korisnik FOREIGN KEY (korisnik_id) REFERENCES korisnik(id),
  	CONSTRAINT fk_recenzija_knjiga FOREIGN KEY (knjiga_id) REFERENCES knjiga(id),
  	CONSTRAINT CHECK (ocjena >= 1 AND ocjena <= 5),
	
	CONSTRAINT unique_korisnik_knjiga_ocjena UNIQUE (korisnik_id, knjiga_id) -- korisnik moze na pojedinu knjigu ostaviti recenziju samo jednom 
);