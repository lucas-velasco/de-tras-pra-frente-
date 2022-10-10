#Faça uma função chamada inverte que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas,
e sem a pontuação.
Dica: remova a pontuação da frase, usando a função que você fez pro exercício anterior. 
Exemplo:
frase lida: “Nossa, como eu gosto de chocolate.”
frase alterada: “chocolate de gosto eu como nossa”


def retira_pontuacao(f):
    '''Função que substitui as pontuaçoes por espaço'''
    t= f.split(',')
    f= ' '.join(t)
    
    t= f.split('.')
    f= ' '.join(t)
    
    t= f.split(';')
    f= ' '.join(t)
    
    t= f.split('!')
    f=' '.join(t)
    
    t= f.split('-')
    f= ' '.join(t)
    
    t= f.split(':')
    f= ' '.join(t)
    
    t= f.split('?')
    f= ' '.join(t)
    
    return f

def inverte(f):
    '''A função inverte e diminui os caracteres maiúsculos da frase'''
    w= retira_pontuacao(f)
    w= w.split()
    w.reverse()
    w = ' '.join(w)
    
    return w.lower()
