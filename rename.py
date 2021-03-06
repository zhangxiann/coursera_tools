import os
import glob
from txt_subtitle_tools import delete_n
import re
import enviroments



# 源文件名
# introduction-tensorflow\1_a-new-programming-paradigm\01_a-new-programming-paradigm\01_introduction-a-conversation-with-andrew-ng.mp4

# 目标文件名
# 1 introduction-tensorflow\1_a-new-programming-paradigm\01_a-new-programming-paradigm\1.1.1 introduction a conversation with andrew ng.mp4

for course in os.listdir(enviroments.root_dir):
    course_dir = os.path.join(enviroments.root_dir, course)
    if os.path.isdir(course_dir):
        course_num = course[0:1]
        coursera_dir = os.path.join(enviroments.root_dir, course)
        for classes in os.listdir(coursera_dir):
            classes_dir = os.path.join(coursera_dir, classes)
            if os.path.isdir(classes_dir):
                class_num = classes[0:1]
                # courses.append(course)
                for section in os.listdir(classes_dir):
                    section_dir = os.path.join(classes_dir, section)
                    if os.path.isdir(section_dir):
                        section_num = section[0:2]
                        section_num = section_num[1:2] if section_num.startswith('0') else section_num
                        # 删除 . 开头的 mp4 文件
                        mp4_files = glob.glob(os.path.join(section_dir, '*.mp4'))
                        for mp4_file in mp4_files:
                            if os.path.basename(mp4_file).startswith('.'):
                                os.remove(mp4_file)

                        # 删除其他语言的 txt 文件，重命名英语的 txt 字幕，加上章节号
                        txt_files = glob.glob(os.path.join(section_dir, '*.txt'))
                        for txt_file in txt_files:
                            # 删除其他语言的 txt 文件
                            if not txt_file.endswith("en.txt") :
                                os.remove(txt_file)
                            else:
                                # 重命名英语的 txt 字幕，加上章节号
                                # 删除换行符
                                delete_n(txt_file)
                                (path, origin_file_name) = os.path.split(txt_file)

                                file_num = origin_file_name[0:2]
                                file_num = file_num[1:2] if file_num.startswith('0') else file_num
                                file_name = re.split('[-|_]', origin_file_name)[1:]
                                file_name = ' '.join(file_name)
                                # file_name = ' '.join(origin_file_name.split('-')[1:])
                                target_file_name = course_num + '.' + class_num + '.' + section_num + '.' + file_num + ' ' + file_name
                                target_txt_file = os.path.join(path, target_file_name)
                                # 重命名
                                os.rename(txt_file, target_txt_file)


                        # 只保留 en.srt 文件和 zh-CN.srt 文件，删除其他 srt 文件
                        srt_files = glob.glob(os.path.join(section_dir, '*.srt'))
                        for srt_file in srt_files:
                            if not (srt_file.endswith("en.srt") or srt_file.endswith("zh-CN.srt")):
                                os.remove(srt_file)

                        # 重新遍历剩下 mp4 文件
                        mp4_files = glob.glob(os.path.join(section_dir, '*.mp4'))
                        # 重命名文件，加上章节号
                        for origin_mp4_file in mp4_files:
                            (path, origin_file_name) = os.path.split(origin_mp4_file)

                            file_num = origin_file_name[0:2]
                            file_num = file_num[1:2]  if file_num.startswith('0') else file_num
                            file_name = re.split('[-|_]',origin_file_name)[1:]
                            file_name = ' '.join(file_name)
                            #file_name = ' '.join(origin_file_name.split('-')[1:])
                            target_file_name = course_num+'.'+class_num+'.'+section_num+'.'+file_num+' '+file_name
                            target_mp4_file = os.path.join(path, target_file_name)
                            os.rename(origin_mp4_file, target_mp4_file)
                            print(target_file_name)



                        # 重新遍历剩下 srt 文件
                        srt_files = glob.glob(os.path.join(section_dir, '*.srt'))
                        # 重命名文件，加上章节号
                        for origin_srt_file in srt_files:
                            (path, origin_file_name) = os.path.split(origin_srt_file)

                            file_num = origin_file_name[0:2]
                            file_num = file_num[1:2]  if file_num.startswith('0') else file_num
                            file_name = re.split('[-|_]', origin_file_name)[1:]
                            file_name = ' '.join(file_name)
                            #file_name = ' '.join(origin_file_name.split('-')[1:])
                            target_file_name = course_num+'.'+class_num+'.'+section_num+'.'+file_num+' '+file_name
                            target_srt_file = os.path.join(path, target_file_name)
                            os.rename(origin_srt_file, target_srt_file)
                            print(target_file_name)