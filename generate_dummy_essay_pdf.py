from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from textwrap import TextWrapper

def wrap_text(text, line_width):
    wrapper = TextWrapper(width=line_width)
    lines = wrapper.wrap(text)
    return lines

def generate_dummy_essay_pdf(filename, num_pages, num_paragraphs, sentences_per_paragraph, words_per_sentence, line_width):
    pdf = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Mengatur margin
    top_margin = 4 * cm
    left_margin = 4 * cm
    right_margin = width - (3 * cm)
    bottom_margin = 3 * cm

    # Mengatur area penulisan teks dengan margin
    text_x = left_margin
    text_y = height - top_margin

    # Mengatur lebar dan tinggi area penulisan teks
    text_width = right_margin - left_margin
    text_height = height - (top_margin + bottom_margin)

    page_count = 0

    for _ in range(num_pages):
        for _ in range(num_paragraphs):
            paragraph = ""

            for _ in range(sentences_per_paragraph):
                sentence = ""

                for _ in range(words_per_sentence):
                    word = generate_dummy_word()
                    sentence += word + " "

                sentence = sentence.strip() + ". "
                paragraph += sentence

            lines = wrap_text(paragraph, line_width)

            for line in lines:
                if text_x + pdf.stringWidth(line) > right_margin:
                    text_x = left_margin
                    text_y -= 14  # Sesuaikan jarak antar baris di sini (dalam satuan poin)

                    if text_y < bottom_margin:
                        text_y = height - top_margin
                        pdf.showPage()
                        page_count += 1

                pdf.setFont("Helvetica", 12)
                pdf.drawString(text_x, text_y, line)
                text_x += pdf.stringWidth(line) + pdf.stringWidth(" ")

        text_x = left_margin
        text_y -= 14  # Sesuaikan jarak antar paragraf di sini (dalam satuan poin)

        if text_y < bottom_margin:
            text_y = height - top_margin
            pdf.showPage()
            page_count += 1

    while page_count < num_pages:
        pdf.showPage()
        page_count += 1

    pdf.save()

# Contoh penggunaan
filename = "dummy_essay.pdf"
num_pages = 5
num_paragraphs = 3
sentences_per_paragraph = 5
words_per_sentence = 8
line_width = 70

generate_dummy_essay_pdf(filename, num_pages, num_paragraphs, sentences_per_paragraph, words_per_sentence, line_width)
