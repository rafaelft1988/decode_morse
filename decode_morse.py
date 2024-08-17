'''
O Código Morse é um sistema de representação de letras, algarismos e sinais de pontuação através
de um sinal codificado enviado de modo intermitente. Foi desenvolvido por Samuel Morse em 1837, 
criador do telégrafo elétrico, dispositivo que utiliza correntes elétricas para controlar eletroímãs 
que atuam na emissão e na recepção de sinais. 
O script tem a finalidade de decifrar uma mensagem em código morse e salvá-la em texto claro.
'''

import os
import sys
import datetime
import pandas as pd
from config import file_path, file_name, dict_morse

def decode_morse(message):
    '''
    Converte um texto em codigo Morse para texto claro.

    Parâmetros:
    message (str): Texto em codigo Morse.

    Retorna:
    str: Texto convertido para texto claro.
    '''   
    word_list = message.split('  ')
    clear_message = []
    for word in word_list:
        char_list = word.split(' ')
        clear_word = []
        for char in char_list:
            clear_word.append(str(dict_morse[char]))
        clear_message.append(''.join(clear_word))
    return ' '.join(clear_message)


def get_morse_from_clear_char(char):
    '''
    Relaciona o valor de um caractere em texto claro pelo respectivo valor do dicionario de código Morse disponibilizado.

    Parâmetros:
    letter (str): caractere em texto claro.

    Retorna:
    str: valor correspondente ao caractere em código Morse.
    ''' 
    if char.isdecimal():
        char = int(char)
    for key, value in dict_morse.items():
        if value == char:
            return key

def create_morse (clear_text):
    '''
    Converte um texto claro para código Morse.

    Parâmetros:
    clear_text (str): Texto claro (pode ser em maiusculo ou minusculo, mas deve ser sem caracteres especiais e acentuação).

    Retorna:
    str: Texto convertido para código Morse.
    '''   
    clear_text = clear_text.upper().split(' ')
    morse_text = []
    for word in clear_text:
        morse_word = []
        for char in word:
            morse_word.append(get_morse_from_clear_char(char))
        morse_text.append(' '.join(morse_word))
    return '  '.join(morse_text)

def save_clear_message_csv_hdr(clear_message):

    '''
    Cria arquivo CSV contendo a mensagem em texto claro e o timestamp do momento da gravação ou adiciona uma nova mensagem ao arquivo CSV.

    Parâmetros:
    clear_message (str): Mensagem em texto claro.

    Output:
    file: Arquivo CSV com nome configurado no config.py, contendo a mensagem em texto claro e timestamp da gravação.
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[clear_message, now]], columns=["mensagem", "datetime"])
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    hdr = not os.path.exists(file_path + file_name)
    df.to_csv(file_path + file_name, mode ="a", index = False, header=hdr)



if __name__ == "__main__":
    clear_message = decode_morse(sys.argv[1])
    save_clear_message_csv_hdr(clear_message)
