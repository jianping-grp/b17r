FROM z10g/b17r:v1

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /b17r
COPY . /b17r
WORKDIR /b17r

# Install dependencies
# RUN pip install -r requirements.txt

