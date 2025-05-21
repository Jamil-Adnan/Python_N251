"""
To be a valid variable name in python the following conditions must meet
    1. variable name must start with a character (cap/small) or underscore character.
    2. Variable name can only contain alphanumeric characters (a-z, 0-9). No special characters are permitted
    (",!,Ä,Ö etc.)
    3. variable name can not start with a number
    4. variable names are case-sensitive, variable Adnan != variable adnan.
    5.  variable name cannot be a python keyword.

    a) hungry     b) 2AB    c) 312.2    d) MOBILE     e) “Ans”     f) $30
g) Yes/No     h) student-id         i) A+3     j) ‘X’        k) return

a) hungry is a valid name.
b) 2AB, invalid, starts with a number.
c) 312.3 invalid, start with a number.
d) MoBILE is valid.
d) "Ans", invalid, contains a special character, ".
e) $30 invalid, contains a special character, $.
f) Yes/No, invalid, contains a special character, /.
g) student-id, valid, contains only alphanumeric characters and underscores.
h) A+3, invalid, contains a special character, +.
i) 'x' invalid, contains a special character, '.
j) return invalid, it is a python keyword. used in methods/functions to return a value.
"""