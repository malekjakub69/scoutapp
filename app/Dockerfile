# Použijte oficiální Python 3.8 obraz jako základní obraz
FROM python:3.8

# Nastavte pracovní adresář v kontejneru
WORKDIR /app

# Zkopírujte requirements.txt do kontejneru
COPY requirements.txt requirements.txt

# Nainstalujte závislosti
RUN pip install -r requirements.txt

# Kopírujte celý zbytek aplikace do kontejneru
COPY . .

# Spusťte aplikaci
CMD ["python", "app.py"]