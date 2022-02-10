FROM continuumio/miniconda3

RUN mkdir desafio1
WORKDIR /desafio1

# Create the environment:
COPY environment.yml .
COPY coordinates_new.csv .
COPY coordinates_old.csv .
RUN conda env create -f environment.yml


# Override default shell and use bash
SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]

# Activate Conda environment and check if it is working properly
RUN python -c "import pandas"
RUN python -c "import matplotlib"

# The code to run when container is started:
COPY utm_graph.py .
ENTRYPOINT ["conda", "run", "-n", "env", "python", "utm_graph.py"]