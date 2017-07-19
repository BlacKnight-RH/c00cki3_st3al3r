#!/usr/bin/python 

import urllib2 
import sys 
import getopt


class colors:
	red = "\033[1;31m"
	white = "\033[1;37m"
	normal = "\033[0;00m"
	blue = "\033[1;34m"
	green = "\033[1;32m"
	lightblue = "\033[0;34m"


def main(argv): 

	user_url = ''
	out_file_name = None

	if len(sys.argv) == 1 : 
		help()

	try :
		opts, args = getopt.getopt(argv,"hu:o:",["url=","ofile="])	
	except getopt.GetoptError:
		print colors.red + './c00ki3_st3al3r.py -u <URL>  [ -o <outputfile> ]'
		sys.exit(2)


	for opt, arg in opts:
		if opt == '-h':
			help()
		elif opt in ("-u", "--url"):
			user_url = arg 
		elif opt in ("-o", "--ofile"):
			out_file_name = arg


	myurl = user_url

	try :
		response = urllib2.urlopen(myurl)
		#html = page.readlines()
		info = response.info()
		print colors.blue + "\nresponse code : {0}\n".format(response.code)
		
		set_cookie_header = info.getheader('set-cookie')

		cookie_output = ""

		if set_cookie_header != None: 
			cookie_output +=  set_cookie_header + "\n"




		if out_file_name != None: 
			
			file = open( out_file_name , 'w')
			
			try:

				file.write(cookie_output)

				print colors.green + "[*] ... output file " + out_file_name

			except Exception as e:
				print colors.red + "[*] ... can't write data into this file "

		else : 

			print colors.normal + cookie_output + "\n"


	except Exception as e : 
		print colors.red + "[x] ... Can't connect to that URL "









def banner():
	signature = colors.red + r""" 
	         ____  _            _        _  __      _       _     _   
		| __ )| | __ _  ___| | __   | |/ /_ __ (_) __ _| |__ | |_ 
		|  _ \| |/ _` |/ __| |/ /   | ' /| '_ \| |/ _` | '_ \| __|
		| |_) | | (_| | (__|   <    | . \| | | | | (_| | | | | |_ 
		|____/|_|\__,_|\___|_|\_\___|_|\_\_| |_|_|\__, |_| |_|\__|
		                        |_____|            |___/           
		""" + "\n"
	print signature 

def help():
	banner()
	print colors.red + './c00ki3_st3al3r.py -u <URL>  [ -o <outputfile> ] \n'
	print colors.blue + '-h' + colors.normal +'\t' + 'show help menu'
	print colors.blue + '-u' + colors.normal +'\t' + 'URL link ex: http://google.com '
	print colors.blue + '-o' + colors.normal +'\t' + 'output file'
	sys.exit(3) 
	


if __name__ == "__main__" : 
	main(sys.argv[1:])