#GUI file
from __future__ import division
import Tkinter
import dataManip



def finalResult():
    
    resultBox.delete(0,16)

    x = NumOfSamples_var.get()
    y = SpinsPerSample_var.get()
    
    result_var = dataManip.countAboveThresh(Threshold_var.get(), x, y)
    float(result_var)
    result_var = (result_var / x) * 100
    result_var = str(result_var)
    result_var = result_var + "%"
    resultBox.insert(0,result_var)


def test():
    Threshold_var = ThresholdBox.get()
    print Threshold_var

def run():
    top.mainloop()


top = Tkinter.Tk()
top.geometry("650x400")

finalResult_var = Tkinter.StringVar()


canv = Tkinter.Canvas(top, bd = 2)

NumOfSamples_var = Tkinter.IntVar()
NumOfSamplesBox = Tkinter.Entry(top, width=10, font = ("Arial",12), bd=2, textvariable=NumOfSamples_var)
NumOfSamplesBox.place(x=180, y=32)
NumOfSamplesLabel = Tkinter.Label(top, text="Number of Samples:", font=("Arial Bold",12))
NumOfSamplesLabel.place(x=10,y=30)

SpinsPerSample_var = Tkinter.IntVar()
SpinsPerSampleBox = Tkinter.Entry(top, width=10, font = ("Arial",12), bd=2, textvariable=SpinsPerSample_var)
SpinsPerSampleBox.place(x=180, y=82)
SpinsPerSampleLabel = Tkinter.Label(top, text="Spins per Sample:", font=("Arial Bold",12))
SpinsPerSampleLabel.place(x=26,y=80)

Threshold_var = Tkinter.DoubleVar()
ThresholdBox = Tkinter.Entry(top, width=10, font = ("Arial",12), bd=2, textvariable = Threshold_var)
ThresholdBox.place(x=180, y=132)
ThresholdLabel = Tkinter.Label(top, text="Threshold (%):", font=("Arial Bold",12))
ThresholdLabel.place(x=53,y=130)
resultBox = Tkinter.Entry(top, text = finalResult_var, width = 10, bd = 4, font = ("Arial",16), bg="light cyan", justify = Tkinter.CENTER)
resultBox.place(x=120, y=320)
resultLabel = Tkinter.Label(top, font = ("Arial",12), text="Probability that a pocket occuring above the")
resultLabel2= Tkinter.Label(top, font = ("Arial",12), text="threshold is due to random chance:")
resultLabel.place(x=35, y=250)
resultLabel2.place(x=58,y=280)

bt = Tkinter.Button(top, command = finalResult, text="Calculate Results", font = ("Arial Bold",15), bg="light cyan", bd=4)
bt.place(x=90, y=190)

InfoBox_var = "Info:\n\nProbability of any given pocket occuring on a perfect table: 2.63% \n \nThe house edge at this probability is 5.26% \n\nFor the player to gain an edge over the house, the Threshold must be at least 2.857% \n\nThe final result shows the probability of a perfect table showing false bias at or above the threshold percentage."
InfoBox = Tkinter.Message(top, width = 250, text = InfoBox_var, justify = Tkinter.CENTER, relief=Tkinter.RIDGE, bd=5)
InfoBox.place(x=365, y=30)


if __name__ == "__main__":
    run()




