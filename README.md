# BookLog

### 1. Kloniranje repozitorija (unutar laragon/www/ direktorija nakon instalacije [Laragona](https://laragon.org/download))
```bash
git clone git@github.com:markosalai/BookLog.git
cd app
```
### 2. Kreiranje virtualnog okruženja i instaliranje paketa
```bash
python -m venv .venv
.\.venv\Scripts\activate # Windows
source .venv/bin/activate # MacOS i Linux
pip install -r ../requirements.txt
```
### 3. Kreiranje baze u Laragonu (HeidiSQL) - prazne baze pod nazivom `booklog`

### 4. Pokretanje migracija za inicijalizaciju baze
` python manage.py migrate `

### 5. Pokretanje servera
` python manage.py runserver `
