#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    print("这里是main.py，是总文件夹目录 django-admin startproject backend使用这里命令创建backend作为django目录")
    print("并且创建一个web项目 使用django-admin startapp web 是django用来定义页面 html->view->url")
    print("python manage.py migrate 创建数据库表,之后还可以对接其他数据库再setting里面修改配置")
    print("python manage.py createsuperuser 创建超级用户 admin 123456 123@qq.com")
    print("python manage.py runserver 启动项目")
    print("修改配置文件settings.py 集成DRF、JWT和跨域支持")
    print("修改配置文件urls.py JWT接口，静态文件配置支持")
    print("配置python 对django的支持")


if __name__ == "__main__":
    main()
