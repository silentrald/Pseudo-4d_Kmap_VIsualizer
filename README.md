# Pseudo-4d_Kmap_VIsualizer
This is a representation of a karnaugh map in 4 dimensions and will help find the minimized expression for a 8 input variable.


## Requirements
>Python

## How to Use
#### minterm_generator.py
This will generate all the minterms given certain conditions. Only works for conditions in a product of sum(POS) expression. The format of the condition is as follows:
> __1__ - The variable must be true in all cases to produce an output of 1.
__0__ - The variable must be false in all cases to produce an output of 1.
__x__ - The variable does not matter to produce an output of 1.

**EG.**
4 input variable - _10x1_
**bit 1 & 4** should always be true,
**bit 2** should always be false,
and **bit 3** can be a 0 or 1 since the variable does not matter.

#### pseudo-4d_k-map.py
This will produce a 4d representation of the kmap. **Note: This will only work for 8 input variable.** The 1st input will get the file name of the minterm file and the 2nd input will be the don't care conditions. This will then automatically print the full truth table and the 4d Kmap. If you want to put this into a file just simply do a file redirection in your cmd/terminal.
```
python pseudo-4d_k-map.py > [name of file].txt
```

#### Reminders
This code can be manipulated for your needs, only thing you need is python understanding and a little bit of imagination.