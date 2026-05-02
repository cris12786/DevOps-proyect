# 1. Imagen base
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 2.5. librerias Postgre y compilador c
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc

# 3. Copiar dependencias
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código
COPY . .

# 6. Puerto que usará la app
EXPOSE 5000

# 7. Comando para ejecutar la app
CMD ["python", "-m", "app.main"]
