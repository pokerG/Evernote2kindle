import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStore
from evernote.api.client import EvernoteClient
import os
import re
import binascii
import gl

dev_token = "S=s1:U=90352:E=152493fde69:C=14af18eb060:P=1cd:A=en-devtoken:V=2:H=b78b93ed81c6c86246d15da2293430b8"

def downNote(fromnBs):
	if os.path.exists("images"):
		os.system('rm -rf '+ 'images')

	os.mkdir("images")
	
	client = EvernoteClient(token=dev_token)
	noteStore = client.get_note_store()
	nl = []
	guids = []
	note = Types.Note()
	noteBooks = noteStore.listNotebooks()
	for n in noteBooks:
		if (n.name in fromnBs) and (not n.guid in guids):
			# print n.name
			guids.append(n.guid) 

	# print guids
	
	for i in guids:
		nl.append(NoteStore.NoteFilter(notebookGuid=i))
	
	notes = []

	for i in nl:
		ns = noteStore.findNotes(i,0,20)
		for n in ns.notes:
			tm = noteStore.getNote(n.guid,True,True,False,False)
			notes.append(tm)
			print(tm.title)
	
			if tm.resources == None:
				with open("articles/" + tm.title + '.html','w') as f:
					f.write(tm.content)
				continue

			for j in tm.resources:
				print(j.attributes.fileName)
				tm.content = re.sub('en-media','img',tm.content)
				tm.content = re.sub('hash="'+binascii.hexlify(j.data.bodyHash)+'"','src="/home/pokerface/GitHub/Evernote2kindle/articles/images/'+j.attributes.fileName+'"',tm.content)
				# print(tm.content)
				print(binascii.hexlify(j.data.bodyHash))
				with open("articles/images/" + j.attributes.fileName,'w') as f:
					f.write(j.data.body)
				gl.imgs.append("articles/images/"+j.attributes.fileName)

			with open("articles/" + tm.title + '.html','w') as f:
					f.write(tm.content)
	return notes

if __name__ == '__main__':
	fromnBs = ['kindle']
	ns = downNote(fromnBs)
	# for i in ns:
	# 	print i.resources
	