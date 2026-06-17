import os
import requests
from dotenv import load_dotenv
from supabase import create_client

# 1 Configurações
load_dotenv()
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
ZAPI_URL = os.environ.get("ZAPI_URL")
ZAPI_TOKEN = os.environ.get("ZAPI_TOKEN")

# 2 Conexão
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 3 Busca Supabase
try:
    print("Buscando contatos no Supabase...")
    # Buscando na tabela os Contatos
    response = supabase.table("Contatos").select("*", count='exact').execute()
    
    # Mostra o que o banco respondeu para sabermos se há dados
    print(f"DEBUG: Dados recebidos: {response.data}")
    
    if not response.data:
        print("Nenhum contato encontrado na tabela.")
    else:
        for contato in response.data:
            nome = contato.get('nome', 'Cliente')
            # Ajustado para buscar pela coluna correta 'numero'
            telefone = contato.get('numero') 
            
            print(f"Tentando enviar para {nome} ({telefone})...")
            
            # Envio Z-API
            payload = {"phone": telefone, "message": f"Olá {nome}, tudo bem com você?"}
            headers = {"client-token": ZAPI_TOKEN}
            
            r = requests.post(f"{ZAPI_URL}/send-text", json=payload, headers=headers)
            
            if r.status_code == 200:
                print(">>> Mensagem enviada com sucesso!")
            else:
                print(f">>> Erro ao enviar. Resposta da API: {r.text}")

except Exception as e:
    print(f"Erro no sistema: {e}")
    