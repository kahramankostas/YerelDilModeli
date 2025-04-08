# Yerel Chat API

Bu proje, LM Studio aracılığıyla çalışan bir Gemma-3-12b-it modeli ile basit bir sohbet arayüzü sağlar. API tabanlı bir yapı kullanarak, kullanıcıların komut satırı üzerinden modelle Türkçe etkileşime girmesine olanak tanır.

## Proje Bileşenleri

Proje iki ana dosyadan oluşmaktadır:

1. **app.py**: Flask tabanlı bir API sunucusudur. Kullanıcı mesajlarını alır ve LM Studio'nun sunduğu yerel Gemma API'sine iletir.
2. **model.py**: Komut satırı arayüzü sağlayan istemci uygulamasıdır. Kullanıcıdan girdi alır ve API sunucusuna iletir.

## Gereksinimler

Projeyi çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız vardır:

* Python 3.8 veya daha üst sürümü
* Flask
* Requests
* LM Studio (Gemma-3-12b-it modeli yüklü olmalı)

## Kurulum

1. Gerekli Python paketlerini yükleyin:

```bash
pip install flask requests
```

2. LM Studio'yu indirin ve kurun. LM Studio'nun [resmi web sitesinden](https://lmstudio.ai/) en son sürümünü edinebilirsiniz.

3. LM Studio içinde Gemma-3-12b-it modelini indirin.

## Kullanım

1. LM Studio'yu açın ve Gemma-3-12b-it modelini seçin.

2. Local Server özelliğini etkinleştirin ve API sunucusunu 1234 portunda başlatın.

3. İkinci bir terminal penceresi açın ve şu komutu çalıştırarak Flask API sunucusunu başlatın:

```bash
python app.py
```

4. Üçüncü bir terminal penceresi açın ve komut satırı arayüzünü başlatmak için:

```bash
python model.py
```

5. Açılan komut satırı arayüzüne sorularınızı Türkçe olarak yazabilirsiniz.

## API Yapısı

### `/api/chat` Endpoint'i (POST)

**İstek formatı:**

```json
{
  "text": "Kullanıcının sorusu buraya"
}
```

**Başarılı yanıt formatı:**

```json
{
  "response": "Model'in cevabı"
}
```

## Hata Ayıklama

- API sunucusu varsayılan olarak debug modunda çalışır (port 5000).
- Bağlantı hataları ve API yanıtları terminal üzerinde görüntülenir.
- LM Studio API'sine bağlanılamıyorsa, LM Studio'nun çalıştığından ve doğru portta dinleme yaptığından emin olun.

## Özelleştirme

Model parametrelerini değiştirmek için `app.py` dosyasındaki payload değişkenini düzenleyebilirsiniz:

```python
payload = {
    "model": "gemma-3-12b-it",  # Kullanılan model
    "messages": [
        {"role": "user", "content": user_input}
    ],
    "temperature": 0.7  # Yaratıcılık seviyesi (0.0-1.0)
}
```
---
**Not:** Bu proje, LM Studio'nun sunduğu yerel API ile entegre çalışmak üzere tasarlanmıştır. Gemma-3-12b-it modeli, LM Studio aracılığıyla yerel makinenizde çalıştırılır.