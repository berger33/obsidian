from pathlib import Path
import json
import shutil
import zipfile
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "obsidian-vault-piloto"
ZIP_PATH = ROOT / "obsidian-vault-piloto.zip"

if VAULT.exists():
    shutil.rmtree(VAULT)
VAULT.mkdir(parents=True)

for p in [
    "00-Mapas",
    "01-Notas",
    "90-Sistema/Templates",
    "automation",
    ".obsidian",
]:
    (VAULT / p).mkdir(parents=True, exist_ok=True)

notes = {
    "Requisitos jogáveis": {
        "tags": ["software", "jogos2d", "ponte", "requisitos"],
        "camada": "ponte",
        "moc": "MOC - Índice Geral",
        "resumo": "Transforma objetivos de produto em comportamentos observáveis dentro do jogo, evitando requisitos abstratos demais para orientar implementação.",
        "pergunta": "Como converter uma ideia de jogo em critérios testáveis dentro de uma cena, fase ou protótipo?",
        "definicao": "Requisitos jogáveis são declarações de comportamento que podem ser experimentadas, gravadas, testadas ou validadas por um jogador ou desenvolvedor. Em vez de 'o combate deve ser divertido', usa-se 'o inimigo avança, telegrava o ataque por 0,4 s e recua se o jogador contra-atacar'.",
        "quando": ["Ao iniciar um protótipo.", "Ao escrever histórias de usuário para sistemas de gameplay.", "Ao decidir se uma mecânica está pronta para ser integrada."],
        "sinais": ["Critérios de aceitação podem ser demonstrados em uma cena.", "A nota se conecta tanto a produto quanto a implementação.", "Há exemplos de inputs, estados e feedbacks esperados."],
        "links": ["Prototipagem jogável", "Game loop", "Estado do jogo", "Testes automatizados", "Level design 2D"]
    },
    "Modelagem de domínio": {
        "tags": ["software", "arquitetura", "dominio"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Organiza conceitos, regras e vocabulário do problema antes de escolher frameworks ou estruturas de código.",
        "pergunta": "Quais objetos, regras e eventos existem no problema independentemente da tecnologia?",
        "definicao": "Modelagem de domínio é a prática de representar entidades, valores, eventos, políticas e invariantes do negócio ou do sistema. Em jogos 2D, o domínio pode incluir jogador, inimigo, dano, inventário, fase, checkpoint e progressão.",
        "quando": ["Quando o código começa a refletir nomes confusos.", "Antes de separar módulos.", "Ao criar sistemas de jogo com regras complexas."],
        "sinais": ["Os nomes do código batem com os nomes usados pela equipe.", "Regras importantes ficam perto dos conceitos que protegem.", "A arquitetura fica menos dependente de detalhes de engine."],
        "links": ["Arquitetura hexagonal", "Estado do jogo", "Sistema de inventário", "Coesão e acoplamento", "Documentação viva"]
    },
    "Coesão e acoplamento": {
        "tags": ["software", "arquitetura", "qualidade"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Critério central para decidir se uma parte do sistema deve ficar junto ou separada.",
        "pergunta": "O que muda junto deve morar junto? O que muda por motivos diferentes está separado?",
        "definicao": "Coesão mede o quanto os elementos de um módulo pertencem ao mesmo propósito. Acoplamento mede o quanto um módulo depende de detalhes de outro. Bons sistemas têm alta coesão e baixo acoplamento intencional.",
        "quando": ["Ao refatorar classes grandes.", "Ao criar sistemas independentes de gameplay.", "Ao avaliar fronteiras entre módulos."],
        "sinais": ["Mudanças pequenas não atravessam muitas pastas.", "Dependências apontam para abstrações estáveis.", "O grafo de notas mostra clusters claros, não um centro único inchado."],
        "links": ["Monólito modular", "Arquitetura em camadas", "ECS", "Refatoração", "Dívida técnica"]
    },
    "SOLID com pragmatismo": {
        "tags": ["software", "design", "qualidade"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Usa princípios de design como heurísticas, não como religião arquitetural.",
        "pergunta": "Qual princípio reduz mudança dolorosa sem adicionar abstração prematura?",
        "definicao": "SOLID é um conjunto de princípios para orientar responsabilidade, extensão, substituição, interfaces e dependências. Em projetos pequenos ou jogos, o valor está em perceber tensão de mudança, não em criar camadas para tudo.",
        "quando": ["Quando uma classe tem motivos demais para mudar.", "Quando uma interface cresce sem necessidade.", "Quando testes ficam difíceis por dependências concretas."],
        "sinais": ["Abstrações aparecem depois de repetição real.", "A leitura do código melhora.", "O princípio escolhido resolve uma dor específica."],
        "links": ["Coesão e acoplamento", "Refatoração", "Testes automatizados", "Arquitetura hexagonal", "Monólito modular"]
    },
    "Testes automatizados": {
        "tags": ["software", "qualidade", "automacao"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Protegem comportamento importante e permitem mudar o sistema com menos medo.",
        "pergunta": "Que comportamento precisa continuar verdadeiro quando a implementação mudar?",
        "definicao": "Testes automatizados executam verificações repetíveis sobre unidades, integrações, regras de domínio, cenas ou simulações. Em jogos, testes podem validar dano, colisão, inventário, carregamento de fase e estados do personagem.",
        "quando": ["Quando uma regra é crítica.", "Quando bugs voltam após correções.", "Antes de refatorar sistemas centrais."],
        "sinais": ["O teste descreve comportamento, não implementação acidental.", "Falhas apontam para uma regra quebrada.", "A suíte roda rápido o bastante para ser usada diariamente."],
        "links": ["CI-CD", "Refatoração", "Requisitos jogáveis", "Sistemas determinísticos", "Estado do jogo"]
    },
    "Refatoração": {
        "tags": ["software", "qualidade", "evolucao"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Melhora a estrutura interna sem alterar o comportamento observável.",
        "pergunta": "Como tornar a próxima mudança mais barata mantendo o jogo funcionando?",
        "definicao": "Refatoração é mudança estrutural guiada por segurança. Ela remove duplicação, explicita conceitos, melhora nomes e separa responsabilidades, idealmente apoiada por testes e pequenos commits.",
        "quando": ["Antes de adicionar uma variação complexa.", "Quando um módulo acumula exceções.", "Quando o custo de entender supera o custo de mudar."],
        "sinais": ["O comportamento final é igual.", "Os nomes ficam mais próximos do domínio.", "A alteração reduz caminhos alternativos e casos especiais."],
        "links": ["Testes automatizados", "Coesão e acoplamento", "Dívida técnica", "SOLID com pragmatismo", "Documentação viva"]
    },
    "CI-CD": {
        "tags": ["software", "automacao", "entrega"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Automatiza validação e entrega para reduzir risco acumulado entre mudanças e builds.",
        "pergunta": "O que deve ser verificado automaticamente antes de uma mudança virar build jogável?",
        "definicao": "CI/CD combina integração contínua, testes, empacotamento e distribuição. Para jogos 2D, pode gerar builds por plataforma, rodar testes de lógica e publicar protótipos para playtest.",
        "quando": ["Quando builds manuais começam a falhar por esquecimento.", "Quando há mais de uma pessoa no projeto.", "Quando playtests precisam de versões frequentes."],
        "sinais": ["Builds são reproduzíveis.", "Erros aparecem perto da mudança que os causou.", "Existe histórico claro de versões."],
        "links": ["Testes automatizados", "Observabilidade", "Prototipagem jogável", "Pipeline de assets", "Documentação viva"]
    },
    "Observabilidade": {
        "tags": ["software", "operacao", "qualidade"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Permite entender o comportamento real do sistema por logs, métricas, traces ou telemetria.",
        "pergunta": "Quando algo dá errado, que sinais mostram onde e por quê?",
        "definicao": "Observabilidade é a capacidade de fazer perguntas novas sobre o sistema sem precisar lançar uma versão especial para depuração. Em jogos, se aproxima de telemetria de sessões, eventos de erro, funis e métricas de performance.",
        "quando": ["Quando bugs só aparecem em máquinas específicas.", "Quando playtests geram dúvidas de comportamento.", "Quando performance precisa ser acompanhada."],
        "sinais": ["Eventos têm contexto suficiente.", "Métricas influenciam decisões de produto.", "Logs não expõem dados sensíveis nem viram ruído."],
        "links": ["Telemetria em jogos", "Performance em jogos 2D", "CI-CD", "Documentação viva", "Dívida técnica"]
    },
    "Documentação viva": {
        "tags": ["software", "conhecimento", "obsidian"],
        "camada": "software",
        "moc": "MOC - Engenharia de Software",
        "resumo": "Mantém conhecimento útil conectado às decisões, ao código e aos problemas atuais.",
        "pergunta": "Qual conhecimento precisa sobreviver à memória da equipe?",
        "definicao": "Documentação viva é documentação que muda junto com o sistema. Ela evita páginas mortas ao priorizar notas curtas, links, decisões arquiteturais, exemplos executáveis e mapas de conteúdo.",
        "quando": ["Quando decisões se perdem no chat.", "Quando onboardings repetem as mesmas explicações.", "Quando o grafo de conhecimento precisa orientar pesquisa."],
        "sinais": ["Notas citam decisões e contexto.", "MOCs revelam lacunas.", "O grafo mostra clusters úteis e pontes explícitas."],
        "links": ["Registro de decisões arquiteturais", "Modelagem de domínio", "MOC - Índice Geral", "Refatoração", "CI-CD"]
    },
    "Monólito modular": {
        "tags": ["arquitetura", "software", "modularidade"],
        "camada": "arquitetura",
        "moc": "MOC - Arquitetura de Software",
        "resumo": "Mantém um deploy simples com módulos internos bem definidos e fronteiras explícitas.",
        "pergunta": "Como ganhar modularidade sem pagar cedo o custo de distribuição?",
        "definicao": "Monólito modular é uma arquitetura em que o sistema roda como uma unidade, mas o código é dividido por módulos coesos. É uma escolha forte para produtos em evolução e jogos com ferramentas internas.",
        "quando": ["Quando microserviços seriam complexidade prematura.", "Quando o time é pequeno.", "Quando fronteiras de domínio ainda estão amadurecendo."],
        "sinais": ["Módulos têm APIs internas claras.", "Dependências entre módulos são visíveis.", "É possível extrair partes depois, se houver necessidade real."],
        "links": ["Coesão e acoplamento", "Arquitetura em camadas", "Arquitetura hexagonal", "Ferramentas internas", "Dívida técnica"]
    },
    "Arquitetura em camadas": {
        "tags": ["arquitetura", "software", "padroes"],
        "camada": "arquitetura",
        "moc": "MOC - Arquitetura de Software",
        "resumo": "Organiza responsabilidades em níveis, normalmente interface, aplicação, domínio e infraestrutura.",
        "pergunta": "Quais dependências devem apontar para dentro e quais detalhes podem ficar nas bordas?",
        "definicao": "Arquitetura em camadas separa apresentação, orquestração, regras e infraestrutura. Ela é simples de explicar, mas pode virar rigidez se cada mudança pequena atravessar camadas sem valor claro.",
        "quando": ["Quando o sistema precisa separar UI, regras e persistência.", "Quando há muita lógica misturada com interface.", "Quando o time precisa de uma convenção inicial."],
        "sinais": ["Cada camada tem motivo de mudança distinto.", "O domínio não depende de frameworks.", "A regra não fica escondida em callbacks de UI."],
        "links": ["Arquitetura hexagonal", "Monólito modular", "Coesão e acoplamento", "Estado do jogo", "Sistema de save"]
    },
    "Arquitetura hexagonal": {
        "tags": ["arquitetura", "software", "padroes"],
        "camada": "arquitetura",
        "moc": "MOC - Arquitetura de Software",
        "resumo": "Protege regras centrais de detalhes externos por portas e adaptadores.",
        "pergunta": "Como testar regras sem depender de banco, engine, rede ou UI?",
        "definicao": "A arquitetura hexagonal coloca o domínio e os casos de uso no centro. Entradas e saídas passam por portas, e detalhes como engine, armazenamento e APIs ficam em adaptadores substituíveis.",
        "quando": ["Quando regras importantes precisam de testes rápidos.", "Quando detalhes externos mudam com frequência.", "Quando a lógica está presa demais à engine."],
        "sinais": ["Casos de uso podem rodar fora da interface.", "Adaptadores dependem do centro, não o contrário.", "Mocks e fakes ficam naturais."],
        "links": ["Modelagem de domínio", "Testes automatizados", "Arquitetura em camadas", "Sistema de save", "Ferramentas internas"]
    },
    "Event-driven": {
        "tags": ["arquitetura", "eventos", "software"],
        "camada": "arquitetura",
        "moc": "MOC - Arquitetura de Software",
        "resumo": "Usa eventos para desacoplar produtores e consumidores de mudanças relevantes no sistema.",
        "pergunta": "Quais fatos do sistema interessam a mais de uma parte?",
        "definicao": "Arquitetura orientada a eventos organiza comunicação por fatos: inimigo derrotado, item coletado, fase concluída, build publicada. Isso reduz dependências diretas, mas exige cuidado com ordem, rastreabilidade e excesso de eventos.",
        "quando": ["Quando múltiplos sistemas reagem ao mesmo fato.", "Quando módulos não devem se conhecer diretamente.", "Quando telemetria e conquistas observam gameplay."],
        "sinais": ["Eventos são nomeados como fatos passados.", "Consumidores são independentes.", "Fluxos críticos ainda são rastreáveis."],
        "links": ["Estado do jogo", "Telemetria em jogos", "CQRS", "Sistema de conquistas", "Coesão e acoplamento"]
    },
    "CQRS": {
        "tags": ["arquitetura", "padroes", "software"],
        "camada": "arquitetura",
        "moc": "MOC - Arquitetura de Software",
        "resumo": "Separa comandos que mudam estado de consultas que leem estado.",
        "pergunta": "Leitura e escrita têm necessidades tão diferentes que merecem modelos separados?",
        "definicao": "CQRS divide operações de escrita e leitura. Em jogos, a ideia aparece quando a simulação muda estado por comandos, enquanto HUD, debug e telemetria leem projeções simplificadas.",
        "quando": ["Quando leitura e escrita têm modelos conflitantes.", "Quando projeções de UI ficam complexas.", "Quando eventos alimentam visões derivadas."],
        "sinais": ["Comandos expressam intenção.", "Consultas não mudam estado.", "A separação reduz complexidade, não aumenta por moda."],
        "links": ["Event-driven", "Estado do jogo", "Sistemas determinísticos", "Arquitetura hexagonal", "Telemetria em jogos"]
    },
    "Registro de decisões arquiteturais": {
        "tags": ["arquitetura", "conhecimento", "adr"],
        "camada": "arquitetura",
        "moc": "MOC - Arquitetura de Software",
        "resumo": "Captura contexto, decisão e consequências para evitar rediscutir escolhas sem memória.",
        "pergunta": "Que escolha importante precisa ser compreendida por alguém no futuro?",
        "definicao": "Um ADR registra uma decisão arquitetural com data, contexto, opções, decisão e consequências. É pequeno, versionável e conectado a notas conceituais no Obsidian.",
        "quando": ["Quando há trade-offs reais.", "Quando uma escolha limita escolhas futuras.", "Quando o time muda de ideia com frequência por falta de histórico."],
        "sinais": ["A decisão tem alternativas rejeitadas.", "As consequências são honestas.", "A nota aponta para conceitos envolvidos."],
        "links": ["Documentação viva", "Dívida técnica", "Monólito modular", "Arquitetura hexagonal", "Pipeline de assets"]
    },
    "Dívida técnica": {
        "tags": ["software", "arquitetura", "evolucao"],
        "camada": "ponte",
        "moc": "MOC - Índice Geral",
        "resumo": "Representa custo futuro assumido conscientemente ou acumulado por pressão, desconhecimento ou negligência.",
        "pergunta": "Que decisão está tornando mudanças futuras mais caras?",
        "definicao": "Dívida técnica é uma metáfora para compromissos estruturais que geram juros. Nem toda dívida é ruim: protótipos podem assumir atalhos para aprender rápido, desde que a dívida seja visível e gerenciada.",
        "quando": ["Quando o time evita tocar em uma área.", "Quando bugs se acumulam em torno do mesmo módulo.", "Quando atalhos de protótipo viram base permanente."],
        "sinais": ["Existe dono e prazo de revisão.", "A dívida está ligada a uma decisão concreta.", "O custo de manter já aparece em mudanças reais."],
        "links": ["Refatoração", "Registro de decisões arquiteturais", "Prototipagem jogável", "Coesão e acoplamento", "Performance em jogos 2D"]
    },
    "Game loop": {
        "tags": ["jogos2d", "gameplay", "fundamentos"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Ciclo central que processa entrada, atualiza estado e desenha frames.",
        "pergunta": "Em que ordem o jogo lê, simula, resolve e renderiza?",
        "definicao": "O game loop é a repetição contínua que mantém o jogo vivo. Ele recebe inputs, atualiza lógica, aplica física, resolve eventos, toca áudio e renderiza. Suas decisões afetam sensação, determinismo e performance.",
        "quando": ["Ao escolher timestep fixo ou variável.", "Ao depurar bugs que dependem de FPS.", "Ao organizar sistemas de gameplay."],
        "sinais": ["A ordem de atualização é explícita.", "Sistemas críticos não dependem de FPS acidental.", "Renderização e simulação têm responsabilidades separadas."],
        "links": ["Sistemas determinísticos", "Estado do jogo", "Colisão 2D", "Performance em jogos 2D", "Requisitos jogáveis"]
    },
    "Estado do jogo": {
        "tags": ["jogos2d", "arquitetura", "gameplay"],
        "camada": "ponte",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Conjunto de dados que representa a situação atual da partida, fase, menus e progressão.",
        "pergunta": "Onde mora a verdade sobre o que está acontecendo no jogo?",
        "definicao": "Estado do jogo inclui posição, vida, inventário, flags, fase atual, pausa, diálogo e progressão. O desenho arquitetural deve deixar claro quem pode ler, alterar, salvar e observar esse estado.",
        "quando": ["Quando bugs surgem por duplicação de informação.", "Quando menus, HUD e gameplay discordam.", "Quando o save precisa restaurar uma sessão."],
        "sinais": ["Há uma fonte de verdade clara.", "Transições de estado são nomeadas.", "UI observa o estado sem dominar as regras."],
        "links": ["Game loop", "Sistema de save", "Event-driven", "CQRS", "Modelagem de domínio"]
    },
    "ECS": {
        "tags": ["jogos2d", "arquitetura", "padroes"],
        "camada": "ponte",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Organiza entidades por composição de componentes e sistemas, favorecendo flexibilidade e performance em certos contextos.",
        "pergunta": "O comportamento deve nascer de hierarquias de classes ou da combinação de componentes?",
        "definicao": "Entity Component System separa identidade, dados e processamento. Entidades são IDs, componentes guardam dados e sistemas processam conjuntos de componentes. É poderoso, mas pode ser excesso para projetos simples.",
        "quando": ["Quando há muitas entidades similares com combinações variadas.", "Quando composição supera herança.", "Quando performance de processamento em lote importa."],
        "sinais": ["Componentes são dados simples.", "Sistemas têm responsabilidade clara.", "A arquitetura não sacrifica legibilidade sem ganho real."],
        "links": ["Coesão e acoplamento", "Game loop", "Sistemas determinísticos", "IA de inimigos 2D", "Colisão 2D"]
    },
    "Tilemaps": {
        "tags": ["jogos2d", "leveldesign", "renderizacao"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Representam cenários por blocos reutilizáveis, facilitando produção de fases e colisões discretas.",
        "pergunta": "O mundo 2D é melhor descrito por grade, objetos livres ou uma mistura?",
        "definicao": "Tilemaps usam tiles em uma grade para construir ambientes. Eles reduzem custo de arte, simplificam colisão e permitem ferramentas de level design, mas podem gerar repetição visual se mal usados.",
        "quando": ["Em platformers, RPGs, puzzles e metroidvanias.", "Quando fases precisam ser editadas rápido.", "Quando colisões podem seguir uma grade."],
        "sinais": ["Tiles têm semântica clara.", "Camadas separam visual, colisão e decoração.", "O pipeline permite variações sem retrabalho."],
        "links": ["Level design 2D", "Pipeline de assets", "Colisão 2D", "Renderização 2D", "Pathfinding 2D"]
    },
    "Sprites e atlases": {
        "tags": ["jogos2d", "arte", "performance"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Sprites são imagens 2D; atlases agrupam sprites para reduzir trocas de textura e organizar assets.",
        "pergunta": "Como preparar arte para renderizar bem sem destruir o fluxo dos artistas?",
        "definicao": "Um sprite representa um elemento visual 2D. Um atlas reúne múltiplos sprites em uma textura maior, otimizando renderização e empacotamento. A decisão afeta memória, draw calls, animação e pipeline.",
        "quando": ["Quando há muitos elementos visuais pequenos.", "Quando performance cai por trocas de textura.", "Quando a equipe precisa padronizar exportação de assets."],
        "sinais": ["Nomes e pivôs são consistentes.", "Atlas não mistura assets com ciclos de mudança muito diferentes.", "A compactação não causa artefatos visuais."],
        "links": ["Pipeline de assets", "Renderização 2D", "Animação 2D", "Performance em jogos 2D", "Câmera 2D"]
    },
    "Colisão 2D": {
        "tags": ["jogos2d", "fisica", "gameplay"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Detecta e resolve interações espaciais entre personagens, objetos, tiles e gatilhos.",
        "pergunta": "O jogo precisa de colisão física realista ou de regras de gameplay previsíveis?",
        "definicao": "Colisão 2D envolve formas, layers, máscaras, detecção, resolução e eventos. Em muitos jogos, sensação e previsibilidade valem mais que realismo físico.",
        "quando": ["Ao implementar movimento, dano, plataformas e pickups.", "Ao separar hitboxes, hurtboxes e triggers.", "Quando bugs de atravessar parede aparecem."],
        "sinais": ["Camadas de colisão têm nomes claros.", "Hitbox e visual não precisam ser idênticos.", "O comportamento é previsível em bordas e alta velocidade."],
        "links": ["Game loop", "Física 2D", "Tilemaps", "IA de inimigos 2D", "Sistemas determinísticos"]
    },
    "Física 2D": {
        "tags": ["jogos2d", "fisica", "gameplay"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Simula movimento, forças, gravidade e contatos quando a experiência pede comportamento físico.",
        "pergunta": "A física deve ser simulação emergente ou controle manual com sensação calibrada?",
        "definicao": "Física 2D pode usar motores prontos ou lógica customizada. Platformers frequentemente misturam controle manual com colisão para preservar responsividade.",
        "quando": ["Quando objetos empurram, caem, quicam ou deslizam.", "Quando o jogo depende de massa, força e impulso.", "Quando o movimento do personagem precisa de consistência."],
        "sinais": ["A sensação de controle vem antes do realismo.", "Timestep é estável.", "Parâmetros são ajustáveis para design."],
        "links": ["Colisão 2D", "Game loop", "Sistemas determinísticos", "Performance em jogos 2D", "Level design 2D"]
    },
    "Câmera 2D": {
        "tags": ["jogos2d", "ux", "gameplay"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Controla enquadramento, leitura espacial e sensação de movimento.",
        "pergunta": "O que o jogador precisa ver agora para agir bem?",
        "definicao": "A câmera 2D não é apenas seguir o jogador. Ela antecipa movimento, mostra ameaças, revela objetivos, suaviza deslocamento e respeita limites de fase.",
        "quando": ["Em jogos com exploração, combate ou plataformas.", "Quando o jogador perde informação fora da tela.", "Quando movimento causa enjoo ou confusão."],
        "sinais": ["A câmera comunica intenção de design.", "Transições são suaves sem atrasar controle.", "A área visível favorece decisões justas."],
        "links": ["Level design 2D", "Feedback ao jogador", "Performance em jogos 2D", "Sprites e atlases", "Game feel"]
    },
    "Animação 2D": {
        "tags": ["jogos2d", "arte", "feedback"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Comunica estado, intenção, peso e resposta por movimento visual.",
        "pergunta": "Que informação de gameplay a animação precisa tornar legível?",
        "definicao": "Animação 2D inclui spritesheets, skeletal animation, state machines, blending simples e efeitos. Ela não serve só para beleza: telegrava ataques, confirma ações e vende impacto.",
        "quando": ["Quando estados precisam ser lidos rapidamente.", "Quando ataques e dano precisam de antecipação.", "Quando o jogo parece rígido apesar da mecânica funcionar."],
        "sinais": ["Cada estado importante tem pose reconhecível.", "Transições não escondem controle.", "Timing e feedback reforçam regras."],
        "links": ["Sprites e atlases", "Feedback ao jogador", "Game feel", "IA de inimigos 2D", "Pipeline de assets"]
    },
    "Level design 2D": {
        "tags": ["jogos2d", "leveldesign", "produto"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Organiza espaço, ritmo, desafio e aprendizagem dentro de fases ou arenas.",
        "pergunta": "Como o espaço ensina, testa e recompensa o jogador?",
        "definicao": "Level design 2D usa geometria, inimigos, recursos, câmera, checkpoints e ritmo para criar experiência. Ele conecta mecânicas a situações concretas.",
        "quando": ["Depois que uma mecânica básica funciona.", "Ao criar curva de aprendizado.", "Quando o jogo precisa de variedade sem sistemas novos."],
        "sinais": ["Cada trecho tem intenção.", "O jogador aprende antes de ser punido.", "Risco, recompensa e descanso se alternam."],
        "links": ["Tilemaps", "Câmera 2D", "Requisitos jogáveis", "Prototipagem jogável", "Balanceamento"]
    },
    "Feedback ao jogador": {
        "tags": ["jogos2d", "ux", "feedback"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Confirma ações, explica consequências e torna o sistema legível.",
        "pergunta": "Como o jogador sabe que sua ação aconteceu e importou?",
        "definicao": "Feedback combina visual, som, vibração, pausa, partículas, UI e mudança de estado. Bons jogos 2D usam feedback para reduzir ambiguidade e aumentar sensação de impacto.",
        "quando": ["Quando ações parecem fracas.", "Quando o jogador não entende dano, erro ou sucesso.", "Ao polir uma mecânica já funcional."],
        "sinais": ["Cada ação importante tem resposta perceptível.", "Feedback não esconde informação crítica.", "O feedback reforça a hierarquia de importância."],
        "links": ["Game feel", "Animação 2D", "Câmera 2D", "UX em jogos", "Telemetria em jogos"]
    },
    "Game feel": {
        "tags": ["jogos2d", "ux", "gameplay"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Qualidade sensorial da interação: resposta, peso, ritmo, impacto e controle percebido.",
        "pergunta": "O jogo responde de um jeito que dá prazer antes mesmo do conteúdo final existir?",
        "definicao": "Game feel emerge de latência, aceleração, hit stop, squash/stretch, câmera, áudio, partículas e tolerâncias como coyote time. É ponte entre design, programação e arte.",
        "quando": ["Ao prototipar mecânicas centrais.", "Quando o jogo funciona mas parece sem vida.", "Ao calibrar combate, movimento ou plataforma."],
        "sinais": ["Inputs parecem responsivos.", "Impactos têm peso.", "O sistema perdoa erros humanos sem parecer injusto."],
        "links": ["Feedback ao jogador", "Câmera 2D", "Animação 2D", "Prototipagem jogável", "Física 2D"]
    },
    "Performance em jogos 2D": {
        "tags": ["jogos2d", "performance", "arquitetura"],
        "camada": "ponte",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Mantém frame rate, memória e responsividade dentro de limites adequados à plataforma.",
        "pergunta": "Qual gargalo realmente impede a experiência desejada?",
        "definicao": "Performance 2D envolve draw calls, fill rate, física, alocação, scripts, carregamento, pathfinding e partículas. Otimizar cedo demais atrapalha, mas ignorar medições cria dívida.",
        "quando": ["Quando frames caem em cenas representativas.", "Antes de lançar em hardware limitado.", "Quando sistemas multiplicam entidades ou efeitos."],
        "sinais": ["Medições vêm antes de otimização.", "Há orçamento de frame e memória.", "Otimizações preservam clareza quando possível."],
        "links": ["Observabilidade", "Sprites e atlases", "Renderização 2D", "Game loop", "Dívida técnica"]
    },
    "Renderização 2D": {
        "tags": ["jogos2d", "renderizacao", "performance"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Transforma estado visual em imagem, respeitando ordem, camadas, materiais e custo de desenho.",
        "pergunta": "Que ordem visual e que custo de renderização a cena exige?",
        "definicao": "Renderização 2D lida com sprites, tilemaps, sorting layers, parallax, iluminação 2D, shaders e efeitos. A clareza visual é tão importante quanto a eficiência.",
        "quando": ["Ao definir estilo visual.", "Quando elementos aparecem na ordem errada.", "Quando efeitos visuais degradam FPS."],
        "sinais": ["Camadas visuais têm convenção.", "Efeitos têm orçamento.", "A cena comunica prioridade sem poluição."],
        "links": ["Sprites e atlases", "Tilemaps", "Performance em jogos 2D", "Câmera 2D", "Pipeline de assets"]
    },
    "IA de inimigos 2D": {
        "tags": ["jogos2d", "ia", "gameplay"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Define percepção, decisão e ação de inimigos de forma legível e ajustável.",
        "pergunta": "O inimigo precisa ser inteligente ou interessante de enfrentar?",
        "definicao": "IA de inimigos 2D pode usar máquinas de estado, árvores de comportamento, steering simples, pathfinding e scripts. O objetivo é criar padrões justos, legíveis e variados.",
        "quando": ["Quando o desafio depende de comportamento de oponentes.", "Quando inimigos precisam patrulhar, perseguir ou atacar.", "Quando designers precisam ajustar padrões sem reprogramar tudo."],
        "sinais": ["Estados são claros e depuráveis.", "Ataques têm telegraph.", "O comportamento cria escolhas, não frustração gratuita."],
        "links": ["Pathfinding 2D", "Animação 2D", "Colisão 2D", "ECS", "Balanceamento"]
    },
    "Pathfinding 2D": {
        "tags": ["jogos2d", "ia", "algoritmos"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Calcula rotas por grades, grafos ou malhas navegáveis para agentes se moverem pelo cenário.",
        "pergunta": "Que representação do espaço torna o caminho correto e barato?",
        "definicao": "Pathfinding em 2D frequentemente usa A*, grid, waypoints ou navmesh simplificada. A escolha depende do tipo de movimento, tamanho do mapa e necessidade de atualização dinâmica.",
        "quando": ["Quando inimigos precisam contornar obstáculos.", "Quando NPCs navegam tilemaps.", "Quando rotas precisam ser recalculadas sem travar o frame."],
        "sinais": ["O espaço de busca é adequado ao jogo.", "Custos refletem design.", "Caminhos são suavizados quando necessário."],
        "links": ["IA de inimigos 2D", "Tilemaps", "Performance em jogos 2D", "Sistemas determinísticos", "Level design 2D"]
    },
    "Sistema de save": {
        "tags": ["jogos2d", "arquitetura", "persistencia"],
        "camada": "ponte",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Persistência confiável de progresso, configurações e estado relevante do jogador.",
        "pergunta": "O que precisa sobreviver entre sessões e em que versão de dados?",
        "definicao": "Sistema de save serializa progresso, inventário, checkpoints, flags, configurações e metadados. Deve lidar com versões, corrupção, slots, autosave e compatibilidade futura.",
        "quando": ["Quando progressão passa de protótipo para produto.", "Quando estados precisam ser restaurados exatamente.", "Quando atualizações podem mudar estrutura de dados."],
        "sinais": ["Há esquema de versionamento.", "Dados transitórios não são salvos por acidente.", "Falhas de escrita não destroem o progresso anterior."],
        "links": ["Estado do jogo", "Arquitetura em camadas", "Arquitetura hexagonal", "Testes automatizados", "Dívida técnica"]
    },
    "Sistema de inventário": {
        "tags": ["jogos2d", "dominio", "gameplay"],
        "camada": "ponte",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Gerencia itens, quantidades, regras de uso, coleta, descarte e efeitos no gameplay.",
        "pergunta": "Inventário é lista de objetos, economia de recursos ou motor de decisões?",
        "definicao": "Um inventário pode ser simples como chaves coletadas ou complexo como slots, peso, crafting e equipamentos. A modelagem correta evita bugs de duplicação, perda e uso indevido.",
        "quando": ["Quando itens afetam progressão.", "Quando UI e regra começam a se misturar.", "Quando há equipamentos, consumíveis ou crafting."],
        "sinais": ["Itens têm identidade e regras claras.", "UI não é fonte de verdade.", "Operações críticas são testáveis."],
        "links": ["Modelagem de domínio", "Estado do jogo", "Sistema de save", "Testes automatizados", "UX em jogos"]
    },
    "Prototipagem jogável": {
        "tags": ["jogos2d", "produto", "aprendizado"],
        "camada": "ponte",
        "moc": "MOC - Índice Geral",
        "resumo": "Cria versões pequenas e jogáveis para aprender sobre mecânicas, sensação e viabilidade.",
        "pergunta": "Qual é a menor experiência jogável que responde à pergunta atual?",
        "definicao": "Prototipagem jogável privilegia aprendizagem rápida sobre código perfeito. O protótipo testa hipóteses de controle, desafio, diversão, produção de arte ou tecnologia.",
        "quando": ["Quando uma ideia parece boa mas ainda não foi sentida.", "Antes de investir em conteúdo final.", "Quando há risco de diversão, técnica ou escopo."],
        "sinais": ["Cada protótipo responde uma pergunta.", "Descartabilidade é aceitável.", "O aprendizado é registrado em notas e decisões."],
        "links": ["Requisitos jogáveis", "Game feel", "Level design 2D", "Dívida técnica", "CI-CD"]
    },
    "Pipeline de assets": {
        "tags": ["jogos2d", "automacao", "arte"],
        "camada": "ponte",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Fluxo que leva arte, áudio e dados da criação até o jogo de forma repetível.",
        "pergunta": "Como transformar arquivos de produção em assets prontos sem depender de passos manuais frágeis?",
        "definicao": "Pipeline de assets define nomes, formatos, exportação, compressão, validação, importação e versionamento. Em jogos 2D, impacta sprites, atlases, tilemaps, animações, áudio e dados de fases.",
        "quando": ["Quando artistas e programadores perdem tempo com importação manual.", "Quando assets quebram por inconsistência de nomes.", "Quando builds precisam ser reproduzíveis."],
        "sinais": ["Convenções são documentadas.", "Validações pegam erros cedo.", "O processo suporta iteração rápida."],
        "links": ["Sprites e atlases", "Tilemaps", "Renderização 2D", "CI-CD", "Registro de decisões arquiteturais"]
    },
    "Ferramentas internas": {
        "tags": ["software", "jogos2d", "produtividade"],
        "camada": "ponte",
        "moc": "MOC - Arquitetura de Software",
        "resumo": "Editores, scripts e utilitários criados para acelerar produção e reduzir erro humano.",
        "pergunta": "Que tarefa repetitiva justifica uma ferramenta pequena em vez de mais processo manual?",
        "definicao": "Ferramentas internas podem editar fases, validar assets, gerar dados, visualizar estados ou automatizar builds. Elas são produtos para a própria equipe e precisam de manutenção proporcional ao valor que entregam.",
        "quando": ["Quando uma tarefa repetitiva consome tempo criativo.", "Quando erros manuais são frequentes.", "Quando designers precisam autonomia."],
        "sinais": ["A ferramenta reduz espera entre ideia e teste.", "Seu escopo é claro.", "Ela não vira plataforma genérica sem necessidade."],
        "links": ["Monólito modular", "Arquitetura hexagonal", "Pipeline de assets", "Level design 2D", "Documentação viva"]
    },
    "Sistemas determinísticos": {
        "tags": ["arquitetura", "jogos2d", "simulacao"],
        "camada": "ponte",
        "moc": "MOC - Índice Geral",
        "resumo": "Produzem o mesmo resultado para a mesma sequência de entradas, facilitando testes, replay e depuração.",
        "pergunta": "A simulação precisa ser reproduzível exatamente ou apenas consistente para o jogador?",
        "definicao": "Determinismo reduz incerteza em simulações. Em jogos, pode ajudar rollback netcode, replays, testes e debug, mas exige controle de tempo, aleatoriedade, ordem de atualização e ponto flutuante.",
        "quando": ["Quando bugs são difíceis de reproduzir.", "Quando replays ou multiplayer dependem de simulação idêntica.", "Quando testes precisam validar sequências de jogo."],
        "sinais": ["Random usa seed controlada.", "Timestep e ordem de execução são definidos.", "Entradas podem ser gravadas e reproduzidas."],
        "links": ["Game loop", "Testes automatizados", "Física 2D", "CQRS", "Pathfinding 2D"]
    },
    "Telemetria em jogos": {
        "tags": ["jogos2d", "observabilidade", "produto"],
        "camada": "ponte",
        "moc": "MOC - Índice Geral",
        "resumo": "Coleta eventos de uso para entender comportamento real, dificuldade, retenção e problemas.",
        "pergunta": "Que eventos ajudam a melhorar o jogo sem invadir a privacidade do jogador?",
        "definicao": "Telemetria em jogos registra eventos como início de fase, morte, item coletado, tempo de sessão, abandono, erro e vitória. Ela deve servir perguntas de design e produto, não acumular dados sem propósito.",
        "quando": ["Durante playtests.", "Ao balancear dificuldade.", "Quando decisões dependem de comportamento real e não só opinião."],
        "sinais": ["Eventos têm pergunta associada.", "Privacidade e consentimento são considerados.", "Métricas geram ações concretas."],
        "links": ["Observabilidade", "Event-driven", "Feedback ao jogador", "Balanceamento", "UX em jogos"]
    },
    "Balanceamento": {
        "tags": ["jogos2d", "produto", "gameplay"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Ajusta números, ritmos e recompensas para produzir desafio justo e interessante.",
        "pergunta": "Que decisão do jogador deve ficar mais interessante com estes números?",
        "definicao": "Balanceamento não é deixar tudo igual; é calibrar tensão, risco, poder, escassez e progressão. Dados ajudam, mas a intenção de design guia a interpretação.",
        "quando": ["Quando dificuldade oscila sem intenção.", "Quando uma estratégia domina todas as outras.", "Quando playtests indicam frustração ou tédio."],
        "sinais": ["Parâmetros são fáceis de ajustar.", "Mudanças têm hipótese explícita.", "Métricas e sensação são analisadas juntas."],
        "links": ["Telemetria em jogos", "Level design 2D", "IA de inimigos 2D", "Sistema de inventário", "Prototipagem jogável"]
    },
    "UX em jogos": {
        "tags": ["jogos2d", "ux", "produto"],
        "camada": "jogos2d",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Facilita compreensão, decisão e controle sem remover profundidade.",
        "pergunta": "O jogador entende o que pode fazer, o que aconteceu e o que importa agora?",
        "definicao": "UX em jogos inclui menus, HUD, onboarding, legibilidade, acessibilidade, feedback, mapeamento de controles e fluxo. Boa UX reduz atrito sem transformar tudo em tutorial excessivo.",
        "quando": ["Quando jogadores se perdem ou interpretam errado regras básicas.", "Ao desenhar HUD e menus.", "Ao adaptar controles para plataformas diferentes."],
        "sinais": ["Informação aparece no momento certo.", "O jogador erra por desafio, não por confusão.", "Acessibilidade entra no design cedo."],
        "links": ["Feedback ao jogador", "Câmera 2D", "Sistema de inventário", "Telemetria em jogos", "Requisitos jogáveis"]
    },
    "Sistema de conquistas": {
        "tags": ["jogos2d", "eventos", "produto"],
        "camada": "ponte",
        "moc": "MOC - Desenvolvimento de Jogos 2D",
        "resumo": "Reconhece marcos e comportamentos do jogador por eventos e condições verificáveis.",
        "pergunta": "Que conquistas reforçam a experiência sem distorcer o jogo?",
        "definicao": "Um sistema de conquistas observa eventos e estados para desbloquear marcos. Ele deve ser desacoplado do gameplay principal para não espalhar condições de conquista pelo código inteiro.",
        "quando": ["Quando progressão e retenção precisam de metas extras.", "Quando eventos de gameplay já existem.", "Quando plataformas externas exigem integração."],
        "sinais": ["Conquistas observam fatos, não controlam regras centrais.", "Condições são testáveis.", "A recompensa não incentiva comportamento ruim."],
        "links": ["Event-driven", "Telemetria em jogos", "Estado do jogo", "Testes automatizados", "Balanceamento"]
    }
}

mocs = {
    "MOC - Índice Geral": {
        "tags": ["moc", "indice", "hub"],
        "summary": "Mapa central do vault-piloto. Mantém três constelações principais e notas-ponte para criar um grafo legível.",
        "sections": {
            "Hubs principais": ["MOC - Engenharia de Software", "MOC - Arquitetura de Software", "MOC - Desenvolvimento de Jogos 2D"],
            "Notas-ponte que desenham conexões entre clusters": ["Requisitos jogáveis", "Estado do jogo", "ECS", "Prototipagem jogável", "Pipeline de assets", "Sistemas determinísticos", "Telemetria em jogos", "Dívida técnica"],
            "Como ler o grafo": ["Documentação viva", "Registro de decisões arquiteturais", "Modelagem de domínio"]
        }
    },
    "MOC - Engenharia de Software": {
        "tags": ["moc", "software", "hub"],
        "summary": "Cluster de práticas para construir, evoluir e sustentar sistemas de software.",
        "sections": {
            "Fundamentos de design": ["Modelagem de domínio", "Coesão e acoplamento", "SOLID com pragmatismo"],
            "Evolução e segurança para mudar": ["Testes automatizados", "Refatoração", "Dívida técnica"],
            "Entrega e aprendizado operacional": ["CI-CD", "Observabilidade", "Documentação viva"]
        }
    },
    "MOC - Arquitetura de Software": {
        "tags": ["moc", "arquitetura", "hub"],
        "summary": "Cluster de decisões estruturais, fronteiras e padrões arquiteturais.",
        "sections": {
            "Estrutura e modularidade": ["Monólito modular", "Arquitetura em camadas", "Arquitetura hexagonal"],
            "Comunicação e fluxo de dados": ["Event-driven", "CQRS", "Registro de decisões arquiteturais"],
            "Pontes com jogos e produção": ["Estado do jogo", "Ferramentas internas", "Pipeline de assets", "Sistemas determinísticos"]
        }
    },
    "MOC - Desenvolvimento de Jogos 2D": {
        "tags": ["moc", "jogos2d", "hub"],
        "summary": "Cluster de fundamentos técnicos, experiência e produção para jogos 2D.",
        "sections": {
            "Loop, estado e simulação": ["Game loop", "Estado do jogo", "ECS", "Sistemas determinísticos"],
            "Mundo, movimento e visual": ["Tilemaps", "Sprites e atlases", "Colisão 2D", "Física 2D", "Câmera 2D", "Renderização 2D"],
            "Experiência e conteúdo": ["Animação 2D", "Level design 2D", "Feedback ao jogador", "Game feel", "UX em jogos"],
            "Sistemas de produto": ["IA de inimigos 2D", "Pathfinding 2D", "Sistema de save", "Sistema de inventário", "Sistema de conquistas", "Balanceamento", "Telemetria em jogos"]
        }
    }
}

def yaml_list(items):
    return "[" + ", ".join(items) + "]"


def slug_path(title, folder):
    return VAULT / folder / f"{title}.md"


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")

for title, data in notes.items():
    links = data["links"]
    frontmatter = dedent(f"""
    ---
    tipo: ficha
    status: semente
    camada: {data['camada']}
    hub: "[[{data['moc']}]]"
    tags: {yaml_list(data['tags'])}
    conexoes_chave: {yaml_list([f'"[[{l}]]"' for l in links[:4]])}
    ---
    """)
    body = f"""
    # {title}

    #""" + " #".join(data["tags"]) + f"\n\n    ## Resumo\n    {data['resumo']}\n\n    ## Pergunta que esta nota responde\n    {data['pergunta']}\n\n    ## Definição operacional\n    {data['definicao']}\n\n    ## Quando usar\n" + "".join([f"    - {x}\n" for x in data["quando"]]) + f"\n    ## Sinais de boa aplicação\n" + "".join([f"    - {x}\n" for x in data["sinais"]]) + f"\n    ## Conexões\n" + "".join([f"    - [[{x}]]\n" for x in links]) + f"\n    ## Próximas pesquisas\n    - Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.\n    - Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.\n    - Conectar novos aprendizados ao hub [[{data['moc']}]].\n    "
    write(slug_path(title, "01-Notas"), frontmatter + body)

for title, data in mocs.items():
    frontmatter = dedent(f"""
    ---
    tipo: moc
    status: ativo
    camada: hub
    tags: {yaml_list(data['tags'])}
    ---
    """)
    body = f"""
    # {title}

    #""" + " #".join(data["tags"]) + f"\n\n    ## Função deste mapa\n    {data['summary']}\n\n    ## Navegação\n    "
    for sec, items in data["sections"].items():
        body += f"\n    ### {sec}\n"
        for item in items:
            body += f"    - [[{item}]]\n"
    body += """

    ## Regra visual do grafo
    Este MOC é um hub. Ele deve se conectar a notas do mesmo cluster, mas não deve tentar conectar tudo. As notas-ponte fazem a ligação entre constelações para evitar um grafo com um único centro inchado.
    """
    write(slug_path(title, "00-Mapas"), frontmatter + body)

write(VAULT / "README.md", """
# Obsidian Vault Piloto — Engenharia de Software, Arquitetura e Jogos 2D

Este vault foi montado para gerar um **Graph View automático** com três constelações principais:

1. **Engenharia de Software** — práticas de evolução, qualidade e entrega.
2. **Arquitetura de Software** — decisões estruturais, padrões e fronteiras.
3. **Desenvolvimento de Jogos 2D** — gameplay, renderização, estado, produção e UX.

O desenho do grafo vem da estrutura de links:

- `00-Mapas/` contém MOCs, que funcionam como hubs.
- `01-Notas/` contém fichas estruturadas e atômicas.
- notas com tag `ponte` conectam clusters diferentes.
- `.obsidian/graph.json` configura cores por grupos de tags.

## Como usar

1. Descompacte `obsidian-vault-piloto.zip` ou copie a pasta `obsidian-vault-piloto`.
2. No Obsidian, escolha **Open folder as vault** e selecione essa pasta.
3. Abra o Graph View.
4. Ative filtros por grupos, se necessário, e use as tags:
   - `tag:#moc`
   - `tag:#software`
   - `tag:#arquitetura`
   - `tag:#jogos2d`
   - `tag:#ponte`

## Como continuar a automação

Para cada nova rodada, forneça:

```text
Tema: <tema central>
Escopo: <o que entra e o que fica fora>
Profundidade: semente | intermediário | avançado
Quantidade: <número de notas>
Objetivo visual: cluster novo | expandir cluster | criar ponte entre clusters
Formato: ficha estruturada
```

Exemplo:

```text
Tema: combate 2D para metroidvania
Escopo: input buffering, hitboxes, inimigos básicos, feedback e balanceamento inicial
Profundidade: intermediário
Quantidade: 20 notas
Objetivo visual: expandir cluster jogos2d e criar ponte com arquitetura
Formato: ficha estruturada
```
""")

write(VAULT / "90-Sistema/Manual do Método.md", """
---
tipo: sistema
status: ativo
tags: [obsidian, metodo, grafo]
---

# Manual do Método

## Objetivo

Construir conhecimento em Obsidian como um grafo bonito e útil: não apenas notas empilhadas, mas constelações com hubs, notas atômicas e pontes semânticas.

## Regras de ouro

1. Uma nota deve responder uma pergunta clara.
2. Cada nota nova deve apontar para 3 a 6 notas existentes.
3. MOCs são hubs, não enciclopédias.
4. Tags definem cor e grupo; links definem significado.
5. Notas-ponte conectam clusters diferentes e criam desenho visual.
6. Evite conectar tudo com tudo; isso destrói a forma do grafo.

## Tipos de nó

- `moc`: mapa de conteúdo e hub visual.
- `ficha`: nota atômica estruturada.
- `ponte`: nota que liga áreas diferentes.
- `adr`: decisão arquitetural.
- `sistema`: regra interna do vault.

## Fórmula de uma rodada

1. Definir tema e escopo.
2. Criar 1 MOC se o tema for novo.
3. Criar 8 a 30 fichas atômicas.
4. Escolher 2 a 5 notas-ponte.
5. Revisar se o grafo tem clusters legíveis.
6. Atualizar MOCs e registrar lacunas.
""")

write(VAULT / "90-Sistema/Glossário de Tags.md", """
---
tipo: sistema
status: ativo
tags: [obsidian, tags, grafo]
---

# Glossário de Tags

- `#moc`: hub visual e mapa de conteúdo.
- `#software`: práticas gerais de engenharia de software.
- `#arquitetura`: decisões estruturais e padrões de sistema.
- `#jogos2d`: desenvolvimento de jogos 2D.
- `#ponte`: conexão entre clusters.
- `#qualidade`: testes, refatoração, observabilidade e manutenção.
- `#performance`: custo de execução, memória, FPS e otimização.
- `#ux`: experiência do usuário ou jogador.
- `#automacao`: pipelines, CI/CD, ferramentas e geração de conteúdo.
""")

write(VAULT / "90-Sistema/Templates/Template - Ficha Estruturada.md", """
---
tipo: ficha
status: semente
camada: 
hub: "[[MOC - Índice Geral]]"
tags: []
conexoes_chave: []
---

# {{title}}

## Resumo

## Pergunta que esta nota responde

## Definição operacional

## Quando usar
- 

## Sinais de boa aplicação
- 

## Conexões
- [[]]
- [[]]
- [[]]

## Próximas pesquisas
- 
""")

write(VAULT / "90-Sistema/Registro de Rodadas.md", """
---
tipo: sistema
status: ativo
tags: [obsidian, automacao, pesquisa]
---

# Registro de Rodadas

## Rodada 001 — Vault piloto

- Tema: Engenharia de software, arquitetura e desenvolvimento de jogos 2D.
- Objetivo visual: três clusters com notas-ponte.
- Formato: ficha estruturada.
- Resultado: MOCs centrais + fichas atômicas + configuração de grupos do Graph View.

## Próximas lacunas sugeridas

- Combate 2D.
- Arquitetura específica para Godot.
- Arquitetura específica para Unity.
- Ferramentas internas para level design.
- Pipeline de pesquisa com fontes e citações.
""")

write(VAULT / "automation/rodada_exemplo.md", """
# Pedido de nova rodada

Copie este modelo e me envie quando quiser expandir o vault.

```text
Tema: 
Escopo: 
Fora do escopo: 
Profundidade: semente | intermediário | avançado
Quantidade de notas: 
Objetivo visual: cluster novo | expandir cluster | criar ponte entre clusters
MOCs que devem receber links: 
Notas obrigatórias: 
Formato: ficha estruturada
Idioma: português
```
""")

# Obsidian graph configuration (best-effort; Obsidian may update this format over time)
graph_config = {
    "collapse-filter": False,
    "search": "",
    "showTags": True,
    "showAttachments": False,
    "hideUnresolved": False,
    "showOrphans": True,
    "collapse-color-groups": False,
    "colorGroups": [
        {"query": "tag:#moc", "color": {"a": 1, "rgb": 16737792}},
        {"query": "tag:#software", "color": {"a": 1, "rgb": 3447003}},
        {"query": "tag:#arquitetura", "color": {"a": 1, "rgb": 10181046}},
        {"query": "tag:#jogos2d", "color": {"a": 1, "rgb": 3066993}},
        {"query": "tag:#ponte", "color": {"a": 1, "rgb": 15105570}},
    ],
    "collapse-display": False,
    "showArrow": False,
    "textFadeMultiplier": 0,
    "nodeSizeMultiplier": 1.2,
    "lineSizeMultiplier": 1.05,
    "collapse-forces": False,
    "centerStrength": 0.35,
    "repelStrength": 10,
    "linkStrength": 1,
    "linkDistance": 250,
    "scale": 1,
    "close": False,
}
write(VAULT / ".obsidian/graph.json", json.dumps(graph_config, ensure_ascii=False, indent=2))

# Add app config placeholder to make folder recognizable but minimal.
write(VAULT / ".obsidian/app.json", json.dumps({"readableLineLength": True, "showLineNumber": False}, indent=2))

# Normalize generated Markdown that came from indented Python blocks.
for md in VAULT.rglob("*.md"):
    lines = md.read_text(encoding="utf-8").splitlines()
    md.write_text("\n".join(line.removeprefix("    ") for line in lines).strip() + "\n", encoding="utf-8")

# Validate links: each wikilink target should exist in either maps or notes/system where relevant.
existing = {p.stem for p in VAULT.rglob("*.md")}
missing = set()
for p in VAULT.rglob("*.md"):
    text = p.read_text(encoding="utf-8")
    idx = 0
    while True:
        start = text.find("[[", idx)
        if start == -1:
            break
        end = text.find("]]", start)
        if end == -1:
            break
        target = text[start+2:end].split("|")[0].split("#")[0]
        if target and target not in existing:
            missing.add(target)
        idx = end + 2
if missing:
    raise SystemExit(f"Missing wikilinks: {sorted(missing)}")

if ZIP_PATH.exists():
    ZIP_PATH.unlink()
with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
    for file in VAULT.rglob("*"):
        if file.is_file():
            z.write(file, file.relative_to(ROOT))

print(f"Created {VAULT}")
print(f"Created {ZIP_PATH}")
print(f"Markdown files: {len(list(VAULT.rglob('*.md')))}")
