# log-analiz-araci

# Proje Adı: Log Analiz Aracı

Bu proje, bir web sunucusu erişim günlüğü (access log) dosyasını okuyarak çeşitli analizler yapan basit bir Python betiğidir.

## Özellikler

- **Hata Tespiti:** HTTP durum kodu 400 ve üzeri olan hatalı veya şüpheli istekleri belirler.
- **En Çok İstek Gönderen IP'ler:** En çok istek gönderen ilk 5 IP adresini listeler.
- **Kullanımı Kolay:** Sadece Python 3 ile çalışır, ek kütüphane gerektirmez.

## Kurulum ve Kullanım

1.  Bu depoyu yerel makinenize klonlayın veya proje dosyalarını indirin.
    ```bash
    git clone [https://github.com/KULLANICI_ADI/DEPO_ADI.git](https://github.com/KULLANICI_ADI/DEPO_ADI.git)
    ```

2.  Terminali açın ve proje klasörüne gidin.
    ```bash
    cd proje-klasoru
    ```

3.  `access.log` adındaki log dosyanızın proje klasöründe olduğundan emin olun.

4.  Python betiğini çalıştırın.
    ```bash
    python3 log_analiz.py
    ```

## Proje Dosyaları

- `log_analiz.py`: Log analizini gerçekleştiren ana Python betiği.
- `access.log`: Analiz için kullanılan örnek web sunucusu erişim günlüğü dosyası.
- `README.md`: Projenin tanıtımını ve kullanımını açıklayan dosya.
