# gelen dizi, daha okunakli olmasi icin birlestirildi ve string yapildi
def birlestir(dizi):
    yazi =" "
    for d in dizi:
        yazi=yazi + d
    return yazi



 # ornek metinler.
metin ="File ile dosya oluşturulmaz yada dosyaya birşey yazılmaz. Sadece dosya ile ilgili belirli bilgiler alınabilir. Örneğin  böyle bir dosya var mı? Dosyanın uzunluğu ne?"
metin2 = "File ile dosya oluşturulmaz yada dosyaya  birşey yazılmaz. Sadece dosya ile ilgili belirli bilgiler alınabilir. Örneğin böyle bir dosya var mı? Dosyanın uzunluğu ne?"

def metinDuzenle(metin):
    # listeler tanimlandi
    myList=[]
  
    # metin split edildi
    metin = metin.split()
   
    
    # metin listeye aktarildi
    for x in range (len(metin)):
        myList.append(metin[x])
        
    return myList
      
       
def metin2Duzenle(metin2): 
    # liste tanimlandi
    myList2=[]
    
    # metin2 split edildi
    metin2 = metin2.split()
    
    # metin listeye aktarildi
    for y in range (len(metin2)):
        myList2.append(metin2[y])
 
    return myList2    


 # fonksiyondan gelen liste degerleri degiskenlere atandı
gelenMyList=metinDuzenle(metin)
gelenMyList2=metin2Duzenle(metin2)

# silinen yani eksik olan metin'e gore eksik bulundu ve yazdirildi
if len(gelenMyList) > len(gelenMyList2):
    
    for x in range (len(gelenMyList)-1):
        
        if gelenMyList[x] != gelenMyList2[x]:
            print("metin2 ' de eksik var")
            print(gelenMyList[x-1] +  " /----------- / " + gelenMyList2[x]+"...")
            
            eksikKelimeBaslangic = metin.index(gelenMyList[x])
            eksikKelimeBitis = metin.index(gelenMyList2[x])
            
            eksikMetin = metin[eksikKelimeBaslangic : eksikKelimeBitis]  
            print(birlestir(eksikMetin))
            break
            
else:
    for x in range (len(gelenMyList2)):
        if gelenMyList2[x] != gelenMyList[x]:
            print("metin ' de eksik var")
            print(gelenMyList2[x-1]+ " / -------- /" + gelenMyList[x]+"...")
            
            eksikKelimeBaslangic =metin2.index(gelenMyList2[x])
            eksikKelimeBitis =    metin2.index(gelenMyList[x])                              
                                              
            eksikMetin  = metin2[eksikKelimeBaslangic : eksikKelimeBitis]  
            print(birlestir(eksikMetin))
            break








