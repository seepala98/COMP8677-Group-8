import tkinter as tk
from tkinter import ttk
import scapy.all as scapy
import threading
import collections


def start_button():
    print('Start button clicked')
    global should_we_stop
    global thread
    global subdomain
    global ttye

    subdomain = subdomain_entry.get()
    ttye = ttye_entry.get()

    if (thread is None) or (not thread.is_alive()):
        should_we_stop = False
        thread = threading.Thread(target=sniffing)
        thread.start()


def stop_button():
    global should_we_stop
    should_we_stop = True


def sniffing():
    scapy.sniff(prn=find_ips, stop_filter=stop_sniffing)


def stop_sniffing(packet):
    global should_we_stop
    return should_we_stop


def find_ips(packet):
    global scr_ip_dict
    global trevv
    global subdomain
    global ttye

    if ttye in packet:
        if 'IP' in packet:

            print(packet.show())
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst

            if src_ip[0:len(subdomain)] == subdomain:
                if src_ip not in scr_ip_dict:
                    scr_ip_dict[src_ip].append((dst_ip))

                    print('******************************')
                    row = treev.insert('', index=tk.END, text=src_ip)
                    treev.insert(row, tk.END, text=dst_ip)
                    treev.pack(fill=tk.X)
                else:
                    print('**********', ttye, subdomain)
                    if dst_ip not in scr_ip_dict[src_ip]:
                        scr_ip_dict[src_ip].append((dst_ip))

                    cur_item = treev.focus()

                    if treev.item(cur_item)['text'] == src_ip:
                        treev.insert(cur_item, tk.END, text=dst_ip)


thread = None
should_we_stop = True
subdomain = ''

scr_ip_dict = collections.defaultdict(list)
root = tk.Tk()
root.geometry('500x500')
root.title('Packet Analyzer')

tk.Label(root, text='Packet Analyzer', font='Helvetica 24 bold').pack()
tk.Label(root, text='Enter an IP Subdomain', font='Helvetica 16 bold').pack()

subdomain_entry = tk.Entry(root)
subdomain_entry.pack(ipady=5, ipadx=50, pady=10)

tk.Label(root, text='Type of Packet', font='Helvetica 16 bold').pack()

ttye_entry = tk.Entry(root)
ttye_entry.pack(ipady=5, ipadx=50, pady=10)

treev = ttk.Treeview(root, height=400)
treev.column('#0')

button_frame = tk.Frame(root)

tk.Button(button_frame, text='Start', command=start_button, width=15, font="Helvetica 16 bold").pack(
    side=tk.LEFT)
tk.Button(button_frame, text='Stop', command=start_button, width=15, font="Helvetica 16 bold").pack(
    side=tk.LEFT)

button_frame.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
