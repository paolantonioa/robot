# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 
#from midiutil import MIDIFile
import PySimpleGUI as sg
#import wiringpi as wp
import time
from threading import Timer
import serial
import threading as th
#def update_file(step):
  #  print ("updated")
  #  global count 
  #  count = int(step)+1
ser = serial.Serial(port = '/dev/ttyS0',baudrate = 115200)
  
  #raspberry pi output code
#ser = serial.Serial(port='/dev/ttyS', baudrate = 115200)


def send_file(b,t,s,tempo,lp,loops_in =100):
   #loop iterations
    z=int(loops_in)
    #wp.wiringPiSetup()
    #serial = wp.serialOpen('/dev/ttyAMA0',9600)
    if lp ==1:
        while z > 0:
            
            for i in range (0,count-1): 
                
                ser.write(str.encode(str(b[i]) + str(t[i]) + str(s[i])))
                print(str(b[i]) + str(t[i]) + str(s[i]) )
                time.sleep((int(tempo)/60))
            z -= 1
        ser.write(str.encode(str(0) + str(0) + str(0)))   
        exit()       
    else:
        for i in range (0,count-1):   
            #wp.serialPuts(serial, str(b[i]) + str(t[i]) + str(s[i]))
            print((str(b[i]) + str(t[i]) + str(s[i])) )
            ser.write(str.encode(str(b[i]) + str(t[i]) + str(s[i])))
            time.sleep(60/int(tempo))
        exit()    
    
    

def submit_file(pr,ct,nm,temp,loop_setting,loops_in):
    bass =[0]*16
    tone =[0]*16
    slap = [0]*16
    for i in range (0,len(pressed)):
        if int(pr[i][0]) < ct:
            bass[int(pr[i][0])-1] = pr[i][1]
        elif int(pressed[i][0]) < (ct*2)-1 and int(pressed[i][0]) > ct-1:
            tone[int(pr[i][0])-17] = pr[i][1]
        elif int(pressed[i][0]) > ct*2-2 and int(pressed[i][0])<ct*3-2:
            slap[int(pr[i][0])-33] = pr[i][1]
    print(bass,tone,slap)
    send_file(bass,tone,slap,temp or 60,loop_setting, loops_in)
  
    
"""
#for midifile
def submit_file(pr,ct,nm,temp):
    print ("submitted")
    #degrees  = [60, 62, 64] # MIDI note number
    track    = 0
    channel  = 0
    time     = 0   # In beats
    duration = 1   # In beats
    tempo    = int(temp)  # In BPM
    volume   = 100 # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
    MyMIDI.addTempo(track,time, tempo)
    print(len(pressed))
    for i in range (0,len(pressed)-1):
        if int(pressed[i]) < ct:
            MyMIDI.addNote(track, channel, 60, int(pressed[i])-1, duration, volume)
            
        elif int(pressed[i]) < (ct*2)-1 and int(pressed[i]) > ct-1:
            MyMIDI.addNote(track, channel, 62, int(pressed[i])-ct, duration, volume)
            
        elif int(pressed[i]) > ct*2-2 and int(pressed[i])<ct*3-2:
            MyMIDI.addNote(track, channel, 64, int(pressed[i])-(ct*2), duration, volume)

        else:
            print (pressed[i])
            
    with open("/Users/anthonypaolantonio/Downloads/"+ nm +".midi", 'wb') as outf:
        MyMIDI.writeFile(outf)  
"""
def down_arrow(temp):
    #temp = int(temp)
    temp -=1
def select_all(x):
    x=int(x)
    if x ==1:
        if pressed.count(['1',3]) == 1:
            for i in range (1,count):
                pressed[pressed.index([str(i),3])] = [str(i),2]
                pressed_button(str(i),2)
                
        elif pressed.count(['1',2]) == 1:
            for i in range (1,count):
                pressed[pressed.index([str(i),2])] = [str(i),1]
                pressed_button(str(i),1)
        elif pressed.count(['1',1]) == 1:
            for i in range (1,count):
                unpressed_button(str(i))
                pressed.remove([str(i),1])
        else:
            for i in range (1,count):
                pressed.append([str(i),3])
                pressed_button(str(i),3)
    if x ==2:
        if pressed.count(['17',3]) == 1:
            for i in range (count,2*count-1):
                pressed[pressed.index([str(i),3])] = [str(i),2]
                pressed_button(str(i),2)
                
        elif pressed.count(['17',2]) == 1:
            for i in range (count,2*count-1):
                pressed[pressed.index([str(i),2])] = [str(i),1]
                pressed_button(str(i),1)
        elif pressed.count(['17',1]) == 1:
            for i in range (count,2*count-1):
                unpressed_button(str(i))
                pressed.remove([str(i),1])
        else:
            for i in range (count,2*count-1):
                pressed.append([str(i),3])
                pressed_button(str(i),3)
    
    if x ==3:
        if pressed.count(['34',3]) == 1:
            for i in range (2*count-1,3*count-2):
                pressed[pressed.index([str(i),3])] = [str(i),2]
                pressed_button(str(i),2)
                
        elif pressed.count(['34',2]) == 1:
            for i in range (2*count-1,3*count-2):
                pressed[pressed.index([str(i),2])] = [str(i),1]
                pressed_button(str(i),1)
        elif pressed.count(['34',1]) == 1:
            for i in range (2*count-1,3*count-2):
                unpressed_button(str(i))
                pressed.remove([str(i),1])
        else:
            for i in range (2*count-1,3*count-2):
                pressed.append([str(i),3])
                pressed_button(str(i),3)
#if button is pressed and is off
def pressed_button(x,dyn):
    if dyn ==3:
        window[x].update(button_color='red')
    if dyn ==2:
        window[x].update(button_color='yellow')
    if dyn ==1:
        window[x].update(button_color='green')
#if button is pressed and is on     
def unpressed_button(y):

    window[y].update(button_color='gray')

Top_Text = [sg.Text("Djembot"), sg.Text("File Name:"), sg.InputText("Default", key="file_name")]
sg.theme('DarkRed')

global count
count = 17

input_row1 = [
    [sg.Button(num,button_color = 'black on gray', key = str(num), enable_events=True) for num in range (1,count)]
    ]

input_row2 = [
    [sg.Button(num,button_color = 'black on gray',key = str(num+count-1), enable_events=True) for num in range (1,count)]
    ]
input_row3 = [
    [sg.Button(num,button_color = 'black on gray',key = str(num+(count+count)-2), enable_events=True) for num in range (1,count)]
    ]
submit_button = [sg.Button("Submit",button_color = 'blue', enable_events=True)]
input_rows= [[sg.Button("Bass",enable_events=True,key='Bass'),sg.Column(input_row1)],[sg.Button("Tone", enable_events=True),sg.Column(input_row2)],[sg.Button("Slap", enable_events=True),sg.Column(input_row3)]]

right_column_group = [input_rows,submit_button]
Inputs = [[sg.Text("Tempo:"), sg.Spin(list(range(1,121)),initial_value=60,key="tempo_input", size=5)],[sg.Button(button_text="Loop",button_color='black on gray',enable_events=True)]]
Loop_in = [[sg.Text("Loops: ")],[sg.InputText(key='loops_in',enable_events=True)]]
layout = [Top_Text,Inputs,Loop_in, right_column_group]

# Create the window
window = sg.Window("Djembot",  layout, resizable=True)
pressed = [];
loop = 0;

# Create an event loop
while True:
    event, values = window.read()
    
    if event == "Loop" and loop ==0:
        loop = 1
        pressed_button(event,2)
    elif event == 'Loop' and loop ==1:
        loop = 0
        unpressed_button(event)
    if event in [str(i) for i in range(1, count*3+1)]:      
        if pressed.count([str(event),3])==1:
            print('2')
            pressed[pressed.index([str(event),3])] = [event,2]
            pressed_button(event,2)

        elif pressed.count([str(event),2])==1:
            print('1')
            pressed[pressed.index([str(event),2])] = [event,1]
            pressed_button(event,1)

        elif pressed.count([str(event),1])==1: 
            unpressed_button(event)
            pressed.remove([str(event),1])
            print(pressed)
        else:
            if len(pressed) > 0:
                if int(event) < count and pressed.count([str(int(event)+count-1),3])==0 and pressed.count([str(int(event)+(2*count-2)),3])==0 and pressed.count([str(int(event)+count-1),2])==0 and pressed.count([str(int(event)+(2*count-2)),2])==0 and pressed.count([str(int(event)+count-1),1])==0 and pressed.count([str(int(event)+(2*count-2)),1])==0:
                    pressed_button(event,3)
                    pressed.append([event,3])
                    print (pressed);
                elif int(event) < (count*2)-1 and int(event) > count-1 and pressed.count([str(int(event)-count+1),3])==0 and pressed.count([str(int(event)+(count-1)),3])==0 and pressed.count([str(int(event)-count+1),2])==0 and pressed.count([str(int(event)+(count-1)),2])==0 and pressed.count([str(int(event)-count+1),1])==0 and pressed.count([str(int(event)+(count-1)),1])==0:
                    pressed_button(event,3)
                    pressed.append([event,3])
                    print (pressed);
                elif int(event) > count*2-2 and int(event)<count*3-2 and pressed.count([str(int(event)-2*count+2),3])==0 and pressed.count([str(int(event)-(count)+1),3])==0 and pressed.count([str(int(event)-2*count+2),2])==0 and pressed.count([str(int(event)-(count)+1),2])==0 and pressed.count([str(int(event)-2*count+2),1])==0 and pressed.count([str(int(event)-(count)+1),1])==0:
                    pressed_button(event,3)
                    pressed.append([event,3])
                    print (pressed);
            elif len(pressed) == 0:
                pressed_button(event,3)
                pressed.append([event,3])
                print (pressed);
    if event == "Submit":
        name = str(values['file_name'])
        submit_file(pressed,count,name,values['tempo_input'],loop, values['loops_in'] or 4)
    if event == "Stop":
        ser.write(str.encode(str(0) + str(0) + str(0)))
        break
    if event == "Bass":
        select_all(1)
    if event == "Tone":
        select_all(2)
    if event == "Slap":
        select_all(3)
   # if event == "Update":
    #    update_file(values['step_input'])


    if event == sg.WIN_CLOSED:
        break

window.close() 
ser.write(str.encode(str(0) + str(0) + str(0)))
