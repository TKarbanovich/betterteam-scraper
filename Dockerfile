FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD scrapy crawl betterteam-auto -O ./shared_volume/scrapped_info.csv