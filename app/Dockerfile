# Použijte oficiální Python 3.8 obraz jako základní obraz
FROM python:3.9

# Nastavte pracovní adresář v kontejneru
WORKDIR /app

# Aktualizace balíčkového správce a instalace potřebných závislostí
RUN apt-get update && apt-get install -y unixodbc-dev

# Zkopírujte requirements.txt do kontejneru
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip 

# Nainstalujte závislosti
RUN pip install -r requirements.txt

# Kopírujte celý zbytek aplikace do kontejneru
COPY . .

# Spusťte aplikaci
CMD ["python", "app.py"]