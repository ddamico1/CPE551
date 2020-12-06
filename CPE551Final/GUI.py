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


InfoBox_var = "This calculator is designed to simulate many spins on perfect American Roulette tables. The user can choose the number of sessions (samples) and the number of spins in each session. They must also select a threshold value for the percentage of times any single number on the roulette table occurs. When there is a session containing a number that occured a higher percentage of the time than the chosen threshold, the calculator will count it, and include it in its final percentage of sessions in the entire set that had a number over this threshold value.\n The purpose of this is to determine the likelyhood that an observed abnormality in a set of a certain size of roulette spins is due to random chance as opposed to an actual wheel bias. It is meant to demonstrate how large a sample size must be in order to find a truly biased roulette wheel with a certain level of confidence."
InfoBox = Tkinter.Message(top, width = 250, text = InfoBox_var, justify = Tkinter.CENTER, relief=Tkinter.RIDGE, bd=5)
InfoBox.place(x=365, y=30)


top.mainloop()




