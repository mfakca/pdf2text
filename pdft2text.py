from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def pdf2text(pdf_file_path = 'pdf', image_path = 'images', output_text_path = 'outputs', dpi = 500):
    
    """
    #### Parametreler:
    
    pdf_file_path: PDF'lerin bulunduğu klasörün yolu.

    image_path: Metne dönüştürmeden önce her bir sayfayı görsel olarak kaydeder. Bu görsellerin kaydedileceği klasörün yolu.

    output_text_path: Görseller üzerindeki metinleri txt formatında kaydedileceği klasörün yolu.

    dpi: Görüntünün kalitesini belirleyen parametre.
    
    #### Çıktı:
    
    Görseller: image_path içerisine kaydedilen, PDF'lerin her sayfasına ait görseller.
    
    Metin: output_text_path klasörüne kaydedilen, PDF dosyasındaki metinler.
    """
    
    pdf_files = [i for i in os.listdir(pdf_file_path) if i[-4:] == '.pdf']
    
    for file in pdf_files:
        
        file_path = pdf_file_path + '/' + file
        print(file_path)
        pages = convert_from_path(file_path, dpi, poppler_path=r'poppler-0.68.0\bin')


        page_counter = 1

        try:
            save_image_folder_path = f'{image_path}/{file[:-4]}'
            os.mkdir(save_image_folder_path)
        except: pass
        
        for page in pages:

            
            filename = f"{save_image_folder_path}/page_"+str(page_counter)+".jpg"
            
            
            page.save(filename, 'JPEG')

            
            page_counter+= 1


             
        filelimit = page_counter-1

        
        outfile = f"{output_text_path}/{file[:-4]}.txt"

        
        f = open(outfile, "a")

        
        for i in range(1, filelimit + 1):

            
            filename = f"{save_image_folder_path}/page_"+str(i)+".jpg"
                
            
            text = str(((pytesseract.image_to_string(Image.open(filename)))))

            
            text = text.replace('-\n', '')	

            
            f.write(" ".join([i for i in text.split()]))

        
        f.close()
pdf2text()
