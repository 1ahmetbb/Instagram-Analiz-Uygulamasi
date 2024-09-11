import instaloader
import tkinter as tk
from tkinter import ttk, messagebox

#Kullanici bilgilerini cek
def get_user_info(username):
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, username)

    #Sozluk olustur
    user_info = {
        'Username' : profile.username,
        'Followers' : profile.followers,
        'Followees' : profile.followees,
        'Post Count' : profile.mediacount,
        'Last Post Date' : get_last_post_date(profile)
    }
    return user_info

#Kullanicinin son gonderi tarihi cekme

def get_last_post_date(profile):
    last_post = None

    for post in profile.get_posts():
        if not last_post or post.date_utc > last_post.date_utc:
            last_post = post
    return last_post.date_utc.strftime("%Y-%m-%d %H:%M:%S")


#Kullanici bilgilerini goruntule

def show_user():
    username = entry_username.get()
    user_info = get_user_info(username)
    if isinstance(user_info,dict):
        for widget in tree.get_children():
            tree.delete(widget)
        #tabloya kullanici verilerini ekle.
        tree.insert('','end', values=(
            user_info['Username'],
            user_info['Followers'],
            user_info['Followees'],
            user_info['Post Count'],
            user_info['Last Post Date']
        ))
    else:
        messagebox.showerror('Hata', user_info)

root = tk.Tk()
root.title('Instagram Kullanici Bilgi Goruntuleyicisi')

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text='Kullanici Adi:')
label.grid(row=0, column=0, padx=5, pady=5)

entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(frame, text='Bilgileri Goruntule', command=show_user)
search_button.grid(row=0, column=2, padx=5, pady=5)

tree = ttk.Treeview(root, columns=('Username', 'Followers', 'Followees', 'Post Count', 'Last Post Date'))
tree.heading('Username',text='Kullanici Adi:')
tree.heading('Followers', text='Takipciler')
tree.heading('Followees', text='Takip Edilenler')
tree.heading('Post Count', text='Gonderi Sayisi')
tree.heading('Last Post Date', text='Son Gonderi Tarihi')
tree.pack(padx=20, pady=20)


root.mainloop()
