#______________| SCRIPT INFO |_________________#
#CODED BY  CYBER-COP
#TEAM > CYBER-COP-BANGLADESH
#GITHUB > CYBERCOP-404
#__________________| IMPORT |__________________#
import os, requests, marshal, zlib, base64
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';Y = '\033[1;33m';G = '\033[1;96m';R = '\x1b[38;5;196m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X5 = '\x1b[38;5;121m'
#__________________| Logo |__________________#
logo = (f'''
\033[1;92m \x1b[38;5;46m  ███████ ███    ██  ██████  
\033[1;92m \x1b[38;5;47m  ██      ████   ██ ██        
\033[1;92m \x1b[38;5;48m  █████   ██ ██  ██ ██      
\033[1;92m \x1b[38;5;49m  ██      ██  ██ ██ ██       
\033[1;92m \x1b[38;5;50m  ███████ ██   ████  ██████  
 {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{X2}【{X5}✦{X2}】{Y}DEVELOPER   {B}»----{A}➤ {G3}CYBER-COP
{X2}【{X5}✦{X2}】{Y}GITHUB      {B}»----{A}➤ {G3}CYBERCOP-404 
{X2}【{X5}✦{X2}】{Y}TELEGRAM    {B}»----{A}➤ {G3}@cybercopbangladesh
{X2}【{X5}✦{X2}】{Y}VERSION     {B}»----{A}➤ {G3}1.0.5
{X2}【{X5}✦{X2}】{Y}TOOL'S NAME {B}»----{A}➤ {G3}[\x1b\033[38;5;196m\x1b[1;97m\x1b[1;41mPYTHON ENCRYPTION\x1b[0m{G3}]
 {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

#__________________| Menu |__________________#
def U7P4L():
    os.system('clear');os.system("xdg-open https://github.com/CYBERCOP-404 ");os.system("clear");print(logo);print(f'{B}【{A}01{B}】{G2}ENCRYPT BASE16');print(f'{B}【{A}02{B}】{G2}ENCRYPT BASE32');print(f'{B}【{A}03{B}】{G2}ENCRYPT BASE64 ');print(f'{B}【{A}04{B}】{G2}ENCRYPT MARSHAL');print(f'{B}【{A}05{B}】{G2}ENCRYPT MARSHAL-ZLIB-BASE16');print(f'{B}【{A}06{B}】{G2}ENCRYPT MARSHAL-ZLIB-BASE32');print(f'{B}【{A}07{B}】{G2}ENCRYPT MARSHAL-ZLIB-BASE64');print(f'{B}【{A}08{B}】{G1}FIND MORE TOOLS ');print(f'{B}【{A}00{B}】{R}EXIT PROGRAMME ')
    print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    u7p4l=input(f'{B}【{A}•{B}】{G}CHOICE {A}➤\033[1;32m ')
    if u7p4l in ['1','01','A','a']:
        os.system('clear');print(logo);x1()
    elif u7p4l in ['2','02','B','b']:
    	os.system('clear');print(logo);x2()
    elif u7p4l in ['3','03','C','c']:
    	os.system('clear');print(logo);x3()
    elif u7p4l in ['4','04','D','d']:
    	os.system('clear');print(logo);x4()
    elif u7p4l in ['5','05','E','e']:
    	os.system('clear');print(logo);x5()
    elif u7p4l in ['6','06','F','f']:
    	os.system('clear');print(logo);x6()
    elif u7p4l in ['7','07','G','g']:
    	os.system('clear');print(logo);x7()
    elif u7p4l in ['8','08','H','h']:
    	os.system('xdg-open https://github.com/CYBERCOP-404')
    elif u7p4l in ['0','00','i','I']:
    	exit(f'{B}【{A}={B}】{G}EXIT DONE \n\n')
    else:
        print(f'{B}【{A}={B}】{G}OPTION NOT FOUND IN MENU...')
        U7P4L()

#__________________|  All Method |__________________#
def x1():
    u7p4l = input(f'\n{B}【{A}={B}】{G1}INPUT FILE NAME {A}➤{G} ')
    ups = open(u7p4l, 'rb').read()
    ui = base64.b16encode(ups)
    output = u7p4l.replace('.py', '') + '_enc.py'
    cok = open(output, 'w').write('#__________________| INFO |___________________#\n#______SCRIPT ENCRYPTED BY PYTHON 3.0\n#______CODING BY: CYBER-COP\n#______GITHUB : https://github.com/CYBERCOP-404\n #________________| SCRIPT DATA |_____________#\n\nimport base64\nexec(base64.b16decode(' + str(ui) + '))')
    print(f"{B}【{A}={B}】{X1}SUCCESSFULLY ENCRYPTED {A}➤{Y} %s" % u7p4l)
    print(f"{B}【{A}={B}】{X2}SAVED AS {A}➤{Y} %s" % output)
    print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def x2():
	u7p4l = input(f'\n{B}【{A}={B}】{G1}INPUT FILE NAME {A}➤{G} ')
	ups = open(u7p4l, 'rb').read()
	ui = base64.b32encode(ups)
	output = u7p4l.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#__________________| INFO |___________________#\n#______SCRIPT ENCRYPTED BY PYTHON 3.0\n#______CODING BY: CYBER-COP\n#______GITHUB : https://github.com/CYBERCOP-404\n #--------------------😇😇-------------------#\n # বাপের script Decode করতে আইছোত মাগির পোলা চুইদা মাইরালামু😂😈🖕🖕\n # আবাল মাদারচোদ বাপের সাথে এ আবলামি করবি না #####\n#________________| SCRIPT DATA |_____________#\n\nimport base64\nexec(base64.b32decode(' + str(ui) + '))')
	print(f"{B}【{A}={B}】{X1}SUCCESSFULLY ENCRYPTED {A}➤{Y} %s" % u7p4l)
	print(f"{B}【{A}={B}】{X1}SAVED AS {A}➤{Y} %s" % output)
	print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	
def x3():
	u7p4l = input(f'\n{B}【{A}={B}】{G1}INPUT FILE NAME {A}➤{G} ')
	ups = open(u7p4l, 'rb').read()
	ui = base64.b64encode(ups)
	output = u7p4l.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#__________________| INFO |___________________#\n#______SCRIPT ENCRYPTED BY PYTHON 3.0\n#______CODING BY: CYBER-COP\n#______GITHUB : https://github.com/CYBERCOP-404\n#________________| SCRIPT DATA |_____________#\n\nimport base64\nexec(base64.b64decode(' + str(ui) + '))')
	print(f"{B}【{A}={B}】{X1}SUCCESSFULLY ENCRYPTED {A}➤{Y} %s" % u7p4l)
	print(f"{B}【{A}={B}】{X2}SAVED AS {A}➤{Y} %s" % output)
	print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	
def x4():
	u7p4l = input(f'\n{B}【{A}={B}】{G1}INPUT FILE NAME {A}➤{G} ')
	fileopen = open(u7p4l, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	s = repr(m)
	output = u7p4l.replace('.py', '') + '_enc.py'
	d = open(output, 'w').write('#__________________| INFO |___________________#\n#______SCRIPT ENCRYPTED BY PYTHON 3.0\n#______CODING BY: CYBER-COP\n#______GITHUB : https://github.com/CYBERCOP-404\n#________________| SCRIPT DATA |_____________#\n\nimport marshal\nexec(marshal.loads(' + s + '))')
	print(f"{B}【{A}={B}】{X1}SUCCESSFULLY ENCRYPTED {A}➤{Y} %s" % u7p4l)
	print(f"{B}【{A}={B}】{X1}SAVED AS {A}➤{Y} %s" % output)
	print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def x5():
	u7p4l = input(f'\n{B}【{A}={B}】{G1}INPUT FILE NAME {A}➤{G} ')
	fileopen = open(u7p4l, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b16encode(z)
	output = u7p4l.replace('.py', '') + '_enc.py'
	d = open(output, 'w').write('#__________________| INFO |___________________#\n#______SCRIPT ENCRYPTED BY PYTHON 3.0\n#______CODING BY: CYBER-COP\n#______GITHUB : https://github.com/CYBERCOP-404\n#________________| SCRIPT DATA |_____________#\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode(' + str(b) + '))))')
	print(f"{B}【{A}={B}】{X1}SUCCESSFULLY ENCRYPTED {A}➤{Y} %s" % u7p4l)
	print(f"{B}【{A}={B}】{X2}SAVED AS {A}➤{Y} %s" % output)
	print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	
def x6():
	u7p4l = input(f'\n{B}【{A}={B}】{G1}INPUT FILE NAME {A}➤{G} ')
	fileopen = open(u7p4l, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b32encode(z)
	output = u7p4l.replace('.py', '') + '_enc.py'
	d =open(output, 'w').write('#__________________| INFO |___________________#\n#______SCRIPT ENCRYPTED BY PYTHON 3.0\n#______CODING BY: CYBER-COP\n#______GITHUB : https://github.com/CYBERCOP-404\n#________________| SCRIPT DATA |_____________#\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode(' + str(b) + '))))') 
	print(f"{B}【{A}={B}】{X1}SUCCESSFULLY ENCRYPTED {A}➤{Y} %s" % u7p4l)
	print(f"{B}【{A}={B}】{X2}SAVED AS {A}➤{Y} %s" % output)
	print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	
def x7():
	u7p4l = input(f'\n{B}【{A}={B}】{G1}INPUT FILE NAME {A}➤{G} ')
	fileopen = open(u7p4l, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b64encode(z)
	output = u7p4l.replace('.py', '') + '_enc.py'
	d = open(output, 'w').write('#__________________| INFO |___________________#\n#______SCRIPT ENCRYPTED BY PYTHON 3.0\n#______CODING BY: CYBER-COP\n#______GITHUB : https://github.com/CYBERCOP-404\n#________________| SCRIPT DATA |_____________#\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode(' + str(b) + '))))')
	print(f"{B}【{A}={B}】{X1}SUCCESSFULLY ENCRYPTED {A}➤{Y} %s" % u7p4l)
	print(f"{B}【{A}={B}】{X2}SAVED AS {A}➤{Y} %s" % output)
	print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	
	
U7P4L()
#__________________| FINISHED  |__________________#
