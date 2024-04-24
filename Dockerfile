FROM python:3.9
COPY . .
WORKDIR /ipynb_checkpoints
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt
CMD ["python","app.py"]