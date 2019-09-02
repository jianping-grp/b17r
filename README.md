# Bioactivity-explorer (b17r)

*For network issue, the b17r site will not be avaliable during 2019/09/01-2019/09/10 and 2019/09/26-2019/09/28. Sorry for the inconvenience.*

## Run in docker (recommended)

1. Download the latest back-end code: `git clone https://github.com/jianping-grp/b17r`
2. Download the postgres restore data: [google drive](https://drive.google.com/drive/folders/1aghIFwSRXQKiWeCDzVqO5ry9QLCSqKnM?usp=sharing`) or [baidu yunpan](https://pan.baidu.com/s/1wvFt5DGY9-nUntoYnYDVmw)
3. Unzip the file (~83GB disk space will be used) `cat pgdata.tgz_* | gunzip -c > pgdata`
4. Move the `pgdata` folder to b17r
5. Run the docker container `docker-compose up -d --build`
6. :tada: The server is running on `[http://0.0.0.0:8000]` the back-end api locate [here](http://0.0.0.0:8000/b17r_api/phin) and [here](http://0.0.0.0:8000/b17r_api/chembl)
7. Now it time to [setup the front-end](https://github.com/jianping-grp/ng-b17r)

## Setup development

### database restoration
1. Download backup file `https://pan.baidu.com/s/10BCFeaHg7lLG7ittO3reag`
2. Restore: `cat b17r.pgsql.gz* | gunzip | psql -U postgres -d b17r`
3. Custom database setting at `settings.py`

### Server setup (development)
1. `pip install -r requirments`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py runserver`
