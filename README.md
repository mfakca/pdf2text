# pdf2text

Klasör içerisindeki tüm PDF'leri metne dönüştürür.

## 1. Kurulum:

### Yüklenmesi gerekenler:
* Poppler (https://blog.alivate.com.au/poppler-windows/)
* Tesseract (https://github.com/UB-Mannheim/tesseract/wiki)

### Yüklenmesi gereken Python kütüphaneleri:
* PIL
* pytesseract
* pdf2image

## 2. Kullanım:

```python
pdf2text(pdf_file_path = 'pdf', image_path = 'images', output_text_path = 'outputs', dpi = 500)
```

**pdf_file_path:** PDF'lerin bulunduğu klasörün yolu.

**image_path:** Metne dönüştürmeden önce her bir sayfayı görsel olarak kaydeder. Bu görsellerin kaydedileceği klasörün yolu.

**output_text_path:** Görseller üzerindeki metinleri txt formatında kaydedileceği klasörün yolu.

**dpi:** Görüntünün kalitesini belirleyen parametre.

## 3. Referans:
* https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
