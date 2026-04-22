✊✌️✋ Taş - Kağıt - Makas (YOLOv11 Object Detection)
Bu proje, bilgisayarlı görü (computer vision) ve derin öğrenme teknikleri kullanılarak geliştirilmiş gerçek zamanlı bir Taş-Kağıt-Makas oyunudur. Proje, kullanıcının el hareketlerini YOLO (You Only Look Once) modeli ile tanıyarak bilgisayara karşı yarışmasını sağlar.

✨ Özellikler
Gerçek Zamanlı Tespit: YOLOv11 mimarisi (veya seçtiğiniz sürüm) ile yüksek doğrulukta el hareketi tespiti.

Oyun Mantığı: Bilgisayar rastgele seçim yapar ve klasik oyun kurallarına göre kazananı belirler.

Akıllı Bekleme Süresi: Her elden sonra 2 saniyelik bir soğuma süresi eklenmiştir, böylece oyun daha kontrollü bir tempoda ilerler.

Skor Takibi: Oyuncu ve bilgisayar arasındaki skor ekranın altında anlık olarak güncellenir.

Kısayol Tuşları:

q: Oyundan çıkış yapar.

r: Skorları sıfırlar.

🚀 Kurulum
Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

Depoyu Klonlayın:

Bash
git clone https://github.com/kullaniciadi/tas-kagit-makas-yolo.git
cd tas-kagit-makas-yolo
Gerekli Kütüphaneleri Yükleyin:

Bash
pip install ultralytics opencv-python
Model Dosyasını Hazırlayın:

Eğittiğiniz best.pt dosyasını projenin ana dizinine yerleştirin.

Not: Model dosyanız 100MB'den büyükse yükleme yaparken Git LFS kullanmayı unutmayın.

🎮 Kullanım
Oyunu başlatmak için terminale şu komutu yazın:

Bash
python main.py
Kamera açıldığında elinizi (Taş, Kağıt veya Makas şeklinde) kameraya gösterin.

Model elinizi tanıdığında (confidence > 0.6), bilgisayar otomatik olarak hamlesini yapacak ve sonucu ekrana yazdıracaktır.

🛠️ Proje Yapısı
Plaintext
.
├── best.pt              # Eğitilmiş YOLO model ağırlıkları
├── main.py              # Oyunun ana kaynak kodu
├── README.md            # Proje dokümantasyonu
└── .gitignore           # Takip edilmeyecek dosyalar


🧠 Nasıl Çalışır?
Görüntü İşleme: OpenCV ile kameradan alınan kareler yatay olarak aynalanır.

Nesne Tespiti: Ultralytics YOLO modeli, görüntüdeki elin hangi sınıfa (tas, kagit, makas) ait olduğunu belirler.

Karar Mekanizması: Eğer bir el hareketi %60'ın üzerinde bir güven oranıyla tespit edilirse, bilgisayar random kütüphanesi ile bir seçim yapar.

Görselleştirme: Sonuçlar ve skor tablosu cv2.putText ile anlık olarak ekrana basılır.

🤝 Katkıda Bulunma
Geliştirme önerileriniz veya hata bildirimleriniz için lütfen bir issue açın veya pull request gönderin.
