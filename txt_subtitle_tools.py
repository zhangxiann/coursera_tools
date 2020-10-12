import os

# 删除换行符，把所有的文字都放到一行里，方便翻译
# def delete_n(txt_file):
#     f = open(txt_file, "rb")
#     data = f.read()
#     data = data.replace('\n'.encode(), ' '.encode())
#     f.close()
#
#     f = open(txt_file, "wb")
#     f.write(data)
#     f.close()

def delete_n(txt_file):
    f = open(txt_file, "r", encoding='utf-8')
    data = f.read()
    data = data.replace('\n', ' ')
    f.close()

    f = open(txt_file, "w", encoding='utf-8')
    f.write(data)
    f.close()


delete_n('C:\\Users\\lenovo\\Desktop\\01_introduction-a-conversation-with-andrew-ng.en.txt')