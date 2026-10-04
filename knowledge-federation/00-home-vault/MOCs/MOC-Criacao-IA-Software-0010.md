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
- Progresso: **100 / 2.000 notas válidas (5,00%)** (`status: in_progress`).
- Gate: **100/100**; revisão factual humana: **0/100**; revisão factual por IA: **100/100**.
- Notas materiais presentes e contadas: **100**, IDs 000001–000100. Para as próximas 1.900 notas, nenhum ID, placeholder ou progresso virtual está reservado ou contado.
- A tranche 1 foi selecionada com documentação primária e concluída em dez trilhas temáticas listadas abaixo; as 19 tranches futuras e seus títulos ainda não estão decididos.

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

A abertura e as regras de contagem estão no [relatório de escopo](../../exports/reports/batch-opening-software-criacao-ia-2000-0004.md) e na [reconciliação inicial](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-initial.md). A tranche 1 tem [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md), [gate por arquivos](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md). Lotes adicionais nesse eixo são uma possibilidade a reavaliar, não uma reserva de progresso.
