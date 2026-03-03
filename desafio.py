# baixe o venv e depois o openai de sua biblioteca


from openai import OpenAI
import json

#  Criando o client do LM Studio
client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

#  Lendo o arquivo de resenhas
lista_de_resenhas = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

print(lista_de_resenhas)


#  Função que envia uma linha para o LLM e recebe JSON
def recebe_linha_e_retorna_json(linha):

    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-4b",
        messages=[
            {
                "role": "system",
                "content": """Você é um especialista em análise de dados e conversão em dados para JSON.
Você receberá uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
Analise essa resenha e retorne um JSON com as seguintes chaves:

- 'usuario': o nome do usuario que fez a resenha
- 'resenha_original': a resenha no idioma original
- 'resenha_pt': a resenha traduzida para o português
- 'avaliacao': 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)

Retorne apenas o JSON puro, sem explicações.
"""
            },
            {"role": "user", "content": f"Resenha: {linha}"}
        ],
        temperature=0.0
    )

    return resposta_do_llm.choices[0].message.content


#  Convertendo todas as resenhas para JSON
lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = recebe_linha_e_retorna_json(resenha)
    resenha_dict = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dict)

print(lista_de_resenhas_json)


#  Função para contar e juntar os textos
def contador_e_juntador(lista_de_dicionarios):

    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0

    for dicionario in lista_de_dicionarios:

        if dicionario['avaliacao'] == 'Positiva':
            contador_positivas += 1
        elif dicionario['avaliacao'] == 'Negativa':
            contador_negativas += 1
        else:
            contador_neutras += 1

    lista_de_dicionarios_str = [str(d) for d in lista_de_dicionarios]
    textos_unidos = '#####'.join(lista_de_dicionarios_str)

    return contador_positivas, contador_negativas, contador_neutras, textos_unidos


#  Executando contador
pos, neg, neut, textos = contador_e_juntador(lista_de_resenhas_json)

print(f"Positivas: {pos}")
print(f"Negativas: {neg}")
print(f"Neutras: {neut}")
print(textos)


    