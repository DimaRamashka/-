import requests
import json
import socket

from pygame import mixer
import pyglet
import urllib3

from tkinter import *

def mycom():
	e = edit.get()
	print (e)

win = Tk()
win.geometry('500x300')


t1 = Label(win, text = 'Enter ' , fg = 'blue')
t1.config(font = ('fjjf', 35))
t2 = Label(win, text = 'Melody' , fg = 'green')
t2.config(font = ('fjjd', 50))

t2.pack()
t1.pack()

edit = Entry (win, width  = 40)
edit.pack()

but = Button(win, text = 'Search', command = mycom )
but.pack()
while True:
	print("ENTER_AUTHOR")
	author_name = str(input())
	if author_name == "quit":
		quit()

	start_pos= 0
	page_size = 10
	choose = 1
	while choose != "quit":
		if choose == 'next_page':
			start_pos += 10
			# page_size = 10

		resp = requests.get("https://frs.noosphere.ru/solr/search/select?wt=json&fl=search.resourceid&fl=location.coll&fl=handle&dc.date&fl=dc.title&fl=dc.source&fl=dc.creator&fl=dc.rights&fl=dc.type&sort=bi_sort_3_sort+desc&rows=16&start=" + str(start_pos) + "&q=search.resourcetype%3A2&fq=dc.type%3A%22%D0%BC%D1%83%D0%B7%D1%8B%D0%BA%D0%B0%22&fq=dc.creator%3A" + author_name + "&omitHeader=true")
		j = json.loads(resp.text)
		aou = [] ##array of urls
		aon = [] #names
		aoid = [] #file id
		# print(j["response"])
		for i in range(page_size):
			aon.append(j["response"]["docs"][i]['dc.title'])
			aoid.append(j["response"]["docs"][i]['handle'])
			print(aon[i][0])
		print("CHOOSE_COMPOSITION_OR_NEXT_PAGE")
		choose = str(input())

		if choose in ["0","1","2","3","4","5","6","7","8","9"]:
			choose = int(choose)
			break



	for i in range(page_size):
		if choose == i:
			track_url = "https://frs.noosphere.ru/xmlui/bitstream/handle/" + aoid[i] + "/" + aoid[i] + "?sequence=1"
		pass



	http = urllib3.PoolManager()
	r = http.request('GET', track_url, preload_content=False)

	# f = open('C:/Bathoven.mp3',"wb")

	mixer.init()
	# mixer.music.load('C:/Bathoven.mp3')
	# mixer.music.play()

	b = open("C:/Bathoven0.mp3", 'wb')
	b.truncate(0)

	n = 0
	k = 0

	queue = []
	for chunk in r.stream(1024):
		b.write(chunk)

		n += 1
		if n > 1000:
			b.close()
			if k == 0:
				mixer.music.load("C:/Bathoven" + str(k) +  ".mp3")
				mixer.music.play(0)
				# mixer.music.set_endevent(next_part_in_queue(k + 2))

			elif k == 1:
				queue.append(k)
				mixer.music.queue("C:/Bathoven" + str(k) +  ".mp3")
				queue.pop(0)
				# mixer.music.set_endevent(next_part_in_queue(k + 2))
			else:
				queue.append(k)
			k += 1
			b = open("C:/Bathoven" + str(k) +  ".mp3", 'wb')
			b.truncate(0)
			n = 0

	b.close()


	queued = 1

	while True:
		# print(mixer.music.get_pos())
		# if mixer.music.get_pos() > 5000 and queued == 1:
		# 	queued = 0
		# if queued == 0 and mixer.music.get_pos() == 500:

		if mixer.music.get_busy() == False:
			# print(music.music.get_pos())
			mixer.music.load("C:/Bathoven" + str(queue[0]) +  ".mp3")
			mixer.music.play(0)
			queue.pop(0)
			queued = 1
		if mixer.music.get_busy() == False and not queue:
			break
		# if mixer.music.get_pos() < -1:
		# 	print('kek',mixer.music.get_pos())
		# 	break

