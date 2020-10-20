

import os
import glob

import enviroments



# 源文件名
# introduction-tensorflow\1_a-new-programming-paradigm\01_a-new-programming-paradigm\01_introduction-a-conversation-with-andrew-ng.mp4

# 目标文件名
# 1 introduction-tensorflow\1_a-new-programming-paradigm\01_a-new-programming-paradigm\1.1.1 introduction a conversation with andrew ng.mp4

for course in os.listdir(enviroments.root_dir):
    course_dir = os.path.join(enviroments.root_dir, course)
    if os.path.isdir(course_dir):
        coursera_dir = os.path.join(enviroments.root_dir, course)
        for classes in os.listdir(coursera_dir):
            classes_dir = os.path.join(coursera_dir, classes)
            if os.path.isdir(classes_dir):
                # courses.append(course)
                for section in os.listdir(classes_dir):
                    section_dir = os.path.join(classes_dir, section)
                    if os.path.isdir(section_dir):
                        # 把文件名中 — 替换为空格
                        mp4_files = glob.glob(os.path.join(section_dir, '*.mp4'))
                        for origin_mp4_file in mp4_files:
                            (path, origin_file_name) = os.path.split(origin_mp4_file)
                            target_file_name = ' '.join(origin_file_name.split('-'))

                            target_mp4_file = os.path.join(path, target_file_name)
                            os.rename(origin_mp4_file, target_mp4_file)

                        # 把文件名中 — 替换为空格
                        srt_files = glob.glob(os.path.join(section_dir, '*.srt'))
                        for origin_srt_file in srt_files:
                            (path, origin_file_name) = os.path.split(origin_srt_file)
                            target_file_name = ' '.join(origin_file_name.split('-'))

                            target_srt_file = os.path.join(path, target_file_name)
                            os.rename(origin_srt_file, target_srt_file)
