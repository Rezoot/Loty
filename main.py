

import Get_link_google as gl 
import requests
from bs4 import BeautifulSoup



if __name__ == "__main__":


    gl=gl.Get_link_google() #generate tfs and url 
 
    date="2025-05-30"
    with open("porty.csv") as file:
        for f in file:
            print(date+" lot: GDN -> "+ f[:3])
            tfs = gl.generate_tfs("GDN", f[:3], date)
            url =  gl.generate_flights_url(tfs)
            print(url)
        
        
        
        


    
    
    



