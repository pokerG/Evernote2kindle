#-*- coding: UTF-8 -*-
import config_parse
import note
import epub
import mail
import time
import os
import gl

config = config_parse.ParseConfig()
b = epub.EpubBook('evernote')

for i in config['evernote']['notebook']:
	notes = note.downNote(str(i))
	for n in notes:
		b.book.append(epub.article(n.title,n.content))
	for j in gl.imgs:
		print(j)
		b.newImg(j)
b.Save2Epub()
b.Calibre_Convert('evernote.mobi')

mail.Run(config['gmail']['user'],config['kindlemail'],os.getcwd(),'evernote.mobi')