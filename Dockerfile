FROM python:3
RUN pip install redis
COPY app.py .
CMD ["python", "app.py"]