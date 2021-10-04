from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams



def convert_pdf(path, target_extension):
    rsrcmgr = PDFResourceManager()
    encoding = 'utf-8'
    laparams = LAParams()
    outfile = path.replace('pdf', target_extension)
    outfp = open(outfile, 'w', encoding=encoding)

    device = TextConverter(rsrcmgr, outfp, laparams=laparams)
    if(target_extension == 'html'):
        device = HTMLConverter(rsrcmgr, outfp, laparams=laparams)
    elif(target_extension == 'xml'):
        device = XMLConverter(rsrcmgr, outfp, laparams=laparams)

    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = b''
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=False):
        interpreter.process_page(page)

    fp.close()
    device.close()
    outfp.close()


def convert_pdfs(path, target_extension):
    import os
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            convert_pdf(os.path.join(path, file), target_extension)


def main():
    path = 'data/'
    convert_pdfs(path, 'txt')


if __name__ == "__main__":
    main()
