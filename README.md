# API Instagram Scrapper

The simple API for web scraping instagram users using Selenium and BeautifulSoap.

## Documentation 
**The syntax of the query**
```text
   /?username=...&method=...&[arg1]=...&[arg2]=...&[arg3]=...
```    

After _question mark_ follow arguments:

```   
    * username - your username or someone else's
        
        Optional: False
    
    * method - method to parse instagram page
    
        Supported Methods:
            - Selenium
        In progress:
            - BeautifulSoap
            
        Optional: False
        
    * [limit] - number of posts to crawl
        
         If the limit has been omitted the whole page is going to be crawled
         
         Type: Integer
         Optional: True
         
    * [pwd] - whether the user wants to log in and scrap his own private account
    
        You cannot crawl the page of the private account belonged to another user
        
        Optional: True
        
    * [headless] - to crawl using headless browser
    
        Type: Boolean (1 or 0)
        Optional: True
```
The output of this API is a `json object`
```json
   {
      "response": {
        "object": {...},
        "settings": {...}
      }
   }
```

## Requirements

### TODO

## Ideas to extend the project

```text 
    * Extend abilities of this API to crawl more data
```   