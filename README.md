 Grafik Teorisi ve Sosyal Ağlar - Bağlantı Tahmini (Link Prediction)

Projenin Amacı
Sosyal ağ graflarında henüz birbirine bağlı olmayan düğümler (kişiler) arasında, gelecekte oluşabilecek potansiyel bağlantıları "Adamic-Adar İndeksi" kullanarak tahmin etmek ve modelin doğruluk oranını analiz etmektir.

Kullanılan Teknolojiler ve Yöntemler
Programlama Dili: Python
Veri Seti: Stanford Network Analysis Project (SNAP) - Facebook Sosyal Ağ Veri Seti (`facebook_combined.txt`)
Veri Yapısı: Bellek optimizasyonu için Komşuluk Listesi (Adjacency List)
Algoritma: Adamic-Adar İndeksi

Proje Adımları
1. Veri Okuma: Ağdaki düğümler ve kenarlar sisteme aktarıldı.
2. Eğitim ve Test Ayrımı: Mevcut bağlantıların %20'si rastgele seçilerek test seti olarak ayrıldı (%80 eğitim seti ile graf oluşturuldu).
3. Skor Hesaplama: Adamic-Adar formülü ile ortak arkadaş derecelerine dayalı bağlantı skorları hesaplandı.
4. Doğruluk Analizi: Modelin tahminleri test setiyle karşılaştırılarak %97.87 doğruluk oranı elde edildi.

Kurulum ve Çalıştırma

Projeyi çalıştırmak için aynı klasör içinde Python yüklü olmalıdır:

python link_prediction.py