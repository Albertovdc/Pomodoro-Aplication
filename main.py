import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global reps
  reps =0
  window.after_cancel(timer)
  h1_text.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  work_secs = WORK_MIN * 60
  short_break = SHORT_BREAK_MIN *60
  long_break = LONG_BREAK_MIN *60
  if reps == 7:
    count_down(long_break)
    h1_text.config(text="Break", fg=RED)
    checkmark.config()
    
  elif reps == 0 or reps  % 2 == 0:
    count_down(work_secs)
    h1_text.config(text="Work", fg=GREEN)

  else:
    count_down(short_break)
    h1_text.config(text="Break", fg=PINK)

  reps +=1
  #count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor(count/60)
  count_sec = count % 60

  if count_sec < 10:
    count_sec = f"0{count_sec}"

  if count_min < 10:
    count_min = f"0{count_min}"
  
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count-1)
  else:
    start_timer()
    marks = ""
    for _ in range(math.floor(reps/2)):
      marks += "✔"
    checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# Button Start
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Butoon Reset
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Text 1
h1_text = Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 40, "bold"))
h1_text.grid(row=0, column=1)

# Text 2
checkmark = Label(fg=GREEN, background=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(row=3, column=1)


window.mainloop()
