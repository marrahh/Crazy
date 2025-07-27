from tkinter import *
from tkinter import ttk
from mtranslate import translate
import random


def tr_text():
    try:
        for _ in range(5):
            translate_btn.config(
                bg=f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}')
            root.update()
            root.after(50)

        text = input_text.get('1.0', END).strip()
        if not text:
            return

        lang_in = langs[scr_lang.get()]
        lang_out = langs[tr_lang.get()]

        translated = translate(text, lang_out, lang_in)
        out_text.delete('1.0', END)
        out_text.insert(END, translated)

        for i in range(1, 6):
            out_text.config(fg=f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}')
            root.update()
            root.after(100)
        out_text.config(fg='black')

    except Exception as e:
        out_text.delete('1.0', END)
        out_text.insert(END, f'ОШИБКА: {str(e).upper()}!!!', 'error')


def clear():
    input_text.delete('1.0', END)
    out_text.delete('1.0', END)
    for x in range(3):
        root.config(bg=f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}')
        root.update()
        root.after(100)
    root.config(bg='#00FFAA')


def change_bg():
    colors = ['#FF00FF', '#00FFFF', '#FFFF00', '#FF00AA', '#AA00FF']
    root.config(bg=random.choice(colors))
    for widget in root.winfo_children():
        try:
            widget.config(bg=random.choice(colors))
        except:
            pass


langs = {
    'АНГЛИЙСКИЙ!!!': 'en',
    'РУССКИЙ!!': 'ru',
    'ИСПАНСКИЙ!': 'es',
    'ФРАНЦУЗСКИЙ?!': 'fr',
    'НЕМЕЦКИЙ??': 'de',
    'КИТАЙСКИЙ O_O': 'zh',
    'ЯПОНСКИЙ ^_^': 'ja',
    'АРАБСКИЙ @_@': 'ar'
}

root = Tk()
root.title('ПЕРЕВОДЧИК')
root.geometry('700x700')
root.resizable(0, 0)

root.config(bg='#00FFAA')

style = ttk.Style()
style.theme_create('crazy', settings={
    'TCombobox': {
        'configure': {
            'fieldbackground': '#FF00FF',
            'background': '#FFFF00',
            'foreground': '#FF0000',
            'font': ('Impact', 14)
        }
    }
})
style.theme_use('crazy')

crazy_font = ('Comic Sans MS', 14, 'bold')

title = Label(root,
              text='╰(*°▽°*)╯ СУМАСШЕДШИЙ ПЕРЕВОДЧИК ╰(*°▽°*)╯',
              bg='#FF00FF',
              fg='#FFFF00',
              font=('Impact', 18, 'bold'),
              relief=RAISED,
              bd=5)
title.pack(fill=X, pady=(10, 20))

input_frame = Frame(root, bg='#FF00AA')
input_frame.pack(pady=10)

scr_lang = ttk.Combobox(input_frame,
                        values=list(langs.keys()),
                        width=25,
                        font=crazy_font)
scr_lang.set('РУССКИЙ!!')
scr_lang.pack(side=TOP, padx=10, pady=5)

input_text = Text(input_frame,
                  height=7,
                  width=50,
                  font=crazy_font,
                  wrap=WORD,
                  bg='#FFFF00',
                  fg='#FF00FF',
                  selectbackground='#00FFFF',
                  selectforeground='#FF0000',
                  insertbackground='#FF0000',
                  relief=GROOVE,
                  bd=8)
input_text.pack(padx=10, pady=5)

translate_frame = Frame(root, bg='#00FFFF')
translate_frame.pack(pady=10)

translate_btn = Button(translate_frame,
                       text='ПЕРЕВЕСТИ!!! (╯°□°)╯',
                       command=tr_text,
                       bg='#FF0000',
                       fg='#00FF00',
                       activebackground='#00FF00',
                       activeforeground='#FF0000',
                       font=crazy_font,
                       relief=RAISED,
                       bd=5)
translate_btn.pack(side=LEFT, padx=5)

crazy_btn = Button(translate_frame,
                   text='CRAZY MODE!!!',
                   command=change_bg,
                   bg='#0000FF',
                   fg='#FF00FF',
                   font=crazy_font,
                   relief=RAISED,
                   bd=5)
crazy_btn.pack(side=LEFT, padx=5)

clear_btn = Button(translate_frame,
                   text='ОЧИСТИТЬ ВСЁ!!!',
                   command=clear,
                   bg='#00FF00',
                   fg='#0000FF',
                   font=crazy_font,
                   relief=RAISED,
                   bd=5)
clear_btn.pack(side=LEFT, padx=5)

tr_lang_frame = Frame(root, bg='#FF00FF')
tr_lang_frame.pack(pady=10)

tr_lang = ttk.Combobox(tr_lang_frame,
                       values=list(langs.keys()),
                       width=25,
                       font=crazy_font)
tr_lang.set('АНГЛИЙСКИЙ!!!')
tr_lang.pack(side=TOP, padx=10, pady=5)

output_frame = Frame(root, bg='#FFFF00')
output_frame.pack(pady=10)

out_text = Text(output_frame,
                height=7,
                width=50,
                font=crazy_font,
                wrap=WORD,
                bg='#00FFFF',
                fg='#FF00FF',
                relief=GROOVE,
                bd=8)
out_text.pack(padx=10, pady=5)
out_text.tag_config('error', foreground='#FF0000', font=('Impact', 16, 'bold'))

footer = Label(root,
               text='(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ПЕРЕВОДИ С УДОВОЛЬСТВИЕМ! ✧ﾟ･: *ヽ(◕ヮ◕ヽ)',
               bg='#00FF00',
               fg='#FF00FF',
               font=crazy_font,
               relief=SUNKEN,
               bd=5)
footer.pack(fill=X, pady=(20, 10))

root.mainloop()
