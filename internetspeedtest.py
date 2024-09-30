from tkinter import *
import speedtest

def speedcheck():
    st = speedtest.Speedtest()  
    st.get_best_server()
    down_speed = round(st.download() / (10**6), 3)  
    up_speed = round(st.upload() / (10**6), 3)      
    
    lab_down.config(text=f"{down_speed} MBPS")
    lab_up.config(text=f"{up_speed} MBPS")

root = Tk()
root.title("Internet Speed Tester Tool")
root.geometry("500x600")
root.config(bg="green")

title_label = Label(root, text="Internet Speed Tester Tool", font=("Times New Roman", 40, "bold"), bg="pink", fg="blue")
title_label.place(x=50, y=50, height=50, width=380)

download_label = Label(root, text="Download Speed", font=("Times New Roman", 40, "bold"))
download_label.place(x=50, y=100, height=50, width=380)

lab_down = Label(root, text="00 MBPS", font=("Times New Roman", 40, "bold"))
lab_down.place(x=50, y=150, height=50, width=380)

upload_label = Label(root, text="Upload Speed", font=("Times New Roman", 40, "bold"))
upload_label.place(x=50, y=250, height=50, width=380)

lab_up = Label(root, text="00 MBPS", font=("Times New Roman", 40, "bold"))
lab_up.place(x=50, y=300, height=50, width=380)

button = Button(root, text="Check Internet Speed", font=("Times New Roman", 40, "bold"), relief=RAISED, bg="yellow", command=speedcheck)
button.place(x=50, y=400, height=50, width=380)

root.mainloop()
