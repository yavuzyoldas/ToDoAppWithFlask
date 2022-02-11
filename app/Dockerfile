#Base Image belirtmek için kullanılan bir Dockerfile komutudur.
FROM python:3.6

# Çalışma dizinini /app olarak ayarlar. Container üzerinde çalıştırılacak olan komutların nerede çalışacağını belirtir.
WORKDIR /app
# requirements.txt dosyasını /app dizinine ekler.
ADD requirements.txt /app

# requirements.txt dosyasında belirtilen tüm gerekli paketleri kurulur
RUN pip install -r requirements.txt

# Geçerli dizin içeriğini /app adresindeki kapsayıcıya kopyalar
ADD . /app

# 5802 numaralı portu konteynır için açar. 
EXPOSE 5802

# Container başlatıldığında todo.py dosyası çalıştırılır.
CMD ["python","todo.py"]
