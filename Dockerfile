FROM ubuntu
FROM python:latest

RUN apt-get update
RUN pip install pandas matplotlib

ADD utm_graph.py /Users/lucasmeireles/Desktop/globotech/desafio1/utm_graph.py
ADD coordinates_new.csv /Users/lucasmeireles/Desktop/globotech/desafio1/coordinates_new.csv
ADD coordinates_old.csv /Users/lucasmeireles/Desktop/globotech/desafio1/coordinates_old.csv


CMD ["/Users/lucasmeireles/Desktop/globotech/desafio1/utm_graph.py"]
ENTRYPOINT ["python"]