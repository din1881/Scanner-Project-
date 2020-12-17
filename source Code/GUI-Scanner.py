import PySimpleGUI as sg
import sys
import re
KEYWORDS = ['else', 'end', 'if', 'repeat', 'then', 'until', 'read', 'write']

OPERATORS = {
        '+'         : 'PLUS',
        '-'         : 'MINUS',
        '*'         : 'MULT',
        '/'         : 'DIV_FLOAT',
        ':'         : 'COLON',
        '='         : 'EQUALS',
        ':='        : 'ASSIGNMENT',
        '>'         : 'GREATER',
        '<'         : 'LESS',
        ';'         : 'SEMICOLON',
        '('         : 'OPEN_PARENTHESIS',
        ')'         : 'CLOSE_PARENTHESIS'
}



filename = sg.popup_get_file('Enter the file you wish to process')

tokens =[]

with open(filename) as f:
    for myfile in f:
        myfile=myfile.replace('\n','')
        myfile=myfile.replace('{','{ ')
        myfile=myfile.replace(';',' ;')
        newfile = myfile.split('{')

        for word in newfile[0].split(' '):
            print(word)
            if word in KEYWORDS:
                tokens.append(word + ", " + word.upper())
            elif word in OPERATORS.keys():
                tokens.append(word + ", " + OPERATORS[word])
            elif word.isalpha():
                tokens.append(word + ", " +"IDENTIFIER")
            elif word.isdigit():
                tokens.append(word + ", " +"NUMBER")

        if len(newfile) > 1:
            tokens.append("{" + newfile[1] + ", " + "COMMENT")



for i in tokens:
    print(i)

with open('outfile2.txt', 'w+') as outfile:
    for i in tokens:
        outfile.write(i+"\n")

