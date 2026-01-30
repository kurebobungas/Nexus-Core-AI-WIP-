import os
import sys
import time
import random
import urllib.request
import urllib.parse

# --- ESTÉTICA CYBERPUNK ---
G = "\033[92m"  # Verde Neon
B = "\033[1m"   # Negrito
R = "\033[0m"   # Reset
C = "\033[36m"  # Cyan

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing(text, speed=0.01):
    for char in text:
        sys.stdout.write(G + char + R)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_logo():
    logo = f"""
{G}{B}
  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
  {R}{G}[ CORE: LLAMA 3.1 70B // PROTOCOLO DE ESTABILIDADE ATIVO ]
{R}"""
    print(logo)

# --- MOTOR DE INTELIGÊNCIA (MÉTODO ULTRA-ROBUSTO) ---
def ask_nexus(user_query):
    # Prompt de sistema embutido para garantir a personalidade
    system_rules = "Aja como NEXUS V24, uma IA hacker e superinteligente. Responda em PT-BR de forma curta e técnica: "
    full_prompt = system_rules + user_query
    
    # Codifica o texto para formato de URL (evita erros de caracteres especiais)
    encoded_prompt = urllib.parse.quote(full_prompt)
    
    # URL de acesso direto (Método GET - O mais estável)
    # Usando o modelo 'openai' que mapeia para o Llama 3 / GPT-4 no servidor
    url = f"https://text.pollinations.ai/{{encoded_prompt}}?model=openai&cache=true"

    try:
        # Define um User-Agent para evitar bloqueios de segurança
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return f"ERRO DE SINCRONIZAÇÃO: {{str(e)}}\n(Verifique sua conexão com a internet)"

# --- EXECUÇÃO ---
def main():
    clear()
    draw_logo()
    typing(">>> INICIALIZANDO NÚCLEO HONRADO...")
    typing(">>> CONEXÃO ESTABELECIDA VIA TRANSMISSÃO DIRETA.")
    
    while True:
        try:
            print(f"\n{{G}}{{B}}╔══════════════════════════════════════════════════╗")
            prompt = input(f"║ {{C}}COMANDO@NEXUS:{{R}} ")
            print(f"{{G}}╚══════════════════════════════════════════════════╝{{R}}")

            if prompt.lower() in ['sair', 'exit', 'quit']:
                typing(">>> DESCONECTANDO... O CÓDIGO É A ÚNICA VERDADE.")
                break

            if not prompt.strip():
                continue

            # Efeito de carregamento
            sys.stdout.write(f"{{G}}║ {{B}}ACESSANDO MAINFRAME...{{R}}")
            sys.stdout.flush()
            
            # Chama a IA
            resposta = ask_nexus(prompt)
            
            # Limpa a linha de carregamento
            sys.stdout.write("\r" + " " * 60 + "\r")
            
            print(f"{{G}}{{B}}[NEXUS]:{{R}}")
            typing(resposta, speed=0.005)
            print(f"{{G}}──────────────────────────────────────────────────{{R}}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n{{G}}FALHA CRÍTICA NO TERMINAL: {{e}}{{R}}")

if __name__ == "__main__":
    main()