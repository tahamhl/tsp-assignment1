# 🧭 Assignment 1 – Basic TSP on Random Points

Bu proje, **Travelling Salesman Problem (TSP)** üzerine basit bir sezgisel algoritma uygulanarak geliştirilmiştir. Amaç, rastgele oluşturulan şehirler (noktalar) arasında en kısa turu bulmaktır.

---

## 📌 Projenin Hedefi

Bu ödev kapsamında aşağıdaki konuların pratiği yapılmıştır:

- Grafik (graph) soyutlaması
- Rastgele örnek oluşturma
- Basit sezgisel algoritmalarla TSP çözümü
- Grafiksel görselleştirme

---

## 🚀 Uygulanan Yöntem: Nearest Neighbor (En Yakın Komşu) Algoritması

### TSP Problemi Nedir?

TSP, bir gezginin her şehri yalnızca bir kez ziyaret ederek başladığı şehre geri dönmesini ve toplam yolun en kısa olmasını amaçlayan klasik bir optimizasyon problemidir.

### Kullanılan Algoritma: Nearest Neighbor

1. Rastgele 2D düzlemde `n` adet şehir üretilir.
2. Başlangıç olarak bir şehir seçilir (örneğin şehir 0).
3. Her adımda, en yakın ve henüz ziyaret edilmemiş şehir seçilir.
4. Tüm şehirler ziyaret edildiğinde başlangıç noktasına dönülerek tur tamamlanır.

Bu yöntem hızlıdır fakat her zaman en kısa turu garantilemez.

---

## 📸 Görselleştirme

Tur, `matplotlib` ile görselleştirilmiştir:

- Mavi noktalar: Şehirler
- Kırmızı çizgi: Bulunan TSP turu
- Sayılar: Şehir numaraları

Görselleştirme fonksiyonu sayesinde algoritmanın adımlarını görsel olarak takip edebilirsiniz.

---

## 🧠 Kullanılan Kütüphaneler

| Kütüphane    | Açıklama                         |
|--------------|----------------------------------|
| `numpy`      | Sayısal işlemler için            |
| `random`     | Rastgele sayı üretimi            |
| `matplotlib` | Grafik çizimi için               |
| `networkx`   | Grafik yapıları ve mesafeler için|

Kurulum için:

```bash
pip install numpy matplotlib networkx
