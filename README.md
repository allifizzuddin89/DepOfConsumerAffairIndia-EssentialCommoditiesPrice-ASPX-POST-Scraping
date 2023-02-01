# Dept Of Consumer Affair India Essential Commodities Price ASPX POST Scraping
- Scraping Essential Commodities Price from Department of Consumer Affair India
- ASPX scraping, include post method. We have to pick the given option in order to parse the data.
- Scraping framework : Scrapy
- Parsed data were saved into dataframe using Pandas and later on published as csv files.

## Requirement : 
- Scrapy 2.7.1
- Python 3.7 or above
- Any working environment to install the required packages such as conda or pyenv.

## Run
- The working directory is [here](https://github.com/allifizzuddin89/DepOfConsumerAffairIndia-EssentialCommoditiesPrice-ASPX-POST-Scraping/tree/main/commodities_price/commodities_price/spiders)
- Activate the installed working environment, e.g:
```bash  
  conda activate my_env 
```
- Enter the main.py in the working directory, e.g:
```bash  
  cd DepOfConsumerAffairIndia-EssentialCommoditiesPrice-ASPX-POST-Scraping/commodities_price/commodities_price/spiders
```

### Install environment
- Refer [CONDA Environment Installation](https://docs.anaconda.com/anaconda/install/).
- OR any your preferred working environment.
 
### HOW-TO
- Clone the repository
```bash  
  git clone https://github.com/allifizzuddin89/DepOfConsumerAffairIndia-EssentialCommoditiesPrice-ASPX-POST-Scraping.git.
  ```
- Create working environment (skip if already have any working environment).
```bash
  conda create --name scraping_env -c conda-forge python=3.9.13 scrapy=2.7.1
```
- Activate the working environment.
```bash
  conda activate scraping_env
```
- Run the spider, if you already inside working directory, please [scrapy runspider main.py], else,
 ```bash
    scrapy runspider /DepOfConsumerAffairIndia-EssentialCommoditiesPrice-ASPX-POST-Scraping/tree/main/commodities_price/commodities_price/spiders/main.py
 ```
- Generated csv files are in the working dorectory.

## Troubleshoot
- Error might happen due to the cookies already expired or request being rejected by the server or the url simply has been changed by the administrator.
  - Please bear in mind, the the web owner might change the web's code dynamically anytime. Therefore this web scraping code might not work anytime in future.
- Solution: 
  1. Refresh the cookies (if any) OR
  2. Using proxy (refer main.py)
  3. Replace with new url
  4. Update the header
  
## DISCLAIMER
- This works only meant for educational, research and proof of work purpose only. 
- I will not responsible for any illegal activities.
- Please respect the robot.txt rules.
- Please don't overload the website with too much parallel frequent request.
- Every action is on your own responsibilities.
