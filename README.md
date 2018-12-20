# Bioactivity-explorer (b17r)

## database restoration
1. Download backup file `https://pan.baidu.com/s/1FkUIC_-S8_vhiXjUMVZDDQ`
or `https://drive.google.com/open?id=1LOm2Hxu7PwuhWg0Ba_rHlQzTCgvIHuix`
2. Restore: `cat b17r.pgsql.gz* | gunzip | psql -U postgres -d b17r`
3. Custom database setting at `settings.py`

## Server setup (development)
1. `pip install -r requirments`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py runserver`

## Docker image (prepare in progress ...)