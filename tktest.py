import tkinter as tk
import sudokuM


class sudokuTk():

    def __init__(self):  #Initializiing the GUI, making a root and calling the necessary functions
        self.sM = sudokuM.sudM()
        self.root = tk.Tk()
        self.targetCell = 0  #A variable that will always change to the coordination that the mouse hovers over
        self.shell = []  #The grid-system that sudoku is built upon
        self.labels = []  #The labels that the grid-system will contain
        self.mkGrid()
        self.mkLabels()
        self.bindFrames()
        self.rootKeyInput()
        self.informBar()
        self.root.mainloop()

    def informBar(self):  #Creates a frame that acts like an information section that lets you know what you've done bad
        self.informationBar = tk.Frame(self.root, height = 15, width = 280, pady = 3,
                                       background = '#aaa')
        self.informationBar.grid(column = 0, row = 1)

    def mkLabels(self):  #Makes a label in every cell of the grid and also assigns it a variable that may be changed
        self.labels = [['', str(cell)]for cell in range(81)]
        for label in range(81):
            self.labels[label][0] = tk.Label(self.shell[label], textvariable = self.labels[label][1])
            self.labels[label][0].place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

    def mkGrid(self):  #Makes a sudoku grid of frames, later to have Labels stored in them and be binded to functions
        self.gridFrame = tk.Frame(self.root)
        self.gridFrame.grid()
        for varx in range(3):
            for vary in range(3):
                temp = tk.Frame(self.gridFrame, bd = 2, relief = "ridge", height = 300, width = 300, )
                temp.grid(row = varx, column = vary)
                for whole in range(9):
                    cell = tk.Frame(temp, bd=1, relief="ridge", height=30, width=30)
                    self.shell.append(cell)
                    cell.grid(row=int(whole / 3), column=whole % 3)
                    cell.grid_propagate(0)

    def bindFrames(self):  #Binds all the frames with Enter, and if you enter they redirect them to focusCell
        for frame in range(len(self.shell)):
            self.shell[frame].bind('<Enter>', lambda event, frame = frame: self.focusCell(event, frame))

    def focusCell(self, event, frame):  #Makes a global variable telling which square you're hovering over.
        self.targetCell = frame

    def rootKeyInput(self):  #Binds key input to root, used to assign squares text
        self.root.bind('<Key>', lambda event: self.contrInput(event))

    def contrInput(self, event):  #Checks if the input is legal sudoku-vise
        print(self.sM.checkS(self.targetCell), self.targetCell, event.char)

        if event.keysym == 'BackSpace':
            self.labelAFrame(event)
        elif int(event.char) in self.sM.checkS(self.targetCell):
            self.labelAFrame(event)

    def labelAFrame(self, event):  #If the keyboard input is appropriate, put it on the square that the mouse is over
        numbers = [str(y) for y in range(1, 10)]
        if event.keysym == 'BackSpace':
            self.labels[self.targetCell][0].setvar(self.labels[self.targetCell][1], ' ')
            self.sM.setS(self.targetCell, 0)
        elif event.char in numbers:
            self.labels[self.targetCell][0].setvar(self.labels[self.targetCell][1], event.char)
            self.sM.setS(self.targetCell, event.char)


a = sudokuTk()
