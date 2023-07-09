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

#### 4. Input your own link from yelp.com

 - Go to the **data.py** file. Insert link form yelp
 - I have added one link in data.py as a sample. You can insert as many link you want.
```bash
      start_urls = [
        # this is the sample url
        # Here you have to put your own search link
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA' 
    ]
```


#### 5. Run the command in the terminal
```bash
  scrapy crawl data -o sample_file.csv
```
 - you can download the data in any format. I have given the format below
```bash
  scrapy crawl "spider name" -o file_name.csv/json/xml
``` 
- Here we have scraped some resturant data which is in **Sample File** folder

## Important Note
 - As Yelp is continuously updating its website, so make sure you are updating **xpath**

