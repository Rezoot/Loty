
import Get_data as gd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta



"""

pomysl pierwszy

pobieramy przez 12 miesięcy każdego dnia dla KAŻDEGO lotniska końcowego najtańsze 2-3 loty do database. 

na początek użytkownik podaje ewentaulnie liste miejsc z których lotnisk go interesują dane
[WAW, GDN]

finalnie dostaniemy wielką strukture database w obu kierunkach 

zostanie wyliczona srednia i znajdywana wartosc minimalna 

import aiohttp??????

KLASY:
Get_link_google - klasa wytwarzająca URL z odnośnikiem do google loty
Database - klasa tworzenia/pobierania danych z database
Get_data - klasa do pobierania informacji z URL (koszt, czas, itp.)


koncowy produkty???   strona/gui/konsola 


aktualnie w porty.csv są wszystkie istniejące lotniska, natomiast jakąś czesc da sie ograniczyc. Jakby sie dalo pobimijac czesc w celu przyspieszenia sprawdzania 
pierwsza mysl jezeli przez miesiac nie ma zadnego lotu to w ogole uniknij dalszego sprawdzania 


"""



if __name__ == "__main__":


    
    
    starting_points=["KTW"]   

    
    #date=datetime.today().strftime('%Y-%m-%d')

    date=(datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    #date=datetime.today().strftime('%Y-%m-%d')
    #date="2026-04-19"
    
    

    #robienie roznych portow asynchronicznie. threating, multiprocesing, jak dziala async (nie wiem) 
    #moze lepsze jest threatowanie linkow, nie jestem pewien. 
    #[linki dobrze jak sa kolejno, porty dowolnie (chyba)]
    #threat+ request lub async + aiohttp
    for start in starting_points:


        #read csv file with ports
        """
        #test 1
        with open("porty.csv") as file:
            for f in file:
                print(date+" lot: "+start+" -> "+ f[:3])
                data=gd.Get_data(start,f[:3])
                data.get_more_info()
                #data.get_info()

                #print(url)
        """


        #get many flights from one start to many ends
        
        #test 2
        print(date+" lot: "+start+" -> "+ "BGY")
        
        data=gd.Get_data(start,"BGY")

        #data.get_more_urls(1,date)
        data.get_more_infos(1, date)
       
        #data.get_info(date)
        for x in data.flights:
            print(x)

        print(data.work/data.all*100)
        


        #test 3
        
        #print(date+" lot: "+start+" -> "+ "ATH")
        #data=gd.Get_data(start,"ATH")
        #data.get_info_httpx(date)

        




        
    
        


    
    
    



