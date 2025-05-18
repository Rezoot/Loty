

import Get_link_google as gl 
import Get_data as gd
import requests
from bs4 import BeautifulSoup



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


    gl=gl.Get_link_google() #generate tfs and url 
    gd=gd.Get_data()

    date="2025-05-30"
    with open("porty.csv") as file:
        for f in file:
            print(date+" lot: GDN -> "+ f[:3])
            tfs = gl.generate_tfs("GDN", f[:3], date)
            url =  gl.generate_flights_url(tfs)
            print(url)
        
        
        
        


    
    
    



