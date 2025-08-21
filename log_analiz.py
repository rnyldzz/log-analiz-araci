# 're' metin içinde desen aramaya (IP ve durum kodu gibi) yarar.
# 'collections' kütüphanesindeki 'Counter' ise sayım yapmak için pratiktir.
import re
from collections import Counter

# Log dosyasının adını bir değişkene atıyoruz.
# Böylece dosya adını değiştirmek istediğinde sadece bu satırı güncellenir
LOG_DOSYASI = "access.log"

def log_analiz_et():
    """Log dosyasını okur, analiz eder ve bir rapor oluşturma"""
    
    # IP adreslerini ve hatalı istekleri tutmak için boş listeler oluşturma
    ip_listesi = []
    hata_istekleri = []
    
    # 'try-except' bloğu, dosya bulunamazsa programın çökmesini engeller
    try:
        # Dosyayı okuma modunda (r) açıyoruz.
        # 'with' yapısı, işlem bittiğinde dosyayı otomatik olarak kapatır
        with open(LOG_DOSYASI, 'r', encoding='utf-8') as f:
            # Dosyadaki her satırı tek tek okuyor
            for satir in f:
                # Regex (düzenli ifade) kullanarak IP adresini ve durum kodunu çekiyor
                # (\S+): Boşluk olmayan karakterleri yakalar (IP adresi).
                # (\d+): Rakamları yakalar (durum kodu).
                match = re.search(r'^(\S+) .*? ".*?" (\d+)', satir)
                if match:
                    # Birinci parantezdeki ifadeyi (IP) al.
                    ip_adresi = match.group(1)
                    # İkinci parantezdeki ifadeyi (durum kodu) al ve sayıya dönüştür
                    durum_kodu = int(match.group(2))
                    
                    # IP adresini listeye ekliyor
                    ip_listesi.append(ip_adresi)
                    
                    # HTTP durum kodu 400 ve üzeri (hata kodları) ise,
                    # o satırı 'hata_istekleri' listesine ekliyor
                    if durum_kodu >= 400:
                        hata_istekleri.append(satir.strip())
                        
    except FileNotFoundError:
        print(f"Hata: '{LOG_DOSYASI}' dosyası bulunamadı. Lütfen aynı klasörde olduğundan emin olun.")
        return

    # --- Raporlama Kısmı ---
    print("--- Güvenlik Günlüğü Analiz Raporu ---")
    print("-" * 35)
    
    # Counter kullanarak hangi IP'nin kaç kez istek gönderdiğini sayıyor
    en_cok_istekler = Counter(ip_listesi)
    
    print("\n[En Çok İstek Gönderen IP Adresleri]")
    # En çok istek gönderen ilk 5 IP adresini listeliyor
    for ip, sayi in en_cok_istekler.most_common(5):
        print(f"IP: {ip}, İstek Sayısı: {sayi}")
    
    print("\n[Hatalı veya Şüpheli İstekler (HTTP Durum Kodu >= 400)]")
    if hata_istekleri:
        for istek in hata_istekleri:
            print(istek)
    else:
        print("Herhangi bir hatalı istek bulunamadı.")

# Bu kısım, dosya doğrudan çalıştırıldığında programın başlamasını sağlar.
if __name__ == "__main__":
    log_analiz_et()
