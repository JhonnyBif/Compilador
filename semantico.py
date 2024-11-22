import numpy as np

tabela_simbolos = []

def verificar_erro_semantico(nome_variavel, tipo_erro):
    simbolo = buscar_simbolo(nome_variavel)
    if simbolo and simbolo['categoria'] == "constante" and tipo_erro == "atribuição":
        print(f"Erro semântico: Tentativa de alteração da constante '{nome_variavel}'")
        return True
    return False

def adicionar_simbolo(nome, categoria, tipo, nivel):
    if buscar_simbolo(nome):
        print(f"Erro semântico: A '{categoria}' '{nome}' já foi declarada.")
        return False 
    else:
        simbolo = {
            'nome': nome,
            'categoria': categoria,
            'tipo': tipo,
            'nivel': nivel
        }
        tabela_simbolos.append(simbolo)
        return True
        
def buscar_simbolo(nome):
    for simbolo in tabela_simbolos:
        if simbolo['nome'] == nome:
            return simbolo
    return False
  
def buscar_simbolo_completo(sim):
  for simbolo in tabela_simbolos:
      if simbolo['nome'] == sim['nome'] and simbolo['nivel'] == sim['nivel'] and simbolo['categoria'] == sim['categoria']:
          return simbolo
  return False

def semantico(token_array, lexemas, token_lines):
  print(token_lines)
  lines = 1
  tokens = np.array(token_array)
  tokens = np.append(tokens, 51)
  indexWhile = 0
  while indexWhile != len(tokens):
    current_line = token_lines[indexWhile] if indexWhile <= len(token_lines) else lines
    if tokens[indexWhile] == 16:
        previousPreviousLexema = lexemas[indexWhile - 2]
        previousLexema = lexemas[indexWhile - 1]
        nome = lexemas[indexWhile]
        if previousLexema == "program":
            tipo = "program"
            if verificar_erro_semantico(nome, "atribuição"):
                print(f"Erro semântico na linha {current_line}: Tentativa de alteração da program {nome}")
                break
            if adicionar_simbolo(nome, "program", tipo, 0):
                print(f'program {nome} adicionada à tabela de símbolos')
                indexWhile += 1
                continue
            else:
                print(f"Erro: A program {nome} já foi declarada.")
        if previousLexema == "const":
            tipo = lexemas[indexWhile + 2]
            if verificar_erro_semantico(nome, "atribuição"):
                print(f"Erro semântico na linha {current_line}: Tentativa de alteração da constante {nome}")
                break
            if adicionar_simbolo(nome, "constante", tipo, 0):
                print(f'Constante {nome} adicionada à tabela de símbolos')
                indexWhile += 1
                continue
            else:
                print(f"Erro na Linha {current_line}: A constante {nome} já foi declarada.")
                break
                
        if previousLexema == "declaravariaveis":
            tipo = lexemas[indexWhile + 2]
            if verificar_erro_semantico(nome, "atribuição"):
                print(f"Erro semântico na linha {current_line}: Declaravaraiveis já declara {nome}")
                break
            if adicionar_simbolo(nome, "declaravariaveis", tipo, 0):
                print(f'declaravariaveis {nome} adicionada à tabela de símbolos')
                indexWhile += 1
                continue
            else:
                print(f"Erro na Linha {current_line}: A declaravariaveis {nome} já foi declarada.")
                break
                
        elif previousPreviousLexema == "begin":
          if previousLexema == "const":
            tipo = lexemas[indexWhile + 2]
            if verificar_erro_semantico(nome, "atribuição"):
                print(f"Erro semântico na linha {current_line}: Tentativa de alteração da constante {nome}")
                break
            if adicionar_simbolo(nome, "constante", tipo, 1):
                print(f'Constante {nome} adicionada à tabela de símbolos')
                indexWhile += 1
                continue
            else:
                print(f"Erro na Linha {current_line}: A constante {nome} já foi declarada.")
                break
                
        if previousLexema == "declaravariaveis":
            tipo = lexemas[indexWhile + 2]
            if verificar_erro_semantico(nome, "atribuição"):
                print(f"Erro semântico na linha {current_line}: Declaravaraiveis já declara {nome}")
                break
            if adicionar_simbolo(nome, "declaravariaveis", tipo, 1):
                print(f'declaravariaveis {nome} adicionada à tabela de símbolos')
                indexWhile += 1
                continue
            else:
                print(f"Erro na Linha {current_line}: A declaravariaveis {nome} já foi declarada.")
                break
              
                
    indexWhile += 1
print('EU TENNTEIIIIIII')
print('Considera aí Marlon')