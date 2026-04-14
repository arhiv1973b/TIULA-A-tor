FROM python:3.12-slim
WORKDIR /vault_b

# Переменные окружения (слои метаданных)
ENV DETENTION_START="2007-07-23"
ENV WARRANT_START="2007-07-24"
ENV FABRICATED_QUANTITY="0.0125g_CAPSULE"
ENV COERCION_METHOD="Forest_Walk_Psychological_Pressure"

# Копируем данные и скрипт
COPY torture_vector_0125.json .
COPY audit.py .

CMD ["python", "audit.py"]
