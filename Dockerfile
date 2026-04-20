FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]  # CMD को सही फॉर्मेट में लिखें (कॉमा सेपरेटेड)
