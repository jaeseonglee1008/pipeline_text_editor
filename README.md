# pipeline_text_editor

written in python by Jason Lee

## How to

A list of command to manipulate is provided in the context

## Main features

```
(1)cmd_h(or l): move cursor one character to the left 
(2)cmd_I(or r): move cursor one character to the right
(3)cmd_j(or u): move cursor vertically one line up
(4)cmd_k(or d): move cursor vertically one line down
(5)cmd_X(or del): delete the character to the left of the cursor
(6)cmd_D(or del_right): remove on current line from cursor to the end
(7)cmd_dd(or del_line): delete current line and move cursor to the beginning of
next line (if next line exists, else do nothing)
(8)cmd_ddp(or trans):transpose two adjacent lines
(9)cmd_n(ex: cmd_n("apple")): search for next occurrence of a string (assume that string
to be searched is fully in one line.
(10)cmd_wq(or save): write your representation as text file and save it
(11)exit(or exit()): Terminate program
```

