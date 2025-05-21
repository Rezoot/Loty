


from pickle import NONE
from tkinter import NO
import Get_link_google as gl 
from datetime import datetime, timedelta
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
        
        self.list_url=[]

        self.flights=[]
        #might be changed to dictionary 
           


        
        self.flight={
            "date":"",
            "cost":0,
            "time":0,
            "airplain":0,
            "name":""
            }



        if(start_date==None):
            self.date=datetime.today().strftime('%Y-%m-%d')

    
    #return url to google from date
    def get_url(self,date):
        link=gl.Get_link_google() #generate tfs and url 
        tfs = link.generate_tfs(self.start, self.end,date)
        return link.generate_flights_url(tfs)

            
    
    #get one info about cost and times
    def get_info(self,date):

        url=self.get_url(date)
        website = requests.get(url)
        soup = BeautifulSoup(website.content, 'html.parser')

        print(url)




    #get async info from list of urls
    def get_more_infos(self):
        pass
      



    #get list of 30*how_many_months urls
    def get_more_urls(self,how_many_months,date):
        
        self.list_url=[]

        for i in range(how_many_months):
            for j in range(30):
                day=(datetime.strptime(date, '%Y-%m-%d') + timedelta(days=j+30*i)).strftime('%Y-%m-%d')
                self.list_url.append(self.get_url(day))
                

                
                


        

        


        

    
    
     
        






