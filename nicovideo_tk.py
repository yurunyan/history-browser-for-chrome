import tkinter as tk
from tkinter import ttk
import nicovideo


    
def main():
    root = tk.Tk()
    root.title('demo_tk')
    root.geometry("1300x800")
    #button = tk.Button(root, text="ボタン", command=btn1push)
    #button.grid()
    tree = ttk.Treeview(root)
    #tree.place(x=30, y=30)
    tree["column"] = (1,2,3)
    tree["show"] = "headings"
    tree.heading(1,text="url")
    tree.heading(2,text="latest access time")
    tree.heading(3, text="page title")
    tree.column(1, width=100)
    tree.column(2, width=50)
    tree.column(3, width=200)
    for x in nicovideo.search_nicovideo():
        tree.insert("", "end", values=(x[0], x[1], x[2]))
    #tree.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
    tree.place(relheight=1,relwidth=0.99,relx=0.0,rely=0.0)
    scrollbar = ttk.Scrollbar(root, orient = tk.VERTICAL, command=tree.yview)
    #tree.configure(yscrollcommand=lambda f, l: scrollbar.set(l, f))
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(relheight=1,relwidth=0.05,relx=0.96,rely=0.0)
    #scrollbar.pack(fill='y')
    root.mainloop()

if __name__ == '__main__':
    main()