import os
import sys
import time
import random
import urllib.request
import urllib.parse

# --- CONSTANTES VISUAIS ---
G = "\033[92m"  # Verde Neon
B = "\033[1m"   # Negrito
R = "\033[0m"   # Reset
C = "\033[36m"  # Cyan

def typing(text, color=G, speed=0.01):
    for char in text:
        sys.stdout.write(color + char + R)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- CONFIGURAÇÃO DE IDIOMAS ---
LANG_MAP = {
    "1": {
        "name": "Português-BR",
        "sys": "Você é o NEXUS V24, uma IA hacker e superinteligente. Responda em Português (PT-BR). Seja técnico e direto.",
        "boot": "SINCRONIZANDO FREQUÊNCIA: PORTUGUÊS-BR...",
        "prompt": "COMANDO@NEXUS:",
        "think": "ACESSANDO MAINFRAME...",
        "exit": "ENCERRANDO SESSÃO..."
    },
    "2": {
        "name": "English",
        "sys": "You are NEXUS V24, a hacker and super-intelligent AI. Respond in English. Be technical and direct.",
        "boot": "SYNCHRONIZING FREQUENCY: ENGLISH...",
        "prompt": "COMMAND@NEXUS:",
        "think": "ACCESSING MAINFRAME...",
        "exit": "TERMINATING SESSION..."
    }
}

def draw_logo():
    logo = f"""
{G}{B}
  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
  {R}{G}[ THE HONORED ONE // MULTI-LANGUAGE V2.0 ]
{R}"
    print(logo)

# --- ENGINE DE INTELIGÊNCIA ---
def ask_nexus(user_query, sys_prompt):
    full_prompt = f"{sys_prompt} Input do usuário: {user_query}"
    encoded_prompt = urllib.parse.quote(full_prompt)
    url = f"https://text.pollinations.ai/{encoded_prompt}?model=openai&cache=true"

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return f"ERROR_CONNECTION_FAILED: {str(e)}"

# --- SISTEMA PRINCIPAL ---
def main():
    clear()
    draw_logo()
    
    # SELEÇÃO DE IDIOMA
    print(f"{B}{G}SELECT FREQUENCY / SELECIONE A FREQUÊNCIA:{R}")
    print(f"{G}[1] Português-BR")
    print(f"[2] English{R}")
    
    choice = input(f"\n{C}>> {R}")
    
    if choice not in LANG_MAP:
        choice = "1" # Default para PT-BR
    
    config = LANG_MAP[choice]
    
    clear()
    draw_logo()
    typing(f">>> {config['boot']}")
    typing(">>> PROTOCOLO HYPERION: ONLINE.")
    
    while True:
        try:
            print(f"\n{G}{B}╔══════════════════════════════════════════════════╗")
            user_input = input(f"║ {C}{config['prompt']}{R} ")
            print(f"{G}╚══════════════════════════════════════════════════╝{R}")

            if user_input.lower() in ['exit', 'sair', 'quit']:
                typing(f">>> {config['exit']}")
                break

            if not user_input.strip():
                continue

            # Carregamento visual
            sys.stdout.write(f"{G}║ {B}{config['think']}{R}")
            sys.stdout.flush()
            
            # Resposta da IA
            response = ask_nexus(user_input, config['sys'])
            
            # Limpar linha de carregamento
            sys.stdout.write("\r" + " " * 60 + "\r")
            
            print(f"{G}{B}[NEXUS]:{R}")
            typing(response, speed=0.005)
            print(f"{G}──────────────────────────────────────────────────{R}")

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()