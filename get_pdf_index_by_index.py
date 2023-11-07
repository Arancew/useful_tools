from PyPDF2 import PdfReader, PdfWriter

# 打开源PDF文件
with open('input.pdf', 'rb') as pdf_file:
    # 创建PDF阅读器对象
    pdf_reader = PdfReader(pdf_file)

    # 创建一个新的PDF写入对象
    start=81
    while True:
    # 定义要截取的页面范围（例如，截取第2页到第4页）
        start_page = start
        end_page = min(start_page+4,95)
        pdf_writer = PdfWriter()
        # 逐页复制要截取的页面到新的PDF
        for page_num in range(start_page, end_page + 1):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # 保存截取后的PDF到新文件
        with open('to_pdf/{}_{}.pdf'.format(start_page,end_page), 'wb') as output_file:
            pdf_writer.write(output_file)
        start=end_page+1
        if start>=95:
            break

print("截取完成")
