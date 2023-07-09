import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import requests

class DataSpider(CrawlSpider):
    name = 'data' 
    allowed_domains = ['yelp.com']
    
    start_urls = [
        # this is the sample url
        # Here you have to put your own search link
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA' 
    ]

    ## For Resturant
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='  padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border-color--default__09f24__NPAKY']/div/div[2]/div/div/div/div/div/h3/span/a"), callback='parse_item', follow=True),
    )
    
    # Resturant with sponsor result
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="//span[@class=' css-1egxyvc']/a"), callback='parse_item', follow=True),
    # )   

    # For Dentist
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="//div[@class='  padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border-color--default__09f24__NPAKY']/div/div[2]/div/div/div/div/div/h3[@class='css-1agk4wl']/span/a"), callback='parse_item', follow=True),
    # )   
    
    # Contractors
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="//div[@class='  toggle__09f24__aaito  padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border-color--default__09f24__NPAKY']/div/div[2]/div/div/div/div/div/div/div/h3/span/a"), callback='parse_item', follow=True),
    # )
    
    # For Rufers
    
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="//div[@class='  toggle__09f24__aaito  padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border-color--default__09f24__NPAKY']/div/div[2]/div/div/div/div/div/div/div/h3[@class='css-1agk4wl']/span/a"), callback='parse_item', follow=True),
    # )

    # For Movers Company
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="//div[@class='  toggle__09f24__aaito padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border-color--default__09f24__NPAKY']/div/div[2]/div/div/div/div/div/div/div/h3[@class='css-1agk4wl']/span/a"), callback='parse_item', follow=True),
    # )


    time.sleep(1)
    
    def parse_item(self, response):
        
        time.sleep(4)
        yelp_url = response.xpath("//link[@rel='canonical']/@href").get()
        link_last_part = yelp_url.split("/")[-1]
        map_with_href = "/map/" + link_last_part



        name = response.xpath("//h1/text()").get()
        
        
        add_len = len(response.xpath("//address/p"))
        if add_len == 3:
            address_1 = response.xpath("//a/span[@class=' raw__09f24__T4Ezm']/text()").get()
            address_2 = response.xpath("(//address/p/span/text())[1]").get()
            address_3 = response.xpath("(//address/p/span/text())[2]").get()
        elif add_len == 2:
            address_1 = response.xpath("//a/span[@class=' raw__09f24__T4Ezm']/text()").get()
            address_2 = ''
            address_3 = response.xpath("(//address/p/span/text())[1]").get()
        else:
            address_1 = ''
            address_2 = ''
            address_3 = response.xpath("//a/span[@class=' raw__09f24__T4Ezm']/text()").get()
            
        try:
            street_address = address_1 + " " + address_2
        except:
            street_address = ''
        try:
            city = address_3.split(", ")[0]
        except:
            city = ''
        try:
            zip_code = address_3.split(", ")[1].split()[1]
        except:
            zip_code = ''
        try:
            state = address_3.split(", ")[1].split()[0]
        except:
            state = ''


        phone = response.xpath("//div[@class=' arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG  border-color--default__09f24__NPAKY']/p[@class=' css-1p9ibgf']/text()").get()
        
        # Reviews and Rating
        try:
            #Review in resturant
            # //div/span[@class=' css-1fdy0l5']/a/text()
            number_of_reviews = response.xpath("//div/span[@class=' css-1fdy0l5']/a/text()").get().replace(' reviews', '')
        except:
            number_of_reviews =''
        try:
            rating = response.xpath("(//div[@class=' five-stars__09f24__mBKym five-stars--large__09f24__Waiqf display--inline-block__09f24__fEDiJ  border-color--default__09f24__NPAKY']/@aria-label)[last()]").get().replace(' star rating', '')
        except:
            rating = ''

        
        # Resturant website
        website_href = response.xpath("(//div[@class=' arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG  border-color--default__09f24__NPAKY']/p[@class=' css-1p9ibgf']/a/@href)[1]").get()
        try:
            website = website_href.split("&")[0].replace("/biz_redir?url=http%3A%2F%2F", "").replace("/biz_redir?url=https%3A%2F%2F", "").replace("%2F", "/").replace("%3F", "/?").replace("%3D", "=").replace("%26", "&").replace(map_with_href, "")
        except:
            website =''

        # Menu Link
        try:
            menu_href = response.xpath("//div[@class=' display--inline-block__09f24__fEDiJ margin-r2__09f24__XL72f  border-color--default__09f24__NPAKY']/a[@class=' css-jb5mb6']/@href").get()
            menu_link = menu_href.split('url=')[1].replace("http%3A%2F%2F", "").replace("https%3A%2F%2F", "").replace("&website_link_type=menu", "").replace("%2F", "/")
        except:
            menu_href = ''
            menu_link = menu_href
        
        # Category Scraping
        try:
            # (//span/span[@class=' css-1fdy0l5']/a[@class='css-1m051bw']/text())[1]
            category_1 = response.xpath("(//span/span[@class=' css-1fdy0l5']/a[@class='css-1m051bw']/text())[1]").get()
        except:
            category_1 = ''
        try:
            category_2 = response.xpath("(//span/span[@class=' css-1fdy0l5']/a[@class='css-1m051bw']/text())[2]").get()
        except:
            category_2 = ''
        try:
            category_3 = response.xpath("(//span/span[@class=' css-1fdy0l5']/a[@class='css-1m051bw']/text())[3]").get()
        except:
            category_3 = ''

        # First 3 image scraping
        try:
            image_1 = response.xpath("(//img[@class=' photo-header-media-image__09f24__A1WR_']/@src)[1]").get()
        except:
            image_1 = ''
        try:
            image_2 = response.xpath("(//img[@class=' photo-header-media-image__09f24__A1WR_']/@src)[2]").get()
        except:
            image_2 = ''
        try:
            image_3 = response.xpath("(//img[@class=' photo-header-media-image__09f24__A1WR_']/@src)[3]").get()
        except:
            image_3 = ''
        
        # Price range of a resturant
        try:
            price_range = response.xpath("(//span[@class=' css-1ir4e44']/text())[1]").get()
        except:
            price_range = ''
        

        # Saving data into any format
        yield {
            'Yelp URL': yelp_url,
            'Name': name,
            'Street Address': street_address,
            'Zip Code': zip_code,
            'City': city,
            'State': state,
            'Price Range': price_range,
            'Phone': phone,
            'Rating': rating,
            'Number of Reviews': number_of_reviews,
            'Website': website,
            'Menu Link': menu_link,
            'Image 1': image_1,
            'Image 2': image_2,
            'Image 3': image_3,
            'Category 1': category_1,
            'Category 2': category_2,
            'Category 3': category_3
        }



