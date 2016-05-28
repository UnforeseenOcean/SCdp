#! python2

import matplotlib, Tkinter, pydub, os, webbrowser, ctypes, wget


def checker():

    if os.path.exists('C:\\Python27') == True and os.path.exists('C:\\ffmpeg') == True:
        audio_w()

    else:
        ctypes.windll.user32.MessageBoxA(0, "Make sure you\'ve got Python 2.7, FFmpeg and SoundScrape installed!",
                                         "ERROR!", 0)

        webbrowser.open('https://www.python.org/downloads/')
        webbrowser.open('https://ffmpeg.zeranoe.com/builds/')
        webbrowser.open('https://www.youtube.com/watch?v=xcdTIDHm4KM')
        webbrowser.open('https://github.com/Miserlou/SoundScrape')


def download(url):
    try:
        ctypes.windll.user32.MessageBoxA(0, "Your music is being downloaded. Please wait...",
                                         "WARNING!", 0)
        os.system('soundscrape %s' % (url))
        ctypes.windll.user32.MessageBoxA(0, "Your music has been downloaded successfully!",
                                         "WARNING!", 0)
    except:
        pass


def convert(file_name):

    pydub.AudioSegment.from_mp3(os.getcwd() + "\\%s.mp3" % (file_name)).\
        export(os.getcwd() + '\\%s.wav' % (file_name), format='wav')
    os.system('del %s\\%s.mp3' % (os.getcwd(), file_name))


def m_search(music):
    global url
    url = 'https://soundcloud.com/search/sounds?q=%s' % (music.replace(' ', '%20'))
    wget.download(url)
    os.system('rename sounds sounds.txt')
    source = open('sounds.txt')
    list = source.readlines()
    # 121 - 130

    global list_def
    list_def=[]
    global list_def_2
    list_def_2=[]


    for i in range(9):
        list_def.append(list[i + 121])

    for i in range(9):
        list_def_2.append(list[i + 121])

    source.close()
    os.system('del sounds.txt')

    for k in range(9):
        for j in range(len(list_def[k][23:])):
            if list_def[k][23:][j] == '>':
                list_def[k] = list_def[k][24 + j:]
                list_def_2[k] = list_def_2[k][23:]
                list_def_2[k] = list_def_2[k][:j - 1]
                break
        list_def[k] = list_def[k][:len(list_def[k]) - 15]


def audio_w():


    root = Tkinter.Tk()
    root.title('SCdp')
    root.geometry('500x400')
    root.resizable(width='FALSE', height='FALSE')
    root.configure(background='gray5')



    f1 = Tkinter.Frame()
    f2 = Tkinter.Frame()


    title = Tkinter.Label(font=('Adobe Myungjo Std M', 32), text= 'SCdp',
                          background='gray5', foreground='white')
    title.pack(anchor='s')


    def get():
        s_term = entry.get()
        m_search(s_term)
        labels()


    entry = Tkinter.Entry(f1,width=60)
    button_1 = Tkinter.Button(f2,command=get, text='Search it!', height=1, width=12, font = ('Helvetica', 8),
                              background = 'gray80')
    def labels():
        tt = True
        try:
            ass = ass+2
            if ass >= 2:
                global ass
                del ass
                root.destroy()
                audio_w()
                tt = False
            else:
                pass
        except:
            global ass
            ass = 0

        la = []
        for i in range(15):
            if tt == True:
                la.append(i)
                if i >= 6:
                        la[i] = Tkinter.Label(font=('Adobe Myungjo Std M', 9), text=list_def[i-6],
                                            background='gray5', foreground='white', cursor="hand2")
                        la[i].bind("<1>", lambda event:download('https://soundcloud.com' + list_def_2[i-6]))
                else:
                        la[i] = Tkinter.Label(font=('Adobe Myungjo Std M', 9), text=' ',
                                            background='gray5', foreground='white')
                la[i].grid(sticky='ssw')
            else:
                tt = True
                break





    f1.pack(side='right',anchor='s', expand=True)
    f2.pack(side='left', expand=True,anchor='s')
    button_1.pack()
    entry.pack()
    root.mainloop()


checker()



