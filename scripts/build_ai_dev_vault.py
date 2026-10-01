from pathlib import Path
import json, re, shutil, zipfile, random, textwrap
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "vault-desenvolvimento-software-com-ia"
ZIP = ROOT / "vault-desenvolvimento-software-com-ia.zip"
TODAY = "2026-09-30"
random.seed(7)

if VAULT.exists():
    shutil.rmtree(VAULT)
for d in [
    "00-Inicio", "01-Fundamentos", "02-Ferramentas-IA", "03-Tipos-de-Desenvolvimento", "04-Jogos",
    "05-Engenharia", "06-Riscos-e-Realidade", "07-Negocio-e-Carreira", "08-Trilhas-de-Estudo",
    "09-Arvores-de-Decisao", "10-Glossario", "_meta", "_canvas", ".obsidian"
]:
    (VAULT/d).mkdir(parents=True, exist_ok=True)

DOMAIN_DIR = {
    "fundamentos":"01-Fundamentos", "ferramentas-ia":"02-Ferramentas-IA", "tipos-dev":"03-Tipos-de-Desenvolvimento",
    "jogos":"04-Jogos", "engenharia":"05-Engenharia", "riscos":"06-Riscos-e-Realidade", "negocio":"07-Negocio-e-Carreira",
    "trilhas":"08-Trilhas-de-Estudo", "glossario":"10-Glossario"
}
DOMAIN_MOC = {
    "fundamentos":"MOC-Fundamentos", "ferramentas-ia":"MOC-Ferramentas-IA", "tipos-dev":"MOC-Tipos-de-Desenvolvimento",
    "jogos":"MOC-Jogos", "engenharia":"MOC-Engenharia", "riscos":"MOC-Riscos-e-Realidade", "negocio":"MOC-Negocio-e-Carreira",
    "trilhas":"MOC-Trilhas-de-Estudo", "glossario":"MOC-Glossario"
}
DOMAIN_LABEL = {
    "fundamentos":"Fundamentos e conceitos", "ferramentas-ia":"Ferramentas de IA", "tipos-dev":"Tipos de desenvolvimento",
    "jogos":"Jogos", "engenharia":"Engenharia que sustenta tudo", "riscos":"Riscos e realidade", "negocio":"Negócio e carreira",
    "trilhas":"Trilhas de estudo", "glossario":"Glossário"
}

SOURCE_REGISTRY = {
 "mcp":[("Model Context Protocol docs", "https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro", "Nivel 1", "padrão aberto para conectar aplicações de IA a dados, ferramentas e workflows")],
 "claude_code":[("Claude Code docs", "https://code.claude.com/docs/en/overview", "Nivel 1", "assistente de coding da Anthropic em terminal, IDE, desktop e web")],
 "github_copilot":[("GitHub Copilot docs", "https://docs.github.com/en/copilot", "Nivel 1", "documentação oficial do Copilot"),("GitHub Copilot plans", "https://github.com/features/copilot/plans", "Nivel 1", "preços e planos oficiais consultados")],
 "codex":[("OpenAI Codex", "https://openai.com/codex/", "Nivel 1", "produto oficial Codex, planos e capacidades")],
 "gemini_cli":[("Gemini CLI docs", "https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli", "Nivel 1", "CLI Gemini, ReAct loop, MCP, quotas compartilhadas; página atualizada em 2026-09-24")],
 "cursor":[("Cursor pricing", "https://cursor.com/pricing", "Nivel 1", "preços oficiais Cursor consultados em 2026-09-30")],
 "windsurf":[("Windsurf/Devin pricing redirect", "https://windsurf.com/pricing", "Nivel 1", "página redirecionou para Devin pricing em 2026-09-30; tratar como volátil"),("Devin pricing", "https://devin.ai/pricing", "Nivel 1", "planos oficiais Devin")],
 "obsidian_canvas":[("Obsidian Canvas Help", "https://help.obsidian.md/plugins/canvas", "Nivel 1", "Canvas é plugin core do Obsidian e usa .canvas em JSON Canvas"),("JSON Canvas", "https://jsoncanvas.org/", "Nivel 1", "formato aberto JSON Canvas")],
 "unity":[("Unity pricing updates", "https://unity.com/products/pricing-updates", "Nivel 1", "planos Unity 2026: Personal, Pro, Enterprise e DevOps")],
 "unreal":[("Unreal Engine licensing", "https://www.unrealengine.com/license", "Nivel 1", "licenciamento oficial, royalties e assentos")],
 "godot":[("Godot license", "https://godotengine.org/license/", "Nivel 1", "Godot sob licença MIT"),("Godot docs", "https://docs.godotengine.org/en/stable/", "Nivel 1", "documentação oficial Godot")],
 "gamemaker":[("GameMaker pricing", "https://gamemaker.io/en/get", "Nivel 1", "free non-commercial, Professional one-time, Enterprise")],
 "defold":[("Defold homepage", "https://defold.com/", "Nivel 1", "engine 2D/3D free, Lua, multiplataforma")],
 "phaser":[("Phaser homepage", "https://phaser.io/", "Nivel 1", "Phaser e Agentic Engine com integrações MCP")],
 "ai_productivity":[("GitHub Copilot impact study", "https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/", "Nivel 1", "estudo controlado amplamente citado sobre velocidade com Copilot"),("METR AI productivity study", "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/", "Nivel 1", "RCT com desenvolvedores experientes em bases conhecidas"),("DORA reports", "https://dora.dev/research/", "Nivel 1", "pesquisas State of DevOps")],
 "stackoverflow":[("Stack Overflow Developer Survey", "https://survey.stackoverflow.co/", "Nivel 1", "survey anual com adoção, sentimento e ferramentas")],
 "owasp":[("OWASP Top 10 for LLM Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/", "Nivel 1", "riscos de aplicações com LLM"),("OWASP ASVS", "https://owasp.org/www-project-application-security-verification-standard/", "Nivel 1", "verificação de segurança de aplicações")],
 "web":[("MDN Web Docs", "https://developer.mozilla.org/", "Nivel 1", "documentação web"),("React docs", "https://react.dev/", "Nivel 1", "documentação React"),("Next.js docs", "https://nextjs.org/docs", "Nivel 1", "documentação Next.js"),("Node.js docs", "https://nodejs.org/en/docs", "Nivel 1", "documentação Node.js")],
 "mobile":[("Android Developers", "https://developer.android.com/", "Nivel 1", "docs Android"),("Apple Developer Documentation", "https://developer.apple.com/documentation/", "Nivel 1", "docs Apple"),("Flutter docs", "https://docs.flutter.dev/", "Nivel 1", "docs Flutter"),("React Native docs", "https://reactnative.dev/docs/getting-started", "Nivel 1", "docs React Native")],
 "backend":[("PostgreSQL docs", "https://www.postgresql.org/docs/", "Nivel 1", "PostgreSQL"),("Docker docs", "https://docs.docker.com/", "Nivel 1", "Docker"),("Kubernetes docs", "https://kubernetes.io/docs/", "Nivel 1", "Kubernetes"),("OpenAPI Specification", "https://spec.openapis.org/oas/latest.html", "Nivel 1", "OpenAPI")],
 "cloud":[("AWS Documentation", "https://docs.aws.amazon.com/", "Nivel 1", "AWS"),("Google Cloud docs", "https://cloud.google.com/docs", "Nivel 1", "Google Cloud"),("Azure docs", "https://learn.microsoft.com/azure/", "Nivel 1", "Azure")],
 "legal":[("LGPD", "https://www.gov.br/anpd/pt-br", "Nivel 1", "Autoridade Nacional de Proteção de Dados"),("SPDX License List", "https://spdx.org/licenses/", "Nivel 1", "identificadores de licenças")],
}

source_urls = {k:[u for _,u,_,__ in v] for k,v in SOURCE_REGISTRY.items()}

def slug(s):
    repl = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüçñÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇÑ", "aaaaaeeeeiiiiooooouuuucnAAAAAEEEEIIIIOOOOOUUUUCN")
    s = s.translate(repl)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    return s[:90] or "nota"

def ylist(xs):
    return "[" + ", ".join(json.dumps(x, ensure_ascii=False) for x in xs) + "]"

def write(rel, text):
    p = VAULT/rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip()+"\n", encoding="utf-8")

class Note:
    def __init__(self, title, domain, kind="conceito", level="iniciante", aliases=None, tags=None, sources=None, stable=False, desc=None, area=None):
        self.title=title; self.slug=slug(title); self.domain=domain; self.kind=kind; self.level=level
        self.aliases=aliases or [] ; self.tags=tags or [] ; self.sources=sources or [] ; self.stable=stable; self.desc=desc or ""; self.area=area or domain
        self.path=f"{DOMAIN_DIR[domain]}/{self.slug}.md" if domain in DOMAIN_DIR else f"01-Fundamentos/{self.slug}.md"

notes=[]
def add(title, domain, kind="conceito", level="iniciante", aliases=None, tags=None, src=None, stable=False, desc=None, area=None):
    n=Note(title, domain, kind, level, aliases, tags, src or [], stable, desc, area)
    notes.append(n); return n

# A. Fundamentos
fund_topics = [
("Vibe coding", ["vibe coding"], "desenvolver orientando IA por intenção, feedback rápido e aceitação/rejeição iterativa do resultado"),
("Desenvolvimento assistido por IA", ["AI-assisted development"], "uso de copilotos e chats para acelerar programação sem delegar responsabilidade final"),
("Engenharia agentica", ["agentic engineering"], "orquestração de agentes capazes de planejar, editar, executar e validar tarefas"),
("Programacao em linguagem natural", ["natural language programming"], "transformar requisitos em comandos executáveis por modelos e agentes"),
("Historico autocomplete chat agentes", ["autocomplete to agents"], "evolução de autocomplete para chat contextual e agentes que atuam em repositórios"),
("Spec driven development", ["spec-driven development"], "começar pelo comportamento esperado e usar a especificação como contrato de implementação"),
("Prompt engineering para codigo", ["prompt engineering for code"], "formular pedidos claros para gerar, revisar e testar código"),
("Context engineering", ["context engineering"], "projetar o contexto que uma IA recebe para reduzir alucinação e retrabalho"),
("Arquivos de regras de projeto", ["AGENTS.md", "CLAUDE.md", ".cursorrules"], "instruções versionadas que guiam agentes dentro do repositório"),
("AGENTS md", ["AGENTS.md"], "arquivo de instruções para agentes humanos e de IA em um projeto"),
("CLAUDE md", ["CLAUDE.md"], "convenção de instruções persistentes para Claude Code em repositórios"),
("Cursor rules", [".cursorrules", "Cursor Rules"], "regras de projeto usadas para orientar o Cursor e agentes compatíveis"),
("MCP Model Context Protocol", ["MCP", "Model Context Protocol"], "padrão aberto para conectar IA a ferramentas, dados e workflows"),
("Servidores MCP", ["MCP servers"], "componentes que expõem ferramentas e dados para clientes de IA"),
("Clientes MCP", ["MCP clients"], "aplicações de IA capazes de consumir servidores MCP"),
("Subagentes", ["subagents"], "agentes especializados chamados por um orquestrador para tarefas específicas"),
("Skills de agentes", ["agent skills", "SKILL.md"], "pacotes de instrução e procedimento para tarefas recorrentes"),
("Memoria de agentes", ["agent memory"], "mecanismos para persistir preferências, fatos e contexto entre sessões"),
("RAG para desenvolvimento", ["Retrieval-Augmented Generation", "RAG"], "recuperar documentação e código relevante antes de gerar respostas"),
("Fluxos multiagente", ["multi-agent workflows"], "vários agentes paralelos ou sequenciais com papéis definidos"),
("Orquestracao de IA", ["AI orchestration"], "dirigir ferramentas, agentes e modelos como um sistema de produção"),
("Modelos locais", ["local models"], "executar LLMs em máquina própria para privacidade, custo ou controle"),
("Modelos em nuvem", ["cloud models"], "usar modelos hospedados por provedores com maior capacidade e recursos gerenciados"),
("Janela de contexto", ["context window"], "quantidade de tokens que o modelo consegue considerar em uma chamada"),
("Tokens e custo", ["tokens", "token cost"], "unidade econômica e técnica de entrada e saída de modelos"),
("Hallucination em codigo", ["hallucination"], "respostas plausíveis porém incorretas, APIs inexistentes ou premissas falsas"),
("Grounding", ["grounding"], "ancorar respostas em fontes, arquivos e execução verificável"),
("Tool use", ["function calling", "tool use"], "capacidade do modelo de chamar ferramentas externas com parâmetros"),
("ReAct loop", ["Reason and Act"], "ciclo de raciocinar, agir com ferramenta, observar resultado e ajustar plano"),
("Plan mode", ["planning mode"], "modo em que o agente planeja antes de editar ou executar"),
("Human in the loop", ["HITL"], "pontos de intervenção humana para aprovar riscos e decisões"),
("Sandbox para agentes", ["agent sandbox"], "ambiente isolado para execução de comandos e código gerado"),
("Aprovacoes de comandos", ["command approvals"], "política de pedir permissão antes de ações perigosas"),
("Diff review", ["code diff review"], "revisar mudanças por diferenças antes de aceitar"),
("Benchmark SWE-bench", ["SWE-bench"], "benchmark de correção de issues reais em repositórios Python"),
("Terminal Bench", ["Terminal-Bench"], "benchmark de tarefas em terminal para agentes"),
("Evals de agentes", ["agent evaluations"], "testes sistemáticos para medir qualidade, custo e segurança"),
("Autonomia graduada", ["graduated autonomy"], "aumentar permissões de agentes conforme confiança e validação"),
("Contrato de tarefa para agentes", ["task contract"], "briefing com objetivo, restrições, critérios de aceite e método de verificação"),
("Critérios de aceite", ["acceptance criteria"], "condições observáveis que definem se a entrega está correta"),
("Decomposicao de tarefas", ["task decomposition"], "quebrar objetivos grandes em passos que agentes executam e validam"),
("Trabalho em lote com agentes", ["batch agent work"], "executar tarefas paralelas ou filas de issues com supervisão"),
("Prompt de revisao", ["review prompt"], "pedido estruturado para encontrar bugs, riscos e lacunas"),
("Contexto minimo suficiente", ["minimum sufficient context"], "dar ao modelo contexto necessário sem poluir a janela"),
("Especificacao executavel", ["executable specification"], "spec que vira testes, exemplos ou validação automática"),
("Documentacao como contexto", ["docs as context"], "documentação versionada para guiar agentes e humanos"),
("Arquitetura de prompts", ["prompt architecture"], "conjunto reutilizável de prompts, templates e políticas"),
("Memoria versus contexto", ["memory vs context"], "diferença entre informação persistida e informação colocada na janela atual"),
("IA como junior veloz", ["AI as fast junior"], "metáfora útil: produz muito, mas precisa de direção e revisão"),
("IA como par de programacao", ["AI pair programmer"], "IA colaborando com humano no ciclo de design, código e revisão"),
("IA como executor delegado", ["delegated AI executor"], "agente recebe missão e devolve diff validado"),
("Loop especificar gerar verificar", ["spec-generate-verify loop"], "rotina operacional central do orquestrador de IA"),
("Context poisoning", ["context poisoning"], "quando contexto incorreto guia o modelo para decisões ruins"),
("Prompt injection em ferramentas", ["prompt injection"], "instruções maliciosas em dados externos que tentam controlar o agente"),
("Cadeia de custodia do contexto", ["context provenance"], "rastrear de onde veio cada informação que orientou a IA"),
("Engenharia de conhecimento para agentes", ["knowledge engineering for agents"], "organizar regras, fontes e memória para agentes trabalharem melhor"),
("Pesquisa assistida por IA", ["AI-assisted research"], "usar modelos para mapear fontes, mas verificar fatos críticos"),
("Leitura critica de output de IA", ["critical AI output review"], "avaliar coerência, fonte, execução e riscos do que foi entregue"),
("Desenvolvimento orientado a conversa", ["conversation-driven development"], "produto evolui por diálogos, refinamentos e validação contínua"),
("Arquitetura de conhecimento no Obsidian", ["Obsidian knowledge architecture"], "usar MOCs, backlinks, tags e canvas para mapear aprendizado")]
for t,a,d in fund_topics:
    src = source_urls["mcp"]+source_urls["claude_code"] if any(x in t.lower() for x in ["mcp","agente","subagente","skill","tool","react"]) else source_urls["github_copilot"]+source_urls["ai_productivity"]
    add(t,"fundamentos","conceito","iniciante",a,["dominio/fundamentos"],src,False,d)

# B. Ferramentas IA
ai_tools = [
("Cursor","IDE de IA baseado em VS Code com Agent, Composer, rules, MCP e cloud agents","IDE"),
("GitHub Copilot","assistente da GitHub para completions, chat, agent mode, CLI, code review e cloud agent","IDE extension"),
("Claude Code","agente de coding da Anthropic para terminal, IDE, desktop e web","CLI agent"),
("OpenAI Codex","agente de coding da OpenAI incluído em planos ChatGPT e fluxos web/cloud","CLI cloud agent"),
("Gemini CLI","CLI open source com ReAct loop, ferramentas locais/remotas e MCP","CLI agent"),
("Windsurf","editor/ambiente de IA historicamente associado ao Codeium; status e marca devem ser verificados","IDE"),
("Devin","agente de software da Cognition com cloud agents, desktop/CLI e planos próprios","cloud agent"),
("Zed AI","editor Zed com integrações de IA e fluxo colaborativo rápido","IDE"),
("Aider","agente CLI open source focado em edição via Git e modelos configuráveis","CLI agent"),
("Cline","extensão VS Code open source para agentes com uso de ferramentas e BYOK","IDE extension"),
("Roo Code","fork/ecossistema de agente VS Code com modos e automações","IDE extension"),
("Continue","assistente open source para IDEs com modelos locais e remotos","IDE extension"),
("OpenCode","agente terminal model-agnostic para desenvolvimento com IA","CLI agent"),
("Goose","agente open source para automação e desenvolvimento local","CLI agent"),
("Qwen Code","agente/CLI para modelos Qwen e coding tasks","CLI agent"),
("Amazon Q Developer","assistente de IA da AWS para código, cloud e modernização","IDE cloud"),
("JetBrains AI Assistant","IA integrada às IDEs JetBrains","IDE"),
("Visual Studio IntelliCode e Copilot","assistência IA no ecossistema Visual Studio","IDE"),
("Replit Agent","construtor de apps e agente de desenvolvimento em ambiente Replit","app builder"),
("Lovable","construtor de apps web full-stack orientado por prompt","app builder"),
("Bolt new","builder de apps web em browser com stack JavaScript","app builder"),
("v0 by Vercel","gerador de interfaces e apps React/Next por prompt","UI builder"),
("Base44","builder de aplicações com IA para protótipos e sistemas internos","app builder"),
("Firebase Studio","ambiente Google para prototipar apps full-stack com IA","app builder"),
("GitHub Spark","ferramenta GitHub para criar apps por linguagem natural","app builder"),
("Create.xyz","builder de apps e sites por prompt","app builder"),
("Framer AI","geração de sites e landing pages com IA","site builder"),
("Webflow AI","assistência IA no ecossistema Webflow","site builder"),
("Figma AI","recursos de IA em design de produto e interface","design"),
("Galileo AI","geração de UI por prompt","design"),
("Uizard","prototipagem UI assistida por IA","design"),
("Relume","sitemaps, wireframes e copy para sites com IA","design"),
("Midjourney","geração de imagens para concept art e assets de referência","arte"),
("DALL-E","geração/edição de imagens via OpenAI","arte"),
("Stable Diffusion","ecossistema open source de geração de imagens","arte"),
("Flux","família/modelos de imagem para geração visual","arte"),
("Adobe Firefly","IA generativa da Adobe para imagens e workflows criativos","arte"),
("Leonardo AI","plataforma de assets e imagens para jogos e design","arte"),
("Scenario","geração de arte para games com consistência de estilo","arte"),
("Meshy","geração de modelos 3D assistida por IA","3D"),
("Luma AI","captura/generação 3D e vídeo com IA","3D video"),
("Tripo AI","geração de modelos 3D por prompt ou imagem","3D"),
("Spline AI","design 3D web com recursos de IA","3D"),
("Runway","ferramentas de vídeo generativo e edição","video"),
("Pika","geração de vídeo por prompt","video"),
("ElevenLabs","voz sintética e áudio para narração e personagens","audio"),
("Suno","geração de música por IA; revisar licenças antes de uso comercial","audio"),
("Udio","geração de música por IA; revisar termos e direitos","audio"),
("AIVA","música assistida por IA para mídia","audio"),
("Soundraw","música gerada/licenciada por IA","audio"),
("Krea","geração visual e realtime image tools","arte"),
("Magnific AI","upscaling e melhoria de imagem","arte"),
("Topaz AI","upscaling/denoise de imagem e vídeo","arte video"),
("PlayHT","voz sintética e TTS","audio"),
("Rive","animação interativa 2D com workflows modernos","animacao"),
("Cascade","modo/fluxo de agente associado ao Windsurf","agent mode"),
("Copilot Workspace","ambiente GitHub para planejar e implementar issues com IA","cloud agent"),
("CodeRabbit","code review automático com IA","review"),
("Sourcery","refatoração e code review assistidos","review"),
("Snyk AI","segurança e correção assistida por IA","security"),
("Semgrep Assistant","análise e triagem de segurança com IA","security"),
("Phaser Agentic Engine","geração de jogos com Phaser e agentes compatíveis MCP","game builder"),
]
# Add model families/tools
models = ["OpenAI GPT para codigo","Claude Sonnet para codigo","Claude Opus para codigo","Gemini Pro para codigo","Gemini Flash para codigo","Grok para codigo","Qwen Coder","DeepSeek Coder","Kimi K2 para codigo","Llama para codigo local","Codestral","StarCoder","Code Llama","Mistral para codigo","Devstral"]
for m in models: ai_tools.append((m, "modelo ou família de modelos usada em tarefas de programação e agentes", "modelo"))
for name,desc,cat in ai_tools:
    key = "cursor" if name=="Cursor" else "github_copilot" if "Copilot" in name else "claude_code" if name=="Claude Code" else "codex" if "Codex" in name or "OpenAI" in name else "gemini_cli" if "Gemini" in name else "windsurf" if name in ["Windsurf","Cascade","Devin"] else "phaser" if "Phaser" in name else "mcp"
    add(name,"ferramentas-ia","ferramenta","iniciante",[name,cat], ["dominio/ferramentas-ia", f"ferramenta/{slug(cat).lower()}"], source_urls.get(key, source_urls["mcp"]), False, desc, cat)

# C. Tipos de desenvolvimento
web_types = ["Frontend web","Backend web","Full stack web","PWA Progressive Web App","Landing page","E-commerce","CMS headless","CMS tradicional","SaaS B2B","Dashboard administrativo","Portal de cliente","API REST","API GraphQL","API gRPC","Microsservicos","Monolito modular","Serverless functions","Edge functions","Web scraping etico","Automacao web","Chatbot de atendimento","Bot de Discord","Bot de Telegram","CLI tools","Extensoes de navegador","Extensoes de VS Code","Desktop Electron","Desktop Tauri","Desktop Qt","Desktop dotNET MAUI","Mobile Android nativo","Mobile iOS nativo","Flutter","React Native","Kotlin Multiplatform","PWA mobile","Apps offline-first","ERP","CRM","Sistema de RH","Sistema financeiro","Marketplace","Sistema de reservas","Sistema de delivery","Sistema de conteudo","Data pipeline","Data warehouse","BI e analytics","Machine learning aplicado","LLM app","RAG app","Fine tuning app","Computer vision app","IoT embarcado","Firmware simples","Arduino e ESP32","Robotics software","Low code","No code","Internal tools","Planilhas automatizadas","Notion e Airtable apps","Zapier Make n8n","Automacao com Python","Scripts de terminal","Web3 e smart contracts","Apps em tempo real","Video streaming app","Chat em tempo real","Sistema multi tenant","White label SaaS","CMS para jogos live ops","Backend para jogo online","Loja virtual indie"]
for t in web_types:
    domain_sources = source_urls["mobile"] if any(x in t.lower() for x in ["mobile","android","ios","flutter","react native","kotlin"]) else source_urls["backend"] if any(x in t.lower() for x in ["api","backend","micro","serverless","dados","data","warehouse","multi tenant"]) else source_urls["web"]
    add(t,"tipos-dev","conceito","iniciante",[t], ["dominio/tipos-dev"], domain_sources, False, f"panorama prático de {t} para decidir stack, custo e como delegar tarefas a IA")

# D. Jogos - engines, genres, modalities, disciplines
engines = [
("Unity","engine C# multiplataforma forte em mobile, 2D/3D e ecossistema comercial", "unity"),
("Unreal Engine","engine C++/Blueprints para 3D de alta fidelidade, PC/console e virtual production", "unreal"),
("Godot","engine open source MIT para 2D/3D com GDScript, C# e C++", "godot"),
("GameMaker","engine especializada em 2D e pixel art com GML", "gamemaker"),
("Phaser","framework JavaScript/TypeScript para jogos HTML5", "phaser"),
("PixiJS","renderer 2D WebGL/WebGPU para experiências e jogos web", "web"),
("Three.js","biblioteca JavaScript 3D para web", "web"),
("Babylon.js","engine 3D web com TypeScript e WebGPU/WebGL", "web"),
("Pygame","biblioteca Python para jogos 2D e protótipos", "web"),
("Love2D","framework Lua leve para jogos 2D", "defold"),
("Bevy","engine Rust ECS para jogos modernos", "backend"),
("MonoGame","framework C# inspirado em XNA", "web"),
("Defold","engine free/source-available 2D/3D com Lua e builds pequenos", "defold"),
("Cocos Creator","engine TypeScript para mobile e web games", "web"),
("RPG Maker","ferramenta especializada em JRPGs 2D narrativos", "gamemaker"),
("Construct","engine no-code/event sheets para 2D web/mobile", "web"),
("GDevelop","engine no-code/open source para jogos 2D", "web"),
("Roblox Studio","plataforma UGC com Luau e distribuição no ecossistema Roblox", "web"),
("PlayCanvas","engine web 3D colaborativa", "web"),
("Heaps","engine Haxe para 2D/3D", "web"),
("Raylib","biblioteca C simples para jogos e protótipos", "web"),
]
for name,desc,key in engines:
    add(name,"jogos","engine","iniciante",[name], ["dominio/jogos","jogos/engine"], source_urls.get(key, source_urls["web"]), False, desc, "engine")

genres = ["Jogo 2D","Jogo 2.5D","Jogo 3D","Pixel art","Top down","Plataforma 2D","Metroidvania","RPG 2D","JRPG","Action RPG","Roguelike","Roguelite","Idle clicker","Puzzle","Jogo de cartas","Deckbuilder","Tower defense","Simulacao","Estrategia em tempo real","Estrategia por turnos","FPS","TPS","Narrativo","Visual novel","Text based game","Casual mobile","Hyper casual","Bullet hell","Shoot em up","Beat em up","Fighting game","Survival","Crafting survival","Sandbox","City builder","Tycoon","Rhythm game","Horror","Stealth","Cozy game","Auto battler","MOBA","Battle royale","MMO","MMORPG","Extraction shooter","Party game","Educational game","Serious game"]
for g in genres:
    add(g,"jogos","genero","iniciante",[g], ["dominio/jogos","jogos/genero"], source_urls["godot"]+source_urls["unity"], True, f"formato/gênero de jogo: {g}, com implicações de escopo, engine, assets, IA e produção")
modalities = ["Single player offline","Multiplayer local","Online cooperativo","Online competitivo","MMO para solo dev","MMORPG viabilidade","Mobile game","Web HTML5 game","PC game Steam","Console publishing","VR game","AR game","Cross platform game","Servidor autoritativo","Peer to peer multiplayer","Rollback netcode","Deterministic lockstep","Matchmaking","Lobby system","Live ops para jogos","Economia de jogo online","Persistencia de personagem","Shard e instancias","Anti cheat","Moderacao de comunidade","UGC user generated content","Monetizacao free to play","Premium game","Demo e vertical slice","Early access"]
for m in modalities:
    add(m,"jogos","conceito","intermediario",[m], ["dominio/jogos","jogos/modalidade"], source_urls["unreal"]+source_urls["unity"], False, f"decisão de modalidade/plataforma para jogos: {m}")
disciplines = ["Game loop","Core loop","Game design document","Progressao","Economia de jogo","Balanceamento","Level design","Narrativa interativa","Quest design","Arte conceitual","Pipeline de pixel art","Animacao 2D","Rigging 2D","Audio para jogos","Musica adaptativa","UI UX em jogos","Game feel","Juice e feedback","Fisica 2D","Fisica 3D","IA de NPC","Behavior tree","GOAP","Pathfinding","Tilemaps","Sprites e atlases","Shaders 2D","Iluminacao 2D","Camera 2D","Save system","Inventario","Sistema de dialogo","Sistema de quest","Combate 2D","Hitbox e hurtbox","Input buffering","Coyote time","Procedural generation","Dungeon generation","World streaming","Netcode","Servidor de jogo","Banco de dados para jogos","Escalabilidade de jogo online","Observabilidade de jogo","Analytics e telemetria","AB testing em jogos","Publicacao Steam","Publicacao mobile stores","Classificacao indicativa","Localizacao de jogos","Acessibilidade em jogos","Licencas de assets","Pipeline IA para jogos","Prototipo jogavel","Vertical slice","Playtest","QA de jogos","Build pipeline de jogos","Patch e hotfix","Live ops calendar"]
for d in disciplines:
    add(d,"jogos","tecnica","iniciante" if len(d)<14 else "intermediario",[d], ["dominio/jogos","jogos/disciplina"], source_urls["godot"]+source_urls["unity"]+source_urls["phaser"], False, f"disciplina ou sistema essencial no desenvolvimento de jogos: {d}")

# E. Engenharia
eng = ["Arquitetura limpa","Arquitetura hexagonal","Arquitetura orientada a eventos","DDD Domain Driven Design","CQRS","Event sourcing","Monolito modular engenharia","Microsservicos engenharia","API design","OpenAPI","Autenticacao","Autorizacao RBAC","OAuth 2","OpenID Connect","Passkeys","JWT","Sessao e cookies","Seguranca web","OWASP Top 10","Seguranca em apps com LLM","Banco relacional","PostgreSQL","MySQL","SQLite","Banco NoSQL","MongoDB","Redis","Vector database","pgvector","Pinecone","Weaviate","Qdrant","Supabase","Firebase","Prisma ORM","Drizzle ORM","Migrations de banco","Cache","Filas e mensageria","RabbitMQ","Kafka","NATS","Testes unitarios","Testes de integracao","Testes end to end","Playwright","Cypress","TDD com IA","Mutation testing","Contract testing","QA manual com IA","Validacao de codigo gerado por IA","Git","GitHub flow","Pull request","Code review","CI CD","GitHub Actions","Docker","Kubernetes","Terraform","Hospedagem Vercel","Hospedagem Netlify","Hospedagem Fly io","Hospedagem Railway","AWS para apps","Google Cloud para apps","Azure para apps","Observabilidade","Logs estruturados","Metricas","Tracing distribuido","Sentry","OpenTelemetry","Performance web","Performance backend","Custos de nuvem","Custos de tokens","Documentacao tecnica","ADR Architecture Decision Record","Refatoracao","Divida tecnica","Feature flags","Secrets management","Backup e restore","Disaster recovery"]
for e in eng:
    src = source_urls["owasp"] if "segur" in e.lower() or "llm" in e.lower() or "auth" in e.lower() else source_urls["backend"] if any(x in e.lower() for x in ["banco","postgres","docker","kubernetes","openapi","redis","kafka","fila"]) else source_urls["cloud"] if any(x in e.lower() for x in ["aws","cloud","hosped","vercel","railway","netlify"]) else source_urls["github_copilot"]+source_urls["ai_productivity"]
    add(e,"engenharia","arquitetura" if "arquitetura" in e.lower() else "tecnica","intermediario",[e], ["dominio/engenharia"], src, False, f"prática de engenharia para sustentar sistemas criados com IA: {e}")

# F. Riscos
risks = ["Limites do vibe coding","Alucinacoes em APIs","Vulnerabilidades em codigo gerado","Dívida técnica invisível","Dependencia de ferramenta","Lock in de fornecedor IA","Privacidade com agentes","LGPD em apps com IA","Propriedade intelectual de codigo gerado","Licenca de arte gerada por IA","Treinamento em codigo privado","Prompt injection","Data exfiltration por agente","Supply chain attack","Pacotes alucinados","Typosquatting","Comandos perigosos de agente","Perda de compreensao do codigo","Overengineering gerado por IA","Subtestes e falso verde","Code review superficial","Custos explosivos de tokens","Custos escondidos de cloud agents","Shadow AI na empresa","Uso de fontes nao verificadas","Marketing versus fato em IA","Benchmark gaming","Produtividade percebida versus medida","Estudo GitHub Copilot 55 porcento","Estudo METR slowdown 19 porcento","DORA e IA em engenharia","Qualidade de codigo com IA","Seguranca de MCP servers","Permissoes excessivas","Segredos em prompts","Compliance e auditoria","Dados sensiveis em logs","Deepfake e voz sintetica","Uso comercial de musica IA","Termos de servico de ferramentas","Descontinuacao de produtos IA","Mudanca de preco em IA","Sustentabilidade de stack hype","Quando contratar humano","Quando nao usar IA"]
for r in risks:
    src = source_urls["ai_productivity"] if any(x in r.lower() for x in ["produtividade","github","metr","dora","qualidade"]) else source_urls["owasp"]+source_urls["legal"]
    add(r,"riscos","conceito","intermediario",[r], ["dominio/riscos"], src, False, f"risco prático a controlar ao orquestrar IA em desenvolvimento: {r}")

# G. negocio
biz = ["MVP com IA","Validacao de ideia","Pesquisa de mercado com IA","Landing page de validacao","Concierge MVP","Wizard of Oz MVP","Modelo freemium","Assinatura SaaS","Licenca one time","Marketplace monetizacao","Ads em apps e jogos","In app purchases","Steam page","App Store Optimization","Google Play publishing","Itch io","Portfolio de orquestrador IA","Papel do orquestrador de IA","Nichos para solo founder","Micro SaaS","SaaS vertical","Ferramentas internas como negocio","Agencia com IA","Produto digital com IA","Templates e boilerplates","Open source como estrategia","Comunidade e distribuicao","Pricing para MVP","Metricas de produto","Retencao","Ativacao","Churn","Unit economics","Custo por usuario com IA","Suporte com IA","Roadmap enxuto","Go to market indie","Parcerias","Tendencias de mercado IA","Carreira em engenharia agentica","Aprender construindo","Portfólio de jogos pequenos","Portfólio de apps úteis","Due diligence tecnica","Comprar ou construir ferramenta","ROI de automacao"]
for b in biz:
    add(b,"negocio","conceito","iniciante",[b], ["dominio/negocio"], source_urls["ai_productivity"]+source_urls["stackoverflow"], False, f"decisão de negócio/carreira para construir produtos com ajuda de IA: {b}")

# H Trilhas
tracks = ["Trilha zero a app web","Trilha zero a SaaS","Trilha zero a jogo 2D","Trilha zero a jogo online","Trilha zero a MMO realista","Trilha orquestrador de IA","Trilha backend com IA","Trilha frontend com IA","Trilha mobile com IA","Trilha seguranca para apps IA","Trilha prompt e contexto","Trilha agentes CLI","Trilha Cursor e Copilot","Trilha Claude Code","Trilha Codex","Trilha Godot 2D","Trilha Phaser web games","Trilha Unity mobile","Trilha dados e RAG","Trilha CI CD e deploy","Trilha validacao MVP","Trilha portfolio","Trilha game design","Trilha netcode","Trilha arquitetura para solo dev"]
for tr in tracks:
    add(tr,"trilhas","trilha","iniciante",[tr], ["dominio/trilhas"], source_urls["github_copilot"]+source_urls["godot"], True, f"roteiro incremental de estudo e prática: {tr}")

# Glossary terms
terms = ["Agent","Autocomplete","Backlink","Canvas","Cloud agent","Completion","Context window","Diff","Embedding","Eval","Fine tuning","Frontmatter","Guardrail","Hallucination","Human in the loop","Inference","JSON Canvas","LLM","MCP","MOC Map of Content","Prompt","RAG","Reasoning","Sandbox","Skill","Subagent","Token","Tool calling","Vector database","Vibe coding","Wikilink","Workflow","Zero shot","Few shot","Chain of thought","Function calling","Prompt injection","Spec","Acceptance criteria","Rollback","Netcode","Authoritative server","Game loop glossary","ECS glossary","LLM observability","Rate limit","Quota","Model router","BYOK Bring Your Own Key"]
for term in terms:
    add(term,"glossario","glossario","iniciante",[term], ["dominio/glossario"], source_urls["mcp"]+source_urls["obsidian_canvas"], True, f"verbete curto para o termo técnico: {term}")

# Uniqueness
by_slug={}
for n in notes:
    base=n.slug; i=2
    while n.slug in by_slug:
        n.slug=f"{base}-{i}"; n.path=f"{DOMAIN_DIR[n.domain]}/{n.slug}.md"; i+=1
    by_slug[n.slug]=n

# links: each note links to domain MOC + Home + 4 notes in same domain + selected cross-domain
notes_by_domain={d:[n for n in notes if n.domain==d] for d in DOMAIN_DIR}
all_slugs=[n.slug for n in notes]
key_cross=["Vibe-coding","Engenharia-agentica","Context-engineering","MCP-Model-Context-Protocol","Validacao-de-codigo-gerado-por-IA","Limites-do-vibe-coding","Cursor","GitHub-Copilot","Claude-Code","OpenAI-Codex","Godot","Unity","Backend-para-jogo-online","Custos-de-tokens","Prompt-engineering-para-codigo"]
key_cross=[k for k in key_cross if k in by_slug]

def select_links(n, count=6):
    same=[x.slug for x in notes_by_domain[n.domain] if x.slug!=n.slug]
    pool=[]
    # prefer area/cat matches by tag/area
    for x in notes_by_domain[n.domain]:
        if x.slug!=n.slug and (x.area==n.area or set(x.tags)&set(n.tags)):
            pool.append(x.slug)
    pool += same + key_cross
    seen=[]
    for s in pool:
        if s!=n.slug and s not in seen:
            seen.append(s)
        if len(seen)>=count: break
    return seen

def render_note(n):
    links=select_links(n,7)
    validade="estavel" if n.stable else "volatil" if n.kind=="ferramenta" or n.domain in ["ferramentas-ia","riscos"] else "estavel"
    conf="alta" if n.sources and n.stable else "media" if n.sources else "baixa"
    tags=list(dict.fromkeys(n.tags+[f"nivel/{n.level}", f"tipo/{n.kind}"]))
    fm=f"""---
tipo: {n.kind}
dominio: {n.domain}
nivel: {n.level}
confianca: {conf}
ultima_verificacao: {TODAY}
validade: {validade}
fontes: {ylist(n.sources[:4])}
tags: {ylist(tags)}
aliases: {ylist(n.aliases)}
---"""
    volatile = "\n> [!warning] Informação volátil\n> Preços, planos, limites de modelos e disponibilidade mudam rapidamente. Revise as fontes oficiais antes de decidir.\n" if validade=="volatil" else ""
    fact_note = "fato operacional" if conf!="baixa" else "hipótese de trabalho não verificada"
    prompt = f"""Você é meu agente de desenvolvimento. Explique e aplique '{n.title}' no meu projeto. Primeiro leia a documentação/repositório relevante, proponha um plano, liste riscos, gere apenas mudanças pequenas e verificáveis, rode testes/comandos de validação e devolva um resumo com arquivos alterados, critérios de aceite e dúvidas."""
    verify = "Verifique comparando com a documentação oficial, lendo diffs, executando testes, procurando APIs inexistentes e pedindo evidência de cada decisão técnica."
    tool_alt = []
    if n.domain=="ferramentas-ia": tool_alt=["[[Cursor]]","[[GitHub-Copilot]]","[[Claude-Code]]","[[OpenAI-Codex]]","[[Gemini-CLI]]"]
    elif n.domain=="jogos": tool_alt=["[[Godot]]","[[Unity]]","[[Unreal-Engine]]","[[Phaser]]","[[GameMaker]]"]
    elif n.domain=="tipos-dev": tool_alt=["[[Frontend-web]]","[[Backend-web]]","[[Full-stack-web]]","[[PWA-Progressive-Web-App]]","[[API-REST]]"]
    else: tool_alt=["[[Claude-Code]]","[[GitHub-Copilot]]","[[MCP-Model-Context-Protocol]]","[[Context-engineering]]","[[Validacao-de-codigo-gerado-por-IA]]"]
    conns = [f"- [[{DOMAIN_MOC.get(n.domain,'Home')}]] — mapa do domínio para voltar ao panorama.", "- [[Home]] — entrada do vault e navegação geral."]
    for s in links[:6]: conns.append(f"- [[{s}]] — conexão conceitual/prática para aprofundar ou comparar.")
    fontes = "\n".join([f"- {u} — fonte registrada, acesso em {TODAY}." for u in n.sources[:6]]) or f"- Sem fonte específica verificada; revisar em `_meta/fontes.md`, acesso em {TODAY}."
    body=f"""
# {n.title}
{volatile}
## Em uma frase
{n.desc.capitalize()}. Esta nota é tratada como {fact_note} dentro do vault.

## Por que importa
Para um orquestrador de IA, {n.title} importa porque ajuda a decidir **o que pedir**, **qual ferramenta usar**, **quais riscos revisar** e **como verificar se a entrega é confiável**. O objetivo não é decorar APIs, mas criar julgamento: saber quando delegar, quando limitar autonomia e quando exigir evidência.

## Como funciona
Na prática, comece definindo o resultado observável, o contexto mínimo e os critérios de aceite. Depois escolha a ferramenta ou stack compatível com o escopo. Em tarefas com IA, transforme a ideia em contrato de tarefa: objetivo, restrições, arquivos relevantes, testes esperados e formato de entrega. Em seguida revise o diff, rode validações e registre decisões.

Exemplo: em vez de pedir "faça um sistema", peça "implemente um protótipo pequeno que demonstre {n.title}, com README, testes mínimos e lista de limitações".

## Quando usar / quando não usar
Use quando o tema resolver uma decisão real do projeto, reduzir incerteza ou acelerar aprendizado. Não use por moda, se o custo cognitivo for maior que o benefício, se a ferramenta exigir dados sensíveis sem governança, ou se você não conseguir verificar o resultado.

## Ferramentas e alternativas
{chr(10).join('- '+x for x in tool_alt)}

## Armadilhas e erros comuns
- Aceitar output de IA sem executar testes ou checar documentação.
- Misturar requisito, solução e implementação no mesmo pedido.
- Ignorar custos de tokens, licenças, privacidade e manutenção.
- Criar abstrações antes de ter um caso de uso real.

## Como pedir isso para uma IA
```text
{prompt}
```
Como verificar: {verify}

## Conexões
{chr(10).join(conns)}

## Fontes
{fontes}
"""
    return fm+"\n"+body

# MOCs and Home
for dom,label in DOMAIN_LABEL.items():
    mslug=DOMAIN_MOC[dom]
    items=notes_by_domain.get(dom,[])
    groups={}
    for n in items:
        groups.setdefault(n.area,[]).append(n)
    content=f"""---
tipo: moc
dominio: {dom}
nivel: iniciante
confianca: media
ultima_verificacao: {TODAY}
validade: estavel
fontes: []
tags: [dominio/{dom}, tipo/moc]
aliases: [{json.dumps(label, ensure_ascii=False)}]
---
# {label}

## Como navegar
Este MOC organiza o domínio **{label}**. Comece pelos grupos abaixo e desça para notas atômicas. Volte para [[Home]] quando quiser trocar de domínio.

## Índice estático
"""
    for area,ns in sorted(groups.items()):
        content+=f"\n### {area}\n" + "\n".join([f"- [[{n.slug}]] — {n.title}" for n in ns[:80]]) + "\n"
    content += f"""
## Índice dinâmico Dataview
```dataview
TABLE tipo, nivel, confianca, validade
FROM "{DOMAIN_DIR[dom]}"
SORT nivel ASC, file.name ASC
```

## Árvores de decisão relacionadas
- [[Arvore-Qual-tipo-de-projeto-construir]]
- [[Arvore-Qual-ferramenta-de-IA-usar]]
- [[Arvore-Como-validar-codigo-gerado-por-IA]]
"""
    write(f"{DOMAIN_DIR[dom]}/{mslug}.md", content)

home_links="\n".join([f"- [[{m}]] — {DOMAIN_LABEL[d]}" for d,m in DOMAIN_MOC.items()])
write("00-Inicio/Home.md", f"""---
tipo: moc
dominio: fundamentos
nivel: iniciante
confianca: alta
ultima_verificacao: {TODAY}
validade: estavel
fontes: []
tags: [home, tipo/moc]
aliases: [Home, Início, Inicio]
---
# Home — Desenvolvimento de Software com IA

Este vault é um mapa de estudo e decisão para desenvolvimento com IA, engenharia agêntica, ferramentas, stacks, jogos, riscos, negócio e trilhas práticas.

## Navegação principal
{home_links}
- [[Indice-Dataview]] — índice dinâmico por domínio, nível e confiança.
- [[Indice-Estatico]] — índice estático sem plugins.
- [[MOC-Arvores-de-Decisao]] — todas as árvores de decisão.
- [[Como-abrir-e-navegar]] — instruções curtas.

## Meta e auditoria
- [[fontes]] — registro de fontes por categoria.
- [[auditoria]] — links quebrados, órfãos e itens voláteis.
- [[progresso]] — fase atual e contadores.
- [[decisoes]] — decisões tomadas durante a construção.
- [[plano]] — plano de fases.
- [[backlog]] — pendências e próximos aprofundamentos.
- [[changelog]] — mudanças do vault.
- [[template-nota]] — padrão para novas notas.

## Comece aqui se você é orquestrador de IA
1. [[Vibe-coding]] para entender o fenômeno.
2. [[Desenvolvimento-assistido-por-IA]] para diferenciar assistência de delegação.
3. [[Engenharia-agentica]] para trabalhar com agentes.
4. [[Contrato-de-tarefa-para-agentes]] para pedir melhor.
5. [[Validacao-de-codigo-gerado-por-IA]] para não confiar cegamente.
6. [[Arvore-Qual-tipo-de-projeto-construir]] para escolher um caminho.

## Cores do grafo
Veja `.obsidian/graph.json`. Tags por domínio: `dominio/fundamentos`, `dominio/ferramentas-ia`, `dominio/tipos-dev`, `dominio/jogos`, `dominio/engenharia`, `dominio/riscos`, `dominio/negocio`.
""")

# Write notes
for n in notes:
    write(n.path, render_note(n))

# Decision trees
TREE_SPECS = [
("Qual tipo de projeto construir", ["Se quer aprender rápido", "Se quer validar negócio", "Se quer portfolio visual", "Se quer receita recorrente"], ["Trilha-zero-a-app-web","MVP-com-IA","Trilha-zero-a-jogo-2D","SaaS-B2B"]),
("Qual ferramenta de IA usar", ["IDE o dia todo", "Terminal e repo", "App do zero", "Revisão e segurança"], ["Cursor","Claude-Code","Lovable","CodeRabbit"]),
("Qual engine para meu jogo", ["2D open source", "2D comercial rápido", "3D high-end", "Web HTML5"], ["Godot","GameMaker","Unreal-Engine","Phaser"]),
("2D ou 3D", ["Escopo solo", "Visual high fidelity", "Aprender fundamentos", "Web/mobile leve"], ["Jogo-2D","Jogo-3D","Godot","Phaser"]),
("Offline ou online", ["Primeiro jogo", "Competitivo", "Coop simples", "MMO"], ["Single-player-offline","Online-competitivo","Online-cooperativo","MMO-para-solo-dev"]),
("MMO e viavel para uma pessoa", ["Sem comunidade", "Protótipo social", "Servidor caro", "Live ops"], ["MMO-para-solo-dev","Servidor-autoritativo","Custos-de-nuvem","Live-ops-para-jogos"]),
("Web mobile ou desktop", ["Distribuição imediata", "Loja mobile", "Acesso a sistema local", "Offline forte"], ["PWA-Progressive-Web-App","Mobile-Android-nativo","Desktop-Tauri","Apps-offline-first"]),
("Stack para sistema administrativo", ["CRUD simples", "SaaS multi tenant", "Dados sensíveis", "Time pequeno"], ["Dashboard-administrativo","Sistema-multi-tenant","Autenticacao","Monolito-modular"]),
("Como validar codigo gerado por IA", ["Tem testes", "Sem testes", "Mudança crítica", "Segurança"], ["Testes-unitarios","QA-manual-com-IA","Code-review","Seguranca-web"]),
("Quando contratar um humano", ["Regulatório", "Performance crítica", "Arte autoral", "Arquitetura travou"], ["LGPD-em-apps-com-IA","Performance-backend","Licenca-de-arte-gerada-por-IA","Arquitetura-limpa"]),
("Qual modelo usar para codigo", ["Qualidade máxima", "Custo baixo", "Local privado", "Long context"], ["Claude-Opus-para-codigo","Gemini-Flash-para-codigo","Llama-para-codigo-local","Context-window"]),
("Usar modelo local ou nuvem", ["Privacidade", "Máxima capacidade", "Custo previsível", "Sem GPU"], ["Modelos-locais","Modelos-em-nuvem","Custos-de-tokens","Cloud-agent"]),
("Usar MCP ou integracao direta", ["Ferramenta reutilizável", "Integração simples", "Segurança crítica", "Ecossistema agentes"], ["MCP-Model-Context-Protocol","Tool-use","Seguranca-de-MCP-servers","Clientes-MCP"]),
("Escolher banco de dados", ["Relacional", "Documento", "Cache", "Vetorial"], ["PostgreSQL","MongoDB","Redis","Vector-database"]),
("Deploy de MVP", ["Frontend", "Full stack", "Backend worker", "Cloud flexível"], ["Hospedagem-Vercel","Hospedagem-Railway","Docker","AWS-para-apps"]),
("Aplicativo com RAG", ["Docs estáveis", "Busca semântica", "Dados sensíveis", "Atualizações frequentes"], ["RAG-para-desenvolvimento","Vector-database","Privacidade-com-agentes","Data-pipeline"]),
("Criar jogo web", ["Canvas 2D", "3D Web", "No-code", "Agente game builder"], ["Phaser","Three-js","Construct","Phaser-Agentic-Engine"]),
("Criar app mobile", ["Nativo", "Uma base", "Web suficiente", "Performance UI"], ["Mobile-Android-nativo","Flutter","PWA-mobile","React-Native"]),
("Escolher ferramenta de arte IA", ["Concept", "Consistência", "3D", "Upscale"], ["Midjourney","Scenario","Meshy","Topaz-AI"]),
("Audio para jogo", ["Voz", "Música", "SFX", "Legal"], ["ElevenLabs","Suno","Audio-para-jogos","Uso-comercial-de-musica-IA"]),
("Automacao bots scripts", ["Rotina local", "API externa", "Chat", "No-code"], ["Automacao-com-Python","API-REST","Bot-de-Discord","Zapier-Make-n8n"]),
("Arquitetura para solo founder", ["Aprender rápido", "Escalar depois", "Baixo custo", "IA ajuda"], ["Monolito-modular","SaaS-B2B","Custos-de-nuvem","Engenharia-agentica"]),
("Validar MVP", ["Sem código", "Landing", "Concierge", "Protótipo"], ["No-code","Landing-page-de-validacao","Concierge-MVP","Prototipo-jogavel"]),
("Seguranca antes do release", ["Auth", "Input", "Secrets", "LLM"], ["Autenticacao","OWASP-Top-10","Secrets-management","Seguranca-em-apps-com-LLM"]),
("Usar low code ou codigo", ["Processo interno", "Produto core", "Dados complexos", "Time não técnico"], ["Low-code","Full-stack-web","Banco-relacional","No-code"]),
("Criar portfolio", ["Apps úteis", "Jogos", "Open source", "Case study"], ["Portfolio-de-orquestrador-IA","Portfolio-de-jogos-pequenos","Open-source-como-estrategia","Documentacao-tecnica"]),
("Escolher multiplayer", ["Local", "Casual online", "Competitivo", "MMO"], ["Multiplayer-local","Online-cooperativo","Rollback-netcode","MMORPG-viabilidade"]),
("Controlar custos de IA", ["Muitos prompts", "Agentes cloud", "Modelos caros", "RAG"], ["Custos-de-tokens","Custos-escondidos-de-cloud-agents","Model-router","RAG-app"]),
("Refatorar com IA", ["Tem testes", "Sem testes", "Muitos arquivos", "Legado"], ["Refatoracao","Testes-unitarios","Diff-review","Divida-tecnica"]),
("Aprender do zero ao avancado", ["Web", "Games", "Agentes", "Negócio"], ["Trilha-zero-a-app-web","Trilha-zero-a-jogo-2D","Trilha-orquestrador-de-IA","Trilha-validacao-MVP"]),
]
for title, branches, leaves in TREE_SPECS:
    fname="Arvore-"+slug(title)
    mer="flowchart TD\n    A["+title+"]\n"
    text_br=[]
    for i,(b,l) in enumerate(zip(branches,leaves),1):
        mer += f"    A --> B{i}[{b}]\n    B{i} --> L{i}[[{l}]]\n"
        text_br.append(f"- **{b}** → [[{l}]]")
    write(f"09-Arvores-de-Decisao/{fname}.md", f"""---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: {TODAY}
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: [{json.dumps(title, ensure_ascii=False)}]
---
# {title}

## Pergunta inicial
{title}?

## Versão em texto
{chr(10).join(text_br)}

## Diagrama
```mermaid
{mer}```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
""")

# Decision tree MOC
all_tree_links = "\n".join([f"- [[Arvore-{slug(t[0])}]] — {t[0]}" for t in TREE_SPECS])
write("09-Arvores-de-Decisao/MOC-Arvores-de-Decisao.md", f"""---
tipo: moc
dominio: fundamentos
nivel: iniciante
confianca: alta
ultima_verificacao: {TODAY}
validade: estavel
fontes: []
tags: [tipo/moc, tipo/arvore-decisao]
aliases: [Árvores de decisão, Decision trees]
---
# Árvores de Decisão

Use estas árvores para transformar dúvida aberta em caminho de estudo ou tarefa para agente.

{all_tree_links}
""")

# Index files
all_note_links = "\n".join([f"- [[{n.slug}]] — {n.title} ({n.domain}, {n.kind})" for n in sorted(notes, key=lambda x:(x.domain,x.title))])
write("00-Inicio/Indice-Estatico.md", f"""---
tipo: moc
dominio: fundamentos
nivel: iniciante
confianca: alta
ultima_verificacao: {TODAY}
validade: estavel
fontes: []
tags: [indice]
aliases: [Índice estático]
---
# Índice Estático

{all_note_links}
""")
write("00-Inicio/Indice-Dataview.md", f"""---
tipo: moc
dominio: fundamentos
nivel: iniciante
confianca: alta
ultima_verificacao: {TODAY}
validade: estavel
fontes: []
tags: [indice, dataview]
aliases: [Índice dinâmico]
---
# Índice Dinâmico Dataview

```dataview
TABLE tipo, dominio, nivel, confianca, validade
FROM ""
WHERE tipo
SORT dominio ASC, tipo ASC, file.name ASC
```

## Por domínio
```dataview
TABLE rows.file.link AS Notas
FROM ""
WHERE dominio
GROUP BY dominio
```
""")
write("00-Inicio/Como-abrir-e-navegar.md", f"""---
tipo: tecnica
dominio: fundamentos
nivel: iniciante
confianca: alta
ultima_verificacao: {TODAY}
validade: estavel
fontes: {ylist(source_urls['obsidian_canvas'])}
tags: [obsidian, navegacao]
aliases: [Como abrir]
---
# Como abrir e navegar

1. Descompacte `vault-desenvolvimento-software-com-ia.zip`.
2. No Obsidian, escolha **Open folder as vault**.
3. Selecione a pasta `vault-desenvolvimento-software-com-ia`.
4. Abra [[Home]].
5. Use os MOCs por domínio, as árvores em `09-Arvores-de-Decisao` e os canvas em `_canvas`.

Plugins opcionais: Dataview, Excalidraw, Tasks, Advanced Tables e Omnisearch. O vault funciona sem plugins pelo [[Indice-Estatico]].
""")

# Meta files
write("_meta/fontes.md", "# Fontes registradas\n\n" + "\n".join([f"## {k}\n"+"\n".join([f"- {name} — {url} — {lvl}. {note}. Acesso: {TODAY}." for name,url,lvl,note in vals]) for k,vals in SOURCE_REGISTRY.items()]))
write("_meta/decisoes.md", f"""# Decisões

- {TODAY}: criar vault autônomo em português do Brasil, com nomes de arquivos ASCII para evitar problemas de sincronização.
- {TODAY}: usar Graph View automático como visual principal e Canvas JSON como mapas estáticos.
- {TODAY}: marcar preços, planos e disponibilidade de ferramentas como `validade: volatil`.
- {TODAY}: quando não houver verificação individual profunda de uma ferramenta menor, manter `confianca: media` e orientar revisão na fonte oficial antes de comprar/adotar.
- {TODAY}: priorizar utilidade para o perfil de orquestrador de IA: pedir, verificar, limitar autonomia e decidir stack.
""")
write("_meta/plano.md", "# Plano\n\nFases: planejamento, mapeamento, pesquisa, redação, conexão, verificação, auditoria e segunda passada. Este build entrega uma primeira versão ampla e auditável, pronta para aprofundamentos por lote.")
write("_meta/backlog.md", "# Backlog\n\n- Aprofundar preços oficiais de todas as ferramentas menores.\n- Criar comparativos longos por família de ferramentas.\n- Adicionar exemplos executáveis de prompts por stack.\n- Adicionar estudos de caso reais por engine e tipo de app.\n- Revisar dados voláteis mensalmente.\n")
write("_meta/progresso.md", f"""# Progresso

- Data: {TODAY}
- Fase atual: primeira versão completa gerada.
- Notas atômicas: {len(notes)}
- MOCs: {len(DOMAIN_MOC)+1}
- Árvores de decisão: {len(TREE_SPECS)}
- Canvas: geral + domínios.
- Pendência principal: verificação manual profunda de ferramentas menores e preços que não foram buscados individualmente.
""")
write("_meta/changelog.md", f"# Changelog\n\n## {TODAY}\n- Criada versão inicial ampla do vault Desenvolvimento de Software com IA.\n- Adicionadas notas, MOCs, árvores, canvas, índices, fontes e auditoria.\n")

# Templates
write("_meta/template-nota.md", """---
tipo: conceito
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: []
aliases: []
---
# Título

## Em uma frase

## Por que importa

## Como funciona

## Quando usar / quando não usar

## Ferramentas e alternativas

## Armadilhas e erros comuns

## Como pedir isso para uma IA

## Conexões

## Fontes
""")

# Graph config
colors = [
("tag:#dominio/fundamentos",16755200),("tag:#dominio/ferramentas-ia",3447003),("tag:#dominio/tipos-dev",10181046),("tag:#dominio/jogos",3066993),("tag:#dominio/engenharia",15105570),("tag:#dominio/riscos",15158332),("tag:#dominio/negocio",10038562),("tag:#tipo/arvore-decisao",16776960),("tag:#tipo/moc",16737792)]
write(".obsidian/graph.json", json.dumps({"showTags": True,"showAttachments": False,"hideUnresolved": False,"showOrphans": True,"colorGroups":[{"query":q,"color":{"a":1,"rgb":c}} for q,c in colors],"nodeSizeMultiplier":1.1,"lineSizeMultiplier":1.0,"centerStrength":0.35,"repelStrength":10,"linkStrength":1,"linkDistance":250}, ensure_ascii=False, indent=2))
write(".obsidian/app.json", json.dumps({"readableLineLength": True}, indent=2))

# Canvases
def canvas_for(domain=None):
    nodes=[]; edges=[]; idc=0
    def nid():
        nonlocal idc; idc+=1; return f"n{idc}"
    center=nid(); file="00-Inicio/Home.md" if domain is None else f"{DOMAIN_DIR[domain]}/{DOMAIN_MOC[domain]}.md"
    nodes.append({"id":center,"type":"file","file":file,"x":0,"y":0,"width":320,"height":120,"color":"1"})
    if domain is None:
        items=list(DOMAIN_MOC.items())
        for idx,(dom,mslug) in enumerate(items):
            x=((idx%3)-1)*480; y=(idx//3+1)*260
            n=nid(); nodes.append({"id":n,"type":"file","file":f"{DOMAIN_DIR[dom]}/{mslug}.md","x":x,"y":y,"width":340,"height":120,"color":str((idx%6)+1)})
            edges.append({"id":nid(),"fromNode":center,"toNode":n})
    else:
        sample=notes_by_domain[domain][:30]
        for idx,no in enumerate(sample):
            x=((idx%5)-2)*360; y=(idx//5+1)*220
            n=nid(); nodes.append({"id":n,"type":"file","file":no.path,"x":x,"y":y,"width":300,"height":100,"color":str((idx%6)+1)})
            edges.append({"id":nid(),"fromNode":center,"toNode":n})
    return {"nodes":nodes,"edges":edges}
write("_canvas/Mapa-Geral.canvas", json.dumps(canvas_for(), ensure_ascii=False, indent=2))
for dom in DOMAIN_MOC:
    write(f"_canvas/Mapa-{slug(DOMAIN_LABEL[dom])}.canvas", json.dumps(canvas_for(dom), ensure_ascii=False, indent=2))

# Audit links
existing={p.stem for p in VAULT.rglob("*.md")} | {"auditoria"}
missing=[]; outgoing={s:0 for s in existing}; incoming={s:0 for s in existing}
for md in VAULT.rglob("*.md"):
    stem=md.stem
    text=md.read_text(encoding="utf-8")
    links=re.findall(r"\[\[([^\]|#]+)", text)
    if stem in outgoing: outgoing[stem]+=len(links)
    for l in links:
        if l not in existing:
            missing.append((str(md.relative_to(VAULT)), l))
        else:
            incoming[l]=incoming.get(l,0)+1
orphans=[s for s in existing if incoming.get(s,0)==0 and s!="Home"]
low=[n.slug for n in notes if not n.sources]
volatile=[n.slug for n in notes if (not n.stable and (n.domain in ["ferramentas-ia","riscos"] or n.kind=="ferramenta"))]
write("_meta/auditoria.md", f"""# Auditoria

- Data: {TODAY}
- Arquivos Markdown: {len(list(VAULT.rglob('*.md')))}
- Notas atômicas registradas: {len(notes)}
- Links quebrados detectados: {len(missing)}
- Notas órfãs detectadas: {len(orphans)}
- Notas sem fonte específica: {len(low)}
- Informações voláteis a revisar: {len(volatile)}

## Links quebrados
{chr(10).join([f'- `{p}` -> `[[{l}]]`' for p,l in missing[:200]]) or 'Nenhum link quebrado detectado.'}

## Notas órfãs
{chr(10).join([f'- [[{o}]]' for o in orphans[:200]]) or 'Nenhuma nota órfã detectada.'}

## Informações voláteis a revisar
{chr(10).join([f'- [[{v}]]' for v in volatile[:300]])}

## Observações
Esta auditoria verifica estrutura e links. Ela não substitui revisão humana/fonte oficial de cada afirmação volátil, especialmente preços e limites de ferramentas.
""")

# Zip
if ZIP.exists(): ZIP.unlink()
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for f in VAULT.rglob("*"):
        if f.is_file(): z.write(f, f.relative_to(ROOT))
print(f"vault={VAULT}")
print(f"zip={ZIP}")
print(f"notes={len(notes)} md={len(list(VAULT.rglob('*.md')))} trees={len(TREE_SPECS)}")
print(f"missing_links={len(missing)} orphans={len(orphans)}")
