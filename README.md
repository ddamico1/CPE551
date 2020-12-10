# CPE551
Space for CPE551 Final Project

This calculator is designed to simulate many spins on perfect American Roulette tables.
The user can choose the number of sessions (samples) and the number of spins in each session.
They must also select a threshold value for the percentage of times any single number on the
roulette table occurs. When there is a session containing a number that occurred a higher
percentage of the time than the chosen threshold, the calculator will count it, and include it in
its final percentage of sessions in the entire set that had a number over this threshold value.
The purpose of this is to determine the likelihood that an observed abnormality in a set
of a certain size of roulette spins is due to random chance as opposed to an actual wheel bias. It
is meant to demonstrate how large a sample size must be in order to find a truly biased roulette
wheel with a certain level of confidence.
To accomplish this, I built a simulator for a perfect roulette table, where a variable
number of samples can be taken at this table, with a variable number of spins per sample. The
results from each sample are stored in a dictionary, and each dictionary is stored as part of an
array. This array is then modified to convert the results in each dictionary to percentages.
Another function then goes through each modified dictionary in the array and counts those that
have a pocket that occurred over the threshold value.
As an additional step, I used Tkinter to build a GUI, where the user can choose the
number of samples to take, and how many spins are in each sample. This was my first time
building a GUI, so seeing that there are a number of packages that can be used to build them
was interesting, and it was a good experience to learn how to utilize documentation to learn
how to utilize and implement an imported package.
