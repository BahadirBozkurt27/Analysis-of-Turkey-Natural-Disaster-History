#!/usr/bin/env python
# coding: utf-8

# In[914]:


import seaborn as sn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import folium

from tkinter import * 
import tkinter as tk
from tkinter import ttk
import webbrowser
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# In[915]:


#open main window
main_window = tk.Tk()
main_window.geometry("400x300")
main_window.title('Türkiye Afet Bilgi Platformu')


# In[916]:


all_data = pd.read_csv('afet_son_durum.csv')

all_data1 = all_data.copy()

all_data1.rename(columns= {'Year': 'Yıl', 'Disaster Type': 'Afet Türü', 'Location': 'Etkilenen Şehirler', 'Dis Mag Value':
                         'Doğal Afet Ölçeği', 'Total Deaths': 'Ölüm Sayısı', 'Total Affected': 'Etkilenen İnsan Sayısı'},inplace=True)

df = pd.DataFrame(all_data1)

istenen_sütunlar = ['Yıl', 'Afet Türü', 'Etkilenen Şehirler', 'Doğal Afet Ölçeği', 
                 'Ölüm Sayısı', 'Etkilenen İnsan Sayısı']

data = df[istenen_sütunlar]

data

# 'Name' sütununda aranacak kelimeyi içeren satırı bulmak için
aranacak_kelime1 = 'Adana'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime1, na=False)).any(axis=1)]
sayı1 = len(sonuc)

aranacak_kelime2 = 'Adiyaman'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime2, na=False)).any(axis=1)]
sayı2 = len(sonuc)

aranacak_kelime3 = 'Afyonkarahisar'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime3, na=False)).any(axis=1)]
sayı3 = len(sonuc)

aranacak_kelime4 = 'Agri'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime4, na=False)).any(axis=1)]
sayı4 = len(sonuc)

aranacak_kelime5 = 'Amasya'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime5, na=False)).any(axis=1)]
sayı5 = len(sonuc)

aranacak_kelime6 = 'Ankara'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime6, na=False)).any(axis=1)]
sayı6 = len(sonuc)

aranacak_kelime7 = 'Antalya'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime7, na=False)).any(axis=1)]
sayı7 = len(sonuc)

aranacak_kelime8 = 'Artvin'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime8, na=False)).any(axis=1)]
sayı8 = len(sonuc)

aranacak_kelime9= 'Aydin'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime9, na=False)).any(axis=1)]
sayı9 = len(sonuc)

aranacak_kelime10 = 'Balikesir'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime10, na=False)).any(axis=1)]
sayı10 = len(sonuc)

aranacak_kelime11 = 'Bilecik'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime11, na=False)).any(axis=1)]
sayı11 = len(sonuc)

aranacak_kelime12 = 'Bingol'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime12, na=False)).any(axis=1)]
sayı12 = len(sonuc)

aranacak_kelime13 = 'Bitlis'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime13, na=False)).any(axis=1)]
sayı13 = len(sonuc)

aranacak_kelime14 = 'Bolu'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime14, na=False)).any(axis=1)]
sayı14 = len(sonuc)

aranacak_kelime15 = 'Burdur'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime15, na=False)).any(axis=1)]
sayı15 = len(sonuc)

aranacak_kelime16 = 'Bursa'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime16, na=False)).any(axis=1)]
sayı16 = len(sonuc)

aranacak_kelime17 = 'Canakkale'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime17, na=False)).any(axis=1)]
sayı17 = len(sonuc)

aranacak_kelime18 = 'Cankiri'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime18, na=False)).any(axis=1)]
sayı18 = len(sonuc)

aranacak_kelime19 = 'Corum'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime19, na=False)).any(axis=1)]
sayı19 = len(sonuc)

aranacak_kelime20 = 'Denizli'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime20, na=False)).any(axis=1)]
sayı20 = len(sonuc)

aranacak_kelime21 = 'Diyarbakir'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime21, na=False)).any(axis=1)]
sayı21 = len(sonuc)

aranacak_kelime22 = 'Edirne'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime22, na=False)).any(axis=1)]
sayı22 = len(sonuc)

aranacak_kelime23 = 'Elazig'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime23, na=False)).any(axis=1)]
sayı23 = len(sonuc)

aranacak_kelime24 = 'Erzincan'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime24, na=False)).any(axis=1)]
sayı24 = len(sonuc)

aranacak_kelime25 = 'Erzurum'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime25, na=False)).any(axis=1)]
sayı25 = len(sonuc)

aranacak_kelime26 = 'Eskisehir'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime26, na=False)).any(axis=1)]
sayı26 = len(sonuc)

aranacak_kelime27 = 'Gaziantep'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime27, na=False)).any(axis=1)]
sayı27 = len(sonuc)

aranacak_kelime28 = 'Giresun'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime28, na=False)).any(axis=1)]
sayı28 = len(sonuc)

aranacak_kelime29 = 'Gumushane'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime29, na=False)).any(axis=1)]
sayı29 = len(sonuc)

aranacak_kelime30 = 'Hakkari'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime30, na=False)).any(axis=1)]
sayı30 = len(sonuc)

aranacak_kelime31 = 'Hatay'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime31, na=False)).any(axis=1)]
sayı31 = len(sonuc)

aranacak_kelime32 = 'Isparta'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime32, na=False)).any(axis=1)]
sayı32 = len(sonuc)

aranacak_kelime33 = 'Mersin'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime33, na=False)).any(axis=1)]
sayı33 = len(sonuc)

aranacak_kelime34 = 'Istanbul'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime34, na=False)).any(axis=1)]
sayı34 = len(sonuc)

aranacak_kelime35 = 'Izmir'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime35, na=False)).any(axis=1)]
sayı35 = len(sonuc)

aranacak_kelime36 = 'Kars'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime36, na=False)).any(axis=1)]
sayı36 = len(sonuc)

aranacak_kelime37 = 'Kastamonu'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime37, na=False)).any(axis=1)]
sayı37 = len(sonuc)

aranacak_kelime38 = 'Kayseri'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime38, na=False)).any(axis=1)]
sayı38 = len(sonuc)

aranacak_kelime39 = 'Kirklareli'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime39, na=False)).any(axis=1)]
sayı39 = len(sonuc)

aranacak_kelime40 = 'Kirsehir'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime40, na=False)).any(axis=1)]
sayı40 = len(sonuc)

aranacak_kelime41 = 'Kocaeli'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime41, na=False)).any(axis=1)]
sayı41 = len(sonuc)

aranacak_kelime42 = 'Konya'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime42, na=False)).any(axis=1)]
sayı42 = len(sonuc)

aranacak_kelime43 = 'Kutahya'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime43, na=False)).any(axis=1)]
sayı43 = len(sonuc)

aranacak_kelime44 = 'Malatya'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime44, na=False)).any(axis=1)]
sayı44 = len(sonuc)

aranacak_kelime45 = 'Manisa'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime45, na=False)).any(axis=1)]
sayı45 = len(sonuc)

aranacak_kelime46 = 'Kahramanmaras'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime46, na=False)).any(axis=1)]
sayı46 = len(sonuc)

aranacak_kelime47 = 'Mardin'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime47, na=False)).any(axis=1)]
sayı47 = len(sonuc)

aranacak_kelime48 = 'Mugla'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime48, na=False)).any(axis=1)]
sayı48 = len(sonuc)

aranacak_kelime49 = 'Mus'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime49, na=False)).any(axis=1)]
sayı49 = len(sonuc)

aranacak_kelime50 = 'Nevsehir'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime50, na=False)).any(axis=1)]
sayı50 = len(sonuc)

aranacak_kelime51 = 'Nigde'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime51, na=False)).any(axis=1)]
sayı51 = len(sonuc)

aranacak_kelime52 = 'Ordu'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime52, na=False)).any(axis=1)]
sayı52 = len(sonuc)

aranacak_kelime53 = 'Rize'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime53, na=False)).any(axis=1)]
sayı53 = len(sonuc)

aranacak_kelime54 = 'Sakarya'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime54, na=False)).any(axis=1)]
sayı54 = len(sonuc)

aranacak_kelime55 = 'Samsun'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime55, na=False)).any(axis=1)]
sayı55 = len(sonuc)

aranacak_kelime56 = 'Siirt'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime56, na=False)).any(axis=1)]
sayı56 = len(sonuc)

aranacak_kelime57 = 'Sinop'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime57, na=False)).any(axis=1)]
sayı57 = len(sonuc)

aranacak_kelime58 = 'Sivas'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime58, na=False)).any(axis=1)]
sayı58 = len(sonuc)

aranacak_kelime59 = 'Tekirdag'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime59, na=False)).any(axis=1)]
sayı59 = len(sonuc)

aranacak_kelime60 = 'Tokat'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime60, na=False)).any(axis=1)]
sayı60 = len(sonuc)

aranacak_kelime61 = 'Trabzon'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime61, na=False)).any(axis=1)]
sayı61 = len(sonuc)

aranacak_kelime62 = 'Tunceli'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime62, na=False)).any(axis=1)]
sayı62 = len(sonuc)

aranacak_kelime63 = 'Sanliurfa'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime63, na=False)).any(axis=1)]
sayı63 = len(sonuc)

aranacak_kelime64 = 'Usak'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime64, na=False)).any(axis=1)]
sayı64 = len(sonuc)

aranacak_kelime65 = 'Van'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime65, na=False)).any(axis=1)]
sayı65 = len(sonuc)

aranacak_kelime66 = 'Yozgat'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime66, na=False)).any(axis=1)]
sayı66 = len(sonuc)

aranacak_kelime67 = 'Zonguldak'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime67, na=False)).any(axis=1)]
sayı67 = len(sonuc)

aranacak_kelime68 = 'Aksaray'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime68, na=False)).any(axis=1)]
sayı68 = len(sonuc)

aranacak_kelime69 = 'Bayburt'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime69, na=False)).any(axis=1)]
sayı69 = len(sonuc)

aranacak_kelime70 = 'Karaman'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime70, na=False)).any(axis=1)]
sayı70 = len(sonuc)

aranacak_kelime71 = 'Kirikkale'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime71, na=False)).any(axis=1)]
sayı71 = len(sonuc)

aranacak_kelime72 = 'Batman'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime72, na=False)).any(axis=1)]
sayı72 = len(sonuc)

aranacak_kelime73 = 'Sırnak'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime73, na=False)).any(axis=1)]
sayı73 = len(sonuc)

aranacak_kelime74 = 'Bartin'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime74, na=False)).any(axis=1)]
sayı74 = len(sonuc)

aranacak_kelime75 = 'Ardahan'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime75, na=False)).any(axis=1)]
sayı75 = len(sonuc)

aranacak_kelime76 = 'İgdir'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime76, na=False)).any(axis=1)]
sayı76 = len(sonuc)

aranacak_kelime77 = 'Yalova'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime77, na=False)).any(axis=1)]
sayı77 = len(sonuc)

aranacak_kelime78 = 'Karabuk'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime78, na=False)).any(axis=1)]
sayı78 = len(sonuc)

aranacak_kelime79 = 'Kilis'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime79, na=False)).any(axis=1)]
sayı79 = len(sonuc)

aranacak_kelime80 = 'Osmaniye'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime80, na=False)).any(axis=1)]
sayı80 = len(sonuc)

aranacak_kelime81 = 'Duzce'
sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime81, na=False)).any(axis=1)]
sayı81 = len(sonuc)



# Türkiye'nin merkezi koordinatları
turkiye_merkezi = [38.9208, 32.8541]

# Folium harita nesnesi oluşturalım
harita = folium.Map(location=turkiye_merkezi, zoom_start=6)

# Örnek veri oluşturalım
veri = [
    
    {'il': 'Adana', 'sayi': sayı1 , 'koordinat': (37.0017, 35.3289)},
    {'il': 'Adıyaman', 'sayi': sayı2, 'koordinat': (37.7648, 38.2766)},
    {'il': 'Afyonkarahisar', 'sayi': sayı3, 'koordinat': (38.7560, 30.5387)},
    {'il': 'Ağrı', 'sayi': sayı4, 'koordinat': (39.7191, 43.0503)},
    {'il': 'Amasya', 'sayi': sayı5, 'koordinat': (40.6539, 35.8336)},
    {'il': 'Ankara', 'sayi': sayı6, 'koordinat': (39.9334, 32.8597)},
    {'il': 'Antalya', 'sayi': sayı7, 'koordinat': (36.8969, 30.7133)},
    {'il': 'Artvin', 'sayi': sayı8, 'koordinat': (41.1828, 41.8176)},
    {'il': 'Aydın', 'sayi': sayı9, 'koordinat': (37.8560, 27.8416)},
    {'il': 'Balıkesir', 'sayi': sayı10, 'koordinat': (39.6484, 27.8826)},
    {'il': 'Bilecik', 'sayi': sayı11, 'koordinat': (40.0567, 30.0665)},
    {'il': 'Bingöl', 'sayi': sayı12, 'koordinat': (39.0626, 40.7696)},
    {'il': 'Bitlis', 'sayi': sayı13, 'koordinat': (38.3938, 42.1230)},
    {'il': 'Bolu', 'sayi': sayı14, 'koordinat': (40.5750, 31.5788)},
    {'il': 'Burdur', 'sayi': sayı15, 'koordinat': (37.4615, 30.0665)},
    {'il': 'Bursa', 'sayi': sayı16, 'koordinat': (40.2669, 29.0634)},
    {'il': 'Çanakkale', 'sayi': sayı17, 'koordinat': (40.1553, 26.4142)},
    {'il': 'Çankırı', 'sayi': sayı18, 'koordinat': (40.6013, 33.6134)},
    {'il': 'Çorum', 'sayi': sayı19, 'koordinat': (40.5506, 34.9556)},
    {'il': 'Denizli', 'sayi': sayı20, 'koordinat': (37.7765, 29.0864)},
    {'il': 'Diyarbakır', 'sayi': sayı21, 'koordinat': (37.9144, 40.2306)},
    {'il': 'Edirne', 'sayi': sayı22, 'koordinat': (41.6818, 26.5623)},
    {'il': 'Elazığ', 'sayi': sayı23, 'koordinat': (38.6810, 39.2264)},
    {'il': 'Erzincan', 'sayi': sayı24, 'koordinat': (39.7500, 39.5000)},
    {'il': 'Erzurum', 'sayi': sayı25, 'koordinat': (39.9086, 41.2765)},
    {'il': 'Eskişehir', 'sayi': sayı26, 'koordinat': (39.7663, 30.5256)},
    {'il': 'Gaziantep', 'sayi': sayı27, 'koordinat': (37.0662, 37.3833)},
    {'il': 'Giresun', 'sayi': sayı28, 'koordinat': (40.9128, 38.3895)},
    {'il': 'Gümüşhane', 'sayi': sayı29, 'koordinat': (40.4608, 39.4819)},
    {'il': 'Hakkari', 'sayi': sayı30, 'koordinat': (37.5744, 43.7408)},
    {'il': 'Hatay', 'sayi': sayı31, 'koordinat': (36.2048, 36.5619)},
    {'il': 'Isparta', 'sayi': sayı32, 'koordinat': (37.7648, 30.5526)},
    {'il': 'Mersin', 'sayi': sayı33, 'koordinat': (36.8000, 34.6127)},
    {'il': 'İstanbul', 'sayi': sayı34, 'koordinat': (41.0082, 28.9784)},
    {'il': 'İzmir', 'sayi': sayı35, 'koordinat': (38.4192, 27.1287)},
    {'il': 'Kars', 'sayi': sayı36, 'koordinat': (40.5966, 43.0772)},
    {'il': 'Kastamonu', 'sayi': sayı37, 'koordinat': (41.3768, 33.7635)},
    {'il': 'Kayseri', 'sayi': sayı38, 'koordinat': (38.7223, 35.4853)},
    {'il': 'Kırklareli', 'sayi': sayı39, 'koordinat': (41.7333, 27.2167)},
    {'il': 'Kırşehir', 'sayi': sayı40, 'koordinat': (39.1425, 34.1709)},
    {'il': 'Kocaeli', 'sayi': sayı41, 'koordinat': (40.8533, 29.8815)},
    {'il': 'Konya', 'sayi': sayı42, 'koordinat': (37.8775, 32.4818)},
    {'il': 'Kütahya', 'sayi': sayı43, 'koordinat': (39.4167, 29.9833)},
    {'il': 'Malatya', 'sayi': sayı44, 'koordinat': (38.3552, 38.3095)},
    {'il': 'Manisa', 'sayi': sayı45, 'koordinat': (38.6191, 27.4289)},
    {'il': 'Kahramanmaraş', 'sayi': sayı46, 'koordinat': (37.5858, 36.9371)},
    {'il': 'Mardin', 'sayi': sayı47, 'koordinat': (37.3124, 40.7425)},
    {'il': 'Muğla', 'sayi': sayı48, 'koordinat': (37.2150, 28.3636)},
    {'il': 'Muş', 'sayi': sayı49, 'koordinat': (38.9462, 41.7539)},
    {'il': 'Nevşehir', 'sayi': sayı50, 'koordinat': (38.6939, 34.6857)},
    {'il': 'Niğde', 'sayi': sayı51, 'koordinat': (37.9667, 34.6794)},
    {'il': 'Ordu', 'sayi': sayı52, 'koordinat': (40.9839, 37.8764)},
    {'il': 'Rize', 'sayi': sayı53, 'koordinat': (41.0201, 40.5234)},
    {'il': 'Sakarya', 'sayi': sayı54, 'koordinat': (40.6940, 30.4358)},
    {'il': 'Samsun', 'sayi': sayı55, 'koordinat': (41.2928, 36.3313)},
    {'il': 'Siirt', 'sayi': sayı56, 'koordinat': (37.9333, 41.9500)},
    {'il': 'Sinop', 'sayi': sayı57, 'koordinat': (42.0265, 35.1555)},
    {'il': 'Sivas', 'sayi': sayı58, 'koordinat': (39.7477, 37.0179)},
    {'il': 'Tekirdağ', 'sayi': sayı59, 'koordinat': (40.9833, 27.5167)},
    {'il': 'Tokat', 'sayi': sayı60, 'koordinat': (40.3167, 36.5500)},
    {'il': 'Trabzon', 'sayi': sayı61, 'koordinat': (41.0000, 39.7333)},
    {'il': 'Tunceli', 'sayi': sayı62, 'koordinat': (39.1063, 39.5486)},
    {'il': 'Şanlıurfa', 'sayi': sayı63, 'koordinat': (37.1591, 38.7969)},
    {'il': 'Uşak', 'sayi': sayı64, 'koordinat': (38.6823, 29.4082)},
    {'il': 'Van', 'sayi': sayı65, 'koordinat': (38.4924, 43.3833)},
    {'il': 'Yozgat', 'sayi': sayı66, 'koordinat': (39.8181, 34.8147)},
    {'il': 'Zonguldak', 'sayi': sayı67, 'koordinat': (41.4564, 31.7987)},
    {'il': 'Aksaray', 'sayi': sayı68, 'koordinat': (38.3687, 34.0370)},
    {'il': 'Bayburt', 'sayi': sayı69, 'koordinat': (40.2551, 40.2249)},
    {'il': 'Karaman', 'sayi': sayı70, 'koordinat': (37.1759, 33.2287)},
    {'il': 'Kırıkkale', 'sayi': sayı71, 'koordinat': (39.8417, 33.5139)},
    {'il': 'Batman', 'sayi': sayı72, 'koordinat': (37.8812, 41.1351)},
    {'il': 'Şırnak', 'sayi': sayı73, 'koordinat': (37.4187, 42.4918)},
    {'il': 'Bartın', 'sayi': sayı74, 'koordinat': (41.5811, 32.4610)},
    {'il': 'Ardahan', 'sayi': sayı75, 'koordinat': (41.1104, 42.7022)},
    {'il': 'Iğdır', 'sayi': sayı76, 'koordinat': (39.9225, 44.0397)},
    {'il': 'Yalova', 'sayi': sayı77, 'koordinat': (40.6550, 29.2769)},
    {'il': 'Karabük', 'sayi': sayı78, 'koordinat': (41.2048, 32.6207)},
    {'il': 'Kilis', 'sayi': sayı79, 'koordinat': (36.7160, 37.1150)},
    {'il': 'Osmaniye', 'sayi': sayı80, 'koordinat': (37.0742, 36.2476)},
    {'il': 'Düzce', 'sayi': sayı81, 'koordinat': (40.8438, 31.1565)}
   
    
]

# Veriyi işaretçilerle haritaya ekleyelim
for veri_satiri in veri:
    folium.Marker(location=veri_satiri['koordinat'], popup=f"İl: {veri_satiri['il']}, Sayı: {veri_satiri['sayi']}").add_to(harita)

def harita_goster():
    harita.save('map.html')
    # Haritayı varsayılan web tarayıcısıyla aç
    webbrowser.open('map.html')

#haritayıgösterbutonu    
button_haritayı_goster = tk.Button(main_window, 
                              text='  Haritayı   Göster  ',
                              activebackground="red",
                              bd=2,
                              bg='black',
                              command=harita_goster,
                              fg="white",
                              font=("calibri",14,"bold"),
                              height=3)
button_haritayı_goster.place(x=30,y=50)



# In[917]:


# function to open other windows
def open_sehirbazli():
    main_window.destroy()
    sehirbazli_window = tk.Tk()
    sehirbazli_window.title("Şehir Bazlı Arama")
    sehirbazli_window.geometry("300x200")
    
    # Sehirler Combobox creation
    sehirler = ttk.Combobox(sehirbazli_window, width = 20)
    sehirler.grid(column = 1, row = 82)
    sehirler['values'] = ('Sehir Secin','Adana', 'Adiyaman', 'Afyonkarahisar', 'Agri', 'Amasya', 'Ankara', 'Antalya',
                          'Artvin', 'Aydin', 'Balikesir', 'Bilecik', 'Bingol', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 
                          'Canakkale', 'Cankiri', 'Corum', 'Denizli', 'Diyarbakir', 'Edirne', 'Elazig', 'Erzincan',
                          'Erzurum', 'Eskisehir', 'Gaziantep', 'Giresun', 'Gumushane', 'Hakkari', 'Hatay', 'Isparta',
                          'Mersin', 'Istanbul', 'Izmir', 'Kars', 'Kastamonu', 'Kayseri', 'Kirklareli', 'Kirsehir',
                          'Kocaeli', 'Konya', 'Kutahya', 'Malatya', 'Manisa', 'Kahramanmaras', 'Mardin', 'Mugla', 
                          'Mus', 'Nevsehir', 'Nigde', 'Ordu', 'Rize', 'Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas',
                          'Tekirdag', 'Tokat', 'Trabzon', 'Tunceli', 'Sanliurfa', 'Usak', 'Van', 'Yozgat', 'Zonguldak',
                          'Aksaray', 'Bayburt', 'Karaman', 'Kirikkale', 'Batman', 'Sirnak', 'Bartin', 'Ardahan', 'Igdir',
                          'Yalova', 'Karabuk', 'Kilis', 'Osmaniye', 'Duzce')
    sehirler.current(0) 
    sehirler.place(x=25,y=25)
    
    def sehir_bilgi_getir():
        aranacak_kelime = sehirler.get()
        sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime, na=False)).any(axis=1)]
        sonuc=sonuc.sort_values('Ölüm Sayısı', ascending=False)
        
        sehirbazli_window2 = tk.Tk()
        sehirbazli_window2.title("Sonuçlar")
        sehirbazli_window2.geometry("1500x500")
        
        #treeview oluştur ve sütunları belirle
        treeview_sehirbazli = ttk.Treeview(sehirbazli_window2)
        treeview_sehirbazli['columns'] = tuple(sonuc.columns)
        
        #treeview sütunlarını başlık olarak ekle
        for column in sonuc.columns:
            treeview_sehirbazli.heading(column, text=column)
        
        #DataFrame verilerini Treeview'a ekle
        for index, row in sonuc.iterrows():
            treeview_sehirbazli.insert("", tk.END, text=index, values=tuple(row))
        
        #Scrollbar ekle
        scrollbar_sehirbazli = ttk.Scrollbar(sehirbazli_window2, orient="vertical", command=treeview_sehirbazli.yview)
        treeview_sehirbazli.configure(yscrollcommand=scrollbar_sehirbazli.set)    
        scrollbar_sehirbazli.pack(side="right", fill="y")    
        treeview_sehirbazli.pack(expand=True, fill=tk.BOTH)
        sehirbazli_window2.mainloop()
        
        sehirbazli_window.mainloop()


    #sehirbilgigetirbutonu    
    sehir_bilgi_getir_button = tk.Button(sehirbazli_window, 
                                      text='GETİR',
                                      activebackground="red",
                                      bd=2,
                                      bg='black',
                                      command=sehir_bilgi_getir,
                                      fg="white",
                                      font=("calibri",14,"bold"),
                                      height=1)
    sehir_bilgi_getir_button.place(x=200,y=20)



    sehirbazli_window.mainloop()
    
  
    
#şehirbazlıaramabutonu    
button_sehirbazli = tk.Button(main_window, 
                              text='Şehre Göre Arama',
                              activebackground="red",
                              bd=2,
                              bg='black',
                              command=open_sehirbazli,
                              fg="white",
                              font=("calibri",14,"bold"),
                              height=3)
button_sehirbazli.place(x=30,y=150)



# In[918]:


def open_afetbazli():
    main_window.destroy()
    afetbazli_window = tk.Tk()
    afetbazli_window.title("Afet Bazlı Arama")
    afetbazli_window.geometry("300x200")
    
    # Afetler COMBOBOX creation
    afetler = ttk.Combobox(afetbazli_window, width = 20)
    afetler.grid(column = 1, row = 5)
    afetler['values'] = ('Afet Secin','Earthquake', 'Flood', 'Extreme temperature', 'Storm')
    afetler.current(0) 
    afetler.place(x=25,y=25)

    def afet_bilgi_getir():
        aranacak_kelime = afetler.get()
        sonuc = data[data.apply(lambda x: x.astype(str).str.contains(aranacak_kelime, na=False)).any(axis=1)]
        sonuc=sonuc.sort_values('Ölüm Sayısı', ascending=False)
        
        afetbazli_window2 = tk.Tk()
        afetbazli_window2.title("Sonuçlar")
        afetbazli_window2.geometry("1500x500")
        
        #treeview oluştur ve sütunları belirle
        treeview_afetbazli = ttk.Treeview(afetbazli_window2)
        treeview_afetbazli['columns'] = tuple(sonuc.columns)
        
        #treeview sütunlarını başlık olarak ekle
        for column in sonuc.columns:
            treeview_afetbazli.heading(column, text=column)
        
        #DataFrame verilerini Treeview'a ekle
        for index, row in sonuc.iterrows():
            treeview_afetbazli.insert("", tk.END, text=index, values=tuple(row))
        
        #Scrollbar ekle
        scrollbar_afetbazli = ttk.Scrollbar(afetbazli_window2, orient="vertical", command=treeview_afetbazli.yview)
        treeview_afetbazli.configure(yscrollcommand=scrollbar_afetbazli.set)    
        scrollbar_afetbazli.pack(side="right", fill="y")    
        treeview_afetbazli.pack(expand=True, fill=tk.BOTH)
        
        afetbazli_window2.mainloop()
        
        afetbazli_window.mainloop()

        
    #afetbilgigetirbutonu    
    afet_bilgi_getir_button = tk.Button(afetbazli_window, 
                                      text='GETİR',
                                      activebackground="red",
                                      bd=2,
                                      bg='black',
                                      command=afet_bilgi_getir,
                                      fg="white",
                                      font=("calibri",14,"bold"),
                                      height=1)
    afet_bilgi_getir_button.place(x=200,y=20)
    
    afetbazli_window.mainloop()
    
#afetbazlıaramabutonu
button_afetbazli = tk.Button(main_window, 
                              text='Afete Göre Arama',
                              activebackground="red",
                              bd=2,
                              bg='black',
                              command=open_afetbazli,
                              fg="white",
                              font=("calibri",14,"bold"),
                              height=3)
button_afetbazli.place(x=200,y=150)




# In[919]:


def open_gorselveri():
    main_window.destroy()
    gorselveri_window = tk.Tk()
    gorselveri_window.title("Görsel Verilerle Afetleri Karşılaştırma")
    gorselveri_window.geometry("800x700")
    
    # Afetler COMBOBOX-1 creation
    afet1 = ttk.Combobox(gorselveri_window, width = 30)
    afet1.grid(column = 1, row = 6)
    afet1['values'] = ('Afet Secin', '2023 Pazarcık Depremi (50096)', '1939 Erzincan Depremi (32962)', 
        '#1999 Depremi (17127)', '1943 Samsun Depremi (4020)','2020 İzmir Depremi(115)')
    afet1.current(0) 
    afet1.place(x=70,y=30)
    
    label = tk.Label(gorselveri_window, text="&")
    label.grid(row=1, column=0, columnspan=2, padx=300, pady=30)

    # Afetler COMBOBOX-2 creation
    afet2 = ttk.Combobox(gorselveri_window, width = 30)
    afet2.grid(column = 1, row = 6)
    afet2['values'] = ('Afet Secin', '2023 Pazarcık Depremi (50096)', '1939 Erzincan Depremi (32962)', 
        '#1999 Depremi (17127)', '1943 Samsun Depremi (4020)','2020 İzmir Depremi(115)')
    afet2.current(0) 
    afet2.place(x=350,y=30)
    
    def afet_karsilastir():
        
        kelime1 = ' '
        kelime2 = ' '
        def ilk_afet():
            if(afet1.get() == "2023 Pazarcık Depremi (50096)"):
                kelime1 = '50096'
            elif(afet1.get() == "1939 Erzincan Depremi (32962)"):
                kelime1 = '32962'
            elif(afet1.get() == "#1999 Depremi (17127)"):
                kelime1 = '17127'
            elif(afet1.get() == "1943 Samsun Depremi (4020)"):
                kelime1 = '4020'
            elif(afet1.get() == "2020 İzmir Depremi(115)"):
                kelime1 = '115'
            else:
                kelime1=''
        
        def ikinci_afet():
            if(afet2.get() == "2023 Pazarcık Depremi (50096)"):
                kelime2 = '50096'
            elif(afet2.get() == "1939 Erzincan Depremi (32962)"):
                kelime2 = '32962'
            elif(afet2.get() == "#1999 Depremi (17127)"):
                kelime2 = '17127'
            elif(afet2.get() == "1943 Samsun Depremi (4020)"):
                kelime2 = '4020'
            elif(afet2.get() == "2020 İzmir Depremi(115)"):
                kelime2 = '115'
            else:
                kelime2=''
        
        deneme = data[data.apply(lambda x: x.astype(str).str.contains(kelime1, na=False)).any(axis=1) | 
              data.apply(lambda x: x.astype(str).str.contains(kelime2, na=False)).any(axis=1)  
             ]

        deneme1 = pd.DataFrame(deneme)

        deneme2 = all_data1[all_data.apply(lambda x: x.astype(str).str.contains(kelime1, na=False)).any(axis=1) | 
                      all_data1.apply(lambda x: x.astype(str).str.contains(kelime2, na=False)).any(axis=1) 
                     ]

        istenen_sütunlar = ['Yıl', 'Total Damages (\'000 US$)']

        deneme3 = deneme2[istenen_sütunlar]

        # Çubuk grafik oluşturma

        fig1 = Figure(figsize=(7,3), dpi=100)
        ax = fig1.add_subplot(111)
        ax.bar(deneme1['Yıl'], deneme1['Ölüm Sayısı'])
        ax.set_xlabel('Yıl')
        ax.set_ylabel('Ölüm Sayısı')
        ax.set_title('Ölüm Sayıları')

        fig2 = Figure(figsize=(7, 3), dpi=100)
        ax = fig2.add_subplot(111)
        ax.bar(deneme3['Yıl'], deneme3['Total Damages (\'000 US$)'], log = True)
        ax.set_xlabel('Yıl')
        ax.set_ylabel('Maddi Kayıp')
        ax.set_title('Toplam Hasarın Maddi Değeri')

        # FigureCanvasTkAgg ile grafik nesnesini oluşturma
        canvas = FigureCanvasTkAgg(fig1, master=gorselveri_window)
        canvas.draw()
        canvas.get_tk_widget().grid(padx=50)

        canvas = FigureCanvasTkAgg(fig2, master=gorselveri_window)
        canvas.draw()
        canvas.get_tk_widget().grid(padx=50)

    
    
    #afetkarşılaştır butonu    
    afet_karsilastir_button = tk.Button(gorselveri_window, 
                                      text='Karşılaştır',
                                      activebackground="red",
                                      bd=2,
                                      bg='black',
                                      command=afet_karsilastir,
                                      fg="white",
                                      font=("calibri",14,"bold"),
                                      height=1, width=10)
    afet_karsilastir_button.place(x=600,y=20)
    
    gorselveri_window.mainloop()

#gorselveributonu
button_gorselveri = tk.Button(main_window, 
                              text='Afetleri Karşılaştır',
                              activebackground="red",
                              bd=2,
                              bg='black',
                              command=open_gorselveri,
                              fg="white",
                              font=("calibri",14,"bold"),
                              height=3)
button_gorselveri.place(x=200,y=50)

main_window.mainloop()


# In[ ]:




