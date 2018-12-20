FROM conda:miniconda2
LABEL maintainer="zhonghua-wang <zhonghua.wang@outlook.com>"

ADD . /code
WORKDIR /code
RUN  conda install -c rdkit rdkit==2017.09.03 && conda install -c rdkit rdkit-postgresql95
RUN pip install -r requirment.txt