#!/usr/bin/python
# coding=cp936
# python 3.x
#
# history:
# version 1.0
# 2010.2.15 support convert wizknowedge html file index.html to body only content.
# 2010.2.15 support wordpress new post, including upload media file.
# 2010.2.16 support get title from html file.
# 2010.2.16 support get fileserver from config file and upload images &post blog on it.
#

import xmlrpc.client
import pyblog
import re
import sys

import postblog_config

def usage():
    help = '''Usage:\r\n
              python.exe postblog.py config_file data_file html_filename\r\n''';
    print(help)


def get_html_content(filename):
	#�򿪴�ͼ��html�ļ�(Unicode����)
	html_file = open(filename, encoding='utf-16')
	html_file_content = html_file.read()
	html_file.close()

	#ɾ��\r\n��\n, re.S��ʾ.��ƥ��\n
	p = re.compile(r"\r?\n",re.S)
	html_file_content = p.sub("",html_file_content)

	#ȥ��ͷ
	p = re.compile(r'<!DOCTYPE HTML PUBLIC.*<TITLE>(.*)</TITLE>.*<BODY>',re.S)
	html_file_title = p.match(html_file_content).group(1)
	html_file_body = p.sub("",html_file_content)

	#ȥ��β
	p = re.compile(r'</BODY>.*</HTML>',re.S)
	html_file_body = p.sub("",html_file_body)
	return html_file_title, html_file_body

def upload_img(blog, imgname):
    print("Upload image file: %s ..." % imgname)
    file = open(imgname, "rb")
    content = xmlrpc.client.Binary(file.read())  #base 64 encoding binary
    file.close()
    type = 'image/jpeg'
    if imgname[-3:] == 'png':
        type = 'image/png'
    media_obj = {'name':imgname, 'type':type, 'bits':content}
    return blog.new_media_object(media_obj)

def proc_imgs(blog, config_file, img_list, content) :
    for img in img_list:
        imgurl = upload_img(blog, img)
        p = re.compile(img,re.S|re.I)
        content = p.sub(imgurl['url'], content)  #�滻html�ļ��е�imgͼƬ·��Ϊ����·��
    return content

def get_img_list(content):
	#��Сд���ԣ�Ҳ������re.I
	p = re.compile(r'''.*?<.*?IMG.*?src\s*=\s*"(.*?)".*?>.*?''',re.S|re.I)  #������ǰ���.*
	img_list = []
	iterator = p.finditer(content)
	for match in iterator:
		img_list.append(match.group(1))
	return img_list

def post_test(blog):
	print(blog.list_methods2());
	print(blog.method_help('metaWeblog.newPost'))
	print(blog.method_signature('metaWeblog.newPost'))
	print(blog.get_capabilities())
	print(blog.method_signature('metaWeblog.newMediaObject'))
	print(blog.get_recent_posts());

def post_blog(config_file, data_file, html_filename):
	#blog = pyblog.WordPress(posturl, username, password)

    print("Parsing html file content...")
    html_file_title, html_file_body = get_html_content(html_filename)

    print("Get image list...")
    img_list = get_img_list(html_file_body)
    print(img_list)

    print("Upload image files and replace content with image remote url...")
    fileserver = postblog_config.get_fileserver(config_file)
    blog = pyblog.WordPress(fileserver['posturl'], fileserver['username'], fileserver['password'])
    html_file_body = proc_imgs(blog, config_file, img_list, html_file_body)

    content = {"description":html_file_body, "title":html_file_title}

    if fileserver['postblog'] == 'true':
    	new_id = blog.new_post(content)
    	print ("Post successful on %s. postid: %s."  %(fileserver['name'], new_id))

##	return new_id


def main():
    if len(sys.argv) < 4:
        usage()
        return -1
    return post_blog(sys.argv[1], sys.argv[2], sys.argv[3])

if   __name__  ==  "__main__":
    main()



#test blog
##blog = pyblog.WordPress(posturl, username, password)
##post_test(blog)

#test get html title
##title, body = get_html_content("test/index.html")
##print(title)

