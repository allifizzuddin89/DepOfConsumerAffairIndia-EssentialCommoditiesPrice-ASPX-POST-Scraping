import scrapy
from scrapy import FormRequest
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
import pandas as pd

# Logging DEBUG
import logging
logger = logging.getLogger('my_logger')
logging.basicConfig(filename="logfile.txt", 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filemode='w',
                    level = logging.DEBUG)
class MainSpider(scrapy.Spider):
    name = 'main'
    start_urls = ['https://fcainfoweb.nic.in/reports/report_menu_web.aspx']
    
    def parse(self, response):
        formdata = {
            "ctl00$MainContent$Ddl_Rpt_type": "Retail",
            "ctl00$MainContent$ddl_Language": "English",
            "ctl00$MainContent$Rbl_Rpt_type": "Price report",
        }

        yield FormRequest.from_response(
            response=response,
            formdata=formdata,
            # headers=self.headers,
            callback=self.step2
        )
    
    def step2(self, response):
        formdata = {
            "ctl00$MainContent$Ddl_Rpt_type": "Retail",
            "ctl00$MainContent$ddl_Language": "English",
            "ctl00$MainContent$Rbl_Rpt_type": "Price report",
            "ctl00$MainContent$Ddl_Rpt_Option0": "Daily Prices",
        }

        yield FormRequest.from_response(
            response=response,
            formdata=formdata,
            callback=self.step3
        )
    
    def step3(self, response):
        formdata = {
            "ctl00$MainContent$Ddl_Rpt_type": "Retail",
            "ctl00$MainContent$ddl_Language": "English",
            "ctl00$MainContent$Rbl_Rpt_type": "Price report",
            "ctl00$MainContent$Ddl_Rpt_Option0": "Daily Prices",
            "ctl00$MainContent$Txt_FrmDate": "30/01/2023",
            "ctl00$MainContent$btn_getdata1": "Get Data",
        }

        yield FormRequest.from_response(
            response=response,
            formdata=formdata,
            callback=self.parse_table
        )
    
    def parse_table(self, response):
        dfs = pd.read_html(response.text)
        for i, df in enumerate(dfs):
            df.to_csv('Commodity_price_{}.csv'.format(i))