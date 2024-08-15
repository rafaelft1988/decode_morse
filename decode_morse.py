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
from config import file_path, dict_morse, test_morse

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
        letter_list = word.split(' ')
        clear_word = []
        for letter in letter_list:
            clear_word.append(str(dict_morse[letter]))
        clear_message.append(''.join(clear_word))
    return ' '.join(clear_message)


def get_morse_from_clear_letter(char):
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
        for letter in word:
            morse_word.append(get_morse_from_clear_letter(letter))
        morse_text.append(' '.join(morse_word))
    return '  '.join(morse_text)

def save_clear_msg_csv_hdr(msg_claro):
    '''
    input : mensagem em texto claro
    output : palavra escrito em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode ="a", index = False, header=hdr)



if __name__ == "__main__":
    #msg_claro = decode_morse(sys.argv[1])
    #save_clear_msg_csv_hdr(msg_claro)
    morse = create_morse('era uma vez um menino que sonhava em construir um barco ele tinha 10 anos e acordo todos os dias as 7 da manha com sua imaginacao ele desenhava o barco em um caderno o menino queria navegar pelo lago que ficava perto de sua casa um dia ele encontrou 5 moedas no quintal e decidiu que usaria para comprar madeira e pregos seus amigos 3 no total decidiram ajudar na construcao juntos trabalharam duro e em poucos dias o barco estava pronto eles partiram em uma grande aventura rindo e se divertindo sob o sol')
    print(morse)
    print(decode_morse(morse))
    morse = create_morse('ola gente espero que estejam bem hoje quero compartilhar algo que achei interessante com voces estive lendo sobre como as novas tecnologias estao transformando o mundo dos negocios e como as empresas precisam se adaptar rapidamente para nao ficar para tras com o avancao da inteligencia artificial e da automacao muitos processos que antes eram feitos manualmente agora sao realizados por maquinas o que traz agilidade e eficiencia mas tambem exige que os profissionais desenvolvam novas habilidades para acompanhar essas mudancas e se manter relevantes no mercado de trabalho e interessante observar como as tecnologias estao mudando a forma como interagimos e trabalhamos e importante estar atento a essas transformacoes e se preparar para elas para garantir que possamos tirar o maximo proveito das oportunidades que surgem com a inovacao entao se voces estao pensando em investir em algum curso ou treinamento essa pode ser uma boa hora para considerar algo que esteja alinhado com as tendencias do mercado e assim estarem mais preparados para o futuro desejado espero que essa informacao tenha sido util para voces e que possam se beneficiar das oportunidades que estao surgindo com as novas tecnologias um abraco e ate mais')
    print(morse)
    print(decode_morse(morse))    
    morse = create_morse('ola a todos espero que estejam bem e com energia para mais uma leitura hoje quero falar sobre um assunto que considero muito relevante nos dias de hoje a evolucao das tecnologias e como elas estao impactando diversos aspectos de nossas vidas desde a maneira como trabalhamos ate como nos relacionamos e nos divertimos com o avancao acelerado da tecnologia muitas coisas que antes pareciam impossiveis se tornaram realidade a cada dia novas inovacoes surgem e transformam o mundo ao nosso redor um exemplo notavel e a inteligencia artificial que esta mudando a forma como interagimos com a tecnologia de maneira geral os assistentes virtuais sao um exemplo claro de como a inteligencia artificial pode facilitar nossas vidas permitindo que realizemos tarefas do dia a dia de forma mais eficiente e conveniente outro aspecto importante e a automacao que esta revolucionando o mercado de trabalho muitas tarefas repetitivas e manuais que antes eram realizadas por pessoas agora sao feitas por maquinas com isso as empresas podem aumentar sua produtividade e reduzir custos mas essa mudanca tambem traz desafios principalmente para os profissionais que precisam se adaptar a novas funcoes e adquirir novas habilidades para se manterem relevantes no mercado de trabalho alem disso a automacao e a inteligencia artificial estao criando novas oportunidades de emprego em areas que antes nao existiam a demanda por especialistas em tecnologia e inovacao esta crescendo e muitos profissionais estao se especializando em areas como desenvolvimento de software analise de dados e seguranca cibernetica a transformacao digital tambem esta impactando o setor educacional com a popularizacao dos cursos online e a aprendizagem a distancia mais pessoas tem acesso a educacao de qualidade e podem desenvolver novas habilidades de maneira flexivel e personalizada isso e especialmente importante em um mundo onde as mudancas tecnologicas sao rapidas e constantes a capacidade de aprender e se adaptar e essencial para o sucesso pessoal e profissional por outro lado e importante estar atento aos desafios eticos e sociais que surgem com essas novas tecnologias questoes como privacidade seguranca de dados e o impacto da automacao no emprego sao temas que precisam ser discutidos e abordados de forma responsavel a medida que avancamos no desenvolvimento tecnologico tambem e fundamental promover um equilibrio entre inovacao e responsabilidade para garantir que os beneficios da tecnologia sejam acessiveis e sustentaveis para todos alem disso a tecnologia tem um papel importante na forma como nos conectamos e comunicamos com outras pessoas as redes sociais e as plataformas de comunicacao tem mudado a maneira como interagimos e mantemos relacionamentos com amigos e familiares embora isso possa ser muito positivo tambem e necessario usar essas ferramentas com cuidado para evitar problemas como o vicio em tecnologia e a superficialidade das interacoes entao ao refletirmos sobre a influencia das tecnologias em nossas vidas e crucial encontrar um equilibrio saudavel entre aproveitar os beneficios e enfrentar os desafios que surgem com as inovacoes a capacidade de se adaptar e aprender continuamente sera uma vantagem significativa em um mundo cada vez mais tecnologico espero que este texto tenha sido util e que ajude a refletir sobre como podemos aproveitar ao maximo as oportunidades oferecidas pela tecnologia enquanto enfrentamos de maneira responsavel os desafios que surgem com ela um grande abraco e ate a proxima')
    print(morse)
    print(decode_morse(morse))