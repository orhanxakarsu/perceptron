import random
import time
class Noron:
    def __init__(self,agirlik=None):
        self.agirlik=agirlik if agirlik !=None else random.randint(0,100)/100
    def ileri(self,gelenDeger):
        #return gelenDeger*self.agirlik if gelenDeger*self.agirlik >0 else 0
        return gelenDeger*self.agirlik

class Yapi:
    toplam=0
    etkinlikIslevi =0 #Çıkış katmanına gelen değer eğer etkinlik işlevini geçiyorsa 1, geçmiyorsa 0 olur
    hataDegeri=0.1 #Bu değeri kullanarak mevcut nörondan gelen E değerini toplarız sonra da;
    duzeltmeDegeri =0.5 #Buradaki düzeltme değeriyle toplama yaparız.
    girisler=[[0,0,1],[0,1,1],[1,0,1],[1,1,1]] #Modeli eğiteceğimiz değerler.
    cikislar=[1,1,1,0]#Doğru olan çıkışlar
    tahminCikislar =[None for i in range(4)] #Bizim tahmin ettiğimiz çıkışlar
    cikisDegerleri=[[0,0,0] for i in range(4)]#Her bir nöronun çıkış değerleri
    def __init__(self):
        self.katmanlar =[Noron() for i in range(3)]#Ağ 1 katman olduğu için katmandaki nöronlar
    
    def ileriYayilim(self,giris,indis=None):
        if indis !=None:
            for i in range(len(giris)):
                
                self.cikisDegerleri[indis][i]=self.katmanlar[i].ileri(giris[i])
                self.toplam+=self.cikisDegerleri[indis][i]
                #print(self.toplam)
            deger =1 if self.toplam >self.etkinlikIslevi else 0
            self.toplam=0
            #print(deger)
            self.tahminCikislar[indis]=deger
            print(f"giris : {self.girisler[indis]} cikis : {self.tahminCikislar[indis]}")
            return deger
        else:
            for i in range(len(giris)): 
                self.toplam+=self.katmanlar[i].ileri(giris[i])
            deger =1 if self.toplam >self.etkinlikIslevi else 0
            print(self.toplam)
            self.toplam=0
            return deger
    
    
    def tahmin(self,giris):
        toplam_=0
        for i in range(len(giris)): 
            toplam_+=self.katmanlar[i].ileri(giris[i])
        deger =1 if toplam_ >self.etkinlikIslevi else 0
        return deger
    def agirliklariAyarla(self):
        for i in range(4):
            self.ileriYayilim(self.girisler[i],i)

        for i in range(4):
            hataMiktari = sum(self.cikisDegerleri[i])
            duzeltme = (hataMiktari+self.hataDegeri)*self.duzeltmeDegeri
            #print(duzeltme)
            
            for j in range(3):
                if(self.tahminCikislar!=self.cikislar):
                    if self.girisler[i][j] !=0:
                        if self.cikislar[i]>self.tahminCikislar[i]:
                            self.katmanlar[j].agirlik+=abs(duzeltme)
                        elif self.cikislar[i]<self.tahminCikislar[i]:
                            self.katmanlar[j].agirlik-=abs(duzeltme)

        
    def egitim(self):
        while(self.tahminCikislar!=self.cikislar):
            self.agirliklariAyarla()
        while True:
            self.sorgu()
    def sorgu(self):
        girisler=[None,None,None]
        for i in range(3):
            giris=int(input(f'{i+1}. degeri gir -> '))
            girisler[i]=giris
        print('Tahmin Edilen Deger -  > ',self.ileriYayilim(girisler))
            
            
            
            
def main():
    yapi=Yapi()
    yapi.egitim()






if __name__=='__main__':
    main()
                
       

            
        
        
        
