import tkinter as tk


class sudokuTk():

    def __init__(self):  #Initializiing the GUI, making a root and calling the necessary functions
        self.root = tk.Tk()
        self.targetFrame = 0
        self.shell = []
        self.mkGrid()
        self.mkLabels()
        self.bindFrames()
        self.rootKeyInput()
        self.root.mainloop()

    def mkLabels(self):  #Makes a label in every cell of the grid and also assigns it a variable that may be changed
        self.labels = [['i1', str(cell)]for cell in range(81)]
        for label in range(81):
            self.labels[label][0] = tk.Label(self.shell[label], textvariable = self.labels[label][1])
            self.labels[label][0].grid()



    def mkGrid(self): #Makes a sudoku grid of frames, later to have Labels stored in them and be binded to functions
        for varx in range(3):
            for vary in range(3):
                temp = tk.Frame(self.root, bd = 2, relief = "ridge", height = 300, width = 300, )
                temp.grid(row = varx, column = vary)
                for whole in range(9):
                    cell = tk.Frame(temp, bd=1, relief="ridge", height=30, width=30)
                    self.shell.append(cell)
                    cell.grid(row=int(whole / 3), column=whole % 3)
                    cell.grid_propagate(0)

    def bindFrames(self): #Binds all the frames with Enter and Leave functions to make them interactive
        for frame in range(len(self.shell)):
            self.shell[frame].bind('<Enter>', lambda event, frame = frame: self.focusCell(event, frame))

    def focusCell(self, event, frame):
        self.targetFrame = frame

    def rootKeyInput(self):
        self.root.bind('<Key>', lambda event: self.labelAFrame(event))

    def labelAFrame(self, event):
        numbers = [str(y) for y in range(1,10)]
        if event.keysym == 'BackSpace':
            self.labels[self.targetFrame][0].setvar(self.labels[self.targetFrame][1], ' ')
        elif event.char in numbers:
            self.labels[self.targetFrame][0].setvar(self.labels[self.targetFrame][1], event.char)


a = sudokuTk()