from ultralytics import YOLO
import cv2
import random
import time

model = YOLO("best.pt")
cap = cv2.VideoCapture(0)

skor = {"bilgisayar":0,"oyuncu":0}
secenekler = ["tas","kagit","makas"]
son_oyun_zamani = 0
bekleme_suresi = 2

def kim_kazanir(oyuncu,bilgisayar):
    if oyuncu == bilgisayar:
        return "berabere"
    kazanan_durumlar=[("tas","makas"),("kagit","tas"),("makas","kagit")]
    if (oyuncu,bilgisayar) in kazanan_durumlar:
        skor["oyuncu"] +=1
        return "kazandın!"
    skor["bilgisayar"] +=1
    return "kaybettin"

bilgisayar  =None
sonuc = None

while True:
    ret,frame = cap.read()
    if not ret:
        break
    frame= cv2.flip(frame, 1) #aynalama
    results = model(frame)[0]
    
    oyuncu_secimi = None
    for result in results.boxes.data.tolist():
        x1,y1,x2,y2,score,class_id  =result
        if score > 0.6:
            x1,y1,x2,y2 = map(int,[x1,y1,x2,y2])
            class_name = results.names[int(class_id)].lower()
            
            if class_name in secenekler:
                oyuncu_secimi = class_name
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame,class_name.upper(),(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                break
    suanki_zaman = time.time()
    if oyuncu_secimi and (suanki_zaman - son_oyun_zamani > bekleme_suresi):
        bilgisayar = random.choice(secenekler)
        sonuc = kim_kazanir(oyuncu_secimi, bilgisayar)
        son_oyun_zamani = suanki_zaman
        
    if bilgisayar and (suanki_zaman - son_oyun_zamani < bekleme_suresi):
        cv2.putText(frame,f"Bilgisayar: {bilgisayar}",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
        cv2.putText(frame,f"Sonuc: {sonuc}",(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        
        kalan = bekleme_suresi - (suanki_zaman - son_oyun_zamani)
        cv2.putText(frame,f"Yeni oyun: {kalan:.1f}.sn",(10,150),cv2.FONT_HERSHEY_COMPLEX,1,(200,200,150),2)
        
    
    else:
        cv2.putText(frame,"Elinizi Gosterin!",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        
    cv2.putText(frame,f"skor - sen: {skor['oyuncu']} PC: {skor['bilgisayar']}",
                    (10,frame.shape[0]-20),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    
    cv2.imshow("TKM",frame)
    key = cv2.waitKey(1) & 0xFF 
    
    if key == ord('q'):
        break
    elif key == ord('r'):
        skor = {"bilgisayar":0,"oyuncu":0}
    
    
cap.release()
cv2.destroyAllWindows()

    
    
    
    
    
    
    
    
    
    
    
    
    
    