# Yelp Restaurant data scraping using python, scrapy spider
![Top-10-Best-Restaurants-in-San-Francisco-CA-July-2023-Yelp](https://github.com/farukalampro/yelp-webscraper-using-scrapy-python-spider/assets/92469073/e3b0e25f-d55b-44b5-b496-828832240397)


## Deployment

#### 1. Clone Repository 

```bash
  git clone https://github.com/farukalampro/yelp-webscraper-using-scrapy-python-spider.git
```
```bash
  cd yelp-webscraper-using-scrapy-python-spider
```
#### 2. Create Virtual Environment
```bash
  python -m venv env
```
 - For Windows:
```bash
  .\env\Scripts\activate
```
 - For macOS/Linux:
```bash
  source env/bin/activate
```

#### 3. To install require packages 

```bash
  pip install -r requirements.txt
```
#### 4. Replace your own document in **data** folder


scrapy crawl "spider name" -o file_name.csv/json/xml
