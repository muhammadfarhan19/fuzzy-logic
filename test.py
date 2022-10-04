from tabulate import tabulate

listBau = []
listLembab = []

def aromaBuah() :
    if bau < 40 :
        if bau <= 20 :
            bauSedikit = (bau - 0) / (20 - 0)
            lumayanBau = 0
            Bau = 0
            sangatBau = 0
        elif bau > 20 and bau <= 40 :
            bauSedikit = (40- bau) / (40 - 20)
            lumayanBau = (bau - 20) / (40 - 20)
            Bau = 0
            sangatBau = 0
    elif bau >= 20 and bau < 60 :
        if bau >= 20 and bau <= 40 :
            bauSedikit = (40 - bau) / (40 - 20)
            lumayanBau = (bau - 20) / (40 - 20)
            Bau = 0
            sangatBau = 0
        elif bau > 40 and bau < 60 :
            bauSedikit = 0
            lumayanBau = (60 - bau) / (60 - 40)
            Bau = (bau - 40) / (60 - 40)
            sangatBau = 0
    elif bau >= 40 and bau < 80 :
        if bau >= 40 and bau <= 60 :
            bauSedikit = 0
            lumayanBau = (60 - bau) / (60 - 40)
            Bau = (bau - 40) / (60 - 40)
            sangatBau = 0
        elif bau > 60 and bau <80 :
            bauSedikit = 0
            lumayanBau = 0
            Bau = (80 - bau) / (80 - 60)
            sangatBau = (bau - 80) / (80 - 60)
    elif bau >= 60 and bau <= 100 :
        if bau >= 60 and bau <= 80 :
            bauSedikit = 0
            lumayanBau = 0
            Bau = (80 - bau) / (80 - 60)
            sangatBau =  (bau - 40) / (60 - 40)
        elif bau > 80 and bau <= 100 :
            bauSedikit = 0
            lumayanBau = 0
            Bau = 0
            sangatBau = (100 - bau) / (100 - 80)

    listBau.extend([bauSedikit, lumayanBau, Bau, sangatBau])
    return listBau



def kelembapanBuah() :
    if lembab < 40 :
        if lembab <= 20 :
            lembabSedikit = (lembab - 0) / (20 - 0)
            lumayanLembab = 0
            Lembab = 0
            sangatLembab = 0
        elif lembab > 20 and lembab <= 40 :
            lembabSedikit = (40- lembab) / (40 - 20)
            lumayanLembab = (lembab - 20) / (40 - 20)
            Lembab = 0
            sangatLembab = 0
    elif lembab >= 20 and lembab < 60 :
        if lembab >= 20 and lembab <= 40 :
            lembabSedikit = (40 - lembab) / (40 - 20)
            lumayanLembab = (lembab - 20) / (40 - 20)
            Lembab = 0
            sangatLembab = 0
        elif lembab > 40 and lembab < 60 :
            lembabSedikit = 0
            lumayanLembab = (60 - lembab) / (60 - 40)
            Lembab = (lembab - 40) / (60 - 40)
            sangatLembab = 0
    elif lembab >= 40 and lembab < 80 :
        if lembab >= 40 and lembab <= 60 :
            lembabSedikit = 0
            lumayanLembab = (60 - lembab) / (60 - 40)
            Lembab = (lembab - 40) / (60 - 40)
            sangatLembab = 0
        elif lembab > 60 and lembab <80 :
            lembabSedikit = 0
            lumayanLembab = 0
            Lembab = (80 - lembab) / (80 - 60)
            sangatLembab = (lembab - 80) / (80 - 60)
    elif lembab >= 60 and lembab <= 100 :
        if lembab >= 60 and lembab <= 80 :
            lembabSedikit = 0
            lumayanLembab = 0
            Lembab = (80 - lembab) / (80 - 60)
            sangatLembab =  (lembab - 40) / (60 - 40)
        elif lembab > 80 and lembab <= 100 :
            lembabSedikit = 0
            lumayanLembab = 0
            Lembab = 0
            sangatLembab = (100 - lembab) / (100 - 80)

    listLembab.extend([lembabSedikit, lumayanLembab, Lembab, sangatLembab])
    return listLembab

listTabel = []
def tabelKeterangan() :
    print('\nBerikut tabel keterangan tingkat kondisi buah')
    listTabel = [
        ['Tekstur/aroma','Lembek sedikit', 'Lumayan lembek', 'Lembek', 'Sangat lembek'], 
        ['Bau sedikit','Sehat', 'Sehat', 'Kurang Sehat', 'Tidak sehat'], 
        ['Lumayan bau', 'Sehat', 'Kurang sehat', 'Tidak Sehat', 'Busuk'], 
        ['Bau', 'Kurang Sehat', 'Tidak Sehat', 'Busuk', 'Busuk'],
        ['Sangat bau', 'Tidak Sehat', 'Busuk', 'Busuk', 'Sangat Busuk']
    ]
    tabel = tabulate(listTabel, headers='firstrow', tablefmt='fancy_grid')
    return tabel


def keteranganSkalaInput() :
    print('\nBerikut tabel keterangan skala input')
    skala = [
        ['Nilai', 'Aroma', 'Kelembapan'],
        ['0 - 40', 'Bau sedikit', 'Lembek sedikit'],
        ['20 - 60', 'Lumayan bau', 'Lumayan lembek'],
        ['40 - 80', 'Bau', 'Lembek'],
        ['60 - 100', 'Sangat bau', 'Sangat lembek']
    ]
    tabelSkala = tabulate(skala, headers='firstrow', tablefmt='grid')
    return tabelSkala

def maxFuzzyficationBau() :
    maxValueBau = max(listBau)
    return maxValueBau

def maxFuzzyficationLembab() :
    maxValueLembab = max(listLembab)
    return maxValueLembab

indexBau = int()
def indexFuzzyficationBau() :
    maxValueBau = max(listBau)
    indexBau = listBau.index(maxValueBau)
    return indexBau

indexLembab = int()
def indexFuzzyficationLembab() :
    maxValueLembab = max(listLembab)
    indexLembab = listLembab.index(maxValueLembab)
    return indexLembab

kondisiAkhirBuah = ''
def hasilAkhir() :
    if indexBau == 0 and indexLembab == 0 :
        kondisiAkhirBuah == 'Sehat'
    if indexBau == 1 and indexLembab == 0 :
        kondisiAkhirBuah == 'Sehat'
    if indexBau == 2 and indexLembab == 0 :
        kondisiAkhirBuah == 'Kurang sehat'
    if indexBau == 3 and indexLembab == 0 :
        kondisiAkhirBuah == 'Tidak sehat'
    if indexBau == 0 and indexLembab == 1 :
        kondisiAkhirBuah == 'Sehat'
    if indexBau == 1 and indexLembab == 1 :
        kondisiAkhirBuah == 'Kurang sehat'
    if indexBau == 2 and indexLembab == 1 :
        kondisiAkhirBuah == 'Tidak sehat'
    if indexBau == 3 and indexLembab == 1 :
        kondisiAkhirBuah == 'Busuk'
    if indexBau == 0 and indexLembab == 2 :
        kondisiAkhirBuah == 'Kurang sehat'
    if indexBau == 1 and indexLembab == 2 :
        kondisiAkhirBuah == 'Tidak sehat'
    if indexBau == 2 and indexLembab == 2 :
        kondisiAkhirBuah == 'Busuk'
    if indexBau == 3 and indexLembab == 2 :
        kondisiAkhirBuah == 'Busuk'
    if indexBau == 0 and indexLembab == 3 :
        kondisiAkhirBuah == 'Tidak sehat'
    if indexBau == 1 and indexLembab == 3 :
        kondisiAkhirBuah == 'Busuk'
    if indexBau == 2 and indexLembab == 3 :
        kondisiAkhirBuah == 'Busuk'
    if indexBau == 3 and indexLembab == 3 :
        kondisiAkhirBuah == 'Sangat busuk'
    return kondisiAkhirBuah




# def hasilAkhir() :
    # kondisiAkhirBuah = 'asu'
    # hasil = kondisiAkhirBuah
    # return hasil

print('\n')
print('                                     FUZZY LOGIC\n')
print('                     Program mengetahui tingkat kebusukan buah \n')
print('Keyword')
print('Tabel skala = skala')
print('Input = input')
print('Hasil fuzifikasi = fuzifikasi')
print('Tabel kondisi = tabel')
print('Nilai maksimal = max')
print('Hasil defuzifikasi = hasil')
print('Keluar program = exit')

while True :
    userInput = input('\nPilihan : ')
    if userInput == 'skala' or userInput == 'Skala' :
        print(keteranganSkalaInput())
    elif userInput == 'input' or userInput == 'Input' :
        bau = int(input('\nTingkat bau tidak sedap (skala 0 s/d 100) : '))
        lembab = int(input('Tingkat kelembapan buah (skala 0 s/d 100) : '))
    elif userInput == 'fuzzyfication' or userInput == 'fuzifikasi' :
        print('\nBerdasarkan indikator bau bernilai', bau, 'dan indikator tekstur bernilai', lembab,', ')
        print('Maka didapatkan hasil Fuzzyfication bau          : ', aromaBuah())
        print('                                    kelembapan   : ', kelembapanBuah())
    elif userInput == 'tabel' or userInput == 'Tabel' :
        print(tabelKeterangan())
    elif userInput == 'max' or userInput == 'maks' :
        print('\nNilai maksimal himpunan bau        :', maxFuzzyficationBau(), ', yang berada pada indeks ke-', indexFuzzyficationBau())
        print('Nilai maksimal Himpunan kelembapan :', maxFuzzyficationLembab(), ', yang berada pada indeks ke-', indexFuzzyficationLembab())
    elif userInput == 'hasil' :
        print(hasilAkhir())
    elif userInput == 'exit' :
        break
    else : 
        print('\nPilihan salah!!')
        
        

