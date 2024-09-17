import numpy as np

with open('exemplo1.txt', 'r') as file:
    palavra = file.read()

token_map = {
    'program': 9,
    'write': 0,
    'while': 1,
    'until': 2,
    'to': 3,
    'then': 4,
    'repeat': 6,
    'real': 7,
    'read': 8,
    'procedure': 10,
    'or': 11,
    'of': 12,
    'integer': 14,
    'if': 15,
    'for': 18,
    'end': 19,
    'else': 20,
    'do': 21,
    'declaravariaveis': 22,
    'const': 23,
    'chamaprocedure': 25,
    'begin': 26,
    'array': 27,
    'and': 28,
    '>=': 29,
    '>': 30,
    '=': 31,
    '<>': 32,
    '<=': 33,
    '<': 34,
    '+': 35,
    ']': 40,
    '[': 41,
    ';': 42,
    ':': 43,
    '/': 44,
    '..': 45,
    '.': 46,
    ',': 47,
    '*': 48,
    '-': 52
}

def error(type, line):
    if type == 'string' :
        print('Error String Too Long, Length > 5 - Linha:', line)
    elif type == 'literal':
        print('Error Literal Too Long, Length > 5 - Line:', line)
    elif type == 'char':
        print('Error Char Too Long, Length > 1, - Linha:', line)
    elif type == 'realBefore':
        print('Error real number > 5 digits before the divisor - Line:', line)
    elif type == 'realAfter':
        print('Error real number > 2 digits after the divisor - Line:', line)
    elif type == 'number':
        print('Error number > 5 digits - Line', line)
    elif type == 'identificadorLength':
        print('Error identificador Too Long, Length > 5. - Line', line)
    elif type == 'identificadorStartDigit':
        print('Error identificador Start with number. - Line', line)
    

def process_lexema(lexema, tokens, lexemas, espacos):
    # Verifica se o lexema está no mapeamento e adiciona o token correspondente
    if lexema in token_map:
        tokens.append(token_map[lexema])
        lexemas.append(lexema)
    else:
        # Caso não esteja no mapeamento, verifica se o lexema é relevante
        #QUER DIZER QUE O LEXEMA É UMA PALAVRA RESERVADA
        if lexema not in espacos and len(lexema) > 0:
            if len(lexema) >5:
                error('identificadorLength', lines)
            if lexema[0].isdigit() :
                error('identificadorStartDigit', lines)
            tokens.append(16)
            lexemas.append(lexema)

    # Reseta o lexema após o processamento
    return ''

lexema = ''
tokens = []
lexemas = []
parenteses= False
conchetes= False
string= False
char= False
literal= False
literalFirst= False
lines = 0
number = False

espacos = [ ' ', '\t', '\n']
print(palavra)

for i in range(len(palavra)):
    if palavra[i].__contains__('\n') :
        lines += 1
    if palavra[i] not in espacos and i != len(palavra) -1 :
        lexema = lexema + palavra[i]
        if palavra[i] == '"':
            if(len(lexema) >5) :
                error('string', lines)
                break
            if(string) :
                tokens.append(5)
                lexemas.append(lexema)
                string= False
                lexema = ''
            else :
                string= True
                char= False
                literal= False
                lexema = palavra[i]
                
        elif palavra[i] == "'":
            if(len(lexema) >2) :
                error('char', lines)
                break
            elif(char) :
                tokens.append(24)
                lexemas.append(lexema.split("'")[0])
                char= False
                lexema = ''
            else :
                string= False
                char= True
                literal= False
                lexema = ''
                
        elif palavra[i] == "@":
            if(len(lexema) >5) :
                error('literal', lines)
                break
            if(literalFirst) :
                tokens.append(13)
                lexemas.append(lexema)
                lexema = ''
                literalFirst = False
            else :
                string= False
                char=False
                literalFirst = True
                lexema = palavra[i]
                
        elif palavra[i] == "(" :
            tokens.append(50)
            lexemas.append(lexema)
            parenteses= True
            lexema = ''
        elif palavra[i] == ")" :
            tokens.append(49)
            lexemas.append(lexema)
            parenteses= False
            lexema = ''
        elif palavra[i] == "[" :
            tokens.append(40)
            lexemas.append(lexema)
            lexema = ''
            conchetes= True
        elif palavra[i] == "]" :
            tokens.append(27)
            lexemas.append(lexema.split(']')[0])
            tokens.append(41)
            lexemas.append(']')
            conchetes= False
            lexema = ''
        elif palavra[i].isdigit():
            if number:
                if palavra[i+1].isdigit() or (palavra[i+1] == '.' and '.' not in lexema):
                    continue
                else:
                    if '.' in lexema and '..' not in lexema:
                        real = lexema.split('.')
                        if len(real[0]) > 5:
                            error('realBefore', lines)
                            break
                        elif len(real[1]) > 2:
                            error('realAfter', lines)
                            break
                        else:
                            tokens.append(36)
                            lexemas.append(lexema)
                            lexema = ''
                    elif  '..' not in lexema:
                        if len(lexema) > 5:
                            error('number',lines )
                            break
                        else:
                            tokens.append(37)
                            lexemas.append(lexema)
                            lexema = ''
                            number = False
            else:
                number = True
    else:
        if not palavra[i].__contains__('\n') :
            lexema = lexema+palavra[i]
        lexema = process_lexema(lexema, tokens, lexemas, espacos)

       

#salvar do lexico para entregar para o sintático
tokens = np.array(tokens) #converte lista do python para numpy array
print(tokens)
for i in range(len(tokens)) :
    print('Token: '+str(tokens[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha:'+str(lines) )
    
    
#-----------------------CODIGO ANTIGO--------------------------------

 # if lexema == 'program':
        #     tokens.append(9) 
        #     lexemas.append(lexema)
        # elif lexema == 'write':
        #     tokens.append(0)
        #     lexemas.append(lexema)
        # elif lexema == 'while':
        #     tokens.append(1)
        #     lexemas.append(lexema)
        # elif lexema == 'until':
        #     tokens.append(2)
        #     lexemas.append(lexema)
        # elif lexema == 'to':
        #     tokens.append(3)
        #     lexemas.append(lexema)
        # elif lexema == 'then':
        #     tokens.append(4)
        #     lexemas.append(lexema)
        # elif lexema == 'repeat':
        #     tokens.append(6)
        #     lexemas.append(lexema)
        # elif lexema == 'real':
        #     tokens.append(7)
        #     lexemas.append(lexema)
        # elif lexema == 'read':
        #     tokens.append(8)
        #     lexemas.append(lexema)
        # elif lexema == 'procedure':
        #     tokens.append(10)
        #     lexemas.append(lexema)
        # elif lexema == 'or':
        #     tokens.append(11)
        #     lexemas.append(lexema)
        # elif lexema == 'of':
        #     tokens.append(12)
        #     lexemas.append(lexema)
        # elif lexema == 'integer':
        #     tokens.append(14)
        #     lexemas.append(lexema)
        # elif lexema == 'if':
        #     tokens.append(15)
        #     lexemas.append(lexema)
        # elif lexema == 'for':
        #     tokens.append(18)
        #     lexemas.append(lexema)
        # elif lexema == 'end':
        #     tokens.append(19)
        #     lexemas.append(lexema)
        # elif lexema == 'else':
        #     tokens.append(20)
        #     lexemas.append(lexema)
        # elif lexema == 'do':
        #     tokens.append(21)
        #     lexemas.append(lexema)
        # elif lexema == 'declaravariaveis':
        #     tokens.append(22)
        #     lexemas.append(lexema)
        # elif lexema == 'const':
        #     tokens.append(23)
        #     lexemas.append(lexema)
        # elif lexema == 'chamaprocedure':
        #     tokens.append(25)
        #     lexemas.append(lexema)
        # elif lexema == 'begin':
        #     tokens.append(26)
        #     lexemas.append(lexema)
        # elif lexema == 'array':
        #     tokens.append(27)
        #     lexemas.append(lexema)
        # elif lexema == 'and':
        #     tokens.append(28)
        #     lexemas.append(lexema)
        # elif lexema == '>=':
        #     tokens.append(29)
        #     lexemas.append(lexema)
        # elif lexema == '>':
        #     tokens.append(30)
        #     lexemas.append(lexema)
        # elif lexema == '=':
        #     tokens.append(31)
        #     lexemas.append(lexema)
        # elif lexema == '<>':
        #     tokens.append(32)
        #     lexemas.append(lexema)
        # elif lexema == '<=':
        #     tokens.append(33)
        #     lexemas.append(lexema)
        # elif lexema == '<':
        #     tokens.append(34)
        #     lexemas.append(lexema)
        # elif lexema == '+':
        #     tokens.append(35)
        #     lexemas.append(lexema)
        # elif lexema == ']':
        #     tokens.append(40)
        #     lexemas.append(lexema)
        # elif lexema == '[':
        #     tokens.append(41)
        #     lexemas.append(lexema)
        #     lexema = ''
        # elif lexema == ';':
        #     tokens.append(42)
        #     lexemas.append(lexema)
        # elif lexema == ':':
        #     tokens.append(43)
        #     lexemas.append(lexema)
        # elif lexema == '/':
        #     tokens.append(44)
        #     lexemas.append(lexema)
        # elif lexema == '..':
        #     tokens.append(45)
        #     lexemas.append(lexema)
        # elif lexema == '.':
        #     tokens.append(46)
        #     lexemas.append(lexema)
        # elif lexema == ',':
        #     tokens.append(47)
        #     lexemas.append(lexema)
        # elif lexema == '*':
        #     tokens.append(48)
        #     lexemas.append(lexema)
        # else:
        #     if(lexema not in espacos and len(lexema)> 0) :
        #         tokens.append(16)
        #         lexemas.append(lexema)
        # lexema = ''
        # print(lexema)