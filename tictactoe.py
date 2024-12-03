import tkinter #graphical user interface lib

#to assign the buttons in the grid
def set_tile(row,column):
    global current_player #to use variable within multiple functions: alternating between players X and O

    #check to make sure game ends after wins/draws
    if (game_over):
        return

    #to avoid overriding player moves: Only when button is empty you can click it.
    if board[row][column]["text"] != "": #if the button text is not empty, exit function
        #spot already taken
        return
    
    #marks the board when clicked
    board[row][column]["text"] = current_player 

    #switch player
    if current_player == playerO:
        current_player = playerX
    else: 
        current_player = playerO
    
    label["text"] = current_player+"'s turn"

    #check or winning conditions
    check_winner()

#check winner 
def check_winner():
    global turns, game_over
    turns += 1

    #horizontal
    for row in range (3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
           and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" WINS!")

            #color change after wins
            for column in range(3):
                board[row][column].config(foreground=Red_color)
            game_over = True
            return

    #horizontal
    for column in range (3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
           and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" WINS!")

            #color change after wins
            for row in range(3):
                board[row][column].config(foreground=Red_color)
            game_over = True
            return
    
    #diagonal
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
       and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" WINS!")
        for i in range(3):
            board[i][i].config(foreground=Red_color)
        game_over = True
        return

    #anti-diagonal
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
    and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" WINS!")
        #config each button bc anti-diagonal (no loop combination)
        board[0][2].config(foreground=Red_color)
        board[1][1].config(foreground=Red_color)
        board[2][0].config(foreground=Red_color)
        game_over = True
        return
    
    #draw
    if(turns == 9):
        game_over = True
        label.config(text="-DRAW-", foreground="yellow")
        
#Restart: New game
def new_game():
    #reset variables to starting conditions
    global turns, game_over
    turns = 0
    game_over = False

    label["text"] = current_player+"'s turn"

    for row in range (3):
        for column in range(3):
            board[row][column].config(text="", foreground=Blue_color, background=Gray_color)


#game setup
playerX = 'X'
playerO = 'O'
current_player = playerX #default player X

# game board 3x3
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#Colors
Blue_color = "#4df0ea"
Red_color = "#e60b0b"
Gray_color = "#272545"
Light_grey_color = "#7a789e"

#turn variable
turns = 0 #increment by 1 every time user clicks on button
game_over = False #draw is 9 turns have passed w/o wins



#Window Setup
window = tkinter.Tk() #creates game window
window.title("Tic Tac Toe")
window.resizable(False,False) #user cant use mouse to expand size of window

#create frame to hold the components (buttons and text lables, etc)
frame = tkinter.Frame(window)#the frame is INSIDE the window

#components INSIDE the frame
label = tkinter.Label(frame, text=current_player+"'s turn", font=("Consolas", 20), 
                      background=Light_grey_color, foreground="black")

#structure lable component and place it in frame
label.grid(row=0, column=0, columnspan=3, sticky="we") #sticky is for the label to stretch from West to East (left to right)
#columnspan=3 to position Label in the centre

#creating the button-grid
for row in range (3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=Gray_color, foreground=Blue_color, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row,column)) #button click events = passing the row and col on the button clicked, calling function set_tile
        board[row][column].grid(row=row+1, column=column) #row+1 bc index0 is for LABEL, shift the rows by 1


#RESTART Button: new game starts
button = tkinter.Button(frame, text="RESTART", font=("Consolas", 20), background=Light_grey_color,
                        foreground="black", command=new_game) #new game starts

#RESTART button position in the grid:
button.grid(row=4, column=0,columnspan=3,sticky="we") #same as label {{to stretch vertically: "ns" north to south}}



frame.pack() #frame inside window

window.mainloop() #keeps window open until user closes it.


