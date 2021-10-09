# Import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def pdf2text(pdf_file_path = 'pdf', image_path = 'images', output_text_path = 'outputs', dpi = 500):
    
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
            
            # Save the image of the page in system
            page.save(filename, 'JPEG')

            # Increment the counter to update filename
            page_counter+= 1


        '''
        Part #2 - Recognizing text from the images using OCR
        '''
            
     
        filelimit = page_counter-1

        
        outfile = f"{output_text_path}/{file[:-4]}.txt"

        # Open the file in append mode so that
        # All contents of all images are added to the same file
        f = open(outfile, "a")

        # Iterate from 1 to total number of pages
        for i in range(1, filelimit + 1):

            # Set filename to recognize text from
            # Again, these files will be:
            # page_1.jpg
            # page_2.jpg
            # ....
            # page_n.jpg
            filename = f"{save_image_folder_path}/page_"+str(i)+".jpg"
                
            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(Image.open(filename)))))

            # The recognized text is stored in variable text
            # Any string processing may be applied on text
            # Here, basic formatting has been done:
            # In many PDFs, at line ending, if a word can't
            # be written fully, a 'hyphen' is added.
            # The rest of the word is written in the next line
            # Eg: This is a sample text this word here GeeksF-
            # orGeeks is half on first line, remaining on next.
            # To remove this, we replace every '-\n' to ''.
            text = text.replace('-\n', '')	

            # Finally, write the processed text to the file.
            f.write(" ".join([i for i in text.split()]))

        # Close the file after writing all the text.
        f.close()
pdf2text()