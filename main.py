import requests
import csv
from bs4 import BeautifulSoup

BASE_URL_HOME='https://www.sportytrader.pt/resultados-directo/futebol/inglaterra/premier-league-49/'
BASE_URL_AWAY='https://www.futebol.com/futebol/inglaterra/equipos/newcastle/'

def scan_page(url):
    page = requests.get(url)
    print(page.status_code)
    return page

def at_home_search(page):
    lista = []
    #Realiza leitura do html
    soup = BeautifulSoup(page.text, 'html.parser')
    #Pega todos os jogos do Watford
    lista=[]
    games= soup.find('div','container-list-compet_49')
    print(games)
    #lista= games.text.split('\n')
    #equipes =games.find_all('nome_popular')
    #print(games)
    visitante=  games.find_all('span','homeScore')
    mandante = games.find_all('span','homeScore')
    for home in games.find_all('div','score-compet'):
        print(home)


    print(mandante)
    print(visitante)



    #for row in lista:
        #index=row.find('Watford')
        #if index ==0:


    return games

def writer_csv(arquivo):
    convert =csv.writer(open('mandante.csv','w'))
    writ=convert.writerow(arquivo)
    return  writ



def away_search(page):
    lista = []
    # Realiza leitura do html
    soup = BeautifulSoup(page.text, 'html.parser')
    # Pega todos os jogos do Newcastle
    games = soup.find('div', 'panel panel-default panel-match-listing-participant')
    #Atribui html em uma lista
    lista = games.text.split('\n')

    print(lista)


if __name__ == '__main__':
    home=scan_page(BASE_URL_HOME)
    #away=scan_page(BASE_URL_AWAY)
    game_home=at_home_search(home)
    #conv=writer_csv(game_home)
    #game_away=away_search(away)







