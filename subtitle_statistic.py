# 统计 已经翻译的字幕 和 没有翻译的字幕
# 保存到 markdown 文件中

import os
import glob

import enviroments

all_count =0
missing_count =0
progress_log = os.path.join(enviroments.root_dir, 'progress.md')
f_log = open(progress_log, "w+")

for course in os.listdir(enviroments.root_dir):
    if course.startswith('.'):
        continue
    course_dir = os.path.join(enviroments.root_dir, course)
    if os.path.isdir(course_dir):
        course_num = course[0:1]
        coursera_dir = os.path.join(enviroments.root_dir, course)
        f_log.write('\n# '+course + '\n')
        for classes in os.listdir(coursera_dir):
            classes_dir = os.path.join(coursera_dir, classes)
            if os.path.isdir(classes_dir):
                class_num = classes[0:1]
                f_log.write('\n## ' + course_num+'.'+class_num +' '+ classes[2:] + '\n')
                # courses.append(course)
                for section in os.listdir(classes_dir):
                    section_dir = os.path.join(classes_dir, section)
                    if os.path.isdir(section_dir):


                        f_log.write('\n## ' + course_num + '.' + class_num + '.'+ section[1:] + '\n')
                        # f_log.write('\n### ' + section + '\n')
                        english_srt_files = glob.glob(os.path.join(section_dir, '*en.srt'))

                        for english_srt_file in english_srt_files:

                            all_count =all_count+1
                            bilingual_srt_file = english_srt_file[:-6] + 'bilingual.srt'
                            if not os.path.exists(bilingual_srt_file):
                                missing_count = missing_count+1
                                f_log.write('- [ ] ' + os.path.basename(english_srt_file) + '\n')
                            else:
                                f_log.write('- [x] ' + os.path.basename(english_srt_file) + '\n')





