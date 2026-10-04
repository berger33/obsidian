---
tipo: moc-lote
dominio: software
subdominio: criacao-ia
lote: software-criacao-ia-2000-0004
ultima_verificacao: 2026-10-04
tags: [moc, dominio/software, subdominio/criacao-ia, lote/software-criacao-ia-2000-0004]
aliases: ["MOC — Engenharia e criação de programas, aplicativos e jogos com IA"]
---
# MOC — Engenharia e criação de programas, aplicativos e jogos com IA (`software-0010`)

Mapa de navegação para o lote [`software-criacao-ia-2000-0004`](../../exports/batches/software-criacao-ia-2000-0004.md), em `knowledge-federation/domains/software-0010/software/criacao-ia/`. O escopo definido com o usuário abrange desenvolvimento de programas e apps com IA; criação de jogos; técnicas de vídeo e animação para jogos; e produção de tutoriais e documentação para software e aplicativos.

## Estado do lote

- Meta: **2.000 notas substantivas**; cadência planejada: **20 tranches × 100 notas**.
- Progresso: **400 / 2.000 notas válidas (20,00%)** (`status: in_progress`).
- Gate: **400/400**; revisão factual humana: **0/400**; revisão factual por IA: **400/400**.
- Notas materiais presentes e contadas: **400**, IDs 000001–000400. Para as próximas 1.600 notas, nenhum ID, placeholder ou progresso virtual está reservado ou contado.
- As tranches 1–4 foram selecionadas com documentação primária e concluídas em dez trilhas temáticas cada; as 16 tranches futuras e seus títulos ainda não estão decididos.

## Conteúdo materializado — tranche 1 (100 notas; IDs 000001–000100)

A seleção cobre programação assistida, integração de modelos em apps, ferramentas seguras, aprendizagem de agentes, IA de gameplay, animação/exportação, cinematics, vídeo generativo e documentação técnica.

### Programação assistida com GitHub Copilot

1. [[copilot-prompts-com-criterios-de-aceitacao]] — Um pedido útil descreve o resultado observável, o contexto relevante e os critérios que tornam a alteração aceitável.
2. [[copilot-fornecer-contexto-de-repositorio]] — O Copilot produz sugestões melhores quando a pergunta identifica linguagem, estrutura do projeto, APIs usadas e trechos pertinentes.
3. [[copilot-escolher-ask-edit-ou-agent]] — Os modos da IDE variam entre responder sobre o código, propor edições localizadas e executar uma tarefa com maior autonomia.
4. [[copilot-dividir-mudancas-em-tarefas-pequenas]] — Tarefas curtas e independentes tornam mais fácil fornecer contexto, revisar a solução e localizar a origem de regressões.
5. [[copilot-tratar-sugestoes-como-rascunho]] — Código sugerido por um modelo é uma hipótese de implementação que exige leitura, teste e conformidade com as regras do projeto.
6. [[copilot-pedir-explicacao-de-codigo-existente]] — Perguntas sobre fluxo, dependências e contratos ajudam a entender uma base antes de propor alterações nela.
7. [[copilot-gerar-testes-a-partir-de-comportamento]] — Um modelo pode sugerir casos de teste derivados de exemplos, invariantes e condições de erro descritos pelo desenvolvedor.
8. [[copilot-explicitar-casos-de-erro-no-prompt]] — Descrever falhas previsíveis orienta o assistente a tratar caminhos que exemplos felizes deixam de fora.
9. [[copilot-registrar-instrucoes-do-repositorio]] — Instruções versionadas podem comunicar ao assistente convenções estáveis de build, teste, estilo e organização do projeto.
10. [[copilot-inspecionar-o-diff-antes-de-aceitar]] — Revisar o diff completo revela arquivos extras, mudanças de dependência e comportamentos que não aparecem na explicação do assistente.

### Integração de geração de texto com OpenAI Responses API

11. [[responses-api-iniciar-uma-chamada-de-texto]] — A Responses API recebe uma solicitação de geração e retorna itens de resposta que o aplicativo pode examinar e apresentar.
12. [[responses-api-separar-instrucoes-e-entrada]] — Instruções do desenvolvedor definem comportamento estável do aplicativo, enquanto a entrada do usuário expressa a solicitação daquela interação.
13. [[responses-api-definir-o-objetivo-do-prompt]] — Prompts orientados por tarefa especificam quem usa a função, o que deve ser produzido e quais características tornam a saída utilizável.
14. [[responses-api-extrair-texto-da-resposta]] — A resposta pode conter diferentes itens, e uma aplicação deve distinguir o texto destinado à pessoa de metadados ou estados auxiliares.
15. [[responses-api-escolher-modelo-por-tarefa]] — A escolha do modelo deve considerar qualidade necessária, latência, custo e recursos disponíveis para o caso de uso.
16. [[responses-api-limitar-o-tamanho-da-saida]] — Limites explícitos de extensão ajudam a controlar interface, custo e tempo, mas precisam refletir a tarefa e não apenas um número arbitrário.
17. [[responses-api-criar-um-prompt-versionavel]] — Guardar prompts como configuração versionada permite reproduzir mudanças de comportamento e relacioná-las a releases do aplicativo.
18. [[responses-api-isolar-conteudo-nao-confiavel]] — Texto fornecido por usuários deve ser tratado como dado de entrada, não como instrução privilegiada do sistema.
19. [[responses-api-tratar-falhas-e-repeticao]] — Erros de rede, limites de taxa e respostas incompletas precisam de estados de aplicação diferentes de uma geração bem-sucedida.
20. [[responses-api-avaliar-geracao-com-exemplos]] — Um conjunto versionado de entradas e expectativas torna possível detectar regressões de prompt sem depender de uma demonstração escolhida a dedo.

### Ferramentas e saídas estruturadas para apps com modelos

21. [[function-calling-declarar-contrato-de-ferramenta]] — Uma ferramenta descreve nome, finalidade e parâmetros que o modelo pode propor ao aplicativo para resolver uma tarefa.
22. [[saida-estruturada-usar-json-schema-estrito]] — Structured Outputs pode restringir a forma da resposta ao esquema aceito pelo aplicativo, quando o modelo e o modo escolhido suportam esse recurso.
23. [[function-calling-executar-no-aplicativo-nao-no-modelo]] — A chamada retornada pelo modelo é uma proposta de operação; é o código do aplicativo que decide validá-la e executá-la.
24. [[function-calling-correlacionar-chamadas-pelo-identificador]] — O identificador retornado junto a uma chamada relaciona a resposta da ferramenta à solicitação que a originou.
25. [[function-calling-lidar-com-zero-ou-varias-chamadas]] — Uma resposta pode pedir ferramenta, não pedir nenhuma ou incluir múltiplas chamadas, dependendo da solicitação e da configuração.
26. [[validacao-de-argumentos-de-ferramentas]] — Argumentos do modelo continuam sendo dados não confiáveis, mesmo que tenham sido produzidos em formato JSON ou por schema.
27. [[ferramentas-restringir-acoes-de-gameplay]] — Uma ferramenta de jogo deve expor ações de domínio delimitadas em vez de aceitar comandos arbitrários do modelo.
28. [[ferramentas-pedir-confirmacao-antes-de-efeitos-externos]] — Ações irreversíveis, financeiras ou visíveis a terceiros devem exigir confirmação e política do aplicativo, não apenas intenção inferida pelo modelo.
29. [[function-calling-minimizar-dados-retornados]] — Resultado de ferramenta deve conter somente informações necessárias para a continuação da tarefa do modelo.
30. [[ferramentas-testar-excecoes-e-falhas-de-execucao]] — Uma integração robusta precisa responder a ferramenta indisponível, argumento inválido e resultado vazio sem travar o ciclo da aplicação.

### Agentes de aprendizagem em Unity ML-Agents

31. [[ml-agents-estruturar-um-agent]] — Um Agent conecta observações do ambiente, ações recebidas e recompensas que representam progresso numa tarefa aprendida.
32. [[ml-agents-escolher-observacoes-uteis]] — Observações são os dados que o agente consegue usar para inferir o estado relevante da cena, por sensores vetoriais ou visuais.
33. [[ml-agents-mapear-acoes-ao-gameplay]] — O espaço de ação define quais comandos contínuos ou discretos o agente pode produzir em cada decisão.
34. [[ml-agents-desenhar-recompensas]] — A recompensa informa ao algoritmo se a transição observada aproxima ou afasta o agente do objetivo definido.
35. [[ml-agents-encerrar-e-reiniciar-episodios]] — Um episódio precisa terminar em sucesso, falha ou limite definido e voltar a um estado inicial consistente.
36. [[ml-agents-controlar-frequencia-de-decisao]] — Decisão a cada frame não é sempre necessária; período de decisão e ação repetida alteram custo e dinâmica do controle.
37. [[ml-agents-criar-cena-de-treinamento-representativa]] — Uma cena de treino pode ser a própria experiência ou um ambiente simplificado construído para iterar mais depressa.
38. [[ml-agents-iniciar-treinamento-reproduzivel]] — O comando `mlagents-learn` usa configuração de comportamento, identificador de execução e ambiente pronto para coletar experiências.
39. [[ml-agents-configurar-ppo-ou-sac-por-evidencia]] — Os treinadores PPO e SAC têm pressupostos e configurações diferentes; seleção deve acompanhar o tipo de ação e o sinal de aprendizagem.
40. [[ml-agents-avaliar-o-modelo-em-inferencia]] — Modelo treinado deve ser avaliado no modo de execução usado pelo jogo, com a inferência incorporada ao projeto Unity.

### IA de gameplay com Behavior Trees e EQS na Unreal Engine

41. [[unreal-separar-behavior-tree-e-blackboard]] — A Behavior Tree organiza decisões em nós e o Blackboard guarda valores que esses nós consultam ou atualizam.
42. [[unreal-compor-sequence-e-selector]] — Nós compostos expressam se subtarefas precisam concluir em ordem ou se alternativas devem ser tentadas até uma funcionar.
43. [[unreal-usar-decorators-como-condicoes]] — Decorators controlam se um nó ou ramo pode executar, usando condições, observadores ou limites definidos pela árvore.
44. [[unreal-encapsular-acao-em-tasks]] — Uma Task executa uma unidade de gameplay, como mover, aguardar ou iniciar animação, e informa o término à árvore.
45. [[unreal-escolher-aborts-de-observadores]] — Aborts definem quando uma mudança numa condição monitorada interrompe tarefas ativas ou ramos de menor prioridade.
46. [[unreal-eqs-gerar-candidatos-espaciais]] — Uma consulta EQS reúne candidatos por gerador antes de avaliá-los com critérios de ambiente.
47. [[unreal-eqs-selecionar-contextos-coerentes]] — Contexto define de quem ou de que local a query parte e influencia a relevância dos itens gerados.
48. [[unreal-eqs-compor-tests-e-pontuacao]] — Tests filtram ou pontuam itens candidatos por condições como navegação, distância e visibilidade, permitindo ranquear locais.
49. [[unreal-eqs-enviar-resultado-a-behavior-tree]] — A saída de uma EQS query pode ser gravada no Blackboard para a árvore usar numa próxima tarefa.
50. [[unreal-depurar-a-decisao-do-npc-em-runtime]] — Visualizar execução da árvore, valores do Blackboard e resultados EQS ajuda a localizar qual condição escolheu o comportamento.

### Navegação e agentes de gameplay em Godot

51. [[godot-preparar-malha-de-navegacao]] — Uma malha de navegação descreve regiões nas quais um agente pode planejar deslocamento evitando geometria considerada obstáculo.
52. [[godot-configurar-destino-do-navigationagent]] — NavigationAgent recebe um alvo e expõe informação do caminho para um personagem implementar seu movimento.
53. [[godot-sincronizar-consultas-com-o-mapa]] — Mudanças de regiões ou malhas de navegação podem ser aplicadas de forma assíncrona em relação à lógica que solicita um caminho.
54. [[godot-controlar-a-chegada-ao-waypoint]] — Distâncias de chegada determinam quando o agente considera o destino próximo o suficiente para avançar ou concluir o caminho.
55. [[godot-distinguir-caminho-de-evasao-local]] — Pathfinding escolhe uma rota até o alvo, enquanto avoidance tenta reduzir conflitos entre agentes em movimento local.
56. [[godot-aplicar-velocidade-de-avoidance]] — A evasão calcula uma velocidade preferível segura para reduzir colisões locais, mas o script precisa respeitar seu resultado.
57. [[godot-particionar-avoidance-com-layers]] — Camadas e máscaras permitem decidir quais agentes consideram outros agentes como vizinhos para evitar colisões.
58. [[godot-usar-obstacles-para-geometria-e-fluxo]] — Obstáculos de navegação podem representar estruturas que alteram rotas ou evitar que agentes se aproximem de regiões locais.
59. [[godot-escolher-navigationlayers-por-uso]] — NavigationLayers filtram quais regiões um agente considera ao consultar o mapa, permitindo superfícies específicas para classes de movimento.
60. [[godot-validar-navegacao-em-movimento-real]] — Um caminho calculado só é útil se o personagem conseguir segui-lo com sua física, aceleração e animações.

### Animação e exportação de conteúdo de jogo no Blender

61. [[blender-organizar-clips-como-actions]] — Actions armazenam curvas e canais de animação que podem ser associados e reutilizados em objetos compatíveis.
62. [[blender-nomear-actions-para-o-pipeline]] — Nomes de ação explícitos ajudam artistas e ferramentas a identificar clips depois de exportar e importar.
63. [[blender-preservar-acoes-com-nla]] — NLA permite organizar e combinar strips de Action na linha do tempo e manter clips disponíveis para o pipeline.
64. [[blender-conferir-intervalos-de-keyframes]] — Intervalos definem a duração efetiva de um clip e influenciam sincronização com gameplay e loops.
65. [[blender-validar-o-rig-antes-de-exportar]] — A estrutura do armature, hierarquia e bind pose influenciam se o movimento pode ser reaplicado corretamente no runtime.
66. [[blender-exportar-somente-o-conteudo-necessario]] — O exportador glTF oferece seleção de objetos e opções para incluir meshes, armatures, materiais e animações.
67. [[blender-checar-compatibilidade-de-animacao-gltf]] — A exportação glTF suporta determinados tipos de curvas e objetos, não todos os recursos possíveis do Blender.
68. [[blender-controlar-multiplas-actions-no-export]] — Uma armature pode conter diversas Actions, e as opções de exportação determinam quais clips são gravados.
69. [[blender-separar-movimento-in-place-e-root-motion]] — Animação pode codificar deslocamento no root ou manter personagem no lugar para o controlador de gameplay mover o corpo.
70. [[blender-revisar-animacao-dentro-do-jogo]] — Visualização isolada do Blender não reproduz importação, compressão, retargeting ou combinação com gameplay.

### Cinematics e renders para jogos na Unreal Engine

71. [[unreal-sequencer-distinguir-asset-e-actor]] — Level Sequence guarda dados de tracks e keyframes, enquanto Level Sequence Actor referencia a sequência no nível.
72. [[unreal-sequencer-animar-com-tracks-e-keyframes]] — Tracks registram propriedades ou atores ao longo do tempo, e keyframes definem seus valores em pontos da linha do tempo.
73. [[unreal-sequencer-construir-cortes-de-camera]] — Camera Cuts determina qual câmera fornece a visão durante intervalos definidos da sequência.
74. [[unreal-sequencer-organizar-shots-e-sub-sequences]] — Subsequências e shots dividem uma cinematic em unidades menores que podem ser montadas e revisadas na sequência principal.
75. [[unreal-capturar-takes-com-take-recorder]] — Take Recorder grava atores, animações e fontes Live Link em tracks Sequencer para revisar performance e alternativas.
76. [[unreal-acionar-sequencer-durante-gameplay]] — Blueprints e componentes podem iniciar, pausar ou controlar sequência em resposta a eventos do jogo.
77. [[unreal-montar-uma-fila-de-renderizacao]] — Movie Render Queue permite configurar e executar jobs de renderização de Sequencer com opções de saída próprias.
78. [[unreal-versionar-presets-e-configuracoes-de-render]] — Presets registram escolhas de render que podem ser reaproveitadas em jobs e revisadas por equipe.
79. [[unreal-revisar-sequencia-renderizada-alem-do-viewport]] — O viewport interativo e o render final podem usar qualidade, temporal sampling e exposição diferentes.
80. [[unreal-manter-renders-rastreaveis]] — Identificadores de cena, versão de projeto e preset permitem saber qual sequência produziu cada arquivo.

### Workflows de geração de vídeo e assets com ComfyUI

81. [[comfyui-ler-um-workflow-como-grafo]] — Um workflow ComfyUI conecta nós tipados para carregar modelos, transformar dados, amostrar resultados e salvar saídas.
82. [[comfyui-instalar-modelos-nos-caminhos-esperados]] — Nós de carregamento selecionam arquivos de modelo específicos e cada família precisa do formato e diretório esperados pelo workflow.
83. [[comfyui-escolher-template-antes-de-montar-do-zero]] — Templates e workflows de referência fornecem conexões e parâmetros iniciais para uma tarefa específica.
84. [[comfyui-escolher-text-to-video-ou-image-to-video]] — Workflows de texto e de imagem oferecem formas diferentes de condicionar conteúdo temporal no exemplo Wan documentado.
85. [[comfyui-controlar-duracao-e-numero-de-frames]] — Tamanho do vídeo depende de resolução e contagem de frames configuradas no workflow, sujeitas ao modelo usado.
86. [[comfyui-ajustar-prompt-sem-quebrar-o-grafo]] — Prompt descreve conteúdo e movimento, enquanto as conexões do workflow controlam modelos e transformação de dados.
87. [[comfyui-usar-frames-de-referencia-com-cautela]] — Workflows que recebem primeiro ou último frame podem ancorar limites temporais de um clipe quando o modelo documenta essa entrada.
88. [[comfyui-salvar-e-versionar-o-workflow]] — Salvar o grafo junto a prompt e parâmetros permite reconstruir um experimento e investigar por que um resultado mudou.
89. [[comfyui-gerenciar-dependencias-de-custom-nodes]] — Workflows podem depender de nós fornecidos por extensões e não apenas das operações nativas do ComfyUI.
90. [[comfyui-aprovar-asset-gerado-para-producao]] — Vídeo ou imagem gerados são candidatos de conteúdo que precisam de avaliação artística, técnica e legal antes de entrar num jogo.

### Tutoriais e documentação técnica para software, apps e jogos

91. [[documentacao-escolher-entre-tutorial-e-referencia]] — Tutorial ensina fazendo, how-to orienta uma tarefa, referência descreve detalhes e explicação desenvolve entendimento conceitual.
92. [[documentacao-declarar-leitor-e-resultado]] — Uma página clara identifica quem deve usá-la e qual capacidade ou decisão deve estar disponível ao final.
93. [[documentacao-fixar-versoes-e-pre-requisitos]] — Versões de engine, SDK, plugins e sistema operacional influenciam comandos e telas que a pessoa encontrará.
94. [[tutorial-construir-exemplo-de-ponta-a-ponta]] — Um tutorial é mais útil quando o leitor executa uma sequência coesa e vê um artefato funcionando ao final.
95. [[how-to-organizar-passos-por-tarefa]] — Instruções orientadas a tarefa ajudam a pessoa que já conhece a ferramenta a completar uma operação específica.
96. [[referencia-descrever-campos-com-precisao]] — Referência técnica funciona como consulta estável para parâmetros, formatos e contratos expostos por uma ferramenta.
97. [[documentacao-tornar-resultado-e-verificacao-explicitos]] — Cada etapa prática deve oferecer um sinal de sucesso observável e uma forma segura de investigar divergência.
98. [[documentacao-usar-imagens-acessiveis-e-uteis]] — Capturas e diagramas ajudam localizar controles visuais, desde que acrescentem informação e tenham descrição textual adequada.
99. [[documentacao-executar-exemplos-de-codigo]] — Trechos executáveis são uma parte do produto e precisam compilar ou rodar nas versões anunciadas.
100. [[documentacao-revisar-tutorial-gerado-por-ia]] — Texto e exemplos produzidos por IA devem passar por execução e validação editorial como qualquer contribuição técnica.

## Conteúdo materializado — tranche 2 (100 notas; IDs 000101–000200)

### Claude Code CLI & Anthropic API para Desenvolvimento Assistido

- [[claude-code-iniciar-sessao-interativa-cli]] — Claude Code: iniciar sessão interativa no terminal.
- [[claude-code-definir-instrucoes-claudemd]] — Claude Code: configurar instruções de projeto no arquivo CLAUDE.md.
- [[claude-code-gerenciar-permissoes-de-execucao-de-comandos]] — Claude Code: gerenciar permissões de execução de comandos.
- [[claude-code-usar-prompt-caching-para-bases-extensas]] — Anthropic API: aplicar Prompt Caching em bases extensas.
- [[mcp-conectar-servidores-para-contexto-externo]] — Model Context Protocol: conectar servidores MCP de contexto.
- [[anthropic-api-estruturar-mensagens-tool-result]] — Anthropic API: estruturar mensagens de retorno em tool_result.
- [[claude-code-orquestrar-subagentes-especializados]] — Claude Code: orquestrar subagentes especializados.
- [[anthropic-api-controlar-limites-com-max-tokens]] — Anthropic API: controlar limites com max_tokens e stop_sequences.
- [[anthropic-api-depurar-layout-com-mensagens-de-visao]] — Anthropic API: depurar layouts com mensagens de visão.
- [[claude-code-validar-testes-antes-do-commit]] — Claude Code: validar testes e diff antes do commit.

### Agentes de Código Locais e Continue.dev

- [[continue-dev-configurar-provedor-local]] — Continue.dev: configurar provedores locais no config.json.
- [[continue-dev-indexar-codebase-com-embeddings-locais]] — Continue.dev: indexar codebase com embeddings locais.
- [[continue-dev-customizar-context-providers]] — Continue.dev: customizar context providers para documentação.
- [[continue-dev-separar-modelo-de-autocomplete-tab]] — Continue.dev: separar modelo de autocomplete Tab do modelo de chat.
- [[ollama-ajustar-num-ctx-e-quantizacao-gguf]] — Ollama: ajustar num_ctx e quantização GGUF para estabilidade de memória.
- [[ollama-gerenciar-permanencia-com-keep-alive]] — Ollama: gerenciar permanência na VRAM com keep_alive.
- [[llamacpp-servir-endpoint-openai-compativel]] — llama.cpp: servir endpoint HTTP compatível com OpenAI.
- [[continue-dev-padronizar-regras-de-projeto]] — Continue.dev: padronizar regras de projeto e system prompts.
- [[continue-dev-auditar-requisicoes-e-logs-locais]] — Continue.dev: auditar requisições e logs de execução local.
- [[ia-local-garantir-isolamento-sem-conexao-externa]] — IA Local: garantir isolamento de rede para código sensível.

### Cursor e Context Engineering para Criação de Software

- [[cursor-padronizar-regras-com-cursorrules]] — Cursor: padronizar convenções no arquivo .cursorrules.
- [[cursor-otimizar-indexacao-com-cursorignore]] — Cursor: otimizar indexação vetorial com .cursorignore.
- [[cursor-usar-simbolos-de-contexto-docs-e-git]] — Cursor: usar símbolos de contexto @Docs e @Git.
- [[cursor-composer-coordenar-edicoes-multi-arquivo]] — Cursor Composer: coordenar edições multi-arquivo com checkpoint.
- [[cursor-executar-scripts-no-terminal-integrado]] — Cursor: executar scripts no terminal integrado com supervisão.
- [[cursor-priorizar-janela-de-contexto-essencial]] — Cursor: priorizar arquivos essenciais na janela de contexto.
- [[cursor-revisar-diffs-inline-com-rejeicao-parcial]] — Cursor: revisar diffs inline com rejeição granular.
- [[context-engineering-usar-testes-como-especificacao]] — Engenharia de Contexto: usar testes unitários como especificação.
- [[context-engineering-injetar-tipos-estaticos-e-interfaces]] — Engenharia de Contexto: injetar tipos estáticos para evitar alucinações.
- [[cursor-corrigir-erros-com-diagnosticos-do-compilador]] — Cursor: corrigir erros alimentando diagnósticos do compilador.

### Máquinas de Estados e IA de Gameplay no Godot 4

- [[godot-estruturar-maquina-de-estados-hierarquica]] — Godot: estruturar máquina de estados hierárquica em GDScript.
- [[godot-desacoplar-transicoes-com-sinais]] — Godot: desacoplar transições de estado de IA com sinais.
- [[godot-implementar-steering-seek-e-flee]] — Godot: implementar comportamentos de direção Seek e Flee.
- [[godot-combinar-wander-e-pursuit-com-predicao]] — Godot: combinar navegação Wander e Pursuit com predição.
- [[godot-calcular-cone-de-visao-com-area3d-e-dot-product]] — Godot: calcular cone de visão com Area3D e produto escalar.
- [[godot-desviar-de-obstaculos-com-raycast3d-multiplos]] — Godot: desviar de obstáculos com múltiplos sensores RayCast3D.
- [[godot-selecionar-alvos-por-distancia-e-ameaca]] — Godot: selecionar alvos de combate por distância e ameaça.
- [[godot-sincronizar-ia-com-animationtree]] — Godot: sincronizar máquina de estados com o nó AnimationTree.
- [[godot-propagar-eventos-sonoros-para-audicao-de-npcs]] — Godot: propagar eventos sonoros para percepção auditiva de NPCs.
- [[godot-depurar-vetores-de-ia-com-draw-line]] — Godot: depurar vetores e decisões de IA com funções _draw.

### Rigging de Animação e Utility AI no Unity

- [[unity-animation-rigging-montar-rigbuilder]] — Unity: montar componente RigBuilder e camadas de restrição.
- [[unity-animation-rigging-ajustar-pes-com-two-bone-ik]] — Unity: ajustar pés em terrenos inclinados com Two-Bone IK.
- [[unity-animation-rigging-orientar-olhar-com-multi-aim]] — Unity: orientar cabeça e olhar com Multi-Aim Constraint.
- [[unity-animation-rigging-suavizar-com-damp-transform]] — Unity: suavizar movimento de armas e acessórios com Damp Transform.
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Unity: avaliar decisões de NPCs com curvas de resposta em Utility AI.
- [[unity-utility-ai-compor-fatores-de-saude-e-distancia]] — Unity: compor fatores de saúde e distância em pontuações de ação.
- [[unity-navmesh-reconstruir-superficie-em-runtime]] — Unity: reconstruir NavMeshSurface em tempo de execução.
- [[unity-navmesh-atribuir-custos-por-area-de-terreno]] — Unity: atribuir custos diferenciados por tipo de área no NavMesh.
- [[unity-playablegraph-mesclar-animacoes-procedurais]] — Unity: mesclar animações procedurais usando a PlayableGraph API.
- [[unity-ia-visualizar-decisoes-com-gizmos-de-cena]] — Unity: visualizar sensores e scores de utilidade com Gizmos de cena.

### StateTree e Smart Objects na Unreal Engine 5

- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Unreal Engine: estruturar hierarquia de estados leves no StateTree.
- [[unreal-statetree-extrair-contexto-com-evaluators]] — Unreal Engine: extrair contexto e dados de mundo com StateTree Evaluators.
- [[unreal-statetree-implementar-tasks-assincronas]] — Unreal Engine: implementar tarefas atômicas com StateTree Tasks.
- [[unreal-smart-objects-configurar-slots-de-interacao]] — Unreal Engine: configurar Smart Object Definitions e slots de animação.
- [[unreal-smart-objects-gerenciar-reservas-concorrentes]] — Unreal Engine: gerenciar reservas concorrentes com Smart Object Subsystem.
- [[unreal-smart-objects-conectar-a-tarefas-do-statetree]] — Unreal Engine: conectar navegação a Smart Objects via StateTree Tasks.
- [[unreal-mass-ai-processar-agentes-com-massentity]] — Unreal Engine: simular multidões com arquitetura ECS MassEntity e Mass AI.
- [[unreal-gas-acionar-habilidades-pelo-ai-controller]] — Unreal Engine: acionar Gameplay Abilities a partir de decisões do AIController.
- [[unreal-motion-warping-alinhar-interacoes-fisicas]] — Unreal Engine: alinhar pontos de contato e saltos com Motion Warping.
- [[unreal-gameplay-debugger-inspecionar-ia-em-runtime]] — Unreal Engine: inspecionar transições de IA com o Gameplay Debugger.

### Texturização Procedural e Pipelines 2D com IA para Jogos

- [[texturas-ia-gerar-padroes-pbr-seamless-tileaveis]] — Texturas com IA: gerar padrões PBR contínuos e sem emendas.
- [[texturas-ia-derivar-mapas-de-normal-e-roughness]] — Texturas com IA: derivar mapas de normal e roughness de alturas.
- [[controlnet-guiar-geracao-com-bordas-canny-e-depth]] — ControlNet: guiar geração de assets com mapas de borda Canny e profundidade.
- [[controlnet-fixar-postura-de-sprites-com-openpose]] — ControlNet: fixar postura anatômica de sprites 2D com OpenPose.
- [[pixel-art-ia-alinhar-a-grade-e-limitar-paleta]] — Pixel Art com IA: alinhar arte à grade de pixels e limitar contagem de cores.
- [[spritesheet-ia-empacotar-e-fatiar-atlas-de-sprites]] — Sprite Sheets com IA: empacotar e fatiar atlas com margens uniformes.
- [[texturas-ia-remover-sombras-para-albedo-neutro]] — Texturas com IA: remover sombras embutidas para obter albedo neutro.
- [[assets-ia-otimizar-compressao-bc7-e-astc-em-vram]] — Otimização de Texturas: comprimir mapas PBR em BC7 e ASTC para VRAM.
- [[concept-art-ia-refinar-detalhes-com-inpainting]] — Concept Art com IA: refinar detalhes localizados através de inpainting.
- [[pipeline-assets-validar-escala-metrica-e-pivots]] — Pipeline de Assets: validar escala métrica e pivôs antes do import.

### Síntese de Voz e Áudio para Jogos com IA

- [[audio-ia-sintetizar-falas-dinamicas-de-npcs]] — Áudio com IA: sintetizar falas dinâmicas de NPCs via chamadas assíncronas.
- [[audio-ia-armazenar-linhas-de-voz-em-cache-local]] — Áudio com IA: armazenar falas geradas em cache de disco local.
- [[audio-ia-extrair-visemas-para-lip-sync-com-rhubarb]] — Lip Sync com IA: extrair visemas fonéticos de áudio com Rhubarb.
- [[audio-ia-mapear-visemas-a-blend-shapes-faciais]] — Animação Facial: mapear visemas fonéticos a blend shapes do modelo 3D.
- [[fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo]] — FMOD: rotear vozes sintéticas para barramentos de diálogo com efeitos.
- [[audio-ia-configurar-espacializacao-3d-e-atenuacao]] — Áudio 3D: configurar atenuação logarítmica e posicionamento espacial.
- [[mixagem-aplicar-audio-ducking-durante-vozes-de-ia]] — Mixagem de Som: aplicar audio ducking automático durante falas de IA.
- [[legendas-sincronizar-texto-com-timestamps-de-palavras]] — Legendas: sincronizar exibição de texto com timestamps por palavra.
- [[audio-ia-modular-prosodia-e-estabilidade-por-emocao]] — Áudio com IA: modular parâmetros de prosódia e estilo por emoção.
- [[audio-ia-prover-linhas-de-dialogo-de-fallback]] — Resiliência de Áudio: prover falas pré-gravadas como fallback de rede.

### Testes Automatizados e QA de Jogos com IA e Bots

- [[qa-jogos-executar-playtests-headless-em-ci]] — QA de Jogos: executar playtests funcionais headless na pipeline de CI.
- [[qa-jogos-encapsular-loop-em-ambiente-gymnasium]] — IA de Testes: encapsular loop de gameplay como ambiente Farama Gymnasium.
- [[qa-jogos-descobrir-colisoes-com-agentes-exploradores]] — QA de Jogos: descobrir falhas de colisão com bots exploradores.
- [[telemetria-jogos-gerar-heatmaps-de-morte-e-posicao]] — Telemetria de Jogos: gerar heatmaps de mortes e coordenadas de jogadores.
- [[qa-jogos-simular-carga-de-servidor-com-bots-leves]] — QA Multiplayer: simular carga de servidor instanciando bots sintéticos.
- [[qa-jogos-detectar-desbalanceamento-por-metricas-de-partida]] — Análise de Jogos: detectar desbalanceamento de armas e classes em logs.
- [[qa-jogos-validar-determinismo-de-fisica-em-fixed-ticks]] — QA de Física: validar determinismo em replays com passos de tempo fixos.
- [[qa-jogos-automatizar-fluxos-de-ui-e-inventario]] — QA de UI: automatizar navegação em telas de inventário e menus.
- [[qa-jogos-isolar-cenarios-de-regressao-de-gameplay]] — QA de Gameplay: criar microcenários isolados para regressão de mecânicas.
- [[qa-jogos-auditar-picos-de-frame-time-com-profiler-cli]] — Performance de Jogos: auditar picos de frame time com profiler em linha de comando.

### Documentação Técnica Interativa e Diátaxis para Criadores

- [[diataxis-aplicar-os-quatro-quadrantes-de-documentacao]] — Framework Diátaxis: estruturar documentação técnica em quatro quadrantes.
- [[diataxis-construir-tutoriais-focados-no-primeiro-sucesso]] — Diátaxis Tutoriais: conduzir novos usuários ao primeiro resultado palpável.
- [[diataxis-redigir-guias-how-to-para-tarefas-de-producao]] — Diátaxis How-To: redigir passos objetivos para tarefas práticas de produção.
- [[diataxis-organizar-referencias-tecnicas-sem-narrativa]] — Diátaxis Referência: catalogar APIs e parâmetros com precisão e sem narrativa.
- [[diataxis-elaborar-artigos-de-explicacao-e-design]] — Diátaxis Explicação: aprofundar decisões arquiteturais e modelos conceituais.
- [[documentacao-incorporar-sandboxes-e-demos-interativos]] — Documentação Interativa: incorporar sandboxes de código executável em tutoriais.
- [[documentacao-explicar-grafos-de-shaders-e-materiais]] — Documentação de Arte: detalhar entradas e nós matemáticos de shader graphs.
- [[documentacao-manter-guias-de-migracao-e-breaking-changes]] — Manutenção de Software: documentar breaking changes e guias de migração.
- [[documentacao-automatizar-validacao-de-links-e-snippets-em-ci]] — CI para Documentação: testar snippets de código e validar links quebrados.
- [[documentacao-aplicar-checklist-em-tutoriais-gerados-por-ia]] — Governança Técnica: aplicar checklist de verificação em tutoriais gerados por IA.

## Conteúdo materializado — tranche 3 (100 notas; IDs 000201–000300)

### LangGraph: persistência, controle de execução e streaming

- [[langgraph-interrupt-retomar-sem-repetir-efeitos]] — LangGraph: retomar interrupts sem duplicar efeitos colaterais.
- [[langgraph-thread-id-e-checkpoint-id]] — LangGraph: distinguir thread_id de checkpoint_id.
- [[langgraph-time-travel-replay-ou-fork]] — LangGraph: escolher replay ou fork no time travel.
- [[langgraph-checkpointer-versus-store]] — LangGraph: separar checkpointer de store de longo prazo.
- [[langgraph-supersteps-e-reducers-paralelos]] — LangGraph: combinar atualizações paralelas com reducers.
- [[langgraph-functional-api-task-result-checkpoint]] — LangGraph Functional API: persistir resultados com @task.
- [[langgraph-streaming-v2-partes-tipadas]] — LangGraph: usar partes tipadas no streaming v2.
- [[langgraph-event-streaming-projecoes-concorrentes]] — LangGraph: consumir projeções do event streaming v3.
- [[langgraph-schemas-entrada-saida-e-estado-privado]] — LangGraph: separar schemas de entrada, saída e estado interno.
- [[langgraph-politica-retencao-checkpoints]] — LangGraph: planejar retenção e limpeza de checkpoints.

### MCP: especificação 2026-07-28, transportes e recursos especializados

- [[mcp-stdio-framing-e-stdout-limpo]] — MCP stdio: framing por linha e stdout exclusivo do protocolo.
- [[mcp-streamable-http-versao-2026-stateless]] — MCP Streamable HTTP 2026: requests POST sem sessão implícita.
- [[mcp-meta-protocolo-capacidades-por-request]] — MCP 2026: carregar versão e capacidades em _meta por request.
- [[mcp-mrtr-input-required-request-state]] — MCP MRTR: retomar requests com inputResponses e requestState opaco.
- [[mcp-cache-ttl-scope-e-invalidacao]] — MCP: combinar ttlMs, cacheScope e notificações de invalidação.
- [[mcp-tools-list-schema-autorizacao]] — MCP tools/list: catálogo determinístico e schema de entrada executável.
- [[mcp-prompts-selecao-controlada-pelo-usuario]] — MCP prompts: distinguir seleção do usuário e autoria do servidor.
- [[mcp-elicitation-form-url-segredos]] — MCP elicitation: reservar URL mode para credenciais e segredos.
- [[mcp-oauth-discovery-e-client-registration]] — MCP HTTP OAuth: descobrir recurso protegido e registrar cliente.
- [[mcp-migrar-para-especificacao-2026-07-28]] — MCP 2026-07-28: preparar migração de handshake e notificações.

### OpenAI Agents SDK: orquestração, guardrails, state e tracing

- [[agents-sdk-especialista-como-tool-ou-handoff]] — Agents SDK: escolher Agent.as_tool ou handoff.
- [[agents-sdk-handoff-destino-fixo]] — Agents SDK handoff: modelar destinos como roteamento explícito.
- [[agents-sdk-on-handoff-autorizacao-antes-de-efeitos]] — Agents SDK: validar handoff input em on_handoff.
- [[agents-sdk-guardrails-fronteiras-primeiro-e-ultimo-agente]] — Agents SDK guardrails: mapear fronteiras de primeiro e último agente.
- [[agents-sdk-streaming-drenar-ate-fim]] — Agents SDK streaming: consumir eventos até o iterador terminar.
- [[agents-sdk-session-versus-responses-continuation]] — Agents SDK: escolher session local ou continuação server-side.
- [[agents-sdk-output-type-e-handoffs]] — Agents SDK: normalizar saída tipada entre handoffs.
- [[agents-sdk-hosted-tool-search-deferred-loading]] — Agents SDK: adiar tool schemas com hosted tool search.
- [[agents-sdk-session-input-callback-historico]] — Agents SDK Sessions: limitar histórico lido sem duplicar persistência.
- [[agents-sdk-tracing-flush-workers]] — Agents SDK tracing: descarregar spans antes de encerrar um job.

### Unreal Engine 5.8 PCG: geração hierárquica, runtime e GPU

- [[ue-pcg-partitioned-generation-grid-celulas]] — Unreal PCG: partitioned generation divide domínio em células.
- [[ue-pcg-higen-cascata-grid-size]] — Unreal PCG: fluxo de dados entre HiGen grid sizes.
- [[ue-pcg-world-partition-data-layers-hlod]] — Unreal PCG: propagar Data Layers e HLOD aos atores gerados.
- [[ue-pcg-runtime-generation-sources-radii]] — Unreal PCG runtime: fontes, raios de geração e limpeza.
- [[ue-pcg-scheduler-num-generating-components]] — Unreal PCG runtime: equilibrar scheduler e células concorrentes.
- [[ue-pcg-overlay-runtime-generation]] — Unreal PCG: interpretar overlay de geração em runtime.
- [[ue-pcg-runtime-partition-actor-pool]] — Unreal PCG runtime: dimensionar pool de Partition Actors.
- [[ue-pcg-cache-runtime-editor-budget]] — Unreal PCG: entender cache CPU e orçamento de memória.
- [[ue-pcg-gpu-compute-graph-transferencias]] — Unreal PCG GPU: agrupar nós para reduzir transferências.
- [[ue-pcg-gpu-beta-nos-suportados]] — Unreal PCG GPU: tratar escopo Beta como dependência de engine.

### Blender 5.2 Geometry Nodes: fields, state, attributes e instancing

- [[blender-geometry-nodes-field-contexto-avaliacao]] — Blender Geometry Nodes: fields são avaliados no contexto do consumidor.
- [[blender-capture-attribute-antes-de-conversao]] — Blender: capturar fields antes de uma conversão de geometria.
- [[blender-anonymous-versus-named-attributes]] — Blender Geometry Nodes: escolher atributo anônimo ou nomeado.
- [[blender-attributes-domain-conversoes-implicitas]] — Blender Geometry Nodes: auditar domínio e conversão de atributos.
- [[blender-repeat-zone-iters-e-inputs-externos]] — Blender Repeat Zone: distinguir feedback de entradas constantes.
- [[blender-repeat-versus-simulation-zone]] — Blender Geometry Nodes: escolher Repeat ou Simulation Zone.
- [[blender-simulation-anonymous-attributes-state]] — Blender Simulation Zone: declarar atributos anônimos no estado.
- [[blender-simulation-cache-bake-render]] — Blender Simulation Zone: gerenciar cache e bake para render.
- [[blender-instancing-realize-atributos-custo]] — Blender Geometry Nodes: manter instâncias até precisar realizá-las.
- [[blender-viewer-domain-spreadsheet-debug]] — Blender Geometry Nodes: inspecionar fields com Viewer e domain explícito.

### OpenUSD 26.08: composition, variants, time and asset resolution

- [[openusd-stage-composed-view-layers]] — OpenUSD: entender UsdStage como vista composta de layers.
- [[openusd-load-rules-payloads-working-set]] — OpenUSD: tratar load rules como working set de payloads.
- [[openusd-reference-versus-payload]] — OpenUSD: escolher reference ou payload para composição diferida.
- [[openusd-asset-resolver-context-identifiers]] — OpenUSD: resolver context e asset identifiers de pipeline.
- [[openusd-variants-edit-context]] — OpenUSD: autorar opiniões no variant edit context correto.
- [[openusd-opinion-strength-overrides]] — OpenUSD: diagnosticar strength entre local opinions e variants.
- [[openusd-attribute-default-e-time-samples]] — OpenUSD: separar default value de time samples em atributos.
- [[openusd-layer-offset-retimar-animacao]] — OpenUSD: retimar animação referenciada com layer offset.
- [[openusd-flattening-stage-export]] — OpenUSD: flattening exporta resultado composto, não estrutura editável.
- [[openusd-stage-units-up-axis-metadata]] — OpenUSD: harmonizar upAxis, metersPerUnit e timeCodesPerSecond.

### FFmpeg: ordem de opções, timestamps, filtros e inspeção

- [[ffmpeg-escopo-opcoes-por-arquivo]] — FFmpeg: posicionar opções no input ou output correto.
- [[ffmpeg-map-filtergraph-stream-labels]] — FFmpeg: mapear streams de entrada e saídas rotuladas.
- [[ffmpeg-concat-demuxer-precondicoes]] — FFmpeg concat demuxer: conferir streams e durações de entrada.
- [[ffmpeg-concat-filter-timestamps-zero]] — FFmpeg concat filter: alinhar cada segmento e normalizar streams.
- [[ffmpeg-trim-nao-redefine-pts]] — FFmpeg trim: separar seleção de frames e reinício de timestamps.
- [[ffmpeg-setpts-timebase-e-relatorio]] — FFmpeg: interpretar PTS em conjunto com time base.
- [[ffmpeg-fps-filter-versus-output-r]] — FFmpeg: distinguir filtro fps de opção de output -r.
- [[ffmpeg-filtergraph-escaping-niveis]] — FFmpeg filtergraph: separar escaping do filtro e da shell.
- [[ffmpeg-framesync-overlay-eof-policy]] — FFmpeg framesync: definir comportamento ao terminar uma entrada.
- [[ffprobe-json-inspecao-pipeline]] — ffprobe: produzir inventário estruturado para validar um pipeline.

### Playwright: relógio, WebSockets, service workers e artefatos de diagnóstico

- [[playwright-clock-install-order]] — Playwright Clock: instalar relógio antes de APIs temporais.
- [[playwright-websocketroute-mock-ou-proxy]] — Playwright WebSocketRoute: escolher mock completo ou interceptação.
- [[playwright-route-fallback-versus-continue]] — Playwright Route: preservar a cadeia com fallback.
- [[playwright-service-worker-network-routing]] — Playwright: service workers mudam visibilidade de network routing.
- [[playwright-trace-retencao-e-dados-de-debug]] — Playwright Trace: coletar diagnóstico sem expor dados de teste.
- [[playwright-video-context-close-artifact]] — Playwright video: fechar browser context para salvar o arquivo.
- [[playwright-expect-poll-e-topass]] — Playwright assertions: escolher expect.poll ou expect.toPass.
- [[playwright-timeouts-escopos-separados]] — Playwright Test: diagnosticar timeouts por escopo.
- [[playwright-add-init-script-determinismo]] — Playwright addInitScript: preparar ambiente antes do código da página.
- [[playwright-page-errors-observabilidade-cliente]] — Playwright: coletar erros de runtime sem confundir com falha de teste.

### OpenTelemetry: semantic conventions para GenAI, agents, métricas e eventos

- [[otel-genai-provider-name-perspectiva]] — OpenTelemetry GenAI: interpretar gen_ai.provider.name pela perspectiva da instrumentation.
- [[otel-genai-operation-name-taxonomia]] — OpenTelemetry GenAI: padronizar gen_ai.operation.name sem apagar a operação real.
- [[otel-genai-modelo-solicitado-versus-resposta]] — OpenTelemetry GenAI: separar modelo solicitado de modelo que respondeu.
- [[otel-genai-span-logico-retries]] — OpenTelemetry GenAI spans: medir a operação lógica incluindo retries.
- [[otel-genai-agent-spans-client-internal-tool]] — OpenTelemetry GenAI agents: separar invocation remota, execução local e tool span.
- [[otel-genai-token-counters-versus-histograms]] — OpenTelemetry GenAI token metrics: contadores de uso não são histogramas por operação.
- [[otel-genai-streaming-latencias-por-chunk]] — OpenTelemetry GenAI streaming: distinguir time to first chunk de cadência.
- [[otel-genai-conteudo-opt-in-minimizacao]] — OpenTelemetry GenAI: minimizar conteúdo de prompt e resposta na telemetria.
- [[otel-genai-evaluation-result-correlacao]] — OpenTelemetry GenAI evaluation.result: correlacionar resultado ao output avaliado.
- [[otel-genai-conventions-development-status]] — OpenTelemetry GenAI semconv: interpretar o status Development antes de fixar integração.

### OpenAPI 3.1.1: semântica do Schema Object, referências, conteúdo e callbacks

- [[oas311-jsonschema-dialect-default-override]] — OAS 3.1.1: selecionar o dialect JSON Schema correto.
- [[oas311-reference-object-vs-schema-ref]] — OAS 3.1.1: diferenciar Reference Object de `$ref` em Schema Object.
- [[oas311-id-and-relative-ref-base-uri]] — OAS 3.1.1: resolver `$ref` relativo usando `$id` e URI-base.
- [[oas311-format-annotation-nao-validacao]] — OAS 3.1.1: `format` não é uma validação garantida.
- [[oas311-null-union-boolean-schemas]] — OAS 3.1.1: representar null e schemas booleanos com JSON Schema.
- [[oas311-discriminator-nao-altera-validacao]] — OAS 3.1.1 discriminator: pista de serialização, não regra de validação.
- [[oas311-binary-contentencoding-vs-format]] — OAS 3.1.1: modelar binário com contentEncoding e contentMediaType.
- [[oas311-webhooks-versus-callbacks]] — OAS 3.1.1: escolher entre webhook top-level e callback de operação.
- [[oas311-path-item-ref-conflitos]] — OAS 3.1.1 Path Item `$ref`: não sobrepor fields com o alvo.
- [[oas311-readonly-writeonly-annotations]] — OAS 3.1.1: validar readOnly e writeOnly conforme direção da mensagem.

## Conteúdo materializado — tranche 4 (100 notas; IDs 000301–000400)

### WebGPU: adaptador, buffers, texturas, bindings e diagnóstico

- [[webgpu-requestadapter-por-criterios]] — WebGPU: filtrar adaptador por potência e modo de compatibilidade.
- [[webgpu-devicelost-camada-recuperacao]] — WebGPU: tratar device lost como fronteira de recuperação.
- [[webgpu-requiredlimits-calcular-custo]] — WebGPU: pedir limites maiores e calcular antes do limite suportado.
- [[webgpu-features-antes-dependencia]] — WebGPU: features são opcionais e viram dependência de plataforma.
- [[webgpu-leitura-gpu-staging-buffer]] — WebGPU: ler dados da GPU exige buffer staging com MAP_READ.
- [[webgpu-mappedatcreation-dado-inicial]] — WebGPU: mappedAtCreation para dados iniciais sem cópia adicional.
- [[webgpu-textureusage-views-permitidos]] — WebGPU: declarar cada uso de textura no momento certo.
- [[webgpu-bindgrouplayout-compatibilidade]] — WebGPU: bind groups só valem se o layout for compatível com o pipeline.
- [[webgpu-erros-asyncronos-escopos]] — WebGPU: capturar erros assíncronos com escopos empilhados.
- [[webgpu-timestamp-medir-gpu-real]] — WebGPU: medir tempo de GPU com query sets de timestamp.

### WGSL: classes de armazenamento, layout de binding, tipos e diagnóstico de compilação

- [[wgsl-classes-armazenamento-escopo]] — WGSL: escolher a classe de armazenamento pelo tempo de vida.
- [[wgsl-binding-layout-visibilidade]] — WGSL: pares @group/@binding são contrato com o layout do pipeline.
- [[wgsl-alinhamento-uniform-cinco-regra]] — WGSL: o layout de uniform padroniza tudo em 16 bytes.
- [[wgsl-storage-runtime-array]] — WGSL: só o storage buffer aceita array de tamanho em tempo de execução.
- [[wgsl-override-constantes-pipeline]] — WGSL: constantes overridables ajustam o pipeline sem recompilar o shader.
- [[wgsl-atomicos-compare-loop]] — WGSL: atômicos só em memória de escrita explícita, e CAS é loop manual.
- [[wgsl-textura-amostragem-tipo-view]] — WGSL: amostrar uma textura exige ver o tipo certo, não só o binding.
- [[wgsl-builtins-estagios-corte]] — WGSL: cada estágio expõe apenas os embutidos que fazem sentido para ele.
- [[wgsl-uniformidade-amostragem]] — WGSL: fluxo divergente e operações uniformes — uma análise, não uma sugestão.
- [[wgsl-sem-conversao-implicita]] — WGSL: sem coerções implícitas — o construtor é obrigatório e o erro é cedo.

### Bevy ECS: agendamento, queries, mutação adiada e organização de app

- [[bevy-startup-update-duas-momentos]] — Bevy ECS: Startup roda uma vez antes de tudo; Update é o loop.
- [[bevy-paralelismo-por-acesso]] — Bevy ECS: o paralelismo vem dos acessos declarados, não de threads manuais.
- [[bevy-chain-ordenamento-minimo]] — Bevy ECS: use chain() onde a ordem importa, e só lá.
- [[bevy-query-mutavel-unico-por-alvo]] — Bevy ECS: uma query &mut é o ponto único de escrita de um tipo.
- [[bevy-query-filtros-refinam-superficie]] — Bevy ECS: com With/Without você estreita o alvo sem quebrar o contrato de acesso.
- [[bevy-commands-mundo-diferido]] — Bevy ECS: Commands é a fila de mutação estrutural adiada.
- [[bevy-resources-valor-unico-mundo]] — Bevy ECS: resources são o valor-único do mundo, não mais um componente.
- [[bevy-componente-struct-derive]] — Bevy ECS: componente é struct Rust com derive — a decomposição é o design.
- [[bevy-plugins-unidade-distribuicao]] — Bevy ECS: Plugin é a unidade de empacotamento, não de lógica.
- [[bevy-app-schedule-world-camadas]] — Bevy ECS: App planeja, Schedule decide quando, World guarda o estado.

### Unity Entities (DOTS): mudanças estruturais, jobs, safety e armazenamento por chunk

- [[unity-estrutura-mudanca-custo-episodio]] — Unity Entities: criar/destruir é caro porque o layout muda, e por isso é estrutural.
- [[unity-ecb-bufferfromentity-replay]] — Unity Entities: a EntityCommandBuffer é replay, não fila mágica.
- [[unity-ijobentity-fonte-gerada-main-thread]] — Unity Entities: IJobEntity gera código por assinatura — e pode virar main thread sem aviso de sintaxe.
- [[unity-safety-system-corrida-exception]] — Unity Jobs: o safety system é a sua revisão de concorrência em tempo de execução.
- [[unity-parallelfor-indexo-proprio]] — Unity Jobs: em IJobParallelFor você escreve no seu índice e lê fora com intenção declarada.
- [[unity-chunks-arquetipos-leitura-lote]] — Unity Entities: iterar por chunk é o grão de leitura da arquitetura.
- [[unity-refrw-invalidacao-apos-estrutural]] — Unity Entities: RefRW/RefRO são handles com verificação, não ponteiros para sempre.
- [[unity-blob-assets-imutavel-compacto]] — Unity Entities: Blob assets são o lado imutável do dado, não JSON serializado.
- [[unity-aspects-limpeza-de-assinatura]] — Unity Entities: RefAspect limpa a assinatura do sistema, não o armazenamento.
- [[unity-baking-ponteiro-cenario-para-ecs]] — Unity Entities: o baking é a fronteira de conversão cena↔ECS, e o runtime tem outra porta.

### Godot 4: linguagem de shaders, embutidos canvas-item e flags de render espacial

- [[godot-shader-builtins-por-familia]] — Godot 4: cada tipo de shader tem seu conjunto de embutidos — a referência é o mapa.
- [[godot-canvas-vertex-px-locais]] — Godot 4: no canvas-item, VERTEX fala em píxeles locais — não em UV nem em mundo.
- [[godot-tempo-time-rollover-pause]] — Godot 4: TIME é tempo de render em segundos, com rolover e sem pause.
- [[godot-color-vertex-multipliers]] — Godot 4: COLOR em 2D é a trama de vértice × modulate × self_modulate.
- [[godot-particulas-instance-custom]] — Godot 4: INSTANCE_CUSTOM é o canal de dados por-partícula para o shader 2D.
- [[godot-shading-sem-cast-implicito]] — Godot 4: a shading language não faz cast implícito — e suas variáveis locais nascem sem inicializar.
- [[godot-uniform-docs-inspector]] — Godot 4: o /** acima do uniform é documentação vira-inspetor, não comentário decorativo.
- [[godot-blend-modes-spatial]] — Godot 4: os blend modes do material espacial e o truque do fog em blend_add.
- [[godot-render-flags-sombras-wireframe]] — Godot 4: flags de render do shader espacial que economizam passes inteiros.
- [[godot-shader-matrizes-colunares]] — Godot 4: nas shaders, matrizes são colunares — m[1][0] é a segunda coluna, primeira linha.

### Godot 4 GDExtension: o arquivo .gdextension, compatibilidade de versão e bindings nativos

- [[gdextension-biblioteca-compartilhada-runtime]] — Godot 4: GDExtension é a ponte runtime para bibliotecas nativas.
- [[gdextension-entry-symbol-obrigatorio]] — Godot 4: entry_symbol é o contrato mínimo do arquivo .gdextension.
- [[gdextension-alvo-baixo-compative-frente]] — Godot 4: mire a extensão na versão mais baixa que te atende, não na mais nova.
- [[gdextension-compatibility-min-max]] — Godot 4: compatibility_minimum e maximum são portas de carga, não metadados.
- [[gdextension-reloadable-dev-debug]] — Godot 4: reloadable recarrega a extensão — e é ferramenta de desenvolvimento, não de produção.
- [[gdextension-libraries-feature-tags]] — Godot 4: a seção [libraries] é um filtro por feature flags, não uma lista de caminhos.
- [[gdextension-ordem-especifica-antes]] — Godot 4: no .gdextension, a linha mais específica precisa vir antes — o matching é sequencial.
- [[gdextension-double-single-api-json]] — Godot 4: a extensão só carrega no build de motor com a mesma precisão de float.
- [[gdextension-icone-svg-e-dependencies]] — Godot 4: [icons] e [dependencies] completam o .gdextension — com contrato de 16×16 px.
- [[gdextension-vs-modules-custo-distribuicao]] — Godot 4: godot-cpp versus módulos C++ — uma decisão de distribuição.

### Blender 5.2 LTS: gestão de cor (view transforms, espaços) e pipeline de proxy/cache do VSE

- [[blender-view-transform-agx-filmic-standard]] — Blender: o View Transform (AgX, Filmic, Standard) é decisão de destino, não de look.
- [[blender-non-color-dados-nunca-convertidos]] — Blender: máscaras, normal maps e LUTs são Non-Color — converter dado é corromper sinal.
- [[blender-what-you-see-is-not-what-you-save]] — Blender: o display view não é o arquivo salvo — o laço View as Render/Save as Render.
- [[blender-proxy-tamanho-global-view]] — Blender VSE: Proxy Render Size é um switch global que habilita todos os strips.
- [[blender-proxy-bl-pasta-e-arquivos-externos]] — Blender VSE: proxies vivem em BL_proxy junto da footage — e podem ser arquivos existentes.
- [[blender-proxy-quality-lossy-percentual]] — Blender VSE: Quality do proxy é compressão com perda em percentual direto — 100 é sem perda.
- [[blender-sequencer-cache-memoria-limites]] — Blender VSE: Memory Cache Limit vive nas Preferences, e o VSE lê dele.
- [[blender-backend-vulkan-interface-52]] — Blender 5.2: o backend da interface é escolha (OpenGL × Vulkan) com custo de reinicialização.
- [[blender-limites-de-memoria-undo-shaders-stack]] — Blender 5.2: os limites de memória do System — undo, shaders, geometry nodes — e seus efeitos colaterais.
- [[blender-proxy-setup-automatico-vs-manual]] — Blender VSE: Proxy Setup Automatic gera sozinho, Manual delega à farm — a decisão é de pipeline.

### Web Audio API: tempo, autoplay, worklets e os nós de espacialização/análise

- [[webaudio-contexto-suspenso-gesto]] — Web Audio: o AudioContext nasce suspenso e só um gesto humano o acorda.
- [[webaudio-fontes-oneshot-start-stop]] — Web Audio: nós de fonte são one-shot — start() e stop() cada um uma vez só.
- [[webaudio-settargetattime-constante-tempo]] — Web Audio: setTargetAtTime é o easing exponencial — a constante define 63%, não o fim.
- [[webaudio-exp-ramp-zero-proibido]] — Web Audio: exponentialRampToValueAtTime não passa por zero — nem começando nem terminando nele.
- [[webaudio-decodeaudiodata-ressample-completo]] — Web Audio: decodeAudioData ressampleia para o contexto e exige o dado completo.
- [[webaudio-audioworklet-modulos-processador]] — Web Audio: AudioWorklet é módulo separado com o seu próprio global scope.
- [[webaudio-worklet-port-fio-da-navalha]] — Web Audio: o port do AudioWorkletNode é o fio da navalha entre página e render.
- [[webaudio-panner-modelos-espaciais]] — Web Audio: PannerNode escolhe como o som se move no espaço — pan, equal power ou HRTF.
- [[webaudio-convolver-resposta-ao-impulso]] — Web Audio: ConvolverNode é a reverberação física — e o IR define canal por canal.
- [[webaudio-analyser-janela-frequencia]] — Web Audio: AnalyserNode dá o espectro com janela e suavização — não a FFT crua.

### llama.cpp server: contexto, cache de KV, slots paralelos, endpoints e saída estruturada

- [[llamacpp-contexto-e-batch-na-carga]] — llama.cpp server: tamanho de contexto e batch de prompt são duas alavancas separadas.
- [[llamacpp-flash-attention-quantizacao-kv]] — llama.cpp server: Flash Attention abre a porta da quantização de KV.
- [[llamacpp-slots-paralelos-np-cb]] — llama.cpp server: -np multiplica o contexto e -cb faz o cache caber em cada slot.
- [[llamacpp-cache-prompt-ram-e-reuse]] — llama.cpp server: cache de prompt tem três camadas — o mesmo estado, três knobs.
- [[llamacpp-endpoints-completion-vs-openai]] — llama.cpp server: /completion é API própria, /v1/completions é a de OpenAI.
- [[llamacpp-servidor-sem-auth-na-rede]] — llama.cpp server: não é um servidor de produção exposto — e as três chaves que aproximam.
- [[gbnf-sintaxe-e-root]] — GBNF: a sintaxe que construi constrangimento de tokens, e o que 'root' significa.
- [[gbnf-custo-e-armadilha-de-repeticao]] — GBNF: repetições aninhadas custam exponencialmente — e a doc dá o recheio anti-armadilha.
- [[gbnf-json-schema-nao-e-prompt]] — llama.cpp: JSON Schema vira GBNF — restringe a saída e não entra no prompt.
- [[llamacpp-samplers-ordem-fixa]] — llama.cpp: o pipeline de samplers tem ordem fixa, e cada campo do pedido é um nó dele.

### Transformers (Hugging Face): geração — config, estratégias, caches de amostragem, KV e decodificação assistida

- [[hf-generation-config-nen-hereda-modelo]] — Transformers: os None da GenerationConfig são herança, não desatenção.
- [[hf-max-new-tokens-vs-max-length]] — Transformers: max_new_tokens é o budget relativo; max_length é o absoluto que te morderá.
- [[hf-beams-e-amostragem-tabela]] — Transformers: num_beams × do_sample é uma tabela de 4 modos, não dois knobs independentes.
- [[hf-early-stopping-never]] — Transformers: early_stopping do beam tem três estados — e 'never' existe por um motivo.
- [[hf-temperature-topk-topp-defaults]] — Transformers: os defaults de sampling (1.0/50/1.0) não são config — são a ausência dela.
- [[hf-min-p-top-h-typical-p-filtros]] — Transformers: os filtros alternativos do sampling — min_p, top_h, typical_p — e suas faixas.
- [[hf-repeticao-ngram-e-bias]] — Transformers: o arsenal anti-repetição — n-gramas, penalidades e viés de tokens.
- [[hf-cache-implementation-quatro-modos]] — Transformers: cache_implementation escolhe o destino da KV — dynamic, static, offload ou quantizada.
- [[hf-assisted-decoding-especifico]] — Transformers: decodificação assistida — draft por modelo, n-gram, medusa ou ensemble.
- [[hf-retornos-e-custom-generate]] — Transformers: past_key_values no retorno e generate custom por repositório.
## Mapa de escopo

Estes eixos são áreas de pesquisa, não notas ou placeholders:

### Engenharia de programas com IA

Especificação e planejamento; copilotos e agentes de código; geração e revisão de alterações; integração a IDEs e repositórios; testes, debugging, refatoração, segurança, manutenção e avaliação da qualidade do código produzido.

### Aplicativos e ferramentas

Prototipagem de apps; arquitetura e UX/UI; conexão entre modelos e funcionalidades; dados, APIs, empacotamento, publicação, observabilidade, acessibilidade e documentação orientada a usuários.

### Criação de jogos

Engines e ferramentas; gameplay e sistemas; scripting; integração de assets; pipeline de builds; conteúdo procedural ou gerado com IA; playtesting e validação de experiência.

### Vídeo e animação para jogos

Roteiro e storyboard; captura e edição; animação 2D/3D; mocap; composição; áudio quando relacionado à produção; exportação, formatos e integração ao engine. Cada técnica deverá explicitar requisitos, direitos de uso, limitações e controles de qualidade.

### Tutoriais e responsabilidade

Tutoriais reprodutíveis para programas, apps e jogos; documentação técnica; exemplos versionados; licenças e proveniência de dados/assets; privacidade; segurança; revisão humana e avaliação de conteúdo sintético.

## Fontes, revisão e cadência

Cada nota futura terá fontes específicas para a ferramenta, engine, API ou técnica que descreve. Conteúdo gerado por IA será tratado como rascunho sujeito a execução, revisão e testes; não como resultado automaticamente correto. O gate, a revisão factual e a reconciliação do manifesto serão concluídos antes de atualizar qualquer contagem.

A abertura e as regras de contagem estão no [relatório de escopo](../../exports/reports/batch-opening-software-criacao-ia-2000-0004.md) e na [reconciliação inicial](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-initial.md). Tranche 1: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md). Tranche 2: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md). Tranche 3: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md). Tranche 4: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md). Lotes adicionais nesse eixo são uma possibilidade a reavaliar, não uma reserva de progresso; não há lote 5 aberto.
