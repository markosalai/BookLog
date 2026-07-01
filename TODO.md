# BookLog

# Napredni razvoj web aplikacija - Studentski projekti

Svaki projekt prolazi kroz ista 6 koraka:
* **Korak 1** - Postavljanje projekta i baze podataka (GitHub push: SQL, ER dijagram, README, ADR-001) 
* **Korak 2** - MVC arhitektura i prikaz podataka (GitHub push: MVC struktura, funkcionalni prikaz) 
* **Korak 3** - REST API s JSON odgovorima (GitHub push: API endpointi, Fetch/AJAX integracija) 
* **Korak 4** - Autentikacija i autorizacija s JWT (GitHub push: auth sustav, zaštićene rute, uloge) 
* **Korak 5** - Sigurnost web aplikacije (GitHub push: XSS, SQL Injection, CSRF zaštita, ADR-002) 
* **Korak 6** - Finalizacija, deployment i dokumentacija (GitHub push: završna verzija, README) 

### Obveze za svaki projekt:
* Svaki korak mora biti pushnut na GitHub u tjednom roku 
* Dokumentacija u obliku ADR zapisa (minimalno 2: ADR-001 i ADR-002) 
* Aplikacija mora raditi na Laragon lokalnom okruženju 
* `README.md` mora sadržavati upute za pokretanje i opis API endpointa 

---

## Projekt 3: BookLog - Evidencija pročitanih knjiga
BookLog je aplikacija za bibliofile koji žele pratiti što su pročitali. Korisnici dodaju knjige, pišu recenzije i daju ocjene. Svaki korisnik ima svoju osobnu knjižnu policu, a administrator može moderirati sadržaj koji je vidljiv svim korisnicima. 

### Entiteti (tablice u bazi podataka)

| Entitet | Atributi |
| :--- | :--- |
| **Korisnik (User)** | `id`, `ime`, `email`, `lozinka_hash`, `uloga (user/admin)`, `datum_registracije` | 
| **Knjiga (Book)** | `id`, `naslov`, `autor`, `isbn`, `godina_izdanja`, `zanr`, `opis`, `korisnik_id` | 
| **Recenzija (Review)** | `id`, `ocjena (1-5)`, `tekst`, `datum_pisanja`, `vidljiva (boolean)`, `knjiga_id`, `korisnik_id` | 

### Zadaci po koracima

#### Korak 1: Postavljanje projekta i baze podataka
- [x] Inicijalizirati GitHub repozitorij s `README.md`
- [x] Konfigurirati Laragon razvojno okruženje 
- [x] Dizajnirati ER dijagram: User, Book, Review 
- [x] Napisati SQL skriptu - uključiti `CHECK` ograničenje za ocjenu (1-5) i `DEFAULT` vrijednosti 
- [x] Osmisliti relacije: korisnik dodaje knjige, korisnik može recenzirati knjigu (jednom) 
- [x] Napisati `ADR-001.md`: obrazložiti odluku o pohrani ISBN-a i validaciji duplikata 
- [x] Pushati na GitHub: SQL, ER dijagram, README, ADR-001 

#### Korak 2: MVC arhitektura i prikaz podataka
- [x] Uspostaviti MVC strukturu projekta 
- [x] Kreirati `BookModel` s metodama: `findAll()`, `findByUser()`, `findById()`, `create()`, `update()`, `delete()`, `search()` 
- [x] Kreirati `ReviewModel` s metodama: `findByBook()`, `findByUser()`, `create()`, `update()`, `toggleVisibility()` 
- [x] Kreirati `BookController` i `ReviewController` (*dodani su ekvivalenti u views.py za Django)
- [x] Kreirati Views: knjižna polica korisnika, detalji knjige s recenzijama, forma za dodavanje knjige 
- [x] Implementirati pretragu knjiga po naslovu ili autoru 
- [x] Prikazati prosječnu ocjenu za svaku knjigu izračunatu u SQL upitu 
- [x] Pushati na GitHub: MVC struktura s prikazom podataka 

#### Korak 3: REST API s JSON odgovorima
- [x] Implementirati `GET /api/books` - lista knjiga s prosječnom ocjenom 
- [x] Implementirati `GET /api/books/{id}` - detalji knjige sa svim recenzijama 
- [x] Implementirati `POST /api/books` - dodavanje nove knjige 
- [x] Implementirati `PUT /api/books/{id}` - uređivanje knjige 
- [x] Implementirati `DELETE /api/books/{id}` - brisanje knjige 
- [x] Implementirati `POST /api/books/{id}/reviews` - dodavanje recenzije 
- [x] Implementirati `DELETE /api/reviews/{id}` - brisanje recenzije 
- [x] Koristiti Fetch API za dinamično učitavanje recenzija bez osvježavanja stranice 
- [x] Pushati na GitHub: API endpointi, Fetch integracija 

#### Korak 4: Autentikacija i autorizacija (JWT)
- [x] Implementirati registraciju i prijavu s JWT tokenom 
- [x] Zaštititi POST, PUT, DELETE endpunkte s JWT middleware-om 
- [x] Filtrirati knjige po korisniku: svaki korisnik vidi svoju policu 
- [ ] Implementirati admin rutu za pregled svih recenzija i opciju moderiranja (`vidljiva = false`) 
- [x] Spriječiti duplikate: jedan korisnik može imati jednu recenziju po knjizi 
- [x] Pushati na GitHub: auth sustav, admin moderacija 

#### Korak 5: Sigurnost web aplikacije
- [x]  Implementirati prepared statements za sve SQL upite 
- [x]  Escapirati sadržaj recenzija u HTML prikazu (XSS zaštita) 
- [x]  CSRF zaštita na forme za dodavanje knjige i recenzije 
- [x]  Validirati ulazne podatke: ocjena mora biti broj između 1 i 5, ISBN format, godina izdanja (razumni raspon) 
- [x]  Implementirati provjeru vlasništva: korisnik može brisati SAMO svoje knjige i recenzije 
- [x]  Napisati `ADR-002.md` s opisom sigurnosnih mjera 
- [x]  Pushati na GitHub: sigurnosne mjere, ADR-002 

#### Korak 6: Finalizacija, deployment i dokumentacija
- [ ] Verificirati rad na Laragon okruženju 
- [ ] Napisati `README.md` s instalacijskim uputama i opisom API-ja 
- [ ] Dodati screenshot knjižne police u `README` 
- [ ] Finalni push i predaja GitHub linka 