


from pickle import NONE
from tkinter import NO
import Get_link_google as gl 
from datetime import datetime
import requests
from bs4 import BeautifulSoup


"""
Get data from url 
cost sth


"""

class Get_data:
    
    
    def __init__(self,start_point,end_point,start_date=None):
        
        self.link="" 
        self.start=start_point
        self.end=end_point
        self.start_date=start_date #from witch day start scraping 
        
        self.date=[]
        self.cost=[]
        self.time=[]
        self.airplains=[]
        
        if(start_date==None):
            self.date=datetime.today().strftime('%Y-%m-%d')

        
    def get_url(self,date):
        link=gl.Get_link_google() #generate tfs and url 
        tfs = link.generate_tfs(self.start, self.end,date)
        return link.generate_flights_url(tfs)

            
    
    def get_info(self,date=datetime.today().strftime('%Y-%m-%d')):

        url=self.get_url(date)
        print(url)



        
        




    def get_more_info(self,how_long=12):

        for i in range(how_long):
            pass

        

        


        

    
    
     
        






