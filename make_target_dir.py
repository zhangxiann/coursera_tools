# 添加目标文件夹，文件夹结构和原来的一样，用于存放添加好字幕的视频文件
import os
import glob
import enviroments


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
                        section_dir = os.path.join(classes_dir, section)
                        enviroments.target_dir = os.path.join(enviroments.target, course, classes, section)
                        if not os.path.exists(enviroments.target_dir):
                            os.makedirs(enviroments.target_dir)
