from bs4 import BeautifulSoup
import urllib.request
import csv
import os


class  Scrap:
    def __init__(self,name):
        self.name = name


    def info(self):
        nome=self.name
        url= 'https://www.instagram.com/'+nome+'/'
        source= urllib.request.urlopen(url)
        soup = BeautifulSoup(source, 'lxml')
        content= soup.find_all('meta')
        con= content[13].attrs['content'].split('-')[0]
        img= content[15].attrs['content']
        Followers = con.split('Followers, ')[0]
        Followings = con.split('Followers, ')[1].split('Following, ')[0]
        Posts = con.split('Followers')[1].split('Following, ')[1].split('Posts')[0]



        return ""+Followers+","+Followings+","+Posts+","+img







