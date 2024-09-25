# t2b
## A text to binary (ascii) converter written in python
Designed as a simple command line tool

### Requirements
- Have a local installation of python 3+

### Usage
- Navigate to the root directory and run
```bash
    $ python t2b.py <text0> <text1> ... <textn>
```
- Press -h for usage

#### TODO:
[ ] Add -s flag that can help split a string by whitespace
    e.g. "I am a book" -> ["I", "am", "a", "book"]
[ ] Add -p flag to set leading zero padding (min 8)
    e.g. p=8 -> 00010010, p=10 -> 0011010010

<!-- #### Known bugs: -->
<!-- #### Feature requests: -->
