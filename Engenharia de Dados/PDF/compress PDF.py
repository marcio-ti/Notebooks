from pypdf import PdfWriter
import os

def comprimir(file):
    writer = PdfWriter(clone_from=file)
    caminho = os.path.dirname((file))
    nome_arquivo = os.path.basename(file)


    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=72)

    for page in writer.pages:
        page.compress_content_streams()

    saida = f"{caminho}\\{nome_arquivo}-comprimido.pdf"
    with open(saida, "wb") as f:
        writer.write(f)

    print("PDF Comprimido com sucesso!")

if __name__ == "__main__":
    comprimir(r'C:\Users\Marcio\Downloads\LE CORDON BLEU - TODAS AS TECNICAS CULINARIAS by JENI WRIGHT, ERIC TREUILLE (z-lib.org).pdf')