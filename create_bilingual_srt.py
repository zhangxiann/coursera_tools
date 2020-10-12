# 把中文字幕和英文字幕合并，创建双语字幕。
# 英文字幕 1.2.1.2 an introduction to computer vision.en.srt
# 中文字幕 1.2.1.2 an introduction to computer vision.zh-CN.srt
# 双语字幕 1.2.1.2 an introduction to computer vision.bilingual.srt
# 实际上，是把英语字幕的内容，直接添加到中文字幕内容的后面即可

import os
import glob

root_dir = 'D:\coursera'

# for course in os.listdir(root_dir):
#     course_dir = os.path.join(root_dir, course)
#     if os.path.isdir(course_dir):
#         coursera_dir = os.path.join(root_dir, course)
#         for classes in os.listdir(coursera_dir):
#             classes_dir = os.path.join(coursera_dir, classes)
#             if os.path.isdir(classes_dir):
#                 # courses.append(course)
#                 for section in os.listdir(classes_dir):
#                     section_dir = os.path.join(classes_dir, section)
#                     if os.path.isdir(section_dir):
#                         english_srt_files = glob.glob(os.path.join(section_dir, '*en.srt'))
#                         for english_srt_file in english_srt_files:
#                             chinese_srt_file = english_srt_file[:-6] + 'zh CN.srt'
#                             if os.path.exists(chinese_srt_file):
#                                 bilingual_srt_file = english_srt_file[:-6] + 'bilingual.srt'
#                                 f_chinese=open(chinese_srt_file, "r")
#                                 f_english=open(english_srt_file, "r")
#                                 f_bilingual=open(bilingual_srt_file, "w+")
#
#                                 chinese = f_chinese.read()
#                                 english = f_english.read()
#
#                                 f_bilingual.write(chinese)
#                                 f_bilingual.write('\n')
#                                 f_bilingual.write(english)
#
#
#                                 f_chinese.close()
#                                 f_english.close()
#                                 f_bilingual.close()

english_srt_file = 'D:\coursera\\1 introduction-tensorflow\\2_introduction-to-computer-vision\\01_introduction-to-computer-vision\\1.2.1.2 an introduction to computer vision.en.srt'

chinese_srt_file = english_srt_file[:-6] + 'zh CN.srt'
if os.path.exists(chinese_srt_file):
    bilingual_srt_file = english_srt_file[:-6] + 'bilingual.srt'
    f_chinese = open(chinese_srt_file, "rb")
    f_english = open(english_srt_file, "rb")
    f_bilingual = open(bilingual_srt_file, "wb+")

    chinese = f_chinese.read()
    english = f_english.read()

    # python bytes和str两种类型可以通过函数encode()和decode()相互转换，
    # str→bytes：encode()方法。str通过encode()方法可以转换为bytes。
    # bytes→str：decode()方法。如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
    # 要把bytes变为str，就需要用decode()方法。

    f_bilingual.write(chinese)
    # 由于上面打开文件时使用了 b，表示使用字节流，使用 encode() 把 str 转为 byte，再写入文件
    f_bilingual.write('\n'.encode())
    # 由于上面打开文件时使用了 b，表示使用字节流，使用 encode() 把 str 转为 byte，再写入文件
    f_bilingual.write('\n'.encode())
    f_bilingual.write(english)

    f_chinese.close()
    f_english.close()
    f_bilingual.close()
