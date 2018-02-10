FROM conda:miniconda2
LABEL maintainer="zhonghua-wang <zhonghua.wang@outlook.com>"

RUN  conda install -c rdkit rdkit && conda install -c rdkit rdkit-postgresql95
