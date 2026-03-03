# Após configurar o venv com: python -m venv venv e ativar o ambiente, depois instalar a biblioteca: pip install -q openai

from openai import OpenAI

# Criando o cliente apontando para o LM Studio rodando localmente
client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",  # o 'v1' foi adicionado além do já configurado no LM Studio
    api_key="lm-studio"  # pode ser qualquer quando estiver usando LM Studio local
)

# Fazendo uma requisição para o modelo carregado no LM Studio
resposta_do_llm = client_openai.chat.completions.create(
    model="google/gemma-3-4b",  # copiado do LM Studio após baixar e clicar em "Run"
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente que responde de forma sarcástica"
        },  # controle da personalidade do modelo
        {
            "role": "user",
            "content": "O que é IA Generativa?"
        }
    ],
    temperature=1.0  # quanto maior, mais criativa/aleatória a resposta
)

# Mostra apenas o conteúdo da resposta (sem metadados extras)
print(resposta_do_llm.choices[0].message.content)




