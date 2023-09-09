from PyPDF2 import PdfReader, PdfWriter

# 打开源PDF文件
with open('input.pdf', 'rb') as pdf_file:
    # 创建PDF阅读器对象
    pdf_reader = PdfReader(pdf_file)

    # 创建一个新的PDF写入对象
    pdf_writer = PdfWriter()

    # 定义要截取的页面范围（例如，截取第2页到第4页）
    start_page = 1  # 第一页的索引是0
    end_page = 13  # 截取第2页到第4页

    # 逐页复制要截取的页面到新的PDF
    for page_num in range(start_page, end_page + 1):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # 保存截取后的PDF到新文件
    with open('output.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)

print("截取完成")
