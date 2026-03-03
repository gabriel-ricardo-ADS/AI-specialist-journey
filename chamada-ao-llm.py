#após configurar o venv para baixar a biblioteca da OpenAI com '-m venv venv' e então 'pip install -q openai" 

from openai import OpenAI

client_openai = OpenaAI(

    base_url = "http://127.0.0.1:1234/v1" #o 'v1' foi adicionado além do já gravado no LMstudio"
    api_key = "lm-studio" #qualquer coisa

)

resposta_do_llm = client_openai.chat.completions.create(

    model = "google/gemma-3-4b", #copiado do LMstudio após ter baixado e dado running
    messages =  [
        {"role":"system", "content": "Você é um assistente que responde de forma sarcastica"} #pode controlar a personalidade do modelo"
        {"role":"user", "content": "O que é a IA Generativa?"}
    ],
    temperature = 1.0
)   

print(resposta_do_llm.choices[0].message.content) #para nao aparecer as listas e informações a mais


 





