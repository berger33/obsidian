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
- Notas materiais redigidas: **100 / 2.000 (5,00%)**
- Gate automatizado: **100/100 aprovadas**
- Revisão factual humana: **0/100** (nenhuma aprovação humana solicitada ou registrada)
- Revisão factual por IA: **100/100** (relatório da tranche 1)
- Notas válidas contabilizadas: **100/2.000 (5,00%)**
- Estado: `in_progress` — tranche 1 concluída e reconciliada; 19 tranches planejadas permanecem sem IDs reservados.

A cadência descreve capacidade planejada, não reserva IDs. As notas materiais existentes são somente os IDs 1–100, com arquivos e conteúdo; para as 1.900 notas ainda não produzidas não há IDs reservados, placeholders ou progresso virtual. MOC, manifesto e relatórios administrativos não são notas do lote e não contam como progresso.

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

## Critério de entrada na contagem

Cada nota futura precisa ter frontmatter rastreável, ao menos 100 palavras, explicação, exemplo, limites, verificação, duas fontes HTTPS específicas, wikilinks resolvidos e ausência de marcadores de template. A revisão factual por IA precisa usar `revisao_ia: aprovada`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia`; não cria nem altera aprovação humana. Gate e revisão factual serão executados e registrados por tranche antes de reconciliar as contagens.

## Artefatos do lote

- MOC: [`MOC-Criacao-IA-Software-0010.md`](../../00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)
- Abertura e escopo: [`batch-opening-software-criacao-ia-2000-0004.md`](../reports/batch-opening-software-criacao-ia-2000-0004.md)
- Reconciliação inicial (snapshot de abertura): [`batch-reconciliation-software-criacao-ia-2000-0004-initial.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-initial.md)
- Revisão factual IA da tranche 1: [`ai-review-software-criacao-ia-2000-0004-tranche-01.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md)
- Gate da tranche 1: [`note-quality-software-criacao-ia-2000-0004-tranche-01.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md)
- Reconciliação da tranche 1: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)
- Diretório das notas: [`domains/software-0010/software/criacao-ia/`](../../domains/software-0010/software/criacao-ia/)
