from tkinter import *
from random import randint

root = Tk()

class RockPaperScissor:
    def __init__(self, root):
        self.root = root
        self.rockImage = PhotoImage(file="assets/rock.png")
        self.paperImage = PhotoImage(file="assets/paper.png")
        self.scissorImage = PhotoImage(file="assets/scissor.png")
        self.defaultImage = PhotoImage(file="assets/default.png")

        self.roboScore = 0
        self.userScore = 0
        self.round = 1
        self.user = ""

        self.root.geometry("600x550")
        self.root.title("Rock Paper Scissor Game")
        self.root.resizable(False, False)
        self.root.config(bg="#96ecfe")

        Label(self.root, text="Rock Paper Scissor", font="arial 18 bold", bg="#000", fg="white", pady=15, justify=CENTER).pack(fill=X)

        self.mainFrame = Frame(self.root, width=600, height=500, bg="#96ecfe", padx=10, pady=10)
        self.mainFrame.place(x=0, y=67)

        self.inputFrame = Frame(self.mainFrame, bg="#79e7f6", width=400, height=200, padx=10, pady=25)
        self.inputFrame.place(x=100, y=120)

        Label(self.inputFrame, text="Enter Your Name", font="arial 14", bg="#79e7f6", padx=5, pady=5).place(x=100, y=0)

        Label(self.inputFrame, text="Enter Name : ", bg="#79e7f6", font="arial 12", padx=3, pady=3).place(x=10, y=50)

        usrName = StringVar()
        usrEntry = Entry(self.inputFrame, textvariable=usrName)
        usrEntry.place(x=150, y=52)

        Button(self.inputFrame, text="Start", bg="green", width=10, padx=3, pady=2, fg="white", command=lambda:self.start(usrName)).place(x=25, y=120)

    def start(self, usrName):

        #destroy frame
        self.inputFrame.destroy()

        self.user = usrName.get()
        if self.user == "":
            self.user = "User"

        self.newMainFrame = Frame(self.root, width=600, height=500, bg="#96ecfe", padx=10, pady=10)
        self.newMainFrame.place(x=0, y=67)

        self.scoreFrame = Frame(self.newMainFrame, width=550, height=60, padx=10, pady=10, bg="#96ecfe")
        self.scoreFrame.place(x=12, y=0)

        # roboScore
        self.roboScoreLabel = Label(self.scoreFrame, text="Robot : 0", font="arial 12 bold", bg="#96ecfe", padx=5, pady=5)
        self.roboScoreLabel.place(x=5, y=0)

        # userScore
        self.userScoreLabel = Label(self.scoreFrame, text=f"{self.user} : 0", font="arial 12 bold", bg="#96ecfe", padx=5, pady=5)
        self.userScoreLabel.place(x=300, y=0)

        #gameFrame
        self.gameFrame = Frame(self.newMainFrame, width=550, height=400, padx=10, pady=10, bg="#96ecfe")
        self.gameFrame.place(x=12, y=62)

        self.roboChoiceImage = Label(self.gameFrame, image=self.defaultImage)
        self.roboChoiceImage.place(x=0, y=0)

        self.userChoiceImage = Label(self.gameFrame, image=self.defaultImage)
        self.userChoiceImage.place(x=300, y=0)

        self.resultLabel = Label(self.newMainFrame, text=f"Round {self.round}", font="arial 12 bold", padx=5, pady=5, bg="#96ecfe", width=40)
        self.resultLabel.place(x=60, y=320)

        self.choiceFrame = Frame(self.gameFrame, bg="#79e7f6", width=400, height=75, padx=10, pady=10)
        self.choiceFrame.place(x=60, y=300)

        Button(self.choiceFrame, text="Rock", width=5, bg="#2c74eb", fg="white", command=lambda:self.selection("rock")).place(x=30, y=10)
        Button(self.choiceFrame, text="Paper", width=5, bg="#2c74eb", fg="white", command=lambda:self.selection("paper")).place(x=110, y=10)
        Button(self.choiceFrame, text="Scissor", width=5, bg="#2c74eb", fg="white", command=lambda:self.selection("scissor")).place(x=190, y=10)
        Button(self.choiceFrame, text="Exit", width=5, bg="red", fg="white", command=quit).place(x=270, y=10)

    def selection(self, usrChoice):

        self.choiceFrame.destroy()

        self.choiceFrame = Frame(self.gameFrame, bg="#79e7f6", width=400, height=75, padx=10, pady=10)
        self.choiceFrame.place(x=60, y=300)

        Button(self.choiceFrame, text="Next Round", width=10, bg="#2c74eb", fg="white", command=self.nextRound).place(x=50, y=10)
        Button(self.choiceFrame, text="Exit", width=10, bg="red", fg="white", command=quit).place(x=200, y=10)

        # robo selection of choice and image
        options = ["rock", "paper", "scissor"]
        roboChoice = options[randint(0, 2)]

        if roboChoice == "rock":
            choiceImageRobo = self.rockImage
        elif roboChoice == "paper":
            choiceImageRobo = self.paperImage
        else:
            choiceImageRobo = self.scissorImage

        self.roboChoiceImage.config(image=choiceImageRobo)

        # user selection of choice and image
        if usrChoice == "rock":
            choiceImageUsr = self.rockImage
        elif usrChoice == "paper":
            choiceImageUsr = self.paperImage
        else:
            choiceImageUsr = self.scissorImage

        self.userChoiceImage.config(image=choiceImageUsr)

        self.result(roboChoice, usrChoice)

    def result(self, rChoice, uChoice):
        result = ""

        if rChoice == "rock" and uChoice == "rock":
            result = "Round Draw"
        elif rChoice == "rock" and uChoice == "paper":
            result = f"{self.user} won the round"
            self.userScore += 10
        elif rChoice == "rock" and uChoice == "scissor":
            result = "Robot win the round"
            self.roboScore += 10

        elif rChoice == "paper" and uChoice == "rock":
            result = "Robot win the round"
            self.roboScore += 10
        elif rChoice == "paper" and uChoice == "paper":
            result = "Round Draw"
        elif rChoice == "paper" and uChoice == "scissor":
            result = f"{self.user} won the round"
            self.userScore += 10

        elif rChoice == "scissor" and uChoice == "rock":
            result = f"{self.user} won the round"
            self.userScore += 10
        elif rChoice == "scissor" and uChoice == "paper":
            result = "Robot win the round"
            self.roboScore += 10
        elif rChoice == "scissor" and uChoice == "scissor":
            result = "Round Draw"
            
        self.roboScoreLabel.config(text=f"Robot : {self.roboScore}")
        self.userScoreLabel.config(text=f"{self.user} : {self.userScore}")
        self.resultLabel.config(text=result)

    def nextRound(self):

        self.choiceFrame.destroy()

        self.round += 1

        self.roboChoiceImage.config(image=self.defaultImage)
        self.userChoiceImage.config(image=self.defaultImage)
        self.resultLabel.config(text=f"Round {self.round}")

        self.choiceFrame = Frame(self.gameFrame, bg="#79e7f6", width=400, height=75, padx=10, pady=10)
        self.choiceFrame.place(x=60, y=300)

        Button(self.choiceFrame, text="Rock", width=5, bg="#2c74eb", fg="white", command=lambda:self.selection("rock")).place(x=30, y=10)
        Button(self.choiceFrame, text="Paper", width=5, bg="#2c74eb", fg="white", command=lambda:self.selection("paper")).place(x=110, y=10)
        Button(self.choiceFrame, text="Scissor", width=5, bg="#2c74eb", fg="white", command=lambda:self.selection("scissor")).place(x=190, y=10)
        Button(self.choiceFrame, text="Exit", width=5, bg="red", fg="white", command=quit).place(x=270, y=10)

start = RockPaperScissor(root)
root.mainloop()