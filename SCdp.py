#! python2

import Tkinter, os, webbrowser, ctypes, wget

def checker():
    if os.path.exists('C:\\Python27') == True:
        audio_w()

    else:
        ctypes.windll.user32.MessageBoxA(0, "Make sure you\'ve got Python 2.7 and SoundScrape installed!",
                                         "ERROR!", 0)
        webbrowser.open('https://www.python.org/downloads/')
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


    def listbox():
            la = []

            lb = Tkinter.Listbox(root)
            lb.configure(width= 70, font=('Helvetica', 10), background ='gray87', bd = 0)
            for bolb in range(9):
                lb.insert(1, list_def[bolb])
            for jj in range(6):
                la.append(jj)
                la[jj] = Tkinter.Label(font=('Adobe Myungjo Std M', 10), text=' ',
                                            background='gray5', foreground='white')
                la[jj].grid(sticky='ssw')


            def ala():
                gay = lb.curselection()
                batata = str(gay)[1]
                download('https://soundcloud.com' + list_def_2[int(batata)])

                global alu
                alu = True
              
            lb.bind('<<ListboxSelect>>', lambda event:ala())
            lb.grid(sticky='ssw')


    def get():
        global alu
        try:
            if alu == True:
                root.destroy()
                audio_w()
                del alu
        except:
            s_term = entry.get()
            m_search(s_term)
            listbox()


    entry = Tkinter.Entry(f1,width=60)
    button_1 = Tkinter.Button(f2,command=get, text='Search it!', height=1, width=12, font = ('Helvetica', 8),
                              background = 'gray80')
    f1.pack(side='right',anchor='s', expand=True)
    f2.pack(side='left', expand=True,anchor='s')
    button_1.pack()
    entry.pack()
    root.mainloop()


checker()



# cr4sh3r
