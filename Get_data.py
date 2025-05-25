


from pickle import NONE
from tkinter import NO, SEL
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



        self.flights=[]#list of dictionarys
        #might be changed to dictionary 
          
        """

        informacyjna struktura dla dictionary

        self.flight={
            "date":string,
            "start":string,
            "stop":string,
            "time":datetime string or int(minit) ,
            "cost":int,
            "jumps":int,
            "name":string
            }
        """


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
      
        first_ul=soup.find("ul",class_="Rk10dc")

        if(first_ul==None):
            #write paramiter none or sth later!!!!!!!!!
            print(url)
            return
     
        second_ul=first_ul.find_next("ul")

        #c-cheap
        #e-expensivee

        #idk why but cost is times 3
        cost_c=first_ul.find_all("div",class_=("YMlIz FpEdX jLMuyc"))
        cost_e1=second_ul.find_all("div",class_=("YMlIz FpEdX jLMuyc"))
        cost_e2=second_ul.find_all("div",class_=("YMlIz FpEdX"))

        time_c=first_ul.find_all("div",class_=("gvkrdb AdWm1c tPgKwe ogfYpf"))
        time_e=second_ul.find_all("div",class_=("gvkrdb AdWm1c tPgKwe ogfYpf"))

        jumps_c=first_ul.find_all("div",class_=("EfT7Ae AdWm1c tPgKwe"))
        jumps_e=second_ul.find_all("div",class_=("EfT7Ae AdWm1c tPgKwe"))

        start_stop_c=first_ul.find_all("span",class_=("mv1WYe"))
        start_stop_e=second_ul.find_all("span",class_=("mv1WYe"))
        
        #get name and sth that will skip every second iteration
        name_c=first_ul.find_all("div",class_=("sSHqwe tPgKwe ogfYpf"))
        name_e=second_ul.find_all("div",class_=("sSHqwe tPgKwe ogfYpf"))


        cost_combine=cost_c+cost_e1+cost_e2
        time_combine=time_c+time_e
        jumps_combine=jumps_c+jumps_e
        start_stop_combine=start_stop_c+start_stop_e
        name_combine=name_c+name_e
        
        how_many=len(time_combine)

        

        for i in range(how_many):
            flight={}
            

            start=start_stop_combine[i].find("span",jscontroller="cNtv4b")
            stop=start.find_next("span",jscontroller="cNtv4b")
            jump = jumps_combine[i].span.get_text()[0]
            cost=cost_combine[i*3].span.get_text()[:-3] #respond: '1\xa0616', or '175' 
            time=time_combine[i].get_text()
            if (time[-1]=="n"):
                t=time[-6:-4]
                time=time.replace("godz.","")
                time=int(time[:-6])*60+int(t)
            else: 
                time=int(time[:-6])*60 

            flight["date"] = date
            flight["start"] = start.span.get_text()
            flight["stop"] = stop.span.get_text()
            flight["time"] = time
            flight["cost"] = int(cost[0]+cost[2:]) if cost[1] =='\xa0' else int(cost)
            flight["jumps"] = 0 if jump == 'B' else int(jump)
            flight["name"] = name_combine[i*2].span.get_text()

            self.flights.append(flight)
            





        for x in self.flights:
            print(x)
        


            
        
        
        
    



    #get async info from list of urls
    def get_more_infos(self,day):
        self.get_info(day)
      



    #get list of 30*how_many_months urls
    def get_more_urls(self,how_many_months,date):
        
        self.list_url=[]

        for i in range(how_many_months):
            for j in range(30):
                day=(datetime.strptime(date, '%Y-%m-%d') + timedelta(days=j+30*i)).strftime('%Y-%m-%d')
                
                #self.list_url.append(self.get_url(day))
                self.get_more_infos(day)
                

                
                


        

        


        

    
    
     
        






