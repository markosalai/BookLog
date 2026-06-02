# BookLog

### 1. Kloniranje repozitorija
```bash
git clone git@github.com:markosalai/BookLog.git
cd app
```
### 2. Kreiranje virtualnog okruženja i instaliranje paketa
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Kreiranje baze u Laragonu(HeidiSQL) - prazne baze pod nazivom `booklog`

### 4. Pokretanje migracija za inicijalizaciju baze
` python manage.py migrate `

### 5. Pokretanje servera
` python manage.py runserver `
