
# Anticheat

A project with some tools to detect cheating in Github classroom assignments.
It's nothing fancy, it just pulls all the repositories and runs diff on a specific
file, reporting the lines of diff output (not even the lines different).

At a glance though, you can see whose code is actually identical, which is pretty nice.


## Contents

`clone_all.py` lets you pull all the repositories associated with an assignment.
`pairwise_compare.py` runs the comparison and reports the top 100 most similar submissions.
 - I must emphasize: Visually look at repositories that score low before grabbing the
   pitchforks. 

This is not a very good anticheat tool. Renaming all of your variables is sufficient to
defeat it.
