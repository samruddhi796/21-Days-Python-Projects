from pypdf import PdfReader, PdfWriter
import os


def merge_pdfs(pdf_files, output_name):
    writer = PdfWriter()

    for pdf in pdf_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_name, "wb") as file:
        writer.write(file)

    print(f"✅ PDFs merged into {output_name}")


def split_pdf(pdf_file):
    reader = PdfReader(pdf_file)

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_name = f"page_{i + 1}.pdf"
        with open(output_name, "wb") as file:
            writer.write(file)

    print("✅ PDF split into individual pages.")


def extract_pages(pdf_file, start, end, output_name):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for i in range(start - 1, end):
        writer.add_page(reader.pages[i])

    with open(output_name, "wb") as file:
        writer.write(file)

    print(f"✅ Pages {start} to {end} saved as {output_name}")


def menu():
    print("\n📄 PDF TOOL")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Extract Pages")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            files = input("Enter PDF file names (comma-separated): ").split(",")
            files = [f.strip() for f in files]
            output = input("Enter output PDF name: ")
            merge_pdfs(files, output)

        elif choice == '2':
            pdf = input("Enter PDF file name: ")
            split_pdf(pdf)

        elif choice == '3':
            pdf = input("Enter PDF file name: ")
            start = int(input("Start page: "))
            end = int(input("End page: "))
            output = input("Output PDF name: ")
            extract_pages(pdf, start, end, output)

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


main()
