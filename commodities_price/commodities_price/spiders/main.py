import scrapy
from scrapy import FormRequest
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
import pandas as pd

class MainSpider(scrapy.Spider):
    name = 'main'
    #allowed_domains = ['x']
    #start_urls = ['http://x/']

    url = 'https://fcainfoweb.nic.in/reports/report_menu_web.aspx'

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Origin": "https://fcainfoweb.nic.in",
        "Referer": "https://fcainfoweb.nic.in/reports/report_menu_web.aspx",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Microsoft Edge\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\""
    }

    cookies = {
        "ASP.NET_SessionId": "i5ic0b3h21wghmoa1vsaf032",
        "BNI_persistence": "XIlVKPHMyFvRq0HtLj7pmqXxmRx7y7byO_ia3T0PrBLraaAiDz2RxPPPWpXCo2y2SGMfsbBJx4Pe4wWpm_C-OA=="
    }

    body = 'ctl00_MainContent_ToolkitScriptManager1_HiddenField=%3B%3BAjaxControlToolkit%2C+Version%3D4.1.51116.0%2C+Culture%3Dneutral%2C+PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3Afd384f95-1b49-47cf-9b47-2fa2a921a36a%3A475a4ef5%3Aaddc6819%3A5546a2b%3Ad2e10b12%3Aeffe2a26%3A37e2e5c9%3A5a682656%3Ac7029a2%3Ae9e598a9&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=cpoVk%2BPKEDy9BwrXszvHDxUIbmQV4NSt1fEn865v2qbcF1UjbUNp%2FARdta1hcN00WnZJY2iceNNllMCqNwONEaVOx2ZsPfrt6%2BAY1F9qBThSGYptTM9CpvacTeDYKMY9YZcRQpVNBHtzzlAxmtHnTPaFKFk9oZJjnNamX%2BTPB%2F4mcP04xgPOdZEo8n6tPZTvMKjlPAi0oIhhvmueW4v1XbJo0b0OHHDK1Gh5Z7hwxU0gdCgOQECuOcqm7PfJbJNcDRVVJQL7vEg0Zp45QQH6I18F3pE7Y%2F2HO0DUQl%2F6zYgE7oKQ4oylGxeYps%2BYKKWlG%2FCZDgrF0SaMiLaPK79FSa2YzgONVCVpAimHt2ZA2v%2BG%2B4r7nEM1zMSlyGI7xESNrNgV%2BgJtNV%2BxzUcHpJOZhAJ8zct1l9ApOdteOq%2BoJawlqHZLoCVAeFpcTQkC%2Bc76l1PksGa8mFAuQwFeLDj%2BT56Kitn5a0rtwesL70D10guRSe2RKOk%2FaluaVChg13nG4Yw7oXsjHHnDiNG2OD7ilJzYteSjNJKpstjCFKuMbkxFaUqH4q1R%2B3ZjNKk%2BVYtiP%2Fvx0yAF19yygpm%2BegdCg2fZqCbo2DxR2jnJUosq66o%3D&__VIEWSTATEGENERATOR=37FEC614&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=04mRo3PwvsemRdtsG0kIiKQh2DnFR9CavLuTVhb0kwCgHGjOZ2nyypH%2BkOks4zfGSZOY5un7MUbl5g2%2B9PJ0GRZgjzBt7waEUpif%2F46IYuO82MOqcMg3Lz8xMt1cuTIctmikZUApcwNFzGgbu8WIPFxKmtw45RvVSaoq8aqYP9tVIKBHeu7CpEv%2FHiw%2FSYOFRUR3z2k6ZEAnIw05jkICI92Lx%2FCFgp4oOuRj12h1M9bSTYzDFnnOrWqMMrFCB5NNLiqHRjvDDS2ferTBFWWsRm%2FxqAeiJKTMPa%2FtmP0kq53uDL2O4Jy7Yc5HBflzg1NiNOLSQOsVufBofpsPDSbK%2BvGuEpCg8iHk94tArg509rMT%2B6L7fGDP7SjikTRkUXe1CL6hlcoZXndJEUMz93vKOKF0fciOSbxnpa04RolIHJpr2bDI3HwXsqJQPosvd0TU9zofsRi16THWIVBf26u0z2l1cynvJgJxPjDC0SnNiNU%3D&ctl00%24MainContent%24Ddl_Rpt_type=Retail&ctl00%24MainContent%24ddl_Language=English&ctl00%24MainContent%24Rbl_Rpt_type=Price+report&ctl00%24MainContent%24Ddl_Rpt_Option0=Daily+Prices&ctl00%24MainContent%24Txt_FrmDate=30%2F01%2F2023&ctl00%24MainContent%24btn_getdata1=Get+Data'

    

    def start_requests(self):
        yield scrapy.Request(
            url=self.url,
            method='POST',
            dont_filter=True,
            cookies=self.cookies,
            headers=self.headers,
            body=self.body,
        )

    def parse(self, response):
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
            headers=self.headers,
            callback=self.parse_table
        )
    
    def parse_table(self, response):
        open_in_browser(response)