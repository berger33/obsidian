---
id: batch.software-criacao-ia-2000-0004
titulo: "Lote — Engenharia e criação de programas, aplicativos e jogos com IA"
dominio: software
subdominio: criacao-ia
status: in_progress
data_abertura: 2026-10-04
moc: knowledge-federation/00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md
---

# Lote `software-criacao-ia-2000-0004` — Engenharia e criação de programas, aplicativos e jogos com IA

## Escopo acordado

Este lote foca engenharia e criação de programas, aplicativos e jogos com apoio de inteligência artificial: técnicas de desenvolvimento de jogos; integração de IA aos fluxos de programação e criação de apps; produção de vídeos e animações para jogos; e técnicas equivalentes de produção, documentação e tutoriais para programas e aplicativos. O recorte foi definido com o usuário, que trabalha atualmente nessa área. O conteúdo deve priorizar orientação técnica prática, verificável e aplicável a ferramentas e pipelines reais.

A cobertura poderá incluir prototipagem, ferramentas e engines de jogos, geração e integração de assets, animação, vídeo, programação assistida, revisão e testes de código gerado, UX/UI, construção de apps, tutoriais, documentação, pipelines de conteúdo, interoperabilidade, licenças, direitos autorais, privacidade, segurança e proveniência. Cada nota deve explicar os limites da ferramenta ou técnica e separar assistência generativa de validação humana e testes determinísticos.

## Estado e contagem

- Domínio / subdomínio: `software` / `criacao-ia` (`knowledge-federation/domains/software-0010/software/criacao-ia/`)
- Meta: **2.000 notas substantivas**
- Cadência: **20 tranches planejadas × 100 notas**
- Notas materiais redigidas: **500 / 2.000 (25,00%)**
- Gate automatizado: **500/500 aprovadas**
- Revisão factual humana: **0/500** (nenhuma aprovação humana solicitada ou registrada)
- Revisão factual por IA: **500/500** (relatórios das tranches 1, 2, 3, 4 e 5)
- Notas válidas contabilizadas: **500/2.000 (25,00%)**
- Estado: `in_progress` — tranches 1, 2, 3, 4 e 5 concluídas e reconciliadas; 15 tranches planejadas permanecem sem IDs reservados.

A cadência descreve capacidade planejada, não reserva IDs. As notas materiais existentes são somente os IDs 1–500, com arquivos e conteúdo; para as 1.500 notas ainda não produzidas não há IDs reservados, placeholders ou progresso virtual. MOC, manifesto e relatórios administrativos não são notas do lote e não contam como progresso.

## Eixos editoriais iniciais

Os eixos abaixo orientam pesquisa e seleção de tópicos; não são títulos de notas nem uma ordem definitiva de tranches:

1. Engenharia de software com IA: especificação, decomposição de tarefas, geração assistida, revisão, refatoração e manutenção.
2. Apps e programas: protótipos, arquitetura, interfaces, integrações, dados, empacotamento e publicação.
3. Jogos: engines, gameplay, sistemas, ferramentas, assets e integração de conteúdo.
4. Vídeo e animação para jogos: roteiro, storyboard, captura, animação, composição, exportação e validação no engine.
5. Tutoriais e documentação: criação, edição, atualização, acessibilidade e demonstração reprodutível de programas, apps e jogos.
6. Qualidade e responsabilidade: testes, segurança, privacidade, direitos e licenças de dados/assets, proveniência, revisão humana e limites dos modelos.

Os tópicos finais de cada tranche serão selecionados com fontes primárias específicas. Novos lotes nesse eixo poderão ser propostos após avaliar a cobertura e a demanda; nenhum lote posterior está aberto ou contado neste manifesto.

## Tranche 1 — copilotos, APIs de IA, gameplay, animação e vídeo (100 notas)

IDs materiais: `software.criacao_ia.tranche01.000001`–`software.criacao_ia.tranche01.000100`. Cada tópico tem fonte(s) primária(s) indicada(s) na própria nota.

### Programação assistida com GitHub Copilot

1. [Copilot: prompts com critérios de aceitação](../../domains/software-0010/software/criacao-ia/copilot-prompts-com-criterios-de-aceitacao.md) — `software.criacao_ia.tranche01.000001`
2. [Copilot: fornecer contexto de repositório](../../domains/software-0010/software/criacao-ia/copilot-fornecer-contexto-de-repositorio.md) — `software.criacao_ia.tranche01.000002`
3. [Copilot: escolher Ask, Edit ou Agent](../../domains/software-0010/software/criacao-ia/copilot-escolher-ask-edit-ou-agent.md) — `software.criacao_ia.tranche01.000003`
4. [Copilot: dividir mudanças em tarefas pequenas](../../domains/software-0010/software/criacao-ia/copilot-dividir-mudancas-em-tarefas-pequenas.md) — `software.criacao_ia.tranche01.000004`
5. [Copilot: tratar sugestões como rascunho](../../domains/software-0010/software/criacao-ia/copilot-tratar-sugestoes-como-rascunho.md) — `software.criacao_ia.tranche01.000005`
6. [Copilot: pedir explicação de código existente](../../domains/software-0010/software/criacao-ia/copilot-pedir-explicacao-de-codigo-existente.md) — `software.criacao_ia.tranche01.000006`
7. [Copilot: gerar testes a partir de comportamento](../../domains/software-0010/software/criacao-ia/copilot-gerar-testes-a-partir-de-comportamento.md) — `software.criacao_ia.tranche01.000007`
8. [Copilot: explicitar casos de erro no prompt](../../domains/software-0010/software/criacao-ia/copilot-explicitar-casos-de-erro-no-prompt.md) — `software.criacao_ia.tranche01.000008`
9. [Copilot: registrar instruções do repositório](../../domains/software-0010/software/criacao-ia/copilot-registrar-instrucoes-do-repositorio.md) — `software.criacao_ia.tranche01.000009`
10. [Copilot: inspecionar o diff antes de aceitar](../../domains/software-0010/software/criacao-ia/copilot-inspecionar-o-diff-antes-de-aceitar.md) — `software.criacao_ia.tranche01.000010`

### Integração de geração de texto com OpenAI Responses API

11. [Responses API: iniciar uma chamada de texto](../../domains/software-0010/software/criacao-ia/responses-api-iniciar-uma-chamada-de-texto.md) — `software.criacao_ia.tranche01.000011`
12. [Responses API: separar instruções e entrada](../../domains/software-0010/software/criacao-ia/responses-api-separar-instrucoes-e-entrada.md) — `software.criacao_ia.tranche01.000012`
13. [Responses API: definir o objetivo do prompt](../../domains/software-0010/software/criacao-ia/responses-api-definir-o-objetivo-do-prompt.md) — `software.criacao_ia.tranche01.000013`
14. [Responses API: extrair texto da resposta](../../domains/software-0010/software/criacao-ia/responses-api-extrair-texto-da-resposta.md) — `software.criacao_ia.tranche01.000014`
15. [Responses API: escolher modelo por tarefa](../../domains/software-0010/software/criacao-ia/responses-api-escolher-modelo-por-tarefa.md) — `software.criacao_ia.tranche01.000015`
16. [Responses API: limitar o tamanho da saída](../../domains/software-0010/software/criacao-ia/responses-api-limitar-o-tamanho-da-saida.md) — `software.criacao_ia.tranche01.000016`
17. [Responses API: criar um prompt versionável](../../domains/software-0010/software/criacao-ia/responses-api-criar-um-prompt-versionavel.md) — `software.criacao_ia.tranche01.000017`
18. [Responses API: isolar conteúdo não confiável](../../domains/software-0010/software/criacao-ia/responses-api-isolar-conteudo-nao-confiavel.md) — `software.criacao_ia.tranche01.000018`
19. [Responses API: tratar falhas e repetição](../../domains/software-0010/software/criacao-ia/responses-api-tratar-falhas-e-repeticao.md) — `software.criacao_ia.tranche01.000019`
20. [Responses API: avaliar geração com exemplos](../../domains/software-0010/software/criacao-ia/responses-api-avaliar-geracao-com-exemplos.md) — `software.criacao_ia.tranche01.000020`

### Ferramentas e saídas estruturadas para apps com modelos

21. [Function calling: declarar contrato de ferramenta](../../domains/software-0010/software/criacao-ia/function-calling-declarar-contrato-de-ferramenta.md) — `software.criacao_ia.tranche01.000021`
22. [Saída estruturada: usar JSON Schema estrito](../../domains/software-0010/software/criacao-ia/saida-estruturada-usar-json-schema-estrito.md) — `software.criacao_ia.tranche01.000022`
23. [Function calling: executar no aplicativo, não no modelo](../../domains/software-0010/software/criacao-ia/function-calling-executar-no-aplicativo-nao-no-modelo.md) — `software.criacao_ia.tranche01.000023`
24. [Function calling: correlacionar chamadas pelo identificador](../../domains/software-0010/software/criacao-ia/function-calling-correlacionar-chamadas-pelo-identificador.md) — `software.criacao_ia.tranche01.000024`
25. [Function calling: lidar com zero ou várias chamadas](../../domains/software-0010/software/criacao-ia/function-calling-lidar-com-zero-ou-varias-chamadas.md) — `software.criacao_ia.tranche01.000025`
26. [Validação de argumentos de ferramentas](../../domains/software-0010/software/criacao-ia/validacao-de-argumentos-de-ferramentas.md) — `software.criacao_ia.tranche01.000026`
27. [Ferramentas: restringir ações de gameplay](../../domains/software-0010/software/criacao-ia/ferramentas-restringir-acoes-de-gameplay.md) — `software.criacao_ia.tranche01.000027`
28. [Ferramentas: pedir confirmação antes de efeitos externos](../../domains/software-0010/software/criacao-ia/ferramentas-pedir-confirmacao-antes-de-efeitos-externos.md) — `software.criacao_ia.tranche01.000028`
29. [Function calling: minimizar dados retornados](../../domains/software-0010/software/criacao-ia/function-calling-minimizar-dados-retornados.md) — `software.criacao_ia.tranche01.000029`
30. [Ferramentas: testar exceções e falhas de execução](../../domains/software-0010/software/criacao-ia/ferramentas-testar-excecoes-e-falhas-de-execucao.md) — `software.criacao_ia.tranche01.000030`

### Agentes de aprendizagem em Unity ML-Agents

31. [ML-Agents: estruturar um Agent](../../domains/software-0010/software/criacao-ia/ml-agents-estruturar-um-agent.md) — `software.criacao_ia.tranche01.000031`
32. [ML-Agents: escolher observações úteis](../../domains/software-0010/software/criacao-ia/ml-agents-escolher-observacoes-uteis.md) — `software.criacao_ia.tranche01.000032`
33. [ML-Agents: mapear ações ao gameplay](../../domains/software-0010/software/criacao-ia/ml-agents-mapear-acoes-ao-gameplay.md) — `software.criacao_ia.tranche01.000033`
34. [ML-Agents: desenhar recompensas](../../domains/software-0010/software/criacao-ia/ml-agents-desenhar-recompensas.md) — `software.criacao_ia.tranche01.000034`
35. [ML-Agents: encerrar e reiniciar episódios](../../domains/software-0010/software/criacao-ia/ml-agents-encerrar-e-reiniciar-episodios.md) — `software.criacao_ia.tranche01.000035`
36. [ML-Agents: controlar frequência de decisão](../../domains/software-0010/software/criacao-ia/ml-agents-controlar-frequencia-de-decisao.md) — `software.criacao_ia.tranche01.000036`
37. [ML-Agents: criar cena de treinamento representativa](../../domains/software-0010/software/criacao-ia/ml-agents-criar-cena-de-treinamento-representativa.md) — `software.criacao_ia.tranche01.000037`
38. [ML-Agents: iniciar treinamento reproduzível](../../domains/software-0010/software/criacao-ia/ml-agents-iniciar-treinamento-reproduzivel.md) — `software.criacao_ia.tranche01.000038`
39. [ML-Agents: configurar PPO ou SAC por evidência](../../domains/software-0010/software/criacao-ia/ml-agents-configurar-ppo-ou-sac-por-evidencia.md) — `software.criacao_ia.tranche01.000039`
40. [ML-Agents: avaliar o modelo em inferência](../../domains/software-0010/software/criacao-ia/ml-agents-avaliar-o-modelo-em-inferencia.md) — `software.criacao_ia.tranche01.000040`

### IA de gameplay com Behavior Trees e EQS na Unreal Engine

41. [Unreal: separar Behavior Tree e Blackboard](../../domains/software-0010/software/criacao-ia/unreal-separar-behavior-tree-e-blackboard.md) — `software.criacao_ia.tranche01.000041`
42. [Unreal: compor Sequence e Selector](../../domains/software-0010/software/criacao-ia/unreal-compor-sequence-e-selector.md) — `software.criacao_ia.tranche01.000042`
43. [Unreal: usar Decorators como condições](../../domains/software-0010/software/criacao-ia/unreal-usar-decorators-como-condicoes.md) — `software.criacao_ia.tranche01.000043`
44. [Unreal: encapsular ação em Tasks](../../domains/software-0010/software/criacao-ia/unreal-encapsular-acao-em-tasks.md) — `software.criacao_ia.tranche01.000044`
45. [Unreal: escolher aborts de observadores](../../domains/software-0010/software/criacao-ia/unreal-escolher-aborts-de-observadores.md) — `software.criacao_ia.tranche01.000045`
46. [Unreal EQS: gerar candidatos espaciais](../../domains/software-0010/software/criacao-ia/unreal-eqs-gerar-candidatos-espaciais.md) — `software.criacao_ia.tranche01.000046`
47. [Unreal EQS: selecionar contextos coerentes](../../domains/software-0010/software/criacao-ia/unreal-eqs-selecionar-contextos-coerentes.md) — `software.criacao_ia.tranche01.000047`
48. [Unreal EQS: compor Tests e pontuação](../../domains/software-0010/software/criacao-ia/unreal-eqs-compor-tests-e-pontuacao.md) — `software.criacao_ia.tranche01.000048`
49. [Unreal EQS: enviar resultado à Behavior Tree](../../domains/software-0010/software/criacao-ia/unreal-eqs-enviar-resultado-a-behavior-tree.md) — `software.criacao_ia.tranche01.000049`
50. [Unreal: depurar a decisão do NPC em runtime](../../domains/software-0010/software/criacao-ia/unreal-depurar-a-decisao-do-npc-em-runtime.md) — `software.criacao_ia.tranche01.000050`

### Navegação e agentes de gameplay em Godot

51. [Godot: preparar malha de navegação](../../domains/software-0010/software/criacao-ia/godot-preparar-malha-de-navegacao.md) — `software.criacao_ia.tranche01.000051`
52. [Godot: configurar destino do NavigationAgent](../../domains/software-0010/software/criacao-ia/godot-configurar-destino-do-navigationagent.md) — `software.criacao_ia.tranche01.000052`
53. [Godot: sincronizar consultas com o mapa](../../domains/software-0010/software/criacao-ia/godot-sincronizar-consultas-com-o-mapa.md) — `software.criacao_ia.tranche01.000053`
54. [Godot: controlar a chegada ao waypoint](../../domains/software-0010/software/criacao-ia/godot-controlar-a-chegada-ao-waypoint.md) — `software.criacao_ia.tranche01.000054`
55. [Godot: distinguir caminho de evasão local](../../domains/software-0010/software/criacao-ia/godot-distinguir-caminho-de-evasao-local.md) — `software.criacao_ia.tranche01.000055`
56. [Godot: aplicar velocidade de avoidance](../../domains/software-0010/software/criacao-ia/godot-aplicar-velocidade-de-avoidance.md) — `software.criacao_ia.tranche01.000056`
57. [Godot: particionar avoidance com layers](../../domains/software-0010/software/criacao-ia/godot-particionar-avoidance-com-layers.md) — `software.criacao_ia.tranche01.000057`
58. [Godot: usar obstacles para geometria e fluxo](../../domains/software-0010/software/criacao-ia/godot-usar-obstacles-para-geometria-e-fluxo.md) — `software.criacao_ia.tranche01.000058`
59. [Godot: escolher NavigationLayers por uso](../../domains/software-0010/software/criacao-ia/godot-escolher-navigationlayers-por-uso.md) — `software.criacao_ia.tranche01.000059`
60. [Godot: validar navegação em movimento real](../../domains/software-0010/software/criacao-ia/godot-validar-navegacao-em-movimento-real.md) — `software.criacao_ia.tranche01.000060`

### Animação e exportação de conteúdo de jogo no Blender

61. [Blender: organizar clips como Actions](../../domains/software-0010/software/criacao-ia/blender-organizar-clips-como-actions.md) — `software.criacao_ia.tranche01.000061`
62. [Blender: nomear Actions para o pipeline](../../domains/software-0010/software/criacao-ia/blender-nomear-actions-para-o-pipeline.md) — `software.criacao_ia.tranche01.000062`
63. [Blender: preservar ações com NLA](../../domains/software-0010/software/criacao-ia/blender-preservar-acoes-com-nla.md) — `software.criacao_ia.tranche01.000063`
64. [Blender: conferir intervalos de keyframes](../../domains/software-0010/software/criacao-ia/blender-conferir-intervalos-de-keyframes.md) — `software.criacao_ia.tranche01.000064`
65. [Blender: validar o rig antes de exportar](../../domains/software-0010/software/criacao-ia/blender-validar-o-rig-antes-de-exportar.md) — `software.criacao_ia.tranche01.000065`
66. [Blender: exportar somente o conteúdo necessário](../../domains/software-0010/software/criacao-ia/blender-exportar-somente-o-conteudo-necessario.md) — `software.criacao_ia.tranche01.000066`
67. [Blender: checar compatibilidade de animação glTF](../../domains/software-0010/software/criacao-ia/blender-checar-compatibilidade-de-animacao-gltf.md) — `software.criacao_ia.tranche01.000067`
68. [Blender: controlar múltiplas Actions no export](../../domains/software-0010/software/criacao-ia/blender-controlar-multiplas-actions-no-export.md) — `software.criacao_ia.tranche01.000068`
69. [Blender: separar movimento in-place e root motion](../../domains/software-0010/software/criacao-ia/blender-separar-movimento-in-place-e-root-motion.md) — `software.criacao_ia.tranche01.000069`
70. [Blender: revisar animação dentro do jogo](../../domains/software-0010/software/criacao-ia/blender-revisar-animacao-dentro-do-jogo.md) — `software.criacao_ia.tranche01.000070`

### Cinematics e renders para jogos na Unreal Engine

71. [Unreal Sequencer: distinguir asset e actor](../../domains/software-0010/software/criacao-ia/unreal-sequencer-distinguir-asset-e-actor.md) — `software.criacao_ia.tranche01.000071`
72. [Unreal Sequencer: animar com tracks e keyframes](../../domains/software-0010/software/criacao-ia/unreal-sequencer-animar-com-tracks-e-keyframes.md) — `software.criacao_ia.tranche01.000072`
73. [Unreal Sequencer: construir cortes de câmera](../../domains/software-0010/software/criacao-ia/unreal-sequencer-construir-cortes-de-camera.md) — `software.criacao_ia.tranche01.000073`
74. [Unreal Sequencer: organizar Shots e Sub-Sequences](../../domains/software-0010/software/criacao-ia/unreal-sequencer-organizar-shots-e-sub-sequences.md) — `software.criacao_ia.tranche01.000074`
75. [Unreal: capturar Takes com Take Recorder](../../domains/software-0010/software/criacao-ia/unreal-capturar-takes-com-take-recorder.md) — `software.criacao_ia.tranche01.000075`
76. [Unreal: acionar Sequencer durante gameplay](../../domains/software-0010/software/criacao-ia/unreal-acionar-sequencer-durante-gameplay.md) — `software.criacao_ia.tranche01.000076`
77. [Unreal: montar uma fila de renderização](../../domains/software-0010/software/criacao-ia/unreal-montar-uma-fila-de-renderizacao.md) — `software.criacao_ia.tranche01.000077`
78. [Unreal: versionar presets e configurações de render](../../domains/software-0010/software/criacao-ia/unreal-versionar-presets-e-configuracoes-de-render.md) — `software.criacao_ia.tranche01.000078`
79. [Unreal: revisar sequência renderizada além do viewport](../../domains/software-0010/software/criacao-ia/unreal-revisar-sequencia-renderizada-alem-do-viewport.md) — `software.criacao_ia.tranche01.000079`
80. [Unreal: manter renders rastreáveis](../../domains/software-0010/software/criacao-ia/unreal-manter-renders-rastreaveis.md) — `software.criacao_ia.tranche01.000080`

### Workflows de geração de vídeo e assets com ComfyUI

81. [ComfyUI: ler um workflow como grafo](../../domains/software-0010/software/criacao-ia/comfyui-ler-um-workflow-como-grafo.md) — `software.criacao_ia.tranche01.000081`
82. [ComfyUI: instalar modelos nos caminhos esperados](../../domains/software-0010/software/criacao-ia/comfyui-instalar-modelos-nos-caminhos-esperados.md) — `software.criacao_ia.tranche01.000082`
83. [ComfyUI: escolher template antes de montar do zero](../../domains/software-0010/software/criacao-ia/comfyui-escolher-template-antes-de-montar-do-zero.md) — `software.criacao_ia.tranche01.000083`
84. [ComfyUI: escolher text-to-video ou image-to-video](../../domains/software-0010/software/criacao-ia/comfyui-escolher-text-to-video-ou-image-to-video.md) — `software.criacao_ia.tranche01.000084`
85. [ComfyUI: controlar duração e número de frames](../../domains/software-0010/software/criacao-ia/comfyui-controlar-duracao-e-numero-de-frames.md) — `software.criacao_ia.tranche01.000085`
86. [ComfyUI: ajustar prompt sem quebrar o grafo](../../domains/software-0010/software/criacao-ia/comfyui-ajustar-prompt-sem-quebrar-o-grafo.md) — `software.criacao_ia.tranche01.000086`
87. [ComfyUI: usar frames de referência com cautela](../../domains/software-0010/software/criacao-ia/comfyui-usar-frames-de-referencia-com-cautela.md) — `software.criacao_ia.tranche01.000087`
88. [ComfyUI: salvar e versionar o workflow](../../domains/software-0010/software/criacao-ia/comfyui-salvar-e-versionar-o-workflow.md) — `software.criacao_ia.tranche01.000088`
89. [ComfyUI: gerenciar dependências de custom nodes](../../domains/software-0010/software/criacao-ia/comfyui-gerenciar-dependencias-de-custom-nodes.md) — `software.criacao_ia.tranche01.000089`
90. [ComfyUI: aprovar asset gerado para produção](../../domains/software-0010/software/criacao-ia/comfyui-aprovar-asset-gerado-para-producao.md) — `software.criacao_ia.tranche01.000090`

### Tutoriais e documentação técnica para software, apps e jogos

91. [Documentação: escolher entre tutorial e referência](../../domains/software-0010/software/criacao-ia/documentacao-escolher-entre-tutorial-e-referencia.md) — `software.criacao_ia.tranche01.000091`
92. [Documentação: declarar leitor e resultado](../../domains/software-0010/software/criacao-ia/documentacao-declarar-leitor-e-resultado.md) — `software.criacao_ia.tranche01.000092`
93. [Documentação: fixar versões e pré-requisitos](../../domains/software-0010/software/criacao-ia/documentacao-fixar-versoes-e-pre-requisitos.md) — `software.criacao_ia.tranche01.000093`
94. [Tutorial: construir exemplo de ponta a ponta](../../domains/software-0010/software/criacao-ia/tutorial-construir-exemplo-de-ponta-a-ponta.md) — `software.criacao_ia.tranche01.000094`
95. [How-to: organizar passos por tarefa](../../domains/software-0010/software/criacao-ia/how-to-organizar-passos-por-tarefa.md) — `software.criacao_ia.tranche01.000095`
96. [Referência: descrever campos com precisão](../../domains/software-0010/software/criacao-ia/referencia-descrever-campos-com-precisao.md) — `software.criacao_ia.tranche01.000096`
97. [Documentação: tornar resultado e verificação explícitos](../../domains/software-0010/software/criacao-ia/documentacao-tornar-resultado-e-verificacao-explicitos.md) — `software.criacao_ia.tranche01.000097`
98. [Documentação: usar imagens acessíveis e úteis](../../domains/software-0010/software/criacao-ia/documentacao-usar-imagens-acessiveis-e-uteis.md) — `software.criacao_ia.tranche01.000098`
99. [Documentação: executar exemplos de código](../../domains/software-0010/software/criacao-ia/documentacao-executar-exemplos-de-codigo.md) — `software.criacao_ia.tranche01.000099`
100. [Documentação: revisar tutorial gerado por IA](../../domains/software-0010/software/criacao-ia/documentacao-revisar-tutorial-gerado-por-ia.md) — `software.criacao_ia.tranche01.000100`

## Tranche 2 — Claude Code, Continue.dev, Cursor, Godot IA, Unity Animation Rigging, Unreal StateTree, PBR 2D, Voz/Áudio IA, QA Playtesting e Diátaxis (100 notas)

IDs materiais: `software.criacao_ia.tranche02.000101`–`software.criacao_ia.tranche02.000200`. Cada tópico tem fontes primárias indicadas na própria nota.

### Claude Code CLI & Anthropic API para Desenvolvimento Assistido

101. [Claude Code: iniciar sessão interativa no terminal](../../domains/software-0010/software/criacao-ia/claude-code-iniciar-sessao-interativa-cli.md) — `software.criacao_ia.tranche02.000101`
102. [Claude Code: configurar instruções de projeto no arquivo CLAUDE.md](../../domains/software-0010/software/criacao-ia/claude-code-definir-instrucoes-claudemd.md) — `software.criacao_ia.tranche02.000102`
103. [Claude Code: gerenciar permissões de execução de comandos](../../domains/software-0010/software/criacao-ia/claude-code-gerenciar-permissoes-de-execucao-de-comandos.md) — `software.criacao_ia.tranche02.000103`
104. [Anthropic API: aplicar Prompt Caching em bases extensas](../../domains/software-0010/software/criacao-ia/claude-code-usar-prompt-caching-para-bases-extensas.md) — `software.criacao_ia.tranche02.000104`
105. [Model Context Protocol: conectar servidores MCP de contexto](../../domains/software-0010/software/criacao-ia/mcp-conectar-servidores-para-contexto-externo.md) — `software.criacao_ia.tranche02.000105`
106. [Anthropic API: estruturar mensagens de retorno em tool_result](../../domains/software-0010/software/criacao-ia/anthropic-api-estruturar-mensagens-tool-result.md) — `software.criacao_ia.tranche02.000106`
107. [Claude Code: orquestrar subagentes especializados](../../domains/software-0010/software/criacao-ia/claude-code-orquestrar-subagentes-especializados.md) — `software.criacao_ia.tranche02.000107`
108. [Anthropic API: controlar limites com max_tokens e stop_sequences](../../domains/software-0010/software/criacao-ia/anthropic-api-controlar-limites-com-max-tokens.md) — `software.criacao_ia.tranche02.000108`
109. [Anthropic API: depurar layouts com mensagens de visão](../../domains/software-0010/software/criacao-ia/anthropic-api-depurar-layout-com-mensagens-de-visao.md) — `software.criacao_ia.tranche02.000109`
110. [Claude Code: validar testes e diff antes do commit](../../domains/software-0010/software/criacao-ia/claude-code-validar-testes-antes-do-commit.md) — `software.criacao_ia.tranche02.000110`

### Agentes de Código Locais e Continue.dev

111. [Continue.dev: configurar provedores locais no config.json](../../domains/software-0010/software/criacao-ia/continue-dev-configurar-provedor-local.md) — `software.criacao_ia.tranche02.000111`
112. [Continue.dev: indexar codebase com embeddings locais](../../domains/software-0010/software/criacao-ia/continue-dev-indexar-codebase-com-embeddings-locais.md) — `software.criacao_ia.tranche02.000112`
113. [Continue.dev: customizar context providers para documentação](../../domains/software-0010/software/criacao-ia/continue-dev-customizar-context-providers.md) — `software.criacao_ia.tranche02.000113`
114. [Continue.dev: separar modelo de autocomplete Tab do modelo de chat](../../domains/software-0010/software/criacao-ia/continue-dev-separar-modelo-de-autocomplete-tab.md) — `software.criacao_ia.tranche02.000114`
115. [Ollama: ajustar num_ctx e quantização GGUF para estabilidade de memória](../../domains/software-0010/software/criacao-ia/ollama-ajustar-num-ctx-e-quantizacao-gguf.md) — `software.criacao_ia.tranche02.000115`
116. [Ollama: gerenciar permanência na VRAM com keep_alive](../../domains/software-0010/software/criacao-ia/ollama-gerenciar-permanencia-com-keep-alive.md) — `software.criacao_ia.tranche02.000116`
117. [llama.cpp: servir endpoint HTTP compatível com OpenAI](../../domains/software-0010/software/criacao-ia/llamacpp-servir-endpoint-openai-compativel.md) — `software.criacao_ia.tranche02.000117`
118. [Continue.dev: padronizar regras de projeto e system prompts](../../domains/software-0010/software/criacao-ia/continue-dev-padronizar-regras-de-projeto.md) — `software.criacao_ia.tranche02.000118`
119. [Continue.dev: auditar requisições e logs de execução local](../../domains/software-0010/software/criacao-ia/continue-dev-auditar-requisicoes-e-logs-locais.md) — `software.criacao_ia.tranche02.000119`
120. [IA Local: garantir isolamento de rede para código sensível](../../domains/software-0010/software/criacao-ia/ia-local-garantir-isolamento-sem-conexao-externa.md) — `software.criacao_ia.tranche02.000120`

### Cursor e Context Engineering para Criação de Software

121. [Cursor: padronizar convenções no arquivo .cursorrules](../../domains/software-0010/software/criacao-ia/cursor-padronizar-regras-com-cursorrules.md) — `software.criacao_ia.tranche02.000121`
122. [Cursor: otimizar indexação vetorial com .cursorignore](../../domains/software-0010/software/criacao-ia/cursor-otimizar-indexacao-com-cursorignore.md) — `software.criacao_ia.tranche02.000122`
123. [Cursor: usar símbolos de contexto @Docs e @Git](../../domains/software-0010/software/criacao-ia/cursor-usar-simbolos-de-contexto-docs-e-git.md) — `software.criacao_ia.tranche02.000123`
124. [Cursor Composer: coordenar edições multi-arquivo com checkpoint](../../domains/software-0010/software/criacao-ia/cursor-composer-coordenar-edicoes-multi-arquivo.md) — `software.criacao_ia.tranche02.000124`
125. [Cursor: executar scripts no terminal integrado com supervisão](../../domains/software-0010/software/criacao-ia/cursor-executar-scripts-no-terminal-integrado.md) — `software.criacao_ia.tranche02.000125`
126. [Cursor: priorizar arquivos essenciais na janela de contexto](../../domains/software-0010/software/criacao-ia/cursor-priorizar-janela-de-contexto-essencial.md) — `software.criacao_ia.tranche02.000126`
127. [Cursor: revisar diffs inline com rejeição granular](../../domains/software-0010/software/criacao-ia/cursor-revisar-diffs-inline-com-rejeicao-parcial.md) — `software.criacao_ia.tranche02.000127`
128. [Engenharia de Contexto: usar testes unitários como especificação](../../domains/software-0010/software/criacao-ia/context-engineering-usar-testes-como-especificacao.md) — `software.criacao_ia.tranche02.000128`
129. [Engenharia de Contexto: injetar tipos estáticos para evitar alucinações](../../domains/software-0010/software/criacao-ia/context-engineering-injetar-tipos-estaticos-e-interfaces.md) — `software.criacao_ia.tranche02.000129`
130. [Cursor: corrigir erros alimentando diagnósticos do compilador](../../domains/software-0010/software/criacao-ia/cursor-corrigir-erros-com-diagnosticos-do-compilador.md) — `software.criacao_ia.tranche02.000130`

### Máquinas de Estados e IA de Gameplay no Godot 4

131. [Godot: estruturar máquina de estados hierárquica em GDScript](../../domains/software-0010/software/criacao-ia/godot-estruturar-maquina-de-estados-hierarquica.md) — `software.criacao_ia.tranche02.000131`
132. [Godot: desacoplar transições de estado de IA com sinais](../../domains/software-0010/software/criacao-ia/godot-desacoplar-transicoes-com-sinais.md) — `software.criacao_ia.tranche02.000132`
133. [Godot: implementar comportamentos de direção Seek e Flee](../../domains/software-0010/software/criacao-ia/godot-implementar-steering-seek-e-flee.md) — `software.criacao_ia.tranche02.000133`
134. [Godot: combinar navegação Wander e Pursuit com predição](../../domains/software-0010/software/criacao-ia/godot-combinar-wander-e-pursuit-com-predicao.md) — `software.criacao_ia.tranche02.000134`
135. [Godot: calcular cone de visão com Area3D e produto escalar](../../domains/software-0010/software/criacao-ia/godot-calcular-cone-de-visao-com-area3d-e-dot-product.md) — `software.criacao_ia.tranche02.000135`
136. [Godot: desviar de obstáculos com múltiplos sensores RayCast3D](../../domains/software-0010/software/criacao-ia/godot-desviar-de-obstaculos-com-raycast3d-multiplos.md) — `software.criacao_ia.tranche02.000136`
137. [Godot: selecionar alvos de combate por distância e ameaça](../../domains/software-0010/software/criacao-ia/godot-selecionar-alvos-por-distancia-e-ameaca.md) — `software.criacao_ia.tranche02.000137`
138. [Godot: sincronizar máquina de estados com o nó AnimationTree](../../domains/software-0010/software/criacao-ia/godot-sincronizar-ia-com-animationtree.md) — `software.criacao_ia.tranche02.000138`
139. [Godot: propagar eventos sonoros para percepção auditiva de NPCs](../../domains/software-0010/software/criacao-ia/godot-propagar-eventos-sonoros-para-audicao-de-npcs.md) — `software.criacao_ia.tranche02.000139`
140. [Godot: depurar vetores e decisões de IA com funções _draw](../../domains/software-0010/software/criacao-ia/godot-depurar-vetores-de-ia-com-draw-line.md) — `software.criacao_ia.tranche02.000140`

### Rigging de Animação e Utility AI no Unity

141. [Unity: montar componente RigBuilder e camadas de restrição](../../domains/software-0010/software/criacao-ia/unity-animation-rigging-montar-rigbuilder.md) — `software.criacao_ia.tranche02.000141`
142. [Unity: ajustar pés em terrenos inclinados com Two-Bone IK](../../domains/software-0010/software/criacao-ia/unity-animation-rigging-ajustar-pes-com-two-bone-ik.md) — `software.criacao_ia.tranche02.000142`
143. [Unity: orientar cabeça e olhar com Multi-Aim Constraint](../../domains/software-0010/software/criacao-ia/unity-animation-rigging-orientar-olhar-com-multi-aim.md) — `software.criacao_ia.tranche02.000143`
144. [Unity: suavizar movimento de armas e acessórios com Damp Transform](../../domains/software-0010/software/criacao-ia/unity-animation-rigging-suavizar-com-damp-transform.md) — `software.criacao_ia.tranche02.000144`
145. [Unity: avaliar decisões de NPCs com curvas de resposta em Utility AI](../../domains/software-0010/software/criacao-ia/unity-utility-ai-avaliar-decisoes-com-curvas.md) — `software.criacao_ia.tranche02.000145`
146. [Unity: compor fatores de saúde e distância em pontuações de ação](../../domains/software-0010/software/criacao-ia/unity-utility-ai-compor-fatores-de-saude-e-distancia.md) — `software.criacao_ia.tranche02.000146`
147. [Unity: reconstruir NavMeshSurface em tempo de execução](../../domains/software-0010/software/criacao-ia/unity-navmesh-reconstruir-superficie-em-runtime.md) — `software.criacao_ia.tranche02.000147`
148. [Unity: atribuir custos diferenciados por tipo de área no NavMesh](../../domains/software-0010/software/criacao-ia/unity-navmesh-atribuir-custos-por-area-de-terreno.md) — `software.criacao_ia.tranche02.000148`
149. [Unity: mesclar animações procedurais usando a PlayableGraph API](../../domains/software-0010/software/criacao-ia/unity-playablegraph-mesclar-animacoes-procedurais.md) — `software.criacao_ia.tranche02.000149`
150. [Unity: visualizar sensores e scores de utilidade com Gizmos de cena](../../domains/software-0010/software/criacao-ia/unity-ia-visualizar-decisoes-com-gizmos-de-cena.md) — `software.criacao_ia.tranche02.000150`

### StateTree e Smart Objects na Unreal Engine 5

151. [Unreal Engine: estruturar hierarquia de estados leves no StateTree](../../domains/software-0010/software/criacao-ia/unreal-statetree-estruturar-hierarquia-de-estados.md) — `software.criacao_ia.tranche02.000151`
152. [Unreal Engine: extrair contexto e dados de mundo com StateTree Evaluators](../../domains/software-0010/software/criacao-ia/unreal-statetree-extrair-contexto-com-evaluators.md) — `software.criacao_ia.tranche02.000152`
153. [Unreal Engine: implementar tarefas atômicas com StateTree Tasks](../../domains/software-0010/software/criacao-ia/unreal-statetree-implementar-tasks-assincronas.md) — `software.criacao_ia.tranche02.000153`
154. [Unreal Engine: configurar Smart Object Definitions e slots de animação](../../domains/software-0010/software/criacao-ia/unreal-smart-objects-configurar-slots-de-interacao.md) — `software.criacao_ia.tranche02.000154`
155. [Unreal Engine: gerenciar reservas concorrentes com Smart Object Subsystem](../../domains/software-0010/software/criacao-ia/unreal-smart-objects-gerenciar-reservas-concorrentes.md) — `software.criacao_ia.tranche02.000155`
156. [Unreal Engine: conectar navegação a Smart Objects via StateTree Tasks](../../domains/software-0010/software/criacao-ia/unreal-smart-objects-conectar-a-tarefas-do-statetree.md) — `software.criacao_ia.tranche02.000156`
157. [Unreal Engine: simular multidões com arquitetura ECS MassEntity e Mass AI](../../domains/software-0010/software/criacao-ia/unreal-mass-ai-processar-agentes-com-massentity.md) — `software.criacao_ia.tranche02.000157`
158. [Unreal Engine: acionar Gameplay Abilities a partir de decisões do AIController](../../domains/software-0010/software/criacao-ia/unreal-gas-acionar-habilidades-pelo-ai-controller.md) — `software.criacao_ia.tranche02.000158`
159. [Unreal Engine: alinhar pontos de contato e saltos com Motion Warping](../../domains/software-0010/software/criacao-ia/unreal-motion-warping-alinhar-interacoes-fisicas.md) — `software.criacao_ia.tranche02.000159`
160. [Unreal Engine: inspecionar transições de IA com o Gameplay Debugger](../../domains/software-0010/software/criacao-ia/unreal-gameplay-debugger-inspecionar-ia-em-runtime.md) — `software.criacao_ia.tranche02.000160`

### Texturização Procedural e Pipelines 2D com IA para Jogos

161. [Texturas com IA: gerar padrões PBR contínuos e sem emendas](../../domains/software-0010/software/criacao-ia/texturas-ia-gerar-padroes-pbr-seamless-tileaveis.md) — `software.criacao_ia.tranche02.000161`
162. [Texturas com IA: derivar mapas de normal e roughness de alturas](../../domains/software-0010/software/criacao-ia/texturas-ia-derivar-mapas-de-normal-e-roughness.md) — `software.criacao_ia.tranche02.000162`
163. [ControlNet: guiar geração de assets com mapas de borda Canny e profundidade](../../domains/software-0010/software/criacao-ia/controlnet-guiar-geracao-com-bordas-canny-e-depth.md) — `software.criacao_ia.tranche02.000163`
164. [ControlNet: fixar postura anatômica de sprites 2D com OpenPose](../../domains/software-0010/software/criacao-ia/controlnet-fixar-postura-de-sprites-com-openpose.md) — `software.criacao_ia.tranche02.000164`
165. [Pixel Art com IA: alinhar arte à grade de pixels e limitar contagem de cores](../../domains/software-0010/software/criacao-ia/pixel-art-ia-alinhar-a-grade-e-limitar-paleta.md) — `software.criacao_ia.tranche02.000165`
166. [Sprite Sheets com IA: empacotar e fatiar atlas com margens uniformes](../../domains/software-0010/software/criacao-ia/spritesheet-ia-empacotar-e-fatiar-atlas-de-sprites.md) — `software.criacao_ia.tranche02.000166`
167. [Texturas com IA: remover sombras embutidas para obter albedo neutro](../../domains/software-0010/software/criacao-ia/texturas-ia-remover-sombras-para-albedo-neutro.md) — `software.criacao_ia.tranche02.000167`
168. [Otimização de Texturas: comprimir mapas PBR em BC7 e ASTC para VRAM](../../domains/software-0010/software/criacao-ia/assets-ia-otimizar-compressao-bc7-e-astc-em-vram.md) — `software.criacao_ia.tranche02.000168`
169. [Concept Art com IA: refinar detalhes localizados através de inpainting](../../domains/software-0010/software/criacao-ia/concept-art-ia-refinar-detalhes-com-inpainting.md) — `software.criacao_ia.tranche02.000169`
170. [Pipeline de Assets: validar escala métrica e pivôs antes do import](../../domains/software-0010/software/criacao-ia/pipeline-assets-validar-escala-metrica-e-pivots.md) — `software.criacao_ia.tranche02.000170`

### Síntese de Voz e Áudio para Jogos com IA

171. [Áudio com IA: sintetizar falas dinâmicas de NPCs via chamadas assíncronas](../../domains/software-0010/software/criacao-ia/audio-ia-sintetizar-falas-dinamicas-de-npcs.md) — `software.criacao_ia.tranche02.000171`
172. [Áudio com IA: armazenar falas geradas em cache de disco local](../../domains/software-0010/software/criacao-ia/audio-ia-armazenar-linhas-de-voz-em-cache-local.md) — `software.criacao_ia.tranche02.000172`
173. [Lip Sync com IA: extrair visemas fonéticos de áudio com Rhubarb](../../domains/software-0010/software/criacao-ia/audio-ia-extrair-visemas-para-lip-sync-com-rhubarb.md) — `software.criacao_ia.tranche02.000173`
174. [Animação Facial: mapear visemas fonéticos a blend shapes do modelo 3D](../../domains/software-0010/software/criacao-ia/audio-ia-mapear-visemas-a-blend-shapes-faciais.md) — `software.criacao_ia.tranche02.000174`
175. [FMOD: rotear vozes sintéticas para barramentos de diálogo com efeitos](../../domains/software-0010/software/criacao-ia/fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo.md) — `software.criacao_ia.tranche02.000175`
176. [Áudio 3D: configurar atenuação logarítmica e posicionamento espacial](../../domains/software-0010/software/criacao-ia/audio-ia-configurar-espacializacao-3d-e-atenuacao.md) — `software.criacao_ia.tranche02.000176`
177. [Mixagem de Som: aplicar audio ducking automático durante falas de IA](../../domains/software-0010/software/criacao-ia/mixagem-aplicar-audio-ducking-durante-vozes-de-ia.md) — `software.criacao_ia.tranche02.000177`
178. [Legendas: sincronizar exibição de texto com timestamps por palavra](../../domains/software-0010/software/criacao-ia/legendas-sincronizar-texto-com-timestamps-de-palavras.md) — `software.criacao_ia.tranche02.000178`
179. [Áudio com IA: modular parâmetros de prosódia e estilo por emoção](../../domains/software-0010/software/criacao-ia/audio-ia-modular-prosodia-e-estabilidade-por-emocao.md) — `software.criacao_ia.tranche02.000179`
180. [Resiliência de Áudio: prover falas pré-gravadas como fallback de rede](../../domains/software-0010/software/criacao-ia/audio-ia-prover-linhas-de-dialogo-de-fallback.md) — `software.criacao_ia.tranche02.000180`

### Testes Automatizados e QA de Jogos com IA e Bots

181. [QA de Jogos: executar playtests funcionais headless na pipeline de CI](../../domains/software-0010/software/criacao-ia/qa-jogos-executar-playtests-headless-em-ci.md) — `software.criacao_ia.tranche02.000181`
182. [IA de Testes: encapsular loop de gameplay como ambiente Farama Gymnasium](../../domains/software-0010/software/criacao-ia/qa-jogos-encapsular-loop-em-ambiente-gymnasium.md) — `software.criacao_ia.tranche02.000182`
183. [QA de Jogos: descobrir falhas de colisão com bots exploradores](../../domains/software-0010/software/criacao-ia/qa-jogos-descobrir-colisoes-com-agentes-exploradores.md) — `software.criacao_ia.tranche02.000183`
184. [Telemetria de Jogos: gerar heatmaps de mortes e coordenadas de jogadores](../../domains/software-0010/software/criacao-ia/telemetria-jogos-gerar-heatmaps-de-morte-e-posicao.md) — `software.criacao_ia.tranche02.000184`
185. [QA Multiplayer: simular carga de servidor instanciando bots sintéticos](../../domains/software-0010/software/criacao-ia/qa-jogos-simular-carga-de-servidor-com-bots-leves.md) — `software.criacao_ia.tranche02.000185`
186. [Análise de Jogos: detectar desbalanceamento de armas e classes em logs](../../domains/software-0010/software/criacao-ia/qa-jogos-detectar-desbalanceamento-por-metricas-de-partida.md) — `software.criacao_ia.tranche02.000186`
187. [QA de Física: validar determinismo em replays com passos de tempo fixos](../../domains/software-0010/software/criacao-ia/qa-jogos-validar-determinismo-de-fisica-em-fixed-ticks.md) — `software.criacao_ia.tranche02.000187`
188. [QA de UI: automatizar navegação em telas de inventário e menus](../../domains/software-0010/software/criacao-ia/qa-jogos-automatizar-fluxos-de-ui-e-inventario.md) — `software.criacao_ia.tranche02.000188`
189. [QA de Gameplay: criar microcenários isolados para regressão de mecânicas](../../domains/software-0010/software/criacao-ia/qa-jogos-isolar-cenarios-de-regressao-de-gameplay.md) — `software.criacao_ia.tranche02.000189`
190. [Performance de Jogos: auditar picos de frame time com profiler em linha de comando](../../domains/software-0010/software/criacao-ia/qa-jogos-auditar-picos-de-frame-time-com-profiler-cli.md) — `software.criacao_ia.tranche02.000190`

### Documentação Técnica Interativa e Diátaxis para Criadores

191. [Framework Diátaxis: estruturar documentação técnica em quatro quadrantes](../../domains/software-0010/software/criacao-ia/diataxis-aplicar-os-quatro-quadrantes-de-documentacao.md) — `software.criacao_ia.tranche02.000191`
192. [Diátaxis Tutoriais: conduzir novos usuários ao primeiro resultado palpável](../../domains/software-0010/software/criacao-ia/diataxis-construir-tutoriais-focados-no-primeiro-sucesso.md) — `software.criacao_ia.tranche02.000192`
193. [Diátaxis How-To: redigir passos objetivos para tarefas práticas de produção](../../domains/software-0010/software/criacao-ia/diataxis-redigir-guias-how-to-para-tarefas-de-producao.md) — `software.criacao_ia.tranche02.000193`
194. [Diátaxis Referência: catalogar APIs e parâmetros com precisão e sem narrativa](../../domains/software-0010/software/criacao-ia/diataxis-organizar-referencias-tecnicas-sem-narrativa.md) — `software.criacao_ia.tranche02.000194`
195. [Diátaxis Explicação: aprofundar decisões arquiteturais e modelos conceituais](../../domains/software-0010/software/criacao-ia/diataxis-elaborar-artigos-de-explicacao-e-design.md) — `software.criacao_ia.tranche02.000195`
196. [Documentação Interativa: incorporar sandboxes de código executável em tutoriais](../../domains/software-0010/software/criacao-ia/documentacao-incorporar-sandboxes-e-demos-interativos.md) — `software.criacao_ia.tranche02.000196`
197. [Documentação de Arte: detalhar entradas e nós matemáticos de shader graphs](../../domains/software-0010/software/criacao-ia/documentacao-explicar-grafos-de-shaders-e-materiais.md) — `software.criacao_ia.tranche02.000197`
198. [Manutenção de Software: documentar breaking changes e guias de migração](../../domains/software-0010/software/criacao-ia/documentacao-manter-guias-de-migracao-e-breaking-changes.md) — `software.criacao_ia.tranche02.000198`
199. [CI para Documentação: testar snippets de código e validar links quebrados](../../domains/software-0010/software/criacao-ia/documentacao-automatizar-validacao-de-links-e-snippets-em-ci.md) — `software.criacao_ia.tranche02.000199`
200. [Governança Técnica: aplicar checklist de verificação em tutoriais gerados por IA](../../domains/software-0010/software/criacao-ia/documentacao-aplicar-checklist-em-tutoriais-gerados-por-ia.md) — `software.criacao_ia.tranche02.000200`

## Tranche 3 — LangGraph, MCP, OpenAI Agents SDK, Unreal PCG, Blender Geometry Nodes, OpenUSD, FFmpeg, Playwright avançado, OpenTelemetry GenAI e OpenAPI 3.1.1 (100 notas)

IDs materiais: `software.criacao_ia.tranche03.000201`–`software.criacao_ia.tranche03.000300`. Playwright foi selecionado em assuntos não cobertos pelo inventário existente; OpenTelemetry é específico às convenções GenAI; OpenAPI aborda semântica própria de OAS 3.1.1.

### LangGraph: persistência, controle de execução e streaming

201. [LangGraph: retomar interrupts sem duplicar efeitos colaterais](../../domains/software-0010/software/criacao-ia/langgraph-interrupt-retomar-sem-repetir-efeitos.md) — `software.criacao_ia.tranche03.000201`
202. [LangGraph: distinguir thread_id de checkpoint_id](../../domains/software-0010/software/criacao-ia/langgraph-thread-id-e-checkpoint-id.md) — `software.criacao_ia.tranche03.000202`
203. [LangGraph: escolher replay ou fork no time travel](../../domains/software-0010/software/criacao-ia/langgraph-time-travel-replay-ou-fork.md) — `software.criacao_ia.tranche03.000203`
204. [LangGraph: separar checkpointer de store de longo prazo](../../domains/software-0010/software/criacao-ia/langgraph-checkpointer-versus-store.md) — `software.criacao_ia.tranche03.000204`
205. [LangGraph: combinar atualizações paralelas com reducers](../../domains/software-0010/software/criacao-ia/langgraph-supersteps-e-reducers-paralelos.md) — `software.criacao_ia.tranche03.000205`
206. [LangGraph Functional API: persistir resultados com @task](../../domains/software-0010/software/criacao-ia/langgraph-functional-api-task-result-checkpoint.md) — `software.criacao_ia.tranche03.000206`
207. [LangGraph: usar partes tipadas no streaming v2](../../domains/software-0010/software/criacao-ia/langgraph-streaming-v2-partes-tipadas.md) — `software.criacao_ia.tranche03.000207`
208. [LangGraph: consumir projeções do event streaming v3](../../domains/software-0010/software/criacao-ia/langgraph-event-streaming-projecoes-concorrentes.md) — `software.criacao_ia.tranche03.000208`
209. [LangGraph: separar schemas de entrada, saída e estado interno](../../domains/software-0010/software/criacao-ia/langgraph-schemas-entrada-saida-e-estado-privado.md) — `software.criacao_ia.tranche03.000209`
210. [LangGraph: planejar retenção e limpeza de checkpoints](../../domains/software-0010/software/criacao-ia/langgraph-politica-retencao-checkpoints.md) — `software.criacao_ia.tranche03.000210`

### MCP: especificação 2026-07-28, transportes e recursos especializados

211. [MCP stdio: framing por linha e stdout exclusivo do protocolo](../../domains/software-0010/software/criacao-ia/mcp-stdio-framing-e-stdout-limpo.md) — `software.criacao_ia.tranche03.000211`
212. [MCP Streamable HTTP 2026: requests POST sem sessão implícita](../../domains/software-0010/software/criacao-ia/mcp-streamable-http-versao-2026-stateless.md) — `software.criacao_ia.tranche03.000212`
213. [MCP 2026: carregar versão e capacidades em _meta por request](../../domains/software-0010/software/criacao-ia/mcp-meta-protocolo-capacidades-por-request.md) — `software.criacao_ia.tranche03.000213`
214. [MCP MRTR: retomar requests com inputResponses e requestState opaco](../../domains/software-0010/software/criacao-ia/mcp-mrtr-input-required-request-state.md) — `software.criacao_ia.tranche03.000214`
215. [MCP: combinar ttlMs, cacheScope e notificações de invalidação](../../domains/software-0010/software/criacao-ia/mcp-cache-ttl-scope-e-invalidacao.md) — `software.criacao_ia.tranche03.000215`
216. [MCP tools/list: catálogo determinístico e schema de entrada executável](../../domains/software-0010/software/criacao-ia/mcp-tools-list-schema-autorizacao.md) — `software.criacao_ia.tranche03.000216`
217. [MCP prompts: distinguir seleção do usuário e autoria do servidor](../../domains/software-0010/software/criacao-ia/mcp-prompts-selecao-controlada-pelo-usuario.md) — `software.criacao_ia.tranche03.000217`
218. [MCP elicitation: reservar URL mode para credenciais e segredos](../../domains/software-0010/software/criacao-ia/mcp-elicitation-form-url-segredos.md) — `software.criacao_ia.tranche03.000218`
219. [MCP HTTP OAuth: descobrir recurso protegido e registrar cliente](../../domains/software-0010/software/criacao-ia/mcp-oauth-discovery-e-client-registration.md) — `software.criacao_ia.tranche03.000219`
220. [MCP 2026-07-28: preparar migração de handshake e notificações](../../domains/software-0010/software/criacao-ia/mcp-migrar-para-especificacao-2026-07-28.md) — `software.criacao_ia.tranche03.000220`

### OpenAI Agents SDK: orquestração, guardrails, state e tracing

221. [Agents SDK: escolher Agent.as_tool ou handoff](../../domains/software-0010/software/criacao-ia/agents-sdk-especialista-como-tool-ou-handoff.md) — `software.criacao_ia.tranche03.000221`
222. [Agents SDK handoff: modelar destinos como roteamento explícito](../../domains/software-0010/software/criacao-ia/agents-sdk-handoff-destino-fixo.md) — `software.criacao_ia.tranche03.000222`
223. [Agents SDK: validar handoff input em on_handoff](../../domains/software-0010/software/criacao-ia/agents-sdk-on-handoff-autorizacao-antes-de-efeitos.md) — `software.criacao_ia.tranche03.000223`
224. [Agents SDK guardrails: mapear fronteiras de primeiro e último agente](../../domains/software-0010/software/criacao-ia/agents-sdk-guardrails-fronteiras-primeiro-e-ultimo-agente.md) — `software.criacao_ia.tranche03.000224`
225. [Agents SDK streaming: consumir eventos até o iterador terminar](../../domains/software-0010/software/criacao-ia/agents-sdk-streaming-drenar-ate-fim.md) — `software.criacao_ia.tranche03.000225`
226. [Agents SDK: escolher session local ou continuação server-side](../../domains/software-0010/software/criacao-ia/agents-sdk-session-versus-responses-continuation.md) — `software.criacao_ia.tranche03.000226`
227. [Agents SDK: normalizar saída tipada entre handoffs](../../domains/software-0010/software/criacao-ia/agents-sdk-output-type-e-handoffs.md) — `software.criacao_ia.tranche03.000227`
228. [Agents SDK: adiar tool schemas com hosted tool search](../../domains/software-0010/software/criacao-ia/agents-sdk-hosted-tool-search-deferred-loading.md) — `software.criacao_ia.tranche03.000228`
229. [Agents SDK Sessions: limitar histórico lido sem duplicar persistência](../../domains/software-0010/software/criacao-ia/agents-sdk-session-input-callback-historico.md) — `software.criacao_ia.tranche03.000229`
230. [Agents SDK tracing: descarregar spans antes de encerrar um job](../../domains/software-0010/software/criacao-ia/agents-sdk-tracing-flush-workers.md) — `software.criacao_ia.tranche03.000230`

### Unreal Engine 5.8 PCG: geração hierárquica, runtime e GPU

231. [Unreal PCG: partitioned generation divide domínio em células](../../domains/software-0010/software/criacao-ia/ue-pcg-partitioned-generation-grid-celulas.md) — `software.criacao_ia.tranche03.000231`
232. [Unreal PCG: fluxo de dados entre HiGen grid sizes](../../domains/software-0010/software/criacao-ia/ue-pcg-higen-cascata-grid-size.md) — `software.criacao_ia.tranche03.000232`
233. [Unreal PCG: propagar Data Layers e HLOD aos atores gerados](../../domains/software-0010/software/criacao-ia/ue-pcg-world-partition-data-layers-hlod.md) — `software.criacao_ia.tranche03.000233`
234. [Unreal PCG runtime: fontes, raios de geração e limpeza](../../domains/software-0010/software/criacao-ia/ue-pcg-runtime-generation-sources-radii.md) — `software.criacao_ia.tranche03.000234`
235. [Unreal PCG runtime: equilibrar scheduler e células concorrentes](../../domains/software-0010/software/criacao-ia/ue-pcg-scheduler-num-generating-components.md) — `software.criacao_ia.tranche03.000235`
236. [Unreal PCG: interpretar overlay de geração em runtime](../../domains/software-0010/software/criacao-ia/ue-pcg-overlay-runtime-generation.md) — `software.criacao_ia.tranche03.000236`
237. [Unreal PCG runtime: dimensionar pool de Partition Actors](../../domains/software-0010/software/criacao-ia/ue-pcg-runtime-partition-actor-pool.md) — `software.criacao_ia.tranche03.000237`
238. [Unreal PCG: entender cache CPU e orçamento de memória](../../domains/software-0010/software/criacao-ia/ue-pcg-cache-runtime-editor-budget.md) — `software.criacao_ia.tranche03.000238`
239. [Unreal PCG GPU: agrupar nós para reduzir transferências](../../domains/software-0010/software/criacao-ia/ue-pcg-gpu-compute-graph-transferencias.md) — `software.criacao_ia.tranche03.000239`
240. [Unreal PCG GPU: tratar escopo Beta como dependência de engine](../../domains/software-0010/software/criacao-ia/ue-pcg-gpu-beta-nos-suportados.md) — `software.criacao_ia.tranche03.000240`

### Blender 5.2 Geometry Nodes: fields, state, attributes e instancing

241. [Blender Geometry Nodes: fields são avaliados no contexto do consumidor](../../domains/software-0010/software/criacao-ia/blender-geometry-nodes-field-contexto-avaliacao.md) — `software.criacao_ia.tranche03.000241`
242. [Blender: capturar fields antes de uma conversão de geometria](../../domains/software-0010/software/criacao-ia/blender-capture-attribute-antes-de-conversao.md) — `software.criacao_ia.tranche03.000242`
243. [Blender Geometry Nodes: escolher atributo anônimo ou nomeado](../../domains/software-0010/software/criacao-ia/blender-anonymous-versus-named-attributes.md) — `software.criacao_ia.tranche03.000243`
244. [Blender Geometry Nodes: auditar domínio e conversão de atributos](../../domains/software-0010/software/criacao-ia/blender-attributes-domain-conversoes-implicitas.md) — `software.criacao_ia.tranche03.000244`
245. [Blender Repeat Zone: distinguir feedback de entradas constantes](../../domains/software-0010/software/criacao-ia/blender-repeat-zone-iters-e-inputs-externos.md) — `software.criacao_ia.tranche03.000245`
246. [Blender Geometry Nodes: escolher Repeat ou Simulation Zone](../../domains/software-0010/software/criacao-ia/blender-repeat-versus-simulation-zone.md) — `software.criacao_ia.tranche03.000246`
247. [Blender Simulation Zone: declarar atributos anônimos no estado](../../domains/software-0010/software/criacao-ia/blender-simulation-anonymous-attributes-state.md) — `software.criacao_ia.tranche03.000247`
248. [Blender Simulation Zone: gerenciar cache e bake para render](../../domains/software-0010/software/criacao-ia/blender-simulation-cache-bake-render.md) — `software.criacao_ia.tranche03.000248`
249. [Blender Geometry Nodes: manter instâncias até precisar realizá-las](../../domains/software-0010/software/criacao-ia/blender-instancing-realize-atributos-custo.md) — `software.criacao_ia.tranche03.000249`
250. [Blender Geometry Nodes: inspecionar fields com Viewer e domain explícito](../../domains/software-0010/software/criacao-ia/blender-viewer-domain-spreadsheet-debug.md) — `software.criacao_ia.tranche03.000250`

### OpenUSD 26.08: composition, variants, time and asset resolution

251. [OpenUSD: entender UsdStage como vista composta de layers](../../domains/software-0010/software/criacao-ia/openusd-stage-composed-view-layers.md) — `software.criacao_ia.tranche03.000251`
252. [OpenUSD: tratar load rules como working set de payloads](../../domains/software-0010/software/criacao-ia/openusd-load-rules-payloads-working-set.md) — `software.criacao_ia.tranche03.000252`
253. [OpenUSD: escolher reference ou payload para composição diferida](../../domains/software-0010/software/criacao-ia/openusd-reference-versus-payload.md) — `software.criacao_ia.tranche03.000253`
254. [OpenUSD: resolver context e asset identifiers de pipeline](../../domains/software-0010/software/criacao-ia/openusd-asset-resolver-context-identifiers.md) — `software.criacao_ia.tranche03.000254`
255. [OpenUSD: autorar opiniões no variant edit context correto](../../domains/software-0010/software/criacao-ia/openusd-variants-edit-context.md) — `software.criacao_ia.tranche03.000255`
256. [OpenUSD: diagnosticar strength entre local opinions e variants](../../domains/software-0010/software/criacao-ia/openusd-opinion-strength-overrides.md) — `software.criacao_ia.tranche03.000256`
257. [OpenUSD: separar default value de time samples em atributos](../../domains/software-0010/software/criacao-ia/openusd-attribute-default-e-time-samples.md) — `software.criacao_ia.tranche03.000257`
258. [OpenUSD: retimar animação referenciada com layer offset](../../domains/software-0010/software/criacao-ia/openusd-layer-offset-retimar-animacao.md) — `software.criacao_ia.tranche03.000258`
259. [OpenUSD: flattening exporta resultado composto, não estrutura editável](../../domains/software-0010/software/criacao-ia/openusd-flattening-stage-export.md) — `software.criacao_ia.tranche03.000259`
260. [OpenUSD: harmonizar upAxis, metersPerUnit e timeCodesPerSecond](../../domains/software-0010/software/criacao-ia/openusd-stage-units-up-axis-metadata.md) — `software.criacao_ia.tranche03.000260`

### FFmpeg: ordem de opções, timestamps, filtros e inspeção

261. [FFmpeg: posicionar opções no input ou output correto](../../domains/software-0010/software/criacao-ia/ffmpeg-escopo-opcoes-por-arquivo.md) — `software.criacao_ia.tranche03.000261`
262. [FFmpeg: mapear streams de entrada e saídas rotuladas](../../domains/software-0010/software/criacao-ia/ffmpeg-map-filtergraph-stream-labels.md) — `software.criacao_ia.tranche03.000262`
263. [FFmpeg concat demuxer: conferir streams e durações de entrada](../../domains/software-0010/software/criacao-ia/ffmpeg-concat-demuxer-precondicoes.md) — `software.criacao_ia.tranche03.000263`
264. [FFmpeg concat filter: alinhar cada segmento e normalizar streams](../../domains/software-0010/software/criacao-ia/ffmpeg-concat-filter-timestamps-zero.md) — `software.criacao_ia.tranche03.000264`
265. [FFmpeg trim: separar seleção de frames e reinício de timestamps](../../domains/software-0010/software/criacao-ia/ffmpeg-trim-nao-redefine-pts.md) — `software.criacao_ia.tranche03.000265`
266. [FFmpeg: interpretar PTS em conjunto com time base](../../domains/software-0010/software/criacao-ia/ffmpeg-setpts-timebase-e-relatorio.md) — `software.criacao_ia.tranche03.000266`
267. [FFmpeg: distinguir filtro fps de opção de output -r](../../domains/software-0010/software/criacao-ia/ffmpeg-fps-filter-versus-output-r.md) — `software.criacao_ia.tranche03.000267`
268. [FFmpeg filtergraph: separar escaping do filtro e da shell](../../domains/software-0010/software/criacao-ia/ffmpeg-filtergraph-escaping-niveis.md) — `software.criacao_ia.tranche03.000268`
269. [FFmpeg framesync: definir comportamento ao terminar uma entrada](../../domains/software-0010/software/criacao-ia/ffmpeg-framesync-overlay-eof-policy.md) — `software.criacao_ia.tranche03.000269`
270. [ffprobe: produzir inventário estruturado para validar um pipeline](../../domains/software-0010/software/criacao-ia/ffprobe-json-inspecao-pipeline.md) — `software.criacao_ia.tranche03.000270`

### Playwright: relógio, WebSockets, service workers e artefatos de diagnóstico

271. [Playwright Clock: instalar relógio antes de APIs temporais](../../domains/software-0010/software/criacao-ia/playwright-clock-install-order.md) — `software.criacao_ia.tranche03.000271`
272. [Playwright WebSocketRoute: escolher mock completo ou interceptação](../../domains/software-0010/software/criacao-ia/playwright-websocketroute-mock-ou-proxy.md) — `software.criacao_ia.tranche03.000272`
273. [Playwright Route: preservar a cadeia com fallback](../../domains/software-0010/software/criacao-ia/playwright-route-fallback-versus-continue.md) — `software.criacao_ia.tranche03.000273`
274. [Playwright: service workers mudam visibilidade de network routing](../../domains/software-0010/software/criacao-ia/playwright-service-worker-network-routing.md) — `software.criacao_ia.tranche03.000274`
275. [Playwright Trace: coletar diagnóstico sem expor dados de teste](../../domains/software-0010/software/criacao-ia/playwright-trace-retencao-e-dados-de-debug.md) — `software.criacao_ia.tranche03.000275`
276. [Playwright video: fechar browser context para salvar o arquivo](../../domains/software-0010/software/criacao-ia/playwright-video-context-close-artifact.md) — `software.criacao_ia.tranche03.000276`
277. [Playwright assertions: escolher expect.poll ou expect.toPass](../../domains/software-0010/software/criacao-ia/playwright-expect-poll-e-topass.md) — `software.criacao_ia.tranche03.000277`
278. [Playwright Test: diagnosticar timeouts por escopo](../../domains/software-0010/software/criacao-ia/playwright-timeouts-escopos-separados.md) — `software.criacao_ia.tranche03.000278`
279. [Playwright addInitScript: preparar ambiente antes do código da página](../../domains/software-0010/software/criacao-ia/playwright-add-init-script-determinismo.md) — `software.criacao_ia.tranche03.000279`
280. [Playwright: coletar erros de runtime sem confundir com falha de teste](../../domains/software-0010/software/criacao-ia/playwright-page-errors-observabilidade-cliente.md) — `software.criacao_ia.tranche03.000280`

### OpenTelemetry: semantic conventions para GenAI, agents, métricas e eventos

281. [OpenTelemetry GenAI: interpretar gen_ai.provider.name pela perspectiva da instrumentation](../../domains/software-0010/software/criacao-ia/otel-genai-provider-name-perspectiva.md) — `software.criacao_ia.tranche03.000281`
282. [OpenTelemetry GenAI: padronizar gen_ai.operation.name sem apagar a operação real](../../domains/software-0010/software/criacao-ia/otel-genai-operation-name-taxonomia.md) — `software.criacao_ia.tranche03.000282`
283. [OpenTelemetry GenAI: separar modelo solicitado de modelo que respondeu](../../domains/software-0010/software/criacao-ia/otel-genai-modelo-solicitado-versus-resposta.md) — `software.criacao_ia.tranche03.000283`
284. [OpenTelemetry GenAI spans: medir a operação lógica incluindo retries](../../domains/software-0010/software/criacao-ia/otel-genai-span-logico-retries.md) — `software.criacao_ia.tranche03.000284`
285. [OpenTelemetry GenAI agents: separar invocation remota, execução local e tool span](../../domains/software-0010/software/criacao-ia/otel-genai-agent-spans-client-internal-tool.md) — `software.criacao_ia.tranche03.000285`
286. [OpenTelemetry GenAI token metrics: contadores de uso não são histogramas por operação](../../domains/software-0010/software/criacao-ia/otel-genai-token-counters-versus-histograms.md) — `software.criacao_ia.tranche03.000286`
287. [OpenTelemetry GenAI streaming: distinguir time to first chunk de cadência](../../domains/software-0010/software/criacao-ia/otel-genai-streaming-latencias-por-chunk.md) — `software.criacao_ia.tranche03.000287`
288. [OpenTelemetry GenAI: minimizar conteúdo de prompt e resposta na telemetria](../../domains/software-0010/software/criacao-ia/otel-genai-conteudo-opt-in-minimizacao.md) — `software.criacao_ia.tranche03.000288`
289. [OpenTelemetry GenAI evaluation.result: correlacionar resultado ao output avaliado](../../domains/software-0010/software/criacao-ia/otel-genai-evaluation-result-correlacao.md) — `software.criacao_ia.tranche03.000289`
290. [OpenTelemetry GenAI semconv: interpretar o status Development antes de fixar integração](../../domains/software-0010/software/criacao-ia/otel-genai-conventions-development-status.md) — `software.criacao_ia.tranche03.000290`

### OpenAPI 3.1.1: semântica do Schema Object, referências, conteúdo e callbacks

291. [OAS 3.1.1: selecionar o dialect JSON Schema correto](../../domains/software-0010/software/criacao-ia/oas311-jsonschema-dialect-default-override.md) — `software.criacao_ia.tranche03.000291`
292. [OAS 3.1.1: diferenciar Reference Object de `$ref` em Schema Object](../../domains/software-0010/software/criacao-ia/oas311-reference-object-vs-schema-ref.md) — `software.criacao_ia.tranche03.000292`
293. [OAS 3.1.1: resolver `$ref` relativo usando `$id` e URI-base](../../domains/software-0010/software/criacao-ia/oas311-id-and-relative-ref-base-uri.md) — `software.criacao_ia.tranche03.000293`
294. [OAS 3.1.1: `format` não é uma validação garantida](../../domains/software-0010/software/criacao-ia/oas311-format-annotation-nao-validacao.md) — `software.criacao_ia.tranche03.000294`
295. [OAS 3.1.1: representar null e schemas booleanos com JSON Schema](../../domains/software-0010/software/criacao-ia/oas311-null-union-boolean-schemas.md) — `software.criacao_ia.tranche03.000295`
296. [OAS 3.1.1 discriminator: pista de serialização, não regra de validação](../../domains/software-0010/software/criacao-ia/oas311-discriminator-nao-altera-validacao.md) — `software.criacao_ia.tranche03.000296`
297. [OAS 3.1.1: modelar binário com contentEncoding e contentMediaType](../../domains/software-0010/software/criacao-ia/oas311-binary-contentencoding-vs-format.md) — `software.criacao_ia.tranche03.000297`
298. [OAS 3.1.1: escolher entre webhook top-level e callback de operação](../../domains/software-0010/software/criacao-ia/oas311-webhooks-versus-callbacks.md) — `software.criacao_ia.tranche03.000298`
299. [OAS 3.1.1 Path Item `$ref`: não sobrepor fields com o alvo](../../domains/software-0010/software/criacao-ia/oas311-path-item-ref-conflitos.md) — `software.criacao_ia.tranche03.000299`
300. [OAS 3.1.1: validar readOnly e writeOnly conforme direção da mensagem](../../domains/software-0010/software/criacao-ia/oas311-readonly-writeonly-annotations.md) — `software.criacao_ia.tranche03.000300`

## Tranche 4 — WebGPU, WGSL, Bevy ECS, Unity Entities, Godot shaders, GDExtension, Blender cor/VSE, Web Audio, llama.cpp server e geração no Transformers (100 notas)

IDs materiais: `software.criacao_ia.tranche04.000301`–`software.criacao_ia.tranche04.000400`. Cada tópico tem fontes primárias específicas na própria nota; eixos com cobertura anterior (Playwright, OpenTelemetry, OpenAPI genérico) não foram reescritos.

### WebGPU: adaptador, buffers, texturas, bindings e diagnóstico

301. [WebGPU: filtrar adaptador por potência e modo de compatibilidade](../../domains/software-0010/software/criacao-ia/webgpu-requestadapter-por-criterios.md) — `software.criacao_ia.tranche04.000301`
302. [WebGPU: tratar device lost como fronteira de recuperação](../../domains/software-0010/software/criacao-ia/webgpu-devicelost-camada-recuperacao.md) — `software.criacao_ia.tranche04.000302`
303. [WebGPU: pedir limites maiores e calcular antes do limite suportado](../../domains/software-0010/software/criacao-ia/webgpu-requiredlimits-calcular-custo.md) — `software.criacao_ia.tranche04.000303`
304. [WebGPU: features são opcionais e viram dependência de plataforma](../../domains/software-0010/software/criacao-ia/webgpu-features-antes-dependencia.md) — `software.criacao_ia.tranche04.000304`
305. [WebGPU: ler dados da GPU exige buffer staging com MAP_READ](../../domains/software-0010/software/criacao-ia/webgpu-leitura-gpu-staging-buffer.md) — `software.criacao_ia.tranche04.000305`
306. [WebGPU: mappedAtCreation para dados iniciais sem cópia adicional](../../domains/software-0010/software/criacao-ia/webgpu-mappedatcreation-dado-inicial.md) — `software.criacao_ia.tranche04.000306`
307. [WebGPU: declarar cada uso de textura no momento certo](../../domains/software-0010/software/criacao-ia/webgpu-textureusage-views-permitidos.md) — `software.criacao_ia.tranche04.000307`
308. [WebGPU: bind groups só valem se o layout for compatível com o pipeline](../../domains/software-0010/software/criacao-ia/webgpu-bindgrouplayout-compatibilidade.md) — `software.criacao_ia.tranche04.000308`
309. [WebGPU: capturar erros assíncronos com escopos empilhados](../../domains/software-0010/software/criacao-ia/webgpu-erros-asyncronos-escopos.md) — `software.criacao_ia.tranche04.000309`
310. [WebGPU: medir tempo de GPU com query sets de timestamp](../../domains/software-0010/software/criacao-ia/webgpu-timestamp-medir-gpu-real.md) — `software.criacao_ia.tranche04.000310`

### WGSL: classes de armazenamento, layout de binding, tipos e diagnóstico de compilação

311. [WGSL: escolher a classe de armazenamento pelo tempo de vida](../../domains/software-0010/software/criacao-ia/wgsl-classes-armazenamento-escopo.md) — `software.criacao_ia.tranche04.000311`
312. [WGSL: pares @group/@binding são contrato com o layout do pipeline](../../domains/software-0010/software/criacao-ia/wgsl-binding-layout-visibilidade.md) — `software.criacao_ia.tranche04.000312`
313. [WGSL: o layout de uniform padroniza tudo em 16 bytes](../../domains/software-0010/software/criacao-ia/wgsl-alinhamento-uniform-cinco-regra.md) — `software.criacao_ia.tranche04.000313`
314. [WGSL: só o storage buffer aceita array de tamanho em tempo de execução](../../domains/software-0010/software/criacao-ia/wgsl-storage-runtime-array.md) — `software.criacao_ia.tranche04.000314`
315. [WGSL: constantes overridables ajustam o pipeline sem recompilar o shader](../../domains/software-0010/software/criacao-ia/wgsl-override-constantes-pipeline.md) — `software.criacao_ia.tranche04.000315`
316. [WGSL: atômicos só em memória de escrita explícita, e CAS é loop manual](../../domains/software-0010/software/criacao-ia/wgsl-atomicos-compare-loop.md) — `software.criacao_ia.tranche04.000316`
317. [WGSL: amostrar uma textura exige ver o tipo certo, não só o binding](../../domains/software-0010/software/criacao-ia/wgsl-textura-amostragem-tipo-view.md) — `software.criacao_ia.tranche04.000317`
318. [WGSL: cada estágio expõe apenas os embutidos que fazem sentido para ele](../../domains/software-0010/software/criacao-ia/wgsl-builtins-estagios-corte.md) — `software.criacao_ia.tranche04.000318`
319. [WGSL: fluxo divergente e operações uniformes — uma análise, não uma sugestão](../../domains/software-0010/software/criacao-ia/wgsl-uniformidade-amostragem.md) — `software.criacao_ia.tranche04.000319`
320. [WGSL: sem coerções implícitas — o construtor é obrigatório e o erro é cedo](../../domains/software-0010/software/criacao-ia/wgsl-sem-conversao-implicita.md) — `software.criacao_ia.tranche04.000320`

### Bevy ECS: agendamento, queries, mutação adiada e organização de app

321. [Bevy ECS: Startup roda uma vez antes de tudo; Update é o loop](../../domains/software-0010/software/criacao-ia/bevy-startup-update-duas-momentos.md) — `software.criacao_ia.tranche04.000321`
322. [Bevy ECS: o paralelismo vem dos acessos declarados, não de threads manuais](../../domains/software-0010/software/criacao-ia/bevy-paralelismo-por-acesso.md) — `software.criacao_ia.tranche04.000322`
323. [Bevy ECS: use chain() onde a ordem importa, e só lá](../../domains/software-0010/software/criacao-ia/bevy-chain-ordenamento-minimo.md) — `software.criacao_ia.tranche04.000323`
324. [Bevy ECS: uma query &mut é o ponto único de escrita de um tipo](../../domains/software-0010/software/criacao-ia/bevy-query-mutavel-unico-por-alvo.md) — `software.criacao_ia.tranche04.000324`
325. [Bevy ECS: com With/Without você estreita o alvo sem quebrar o contrato de acesso](../../domains/software-0010/software/criacao-ia/bevy-query-filtros-refinam-superficie.md) — `software.criacao_ia.tranche04.000325`
326. [Bevy ECS: Commands é a fila de mutação estrutural adiada](../../domains/software-0010/software/criacao-ia/bevy-commands-mundo-diferido.md) — `software.criacao_ia.tranche04.000326`
327. [Bevy ECS: resources são o valor-único do mundo, não mais um componente](../../domains/software-0010/software/criacao-ia/bevy-resources-valor-unico-mundo.md) — `software.criacao_ia.tranche04.000327`
328. [Bevy ECS: componente é struct Rust com derive — a decomposição é o design](../../domains/software-0010/software/criacao-ia/bevy-componente-struct-derive.md) — `software.criacao_ia.tranche04.000328`
329. [Bevy ECS: Plugin é a unidade de empacotamento, não de lógica](../../domains/software-0010/software/criacao-ia/bevy-plugins-unidade-distribuicao.md) — `software.criacao_ia.tranche04.000329`
330. [Bevy ECS: App planeja, Schedule decide quando, World guarda o estado](../../domains/software-0010/software/criacao-ia/bevy-app-schedule-world-camadas.md) — `software.criacao_ia.tranche04.000330`

### Unity Entities (DOTS): mudanças estruturais, jobs, safety e armazenamento por chunk

331. [Unity Entities: criar/destruir é caro porque o layout muda, e por isso é estrutural](../../domains/software-0010/software/criacao-ia/unity-estrutura-mudanca-custo-episodio.md) — `software.criacao_ia.tranche04.000331`
332. [Unity Entities: a EntityCommandBuffer é replay, não fila mágica](../../domains/software-0010/software/criacao-ia/unity-ecb-bufferfromentity-replay.md) — `software.criacao_ia.tranche04.000332`
333. [Unity Entities: IJobEntity gera código por assinatura — e pode virar main thread sem aviso de sintaxe](../../domains/software-0010/software/criacao-ia/unity-ijobentity-fonte-gerada-main-thread.md) — `software.criacao_ia.tranche04.000333`
334. [Unity Jobs: o safety system é a sua revisão de concorrência em tempo de execução](../../domains/software-0010/software/criacao-ia/unity-safety-system-corrida-exception.md) — `software.criacao_ia.tranche04.000334`
335. [Unity Jobs: em IJobParallelFor você escreve no seu índice e lê fora com intenção declarada](../../domains/software-0010/software/criacao-ia/unity-parallelfor-indexo-proprio.md) — `software.criacao_ia.tranche04.000335`
336. [Unity Entities: iterar por chunk é o grão de leitura da arquitetura](../../domains/software-0010/software/criacao-ia/unity-chunks-arquetipos-leitura-lote.md) — `software.criacao_ia.tranche04.000336`
337. [Unity Entities: RefRW/RefRO são handles com verificação, não ponteiros para sempre](../../domains/software-0010/software/criacao-ia/unity-refrw-invalidacao-apos-estrutural.md) — `software.criacao_ia.tranche04.000337`
338. [Unity Entities: Blob assets são o lado imutável do dado, não JSON serializado](../../domains/software-0010/software/criacao-ia/unity-blob-assets-imutavel-compacto.md) — `software.criacao_ia.tranche04.000338`
339. [Unity Entities: RefAspect limpa a assinatura do sistema, não o armazenamento](../../domains/software-0010/software/criacao-ia/unity-aspects-limpeza-de-assinatura.md) — `software.criacao_ia.tranche04.000339`
340. [Unity Entities: o baking é a fronteira de conversão cena↔ECS, e o runtime tem outra porta](../../domains/software-0010/software/criacao-ia/unity-baking-ponteiro-cenario-para-ecs.md) — `software.criacao_ia.tranche04.000340`

### Godot 4: linguagem de shaders, embutidos canvas-item e flags de render espacial

341. [Godot 4: cada tipo de shader tem seu conjunto de embutidos — a referência é o mapa](../../domains/software-0010/software/criacao-ia/godot-shader-builtins-por-familia.md) — `software.criacao_ia.tranche04.000341`
342. [Godot 4: no canvas-item, VERTEX fala em píxeles locais — não em UV nem em mundo](../../domains/software-0010/software/criacao-ia/godot-canvas-vertex-px-locais.md) — `software.criacao_ia.tranche04.000342`
343. [Godot 4: TIME é tempo de render em segundos, com rolover e sem pause](../../domains/software-0010/software/criacao-ia/godot-tempo-time-rollover-pause.md) — `software.criacao_ia.tranche04.000343`
344. [Godot 4: COLOR em 2D é a trama de vértice × modulate × self_modulate](../../domains/software-0010/software/criacao-ia/godot-color-vertex-multipliers.md) — `software.criacao_ia.tranche04.000344`
345. [Godot 4: INSTANCE_CUSTOM é o canal de dados por-partícula para o shader 2D](../../domains/software-0010/software/criacao-ia/godot-particulas-instance-custom.md) — `software.criacao_ia.tranche04.000345`
346. [Godot 4: a shading language não faz cast implícito — e suas variáveis locais nascem sem inicializar](../../domains/software-0010/software/criacao-ia/godot-shading-sem-cast-implicito.md) — `software.criacao_ia.tranche04.000346`
347. [Godot 4: o /** acima do uniform é documentação vira-inspetor, não comentário decorativo](../../domains/software-0010/software/criacao-ia/godot-uniform-docs-inspector.md) — `software.criacao_ia.tranche04.000347`
348. [Godot 4: os blend modes do material espacial e o truque do fog em blend_add](../../domains/software-0010/software/criacao-ia/godot-blend-modes-spatial.md) — `software.criacao_ia.tranche04.000348`
349. [Godot 4: flags de render do shader espacial que economizam passes inteiros](../../domains/software-0010/software/criacao-ia/godot-render-flags-sombras-wireframe.md) — `software.criacao_ia.tranche04.000349`
350. [Godot 4: nas shaders, matrizes são colunares — m[1][0] é a segunda coluna, primeira linha](../../domains/software-0010/software/criacao-ia/godot-shader-matrizes-colunares.md) — `software.criacao_ia.tranche04.000350`

### Godot 4 GDExtension: o arquivo .gdextension, compatibilidade de versão e bindings nativos

351. [Godot 4: GDExtension é a ponte runtime para bibliotecas nativas](../../domains/software-0010/software/criacao-ia/gdextension-biblioteca-compartilhada-runtime.md) — `software.criacao_ia.tranche04.000351`
352. [Godot 4: entry_symbol é o contrato mínimo do arquivo .gdextension](../../domains/software-0010/software/criacao-ia/gdextension-entry-symbol-obrigatorio.md) — `software.criacao_ia.tranche04.000352`
353. [Godot 4: mire a extensão na versão mais baixa que te atende, não na mais nova](../../domains/software-0010/software/criacao-ia/gdextension-alvo-baixo-compative-frente.md) — `software.criacao_ia.tranche04.000353`
354. [Godot 4: compatibility_minimum e maximum são portas de carga, não metadados](../../domains/software-0010/software/criacao-ia/gdextension-compatibility-min-max.md) — `software.criacao_ia.tranche04.000354`
355. [Godot 4: reloadable recarrega a extensão — e é ferramenta de desenvolvimento, não de produção](../../domains/software-0010/software/criacao-ia/gdextension-reloadable-dev-debug.md) — `software.criacao_ia.tranche04.000355`
356. [Godot 4: a seção [libraries] é um filtro por feature flags, não uma lista de caminhos](../../domains/software-0010/software/criacao-ia/gdextension-libraries-feature-tags.md) — `software.criacao_ia.tranche04.000356`
357. [Godot 4: no .gdextension, a linha mais específica precisa vir antes — o matching é sequencial](../../domains/software-0010/software/criacao-ia/gdextension-ordem-especifica-antes.md) — `software.criacao_ia.tranche04.000357`
358. [Godot 4: a extensão só carrega no build de motor com a mesma precisão de float](../../domains/software-0010/software/criacao-ia/gdextension-double-single-api-json.md) — `software.criacao_ia.tranche04.000358`
359. [Godot 4: [icons] e [dependencies] completam o .gdextension — com contrato de 16×16 px](../../domains/software-0010/software/criacao-ia/gdextension-icone-svg-e-dependencies.md) — `software.criacao_ia.tranche04.000359`
360. [Godot 4: godot-cpp versus módulos C++ — uma decisão de distribuição](../../domains/software-0010/software/criacao-ia/gdextension-vs-modules-custo-distribuicao.md) — `software.criacao_ia.tranche04.000360`

### Blender 5.2 LTS: gestão de cor (view transforms, espaços) e pipeline de proxy/cache do VSE

361. [Blender: o View Transform (AgX, Filmic, Standard) é decisão de destino, não de look](../../domains/software-0010/software/criacao-ia/blender-view-transform-agx-filmic-standard.md) — `software.criacao_ia.tranche04.000361`
362. [Blender: máscaras, normal maps e LUTs são Non-Color — converter dado é corromper sinal](../../domains/software-0010/software/criacao-ia/blender-non-color-dados-nunca-convertidos.md) — `software.criacao_ia.tranche04.000362`
363. [Blender: o display view não é o arquivo salvo — o laço View as Render/Save as Render](../../domains/software-0010/software/criacao-ia/blender-what-you-see-is-not-what-you-save.md) — `software.criacao_ia.tranche04.000363`
364. [Blender VSE: Proxy Render Size é um switch global que habilita todos os strips](../../domains/software-0010/software/criacao-ia/blender-proxy-tamanho-global-view.md) — `software.criacao_ia.tranche04.000364`
365. [Blender VSE: proxies vivem em BL_proxy junto da footage — e podem ser arquivos existentes](../../domains/software-0010/software/criacao-ia/blender-proxy-bl-pasta-e-arquivos-externos.md) — `software.criacao_ia.tranche04.000365`
366. [Blender VSE: Quality do proxy é compressão com perda em percentual direto — 100 é sem perda](../../domains/software-0010/software/criacao-ia/blender-proxy-quality-lossy-percentual.md) — `software.criacao_ia.tranche04.000366`
367. [Blender VSE: Memory Cache Limit vive nas Preferences, e o VSE lê dele](../../domains/software-0010/software/criacao-ia/blender-sequencer-cache-memoria-limites.md) — `software.criacao_ia.tranche04.000367`
368. [Blender 5.2: o backend da interface é escolha (OpenGL × Vulkan) com custo de reinicialização](../../domains/software-0010/software/criacao-ia/blender-backend-vulkan-interface-52.md) — `software.criacao_ia.tranche04.000368`
369. [Blender 5.2: os limites de memória do System — undo, shaders, geometry nodes — e seus efeitos colaterais](../../domains/software-0010/software/criacao-ia/blender-limites-de-memoria-undo-shaders-stack.md) — `software.criacao_ia.tranche04.000369`
370. [Blender VSE: Proxy Setup Automatic gera sozinho, Manual delega à farm — a decisão é de pipeline](../../domains/software-0010/software/criacao-ia/blender-proxy-setup-automatico-vs-manual.md) — `software.criacao_ia.tranche04.000370`

### Web Audio API: tempo, autoplay, worklets e os nós de espacialização/análise

371. [Web Audio: o AudioContext nasce suspenso e só um gesto humano o acorda](../../domains/software-0010/software/criacao-ia/webaudio-contexto-suspenso-gesto.md) — `software.criacao_ia.tranche04.000371`
372. [Web Audio: nós de fonte são one-shot — start() e stop() cada um uma vez só](../../domains/software-0010/software/criacao-ia/webaudio-fontes-oneshot-start-stop.md) — `software.criacao_ia.tranche04.000372`
373. [Web Audio: setTargetAtTime é o easing exponencial — a constante define 63%, não o fim](../../domains/software-0010/software/criacao-ia/webaudio-settargetattime-constante-tempo.md) — `software.criacao_ia.tranche04.000373`
374. [Web Audio: exponentialRampToValueAtTime não passa por zero — nem começando nem terminando nele](../../domains/software-0010/software/criacao-ia/webaudio-exp-ramp-zero-proibido.md) — `software.criacao_ia.tranche04.000374`
375. [Web Audio: decodeAudioData ressampleia para o contexto e exige o dado completo](../../domains/software-0010/software/criacao-ia/webaudio-decodeaudiodata-ressample-completo.md) — `software.criacao_ia.tranche04.000375`
376. [Web Audio: AudioWorklet é módulo separado com o seu próprio global scope](../../domains/software-0010/software/criacao-ia/webaudio-audioworklet-modulos-processador.md) — `software.criacao_ia.tranche04.000376`
377. [Web Audio: o port do AudioWorkletNode é o fio da navalha entre página e render](../../domains/software-0010/software/criacao-ia/webaudio-worklet-port-fio-da-navalha.md) — `software.criacao_ia.tranche04.000377`
378. [Web Audio: PannerNode escolhe como o som se move no espaço — pan, equal power ou HRTF](../../domains/software-0010/software/criacao-ia/webaudio-panner-modelos-espaciais.md) — `software.criacao_ia.tranche04.000378`
379. [Web Audio: ConvolverNode é a reverberação física — e o IR define canal por canal](../../domains/software-0010/software/criacao-ia/webaudio-convolver-resposta-ao-impulso.md) — `software.criacao_ia.tranche04.000379`
380. [Web Audio: AnalyserNode dá o espectro com janela e suavização — não a FFT crua](../../domains/software-0010/software/criacao-ia/webaudio-analyser-janela-frequencia.md) — `software.criacao_ia.tranche04.000380`

### llama.cpp server: contexto, cache de KV, slots paralelos, endpoints e saída estruturada

381. [llama.cpp server: tamanho de contexto e batch de prompt são duas alavancas separadas](../../domains/software-0010/software/criacao-ia/llamacpp-contexto-e-batch-na-carga.md) — `software.criacao_ia.tranche04.000381`
382. [llama.cpp server: Flash Attention abre a porta da quantização de KV](../../domains/software-0010/software/criacao-ia/llamacpp-flash-attention-quantizacao-kv.md) — `software.criacao_ia.tranche04.000382`
383. [llama.cpp server: -np multiplica o contexto e -cb faz o cache caber em cada slot](../../domains/software-0010/software/criacao-ia/llamacpp-slots-paralelos-np-cb.md) — `software.criacao_ia.tranche04.000383`
384. [llama.cpp server: cache de prompt tem três camadas — o mesmo estado, três knobs](../../domains/software-0010/software/criacao-ia/llamacpp-cache-prompt-ram-e-reuse.md) — `software.criacao_ia.tranche04.000384`
385. [llama.cpp server: /completion é API própria, /v1/completions é a de OpenAI](../../domains/software-0010/software/criacao-ia/llamacpp-endpoints-completion-vs-openai.md) — `software.criacao_ia.tranche04.000385`
386. [llama.cpp server: não é um servidor de produção exposto — e as três chaves que aproximam](../../domains/software-0010/software/criacao-ia/llamacpp-servidor-sem-auth-na-rede.md) — `software.criacao_ia.tranche04.000386`
387. [GBNF: a sintaxe que construi constrangimento de tokens, e o que 'root' significa](../../domains/software-0010/software/criacao-ia/gbnf-sintaxe-e-root.md) — `software.criacao_ia.tranche04.000387`
388. [GBNF: repetições aninhadas custam exponencialmente — e a doc dá o recheio anti-armadilha](../../domains/software-0010/software/criacao-ia/gbnf-custo-e-armadilha-de-repeticao.md) — `software.criacao_ia.tranche04.000388`
389. [llama.cpp: JSON Schema vira GBNF — restringe a saída e não entra no prompt](../../domains/software-0010/software/criacao-ia/gbnf-json-schema-nao-e-prompt.md) — `software.criacao_ia.tranche04.000389`
390. [llama.cpp: o pipeline de samplers tem ordem fixa, e cada campo do pedido é um nó dele](../../domains/software-0010/software/criacao-ia/llamacpp-samplers-ordem-fixa.md) — `software.criacao_ia.tranche04.000390`

### Transformers (Hugging Face): geração — config, estratégias, caches de amostragem, KV e decodificação assistida

391. [Transformers: os None da GenerationConfig são herança, não desatenção](../../domains/software-0010/software/criacao-ia/hf-generation-config-nen-hereda-modelo.md) — `software.criacao_ia.tranche04.000391`
392. [Transformers: max_new_tokens é o budget relativo; max_length é o absoluto que te morderá](../../domains/software-0010/software/criacao-ia/hf-max-new-tokens-vs-max-length.md) — `software.criacao_ia.tranche04.000392`
393. [Transformers: num_beams × do_sample é uma tabela de 4 modos, não dois knobs independentes](../../domains/software-0010/software/criacao-ia/hf-beams-e-amostragem-tabela.md) — `software.criacao_ia.tranche04.000393`
394. [Transformers: early_stopping do beam tem três estados — e 'never' existe por um motivo](../../domains/software-0010/software/criacao-ia/hf-early-stopping-never.md) — `software.criacao_ia.tranche04.000394`
395. [Transformers: os defaults de sampling (1.0/50/1.0) não são config — são a ausência dela](../../domains/software-0010/software/criacao-ia/hf-temperature-topk-topp-defaults.md) — `software.criacao_ia.tranche04.000395`
396. [Transformers: os filtros alternativos do sampling — min_p, top_h, typical_p — e suas faixas](../../domains/software-0010/software/criacao-ia/hf-min-p-top-h-typical-p-filtros.md) — `software.criacao_ia.tranche04.000396`
397. [Transformers: o arsenal anti-repetição — n-gramas, penalidades e viés de tokens](../../domains/software-0010/software/criacao-ia/hf-repeticao-ngram-e-bias.md) — `software.criacao_ia.tranche04.000397`
398. [Transformers: cache_implementation escolhe o destino da KV — dynamic, static, offload ou quantizada](../../domains/software-0010/software/criacao-ia/hf-cache-implementation-quatro-modos.md) — `software.criacao_ia.tranche04.000398`
399. [Transformers: decodificação assistida — draft por modelo, n-gram, medusa ou ensemble](../../domains/software-0010/software/criacao-ia/hf-assisted-decoding-especifico.md) — `software.criacao_ia.tranche04.000399`
400. [Transformers: past_key_values no retorno e generate custom por repositório](../../domains/software-0010/software/criacao-ia/hf-retornos-e-custom-generate.md) — `software.criacao_ia.tranche04.000400`
## Tranche 5 — APIs e runtimes para criação assistida de software, jogos e documentação (100 notas)

IDs materiais: `software.criacao_ia.tranche05.000401`–`software.criacao_ia.tranche05.000500`. Os tópicos foram comparados ao inventário de 400 notas deste subdomínio e pesquisados no vault inteiro; cada nota cita duas fontes primárias específicas.

### Ollama REST API: endereçamento, payloads, catálogo e ciclo dos modelos

401. [Ollama API: diferenciar base URLs local e cloud antes de configurar o cliente](../../domains/software-0010/software/criacao-ia/ollama-api-separar-base-url-local-cloud.md) — `software.criacao_ia.tranche05.000401`
402. [Ollama API: tratar stream de generate até o marcador done](../../domains/software-0010/software/criacao-ia/ollama-api-generate-stream-e-done.md) — `software.criacao_ia.tranche05.000402`
403. [Ollama API: representar a conversa em messages no endpoint chat](../../domains/software-0010/software/criacao-ia/ollama-api-chat-array-de-messages.md) — `software.criacao_ia.tranche05.000403`
404. [Ollama API: validar saídas estruturadas com format JSON Schema](../../domains/software-0010/software/criacao-ia/ollama-api-json-schema-structured-output.md) — `software.criacao_ia.tranche05.000404`
405. [Ollama API: gerar embeddings em lote e escolher a política de truncamento](../../domains/software-0010/software/criacao-ia/ollama-api-embeddings-lote-e-truncamento.md) — `software.criacao_ia.tranche05.000405`
406. [Ollama API: acompanhar o progresso do pull sem fixar mensagens de status](../../domains/software-0010/software/criacao-ia/ollama-api-pull-acompanhar-progresso.md) — `software.criacao_ia.tranche05.000406`
407. [Ollama API: usar tags para inventário e show para metadados de um modelo](../../domains/software-0010/software/criacao-ia/ollama-api-tags-vs-show-model-metadata.md) — `software.criacao_ia.tranche05.000407`
408. [Ollama API: criar um modelo derivado com parâmetros e instruções explícitas](../../domains/software-0010/software/criacao-ia/ollama-api-create-configurar-modelo-derivado.md) — `software.criacao_ia.tranche05.000408`
409. [Ollama API: copiar um modelo para um nome isolado antes de alterar a configuração](../../domains/software-0010/software/criacao-ia/ollama-api-copy-modelo-com-nome-separado.md) — `software.criacao_ia.tranche05.000409`
410. [Ollama API: proteger a remoção de modelos com confirmação do nome exato](../../domains/software-0010/software/criacao-ia/ollama-api-delete-model-protegido.md) — `software.criacao_ia.tranche05.000410`

### ComfyUI Server API: exportar workflows, enfileirar execuções e recuperar resultados

411. [ComfyUI: exportar o grafo no formato API em vez de reutilizar o arquivo visual](../../domains/software-0010/software/criacao-ia/comfyui-api-exportar-workflow-formato-api.md) — `software.criacao_ia.tranche05.000411`
412. [ComfyUI: interpretar POST prompt como validação e enfileiramento, não como resultado](../../domains/software-0010/software/criacao-ia/comfyui-api-prompt-validacao-e-fila.md) — `software.criacao_ia.tranche05.000412`
413. [ComfyUI: abrir o WebSocket com client_id e correlacionar por prompt_id](../../domains/software-0010/software/criacao-ia/comfyui-api-websocket-client-id-correlacao.md) — `software.criacao_ia.tranche05.000413`
414. [ComfyUI: distinguir atualização `executed` do fim e do sucesso da execução](../../domains/software-0010/software/criacao-ia/comfyui-api-evento-final-e-executed.md) — `software.criacao_ia.tranche05.000414`
415. [ComfyUI: recuperar o histórico da execução usando o prompt_id](../../domains/software-0010/software/criacao-ia/comfyui-api-history-resultado-por-prompt-id.md) — `software.criacao_ia.tranche05.000415`
416. [ComfyUI: recuperar arquivos de saída pela rota view e seus parâmetros](../../domains/software-0010/software/criacao-ia/comfyui-api-view-parametros-de-arquivo.md) — `software.criacao_ia.tranche05.000416`
417. [ComfyUI: consultar object_info para descobrir o esquema dos nós disponíveis](../../domains/software-0010/software/criacao-ia/comfyui-api-object-info-nos-instalados.md) — `software.criacao_ia.tranche05.000417`
418. [ComfyUI: separar controle da fila de interrupção da execução ativa](../../domains/software-0010/software/criacao-ia/comfyui-api-distinguir-fila-de-interrupt.md) — `software.criacao_ia.tranche05.000418`
419. [ComfyUI: usar a referência devolvida por upload/image em vez de caminho local](../../domains/software-0010/software/criacao-ia/comfyui-api-upload-image-referencia.md) — `software.criacao_ia.tranche05.000419`
420. [ComfyUI: separar a Server API da superfície versionada Comfy API v2](../../domains/software-0010/software/criacao-ia/comfyui-separar-server-api-e-comfy-api-v2.md) — `software.criacao_ia.tranche05.000420`

### Godot EditorImportPlugin: registrar importadores, definir contratos e salvar recursos

421. [Godot EditorImportPlugin: registrar e remover a instância pelo EditorPlugin](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-registro-no-editorplugin.md) — `software.criacao_ia.tranche05.000421`
422. [Godot EditorImportPlugin: manter importer_name estável e separar o rótulo visível](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-identidade-e-nome-visivel.md) — `software.criacao_ia.tranche05.000422`
423. [Godot EditorImportPlugin: limitar extensões aceitas e declarar prioridade consciente](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-extensoes-prioridade.md) — `software.criacao_ia.tranche05.000423`
424. [Godot EditorImportPlugin: alinhar resource_type ao save_extension declarado](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-tipo-e-extensao-de-saida.md) — `software.criacao_ia.tranche05.000424`
425. [Godot EditorImportPlugin: descrever opções de importação com defaults e presets](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-opcoes-e-presets.md) — `software.criacao_ia.tranche05.000425`
426. [Godot EditorImportPlugin: ocultar opções dependentes sem perder seu contrato](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-visibilidade-de-opcoes.md) — `software.criacao_ia.tranche05.000426`
427. [Godot EditorImportPlugin: validar source_file e propagar Error do import](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-validar-source-file-e-error.md) — `software.criacao_ia.tranche05.000427`
428. [Godot EditorImportPlugin: gravar em save_path e declarar arquivos gerados](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-save-path-gen-files-variants.md) — `software.criacao_ia.tranche05.000428`
429. [Godot EditorImportPlugin: habilitar importação paralela só após provar thread safety](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-threaded-import-safety.md) — `software.criacao_ia.tranche05.000429`
430. [Godot EditorImportPlugin: incrementar format_version ao incompatibilizar recursos importados](../../domains/software-0010/software/criacao-ia/godot-editorimportplugin-format-version-invalidacao.md) — `software.criacao_ia.tranche05.000430`

### Unity Sentis 2.5: preparar tensores, escolher backend e integrar inferência ao frame loop

431. [Unity Sentis 2.5: separar ModelAsset, runtime Model e Worker de execução](../../domains/software-0010/software/criacao-ia/unity-sentis-modelasset-runtime-model-worker.md) — `software.criacao_ia.tranche05.000431`
432. [Unity Sentis 2.5: escolher backend após medir modelo, dados e plataforma](../../domains/software-0010/software/criacao-ia/unity-sentis-escolher-backend-por-modelo.md) — `software.criacao_ia.tranche05.000432`
433. [Unity Sentis 2.5: construir input tensor conforme shape e tipo esperados pelo modelo](../../domains/software-0010/software/criacao-ia/unity-sentis-inspecionar-shape-e-dtype-da-entrada.md) — `software.criacao_ia.tranche05.000433`
434. [Unity Sentis 2.5: tratar dimensões dinâmicas como contrato explícito de entrada](../../domains/software-0010/software/criacao-ia/unity-sentis-shapes-dinamicos-compatibilidade.md) — `software.criacao_ia.tranche05.000434`
435. [Unity Sentis 2.5: conferir layout NCHW e escala ao converter Texture para Tensor](../../domains/software-0010/software/criacao-ia/unity-sentis-texture-nchw-preprocessamento.md) — `software.criacao_ia.tranche05.000435`
436. [Unity Sentis 2.5: validar operadores e tipos antes de fixar backend](../../domains/software-0010/software/criacao-ia/unity-sentis-compatibilidade-operadores-backend.md) — `software.criacao_ia.tranche05.000436`
437. [Unity Sentis 2.5: escolher entre PeekOutput emprestado e CopyOutput próprio](../../domains/software-0010/software/criacao-ia/unity-sentis-peekoutput-copyoutput-propriedade.md) — `software.criacao_ia.tranche05.000437`
438. [Unity Sentis 2.5: evitar leitura síncrona que bloqueia a main thread](../../domains/software-0010/software/criacao-ia/unity-sentis-evitar-readback-sincrono-na-main-thread.md) — `software.criacao_ia.tranche05.000438`
439. [Unity Sentis 2.5: usar ReadbackAndCloneAsync com sincronização e descarte explícitos](../../domains/software-0010/software/criacao-ia/unity-sentis-readback-and-clone-async-lifecycle.md) — `software.criacao_ia.tranche05.000439`
440. [Unity Sentis 2.5: distribuir camadas de inferência entre frames com ScheduleIterable](../../domains/software-0010/software/criacao-ia/unity-sentis-schedule-iterable-frames.md) — `software.criacao_ia.tranche05.000440`

### OpenAI Realtime API: áudio em tempo real, turnos, eventos e chamadas de ferramenta

441. [OpenAI Realtime: configurar server_vad ou semantic_vad como política de turnos](../../domains/software-0010/software/criacao-ia/openai-realtime-vad-configurar-turn-detection.md) — `software.criacao_ia.tranche05.000441`
442. [OpenAI Realtime: implementar push-to-talk com buffer, commit e response.create](../../domains/software-0010/software/criacao-ia/openai-realtime-push-to-talk-sem-vad.md) — `software.criacao_ia.tranche05.000442`
443. [OpenAI Realtime: transmitir input_audio_buffer.append em chunks Base64 limitados](../../domains/software-0010/software/criacao-ia/openai-realtime-append-audio-chunks-base64.md) — `software.criacao_ia.tranche05.000443`
444. [OpenAI Realtime transcription: correlacionar deltas e transcrições finais por item_id](../../domains/software-0010/software/criacao-ia/openai-realtime-transcricao-item-id.md) — `software.criacao_ia.tranche05.000444`
445. [OpenAI Realtime: obter bytes de áudio em output_audio.delta, não em response.done](../../domains/software-0010/software/criacao-ia/openai-realtime-audio-output-delta-vs-done.md) — `software.criacao_ia.tranche05.000445`
446. [OpenAI Realtime: sincronizar áudio interrompido com conversation.item.truncate](../../domains/software-0010/software/criacao-ia/openai-realtime-interromper-audio-e-truncate.md) — `software.criacao_ia.tranche05.000446`
447. [OpenAI Realtime: executar function calls no aplicativo e devolver function_call_output](../../domains/software-0010/software/criacao-ia/openai-realtime-function-call-execucao-aplicacao.md) — `software.criacao_ia.tranche05.000447`
448. [OpenAI Realtime: isolar respostas auxiliares com conversation none e metadata](../../domains/software-0010/software/criacao-ia/openai-realtime-out-of-band-conversation-none.md) — `software.criacao_ia.tranche05.000448`
449. [OpenAI Realtime: tratar session.updated como confirmação do estado efetivo](../../domains/software-0010/software/criacao-ia/openai-realtime-session-update-estado-efetivo.md) — `software.criacao_ia.tranche05.000449`
450. [OpenAI Realtime: usar client secret temporário no browser em vez da API key principal](../../domains/software-0010/software/criacao-ia/openai-realtime-client-secret-browser.md) — `software.criacao_ia.tranche05.000450`

### Vercel AI SDK UI: estado de chat, persistência, ferramentas e protocolos de stream

451. [AI SDK UI: manter o estado do campo de entrada fora de useChat no AI SDK 5](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-input-state-fora-do-usechat.md) — `software.criacao_ia.tranche05.000451`
452. [AI SDK UI: renderizar UIMessage.parts por tipo em vez de presumir texto único](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-renderizar-uimessage-parts.md) — `software.criacao_ia.tranche05.000452`
453. [AI SDK UI: configurar endpoint e cabeçalhos no DefaultChatTransport](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-configurar-chat-transport.md) — `software.criacao_ia.tranche05.000453`
454. [AI SDK UI: persistir UIMessage e validar tools e metadata antes de converter](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-persistir-e-validar-uimessages.md) — `software.criacao_ia.tranche05.000454`
455. [AI SDK UI: separar execução de tools server-side e client-side com addToolOutput](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-tools-execution-and-output.md) — `software.criacao_ia.tranche05.000455`
456. [AI SDK UI: implementar retomada de stream com persistência e endpoint GET](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-retomar-streams-com-storage.md) — `software.criacao_ia.tranche05.000456`
457. [AI SDK UI: em streams retomáveis, distinguir stop local de cancelamento server-side](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-stop-nao-cancela-geracao-retomavel.md) — `software.criacao_ia.tranche05.000457`
458. [AI SDK UI: separar data parts persistentes de eventos transient de interface](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-data-parts-persistentes-transient.md) — `software.criacao_ia.tranche05.000458`
459. [AI SDK UI: escolher text stream ou data stream conforme a forma do evento](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-escolher-text-stream-ou-data-stream.md) — `software.criacao_ia.tranche05.000459`
460. [AI SDK UI: conduzir controles por status e mostrar erro genérico ao usuário](../../domains/software-0010/software/criacao-ia/ai-sdk-ui-status-erro-e-mensagem-publica.md) — `software.criacao_ia.tranche05.000460`

### Storybook: produzir histórias tipadas, mocks de UI e verificações automatizadas

461. [Storybook: organizar CSF com meta default e histórias como exports nomeados](../../domains/software-0010/software/criacao-ia/storybook-csf-default-meta-named-stories.md) — `software.criacao_ia.tranche05.000461`
462. [Storybook: distribuir args por story e componente sem guardar estado global em props](../../domains/software-0010/software/criacao-ia/storybook-args-niveis-serializaveis.md) — `software.criacao_ia.tranche05.000462`
463. [Storybook TypeScript: ligar Meta e StoryObj com satisfies para checar args](../../domains/software-0010/software/criacao-ia/storybook-typescript-meta-storyobj-satisfies.md) — `software.criacao_ia.tranche05.000463`
464. [Storybook: usar globals e toolbar para variar contexto compartilhado como tema](../../domains/software-0010/software/criacao-ia/storybook-globals-toolbar-decorator-theme.md) — `software.criacao_ia.tranche05.000464`
465. [Storybook: usar loaders assíncronos como escape hatch para dados externos](../../domains/software-0010/software/criacao-ia/storybook-loaders-before-render-loaded-context.md) — `software.criacao_ia.tranche05.000465`
466. [Storybook: escrever testes de interação como play com canvas e userEvent awaited](../../domains/software-0010/software/criacao-ia/storybook-play-interaction-canvas-userevent.md) — `software.criacao_ia.tranche05.000466`
467. [Storybook: executar stories como component tests com addon Vitest](../../domains/software-0010/software/criacao-ia/storybook-vitest-addon-stories-como-component-tests.md) — `software.criacao_ia.tranche05.000467`
468. [Storybook: detectar regressões de pixels com visual tests e baselines revisados](../../domains/software-0010/software/criacao-ia/storybook-visual-tests-baselines-chromatic.md) — `software.criacao_ia.tranche05.000468`
469. [Storybook: habilitar Autodocs por tag e estender a documentação com MDX](../../domains/software-0010/software/criacao-ia/storybook-autodocs-tags-living-documentation.md) — `software.criacao_ia.tranche05.000469`
470. [Storybook a11y: combinar varredura axe com verificação manual de acessibilidade](../../domains/software-0010/software/criacao-ia/storybook-a11y-axe-auditoria-manual.md) — `software.criacao_ia.tranche05.000470`

### Docusaurus 3.10: estruturar, versionar e localizar sites de documentação

471. [Docusaurus: separar identidade do documento de sua URL pública com slug explícito](../../domains/software-0010/software/criacao-ia/docusaurus-doc-id-e-slug-permalink.md) — `software.criacao_ia.tranche05.000471`
472. [Docusaurus: construir sidebar autogenerated a partir de diretórios de docs](../../domains/software-0010/software/criacao-ia/docusaurus-autogenerated-sidebar-filesystem.md) — `software.criacao_ia.tranche05.000472`
473. [Docusaurus: controlar ordem de sidebar automática com sidebar_position](../../domains/software-0010/software/criacao-ia/docusaurus-sidebar-position-frontmatter.md) — `software.criacao_ia.tranche05.000473`
474. [Docusaurus: fixar associação de múltiplas sidebars com displayed_sidebar](../../domains/software-0010/software/criacao-ia/docusaurus-sidebar-association-pagination.md) — `software.criacao_ia.tranche05.000474`
475. [Docusaurus: criar versões de documentação como snapshots deliberados](../../domains/software-0010/software/criacao-ia/docusaurus-versioning-freeze-current-docs.md) — `software.criacao_ia.tranche05.000475`
476. [Docusaurus: distinguir versão current da versão latest usada no navbar](../../domains/software-0010/software/criacao-ia/docusaurus-current-vs-latest-version.md) — `software.criacao_ia.tranche05.000476`
477. [Docusaurus: manter links e imports válidos quando docs são versionados](../../domains/software-0010/software/criacao-ia/docusaurus-version-safe-links-and-imports.md) — `software.criacao_ia.tranche05.000477`
478. [Docusaurus: configurar instâncias do plugin docs para catálogos independentes](../../domains/software-0010/software/criacao-ia/docusaurus-docs-multi-instance-unique-id.md) — `software.criacao_ia.tranche05.000478`
479. [Docusaurus: escolher formato MDX ou CommonMark conforme a sintaxe dos docs](../../domains/software-0010/software/criacao-ia/docusaurus-mdx-vs-commonmark-format.md) — `software.criacao_ia.tranche05.000479`
480. [Docusaurus i18n: localizar conteúdo por locale sem supor detecção automática](../../domains/software-0010/software/criacao-ia/docusaurus-i18n-localized-content-layout.md) — `software.criacao_ia.tranche05.000480`

### Ink: integrar narrativa interativa compilada com o runtime do jogo

481. [Ink: compilar arquivos .ink para JSON e carregar uma instância Story](../../domains/software-0010/software/criacao-ia/ink-compile-json-story-runtime.md) — `software.criacao_ia.tranche05.000481`
482. [Ink runtime: escolher Continue ou ContinueMaximally pela granularidade da interface](../../domains/software-0010/software/criacao-ia/ink-continue-output-granularity.md) — `software.criacao_ia.tranche05.000482`
483. [Ink runtime: apresentar currentChoices e retomar com ChooseChoiceIndex](../../domains/software-0010/software/criacao-ia/ink-current-choices-and-choice-index.md) — `software.criacao_ia.tranche05.000483`
484. [Ink runtime: salvar o estado narrativo completo com state.ToJson](../../domains/software-0010/software/criacao-ia/ink-save-complete-story-state-json.md) — `software.criacao_ia.tranche05.000484`
485. [Ink runtime: sincronizar variáveis globais e UI sem polling por frame](../../domains/software-0010/software/criacao-ia/ink-variables-state-and-observers.md) — `software.criacao_ia.tranche05.000485`
486. [Ink runtime: transportar tags de linha, knot e escolha como metadados invisíveis](../../domains/software-0010/software/criacao-ia/ink-tags-como-metadados-de-conteudo.md) — `software.criacao_ia.tranche05.000486`
487. [Ink: classificar funções externas como ações ou operações lookahead-safe](../../domains/software-0010/software/criacao-ia/ink-external-functions-lookahead-safe.md) — `software.criacao_ia.tranche05.000487`
488. [Ink runtime: chamar função do roteiro com EvaluationFunction sem consumir diálogo](../../domains/software-0010/software/criacao-ia/ink-evaluationfunction-call-from-game.md) — `software.criacao_ia.tranche05.000488`
489. [Ink: preferir compilação prévia e configurar includes no fluxo de compilação C#](../../domains/software-0010/software/criacao-ia/ink-precompile-include-filehandler.md) — `software.criacao_ia.tranche05.000489`
490. [Ink runtime: registrar onError para erros que só aparecem durante a narrativa](../../domains/software-0010/software/criacao-ia/ink-runtime-error-handler.md) — `software.criacao_ia.tranche05.000490`

### Unity Addressables 2.7: carregar, baixar, versionar e liberar conteúdo remoto

491. [Addressables: escolher LoadAssetAsync ou LoadAssetsAsync conforme o número de resultados](../../domains/software-0010/software/criacao-ia/addressables-load-single-vs-multiple-keys.md) — `software.criacao_ia.tranche05.000491`
492. [Addressables: tratar AssetReference como referência serializada, não como carregamento automático](../../domains/software-0010/software/criacao-ia/addressables-assetreference-explicit-load-release.md) — `software.criacao_ia.tranche05.000492`
493. [Addressables: aguardar operações assíncronas pelo handle sem bloquear a thread](../../domains/software-0010/software/criacao-ia/addressables-async-operation-handles.md) — `software.criacao_ia.tranche05.000493`
494. [Addressables: equilibrar cada load com release e entender contagem de referências](../../domains/software-0010/software/criacao-ia/addressables-release-reference-count-memory.md) — `software.criacao_ia.tranche05.000494`
495. [Addressables: exibir progresso por bytes com GetDownloadStatus](../../domains/software-0010/software/criacao-ia/addressables-download-progress-bytes.md) — `software.criacao_ia.tranche05.000495`
496. [Addressables: medir e pré-baixar dependências antes de entrar no fluxo de jogo](../../domains/software-0010/software/criacao-ia/addressables-predownload-dependencies-consent.md) — `software.criacao_ia.tranche05.000496`
497. [Addressables: usar Profiles para alternar caminhos de build e load por ambiente](../../domains/software-0010/software/criacao-ia/addressables-profiles-build-load-paths.md) — `software.criacao_ia.tranche05.000497`
498. [Addressables: diferenciar cache remoto em disco de memória e limpar bundles órfãos](../../domains/software-0010/software/criacao-ia/addressables-assetbundle-cache-cleanup.md) — `software.criacao_ia.tranche05.000498`
499. [Addressables: publicar conteúdo alterado com content update build e estado do release](../../domains/software-0010/software/criacao-ia/addressables-content-only-update-build-state.md) — `software.criacao_ia.tranche05.000499`
500. [Addressables: detectar atualizações e trocar catálogos no momento apropriado](../../domains/software-0010/software/criacao-ia/addressables-check-and-update-catalogs-runtime.md) — `software.criacao_ia.tranche05.000500`
## Critério de entrada na contagem

Cada nota futura precisa ter frontmatter rastreável, ao menos 100 palavras, explicação, exemplo, limites, verificação, duas fontes HTTPS específicas, wikilinks resolvidos e ausência de marcadores de template. A revisão factual por IA precisa usar `revisao_ia: aprovada`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia`; não cria nem altera aprovação humana. Gate e revisão factual serão executados e registrados por tranche antes de reconciliar as contagens.

## Artefatos do lote

- MOC: [`MOC-Criacao-IA-Software-0010.md`](../../00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)
- Abertura e escopo: [`batch-opening-software-criacao-ia-2000-0004.md`](../reports/batch-opening-software-criacao-ia-2000-0004.md)
- Reconciliação inicial (snapshot de abertura): [`batch-reconciliation-software-criacao-ia-2000-0004-initial.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-initial.md)
- Revisão factual IA da tranche 1: [`ai-review-software-criacao-ia-2000-0004-tranche-01.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md)
- Gate da tranche 1: [`note-quality-software-criacao-ia-2000-0004-tranche-01.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md)
- Reconciliação da tranche 1: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)
- Revisão factual IA da tranche 2: [`ai-review-software-criacao-ia-2000-0004-tranche-02.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md)
- Gate da tranche 2: [`note-quality-software-criacao-ia-2000-0004-tranche-02.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md)
- Reconciliação da tranche 2: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md)
- Revisão factual IA da tranche 3: [`ai-review-software-criacao-ia-2000-0004-tranche-03.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md)
- Gate da tranche 3: [`note-quality-software-criacao-ia-2000-0004-tranche-03.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md)
- Reconciliação da tranche 3: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)
- Revisão factual IA da tranche 4: [`ai-review-software-criacao-ia-2000-0004-tranche-04.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md)
- Gate da tranche 4: [`note-quality-software-criacao-ia-2000-0004-tranche-04.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md)
- Reconciliação da tranche 4: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)
- Revisão factual IA da tranche 5: [`ai-review-software-criacao-ia-2000-0004-tranche-05.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md)
- Gate da tranche 5: [`note-quality-software-criacao-ia-2000-0004-tranche-05.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md)
- Auditoria de links da tranche 5: [`source-link-audit-software-criacao-ia-2000-0004-tranche-05.md`](../reports/source-link-audit-software-criacao-ia-2000-0004-tranche-05.md)
- Reconciliação da tranche 5: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md)

- Diretório das notas: [`domains/software-0010/software/criacao-ia/`](../../domains/software-0010/software/criacao-ia/)
