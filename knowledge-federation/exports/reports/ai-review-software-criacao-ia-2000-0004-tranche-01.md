---
tipo: revisao-factual-ia
lote: software-criacao-ia-2000-0004
tranche: 01
data: 2026-10-04
resultado: aprovada
---

# Revisão factual por IA — lote 4, tranche 1 (IDs 000001–000100)

## Escopo e procedimento

Esta revisão cobre exatamente 100 notas materiais da primeira tranche, IDs `software.criacao_ia.tranche01.000001` a `software.criacao_ia.tranche01.000100`. Os tópicos foram confrontados com páginas oficiais específicas listadas em cada nota; recomendações editoriais e de engenharia estão identificadas como procedimentos, não como garantias dos fornecedores. A revisão não concede aprovação humana e não altera campos de revisão humana.

Foram revisados: correspondência entre título e fonte; nomenclatura de APIs e ferramentas; passos e exemplos; limites e condições de uso; versão/documentação aplicável; precisão das afirmações sobre o que um modelo, engine ou nó efetivamente faz. Quando há variação por versão, hardware, configuração ou política de produto, a nota explicita essa dependência e inclui verificação local.

## Trilhas e fontes primárias

### Programação assistida com GitHub Copilot

- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento.

Notas revisadas:
- `software.criacao_ia.tranche01.000001` — [Copilot: prompts com critérios de aceitação](../../domains/software-0010/software/criacao-ia/copilot-prompts-com-criterios-de-aceitacao.md)
- `software.criacao_ia.tranche01.000002` — [Copilot: fornecer contexto de repositório](../../domains/software-0010/software/criacao-ia/copilot-fornecer-contexto-de-repositorio.md)
- `software.criacao_ia.tranche01.000003` — [Copilot: escolher Ask, Edit ou Agent](../../domains/software-0010/software/criacao-ia/copilot-escolher-ask-edit-ou-agent.md)
- `software.criacao_ia.tranche01.000004` — [Copilot: dividir mudanças em tarefas pequenas](../../domains/software-0010/software/criacao-ia/copilot-dividir-mudancas-em-tarefas-pequenas.md)
- `software.criacao_ia.tranche01.000005` — [Copilot: tratar sugestões como rascunho](../../domains/software-0010/software/criacao-ia/copilot-tratar-sugestoes-como-rascunho.md)
- `software.criacao_ia.tranche01.000006` — [Copilot: pedir explicação de código existente](../../domains/software-0010/software/criacao-ia/copilot-pedir-explicacao-de-codigo-existente.md)
- `software.criacao_ia.tranche01.000007` — [Copilot: gerar testes a partir de comportamento](../../domains/software-0010/software/criacao-ia/copilot-gerar-testes-a-partir-de-comportamento.md)
- `software.criacao_ia.tranche01.000008` — [Copilot: explicitar casos de erro no prompt](../../domains/software-0010/software/criacao-ia/copilot-explicitar-casos-de-erro-no-prompt.md)
- `software.criacao_ia.tranche01.000009` — [Copilot: registrar instruções do repositório](../../domains/software-0010/software/criacao-ia/copilot-registrar-instrucoes-do-repositorio.md)
- `software.criacao_ia.tranche01.000010` — [Copilot: inspecionar o diff antes de aceitar](../../domains/software-0010/software/criacao-ia/copilot-inspecionar-o-diff-antes-de-aceitar.md)

### Integração de geração de texto com OpenAI Responses API

- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts.

Notas revisadas:
- `software.criacao_ia.tranche01.000011` — [Responses API: iniciar uma chamada de texto](../../domains/software-0010/software/criacao-ia/responses-api-iniciar-uma-chamada-de-texto.md)
- `software.criacao_ia.tranche01.000012` — [Responses API: separar instruções e entrada](../../domains/software-0010/software/criacao-ia/responses-api-separar-instrucoes-e-entrada.md)
- `software.criacao_ia.tranche01.000013` — [Responses API: definir o objetivo do prompt](../../domains/software-0010/software/criacao-ia/responses-api-definir-o-objetivo-do-prompt.md)
- `software.criacao_ia.tranche01.000014` — [Responses API: extrair texto da resposta](../../domains/software-0010/software/criacao-ia/responses-api-extrair-texto-da-resposta.md)
- `software.criacao_ia.tranche01.000015` — [Responses API: escolher modelo por tarefa](../../domains/software-0010/software/criacao-ia/responses-api-escolher-modelo-por-tarefa.md)
- `software.criacao_ia.tranche01.000016` — [Responses API: limitar o tamanho da saída](../../domains/software-0010/software/criacao-ia/responses-api-limitar-o-tamanho-da-saida.md)
- `software.criacao_ia.tranche01.000017` — [Responses API: criar um prompt versionável](../../domains/software-0010/software/criacao-ia/responses-api-criar-um-prompt-versionavel.md)
- `software.criacao_ia.tranche01.000018` — [Responses API: isolar conteúdo não confiável](../../domains/software-0010/software/criacao-ia/responses-api-isolar-conteudo-nao-confiavel.md)
- `software.criacao_ia.tranche01.000019` — [Responses API: tratar falhas e repetição](../../domains/software-0010/software/criacao-ia/responses-api-tratar-falhas-e-repeticao.md)
- `software.criacao_ia.tranche01.000020` — [Responses API: avaliar geração com exemplos](../../domains/software-0010/software/criacao-ia/responses-api-avaliar-geracao-com-exemplos.md)

### Ferramentas e saídas estruturadas para apps com modelos

- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações.

Notas revisadas:
- `software.criacao_ia.tranche01.000021` — [Function calling: declarar contrato de ferramenta](../../domains/software-0010/software/criacao-ia/function-calling-declarar-contrato-de-ferramenta.md)
- `software.criacao_ia.tranche01.000022` — [Saída estruturada: usar JSON Schema estrito](../../domains/software-0010/software/criacao-ia/saida-estruturada-usar-json-schema-estrito.md)
- `software.criacao_ia.tranche01.000023` — [Function calling: executar no aplicativo, não no modelo](../../domains/software-0010/software/criacao-ia/function-calling-executar-no-aplicativo-nao-no-modelo.md)
- `software.criacao_ia.tranche01.000024` — [Function calling: correlacionar chamadas pelo identificador](../../domains/software-0010/software/criacao-ia/function-calling-correlacionar-chamadas-pelo-identificador.md)
- `software.criacao_ia.tranche01.000025` — [Function calling: lidar com zero ou várias chamadas](../../domains/software-0010/software/criacao-ia/function-calling-lidar-com-zero-ou-varias-chamadas.md)
- `software.criacao_ia.tranche01.000026` — [Validação de argumentos de ferramentas](../../domains/software-0010/software/criacao-ia/validacao-de-argumentos-de-ferramentas.md)
- `software.criacao_ia.tranche01.000027` — [Ferramentas: restringir ações de gameplay](../../domains/software-0010/software/criacao-ia/ferramentas-restringir-acoes-de-gameplay.md)
- `software.criacao_ia.tranche01.000028` — [Ferramentas: pedir confirmação antes de efeitos externos](../../domains/software-0010/software/criacao-ia/ferramentas-pedir-confirmacao-antes-de-efeitos-externos.md)
- `software.criacao_ia.tranche01.000029` — [Function calling: minimizar dados retornados](../../domains/software-0010/software/criacao-ia/function-calling-minimizar-dados-retornados.md)
- `software.criacao_ia.tranche01.000030` — [Ferramentas: testar exceções e falhas de execução](../../domains/software-0010/software/criacao-ia/ferramentas-testar-excecoes-e-falhas-de-execucao.md)

### Agentes de aprendizagem em Unity ML-Agents

- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python.

Notas revisadas:
- `software.criacao_ia.tranche01.000031` — [ML-Agents: estruturar um Agent](../../domains/software-0010/software/criacao-ia/ml-agents-estruturar-um-agent.md)
- `software.criacao_ia.tranche01.000032` — [ML-Agents: escolher observações úteis](../../domains/software-0010/software/criacao-ia/ml-agents-escolher-observacoes-uteis.md)
- `software.criacao_ia.tranche01.000033` — [ML-Agents: mapear ações ao gameplay](../../domains/software-0010/software/criacao-ia/ml-agents-mapear-acoes-ao-gameplay.md)
- `software.criacao_ia.tranche01.000034` — [ML-Agents: desenhar recompensas](../../domains/software-0010/software/criacao-ia/ml-agents-desenhar-recompensas.md)
- `software.criacao_ia.tranche01.000035` — [ML-Agents: encerrar e reiniciar episódios](../../domains/software-0010/software/criacao-ia/ml-agents-encerrar-e-reiniciar-episodios.md)
- `software.criacao_ia.tranche01.000036` — [ML-Agents: controlar frequência de decisão](../../domains/software-0010/software/criacao-ia/ml-agents-controlar-frequencia-de-decisao.md)
- `software.criacao_ia.tranche01.000037` — [ML-Agents: criar cena de treinamento representativa](../../domains/software-0010/software/criacao-ia/ml-agents-criar-cena-de-treinamento-representativa.md)
- `software.criacao_ia.tranche01.000038` — [ML-Agents: iniciar treinamento reproduzível](../../domains/software-0010/software/criacao-ia/ml-agents-iniciar-treinamento-reproduzivel.md)
- `software.criacao_ia.tranche01.000039` — [ML-Agents: configurar PPO ou SAC por evidência](../../domains/software-0010/software/criacao-ia/ml-agents-configurar-ppo-ou-sac-por-evidencia.md)
- `software.criacao_ia.tranche01.000040` — [ML-Agents: avaliar o modelo em inferência](../../domains/software-0010/software/criacao-ia/ml-agents-avaliar-o-modelo-em-inferencia.md)

### IA de gameplay com Behavior Trees e EQS na Unreal Engine

- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente.

Notas revisadas:
- `software.criacao_ia.tranche01.000041` — [Unreal: separar Behavior Tree e Blackboard](../../domains/software-0010/software/criacao-ia/unreal-separar-behavior-tree-e-blackboard.md)
- `software.criacao_ia.tranche01.000042` — [Unreal: compor Sequence e Selector](../../domains/software-0010/software/criacao-ia/unreal-compor-sequence-e-selector.md)
- `software.criacao_ia.tranche01.000043` — [Unreal: usar Decorators como condições](../../domains/software-0010/software/criacao-ia/unreal-usar-decorators-como-condicoes.md)
- `software.criacao_ia.tranche01.000044` — [Unreal: encapsular ação em Tasks](../../domains/software-0010/software/criacao-ia/unreal-encapsular-acao-em-tasks.md)
- `software.criacao_ia.tranche01.000045` — [Unreal: escolher aborts de observadores](../../domains/software-0010/software/criacao-ia/unreal-escolher-aborts-de-observadores.md)
- `software.criacao_ia.tranche01.000046` — [Unreal EQS: gerar candidatos espaciais](../../domains/software-0010/software/criacao-ia/unreal-eqs-gerar-candidatos-espaciais.md)
- `software.criacao_ia.tranche01.000047` — [Unreal EQS: selecionar contextos coerentes](../../domains/software-0010/software/criacao-ia/unreal-eqs-selecionar-contextos-coerentes.md)
- `software.criacao_ia.tranche01.000048` — [Unreal EQS: compor Tests e pontuação](../../domains/software-0010/software/criacao-ia/unreal-eqs-compor-tests-e-pontuacao.md)
- `software.criacao_ia.tranche01.000049` — [Unreal EQS: enviar resultado à Behavior Tree](../../domains/software-0010/software/criacao-ia/unreal-eqs-enviar-resultado-a-behavior-tree.md)
- `software.criacao_ia.tranche01.000050` — [Unreal: depurar a decisão do NPC em runtime](../../domains/software-0010/software/criacao-ia/unreal-depurar-a-decisao-do-npc-em-runtime.md)

### Navegação e agentes de gameplay em Godot

- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões.

Notas revisadas:
- `software.criacao_ia.tranche01.000051` — [Godot: preparar malha de navegação](../../domains/software-0010/software/criacao-ia/godot-preparar-malha-de-navegacao.md)
- `software.criacao_ia.tranche01.000052` — [Godot: configurar destino do NavigationAgent](../../domains/software-0010/software/criacao-ia/godot-configurar-destino-do-navigationagent.md)
- `software.criacao_ia.tranche01.000053` — [Godot: sincronizar consultas com o mapa](../../domains/software-0010/software/criacao-ia/godot-sincronizar-consultas-com-o-mapa.md)
- `software.criacao_ia.tranche01.000054` — [Godot: controlar a chegada ao waypoint](../../domains/software-0010/software/criacao-ia/godot-controlar-a-chegada-ao-waypoint.md)
- `software.criacao_ia.tranche01.000055` — [Godot: distinguir caminho de evasão local](../../domains/software-0010/software/criacao-ia/godot-distinguir-caminho-de-evasao-local.md)
- `software.criacao_ia.tranche01.000056` — [Godot: aplicar velocidade de avoidance](../../domains/software-0010/software/criacao-ia/godot-aplicar-velocidade-de-avoidance.md)
- `software.criacao_ia.tranche01.000057` — [Godot: particionar avoidance com layers](../../domains/software-0010/software/criacao-ia/godot-particionar-avoidance-com-layers.md)
- `software.criacao_ia.tranche01.000058` — [Godot: usar obstacles para geometria e fluxo](../../domains/software-0010/software/criacao-ia/godot-usar-obstacles-para-geometria-e-fluxo.md)
- `software.criacao_ia.tranche01.000059` — [Godot: escolher NavigationLayers por uso](../../domains/software-0010/software/criacao-ia/godot-escolher-navigationlayers-por-uso.md)
- `software.criacao_ia.tranche01.000060` — [Godot: validar navegação em movimento real](../../domains/software-0010/software/criacao-ia/godot-validar-navegacao-em-movimento-real.md)

### Animação e exportação de conteúdo de jogo no Blender

- [Blender Manual — Nonlinear Animation Editor](https://docs.blender.org/manual/en/latest/editors/nla/index.html) — apresenta faixas, strips e ações no editor NLA; usado na nota específica sobre organização de Actions nesse editor.
- [Blender Manual — Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) — Descreve ações e seu uso para organizar dados de animação no Blender.
- [Blender Manual — glTF 2.0 export](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html) — Documenta opções, objetos e animações suportados pela exportação glTF do Blender.

Notas revisadas:
- `software.criacao_ia.tranche01.000061` — [Blender: organizar clips como Actions](../../domains/software-0010/software/criacao-ia/blender-organizar-clips-como-actions.md)
- `software.criacao_ia.tranche01.000062` — [Blender: nomear Actions para o pipeline](../../domains/software-0010/software/criacao-ia/blender-nomear-actions-para-o-pipeline.md)
- `software.criacao_ia.tranche01.000063` — [Blender: preservar ações com NLA](../../domains/software-0010/software/criacao-ia/blender-preservar-acoes-com-nla.md)
- `software.criacao_ia.tranche01.000064` — [Blender: conferir intervalos de keyframes](../../domains/software-0010/software/criacao-ia/blender-conferir-intervalos-de-keyframes.md)
- `software.criacao_ia.tranche01.000065` — [Blender: validar o rig antes de exportar](../../domains/software-0010/software/criacao-ia/blender-validar-o-rig-antes-de-exportar.md)
- `software.criacao_ia.tranche01.000066` — [Blender: exportar somente o conteúdo necessário](../../domains/software-0010/software/criacao-ia/blender-exportar-somente-o-conteudo-necessario.md)
- `software.criacao_ia.tranche01.000067` — [Blender: checar compatibilidade de animação glTF](../../domains/software-0010/software/criacao-ia/blender-checar-compatibilidade-de-animacao-gltf.md)
- `software.criacao_ia.tranche01.000068` — [Blender: controlar múltiplas Actions no export](../../domains/software-0010/software/criacao-ia/blender-controlar-multiplas-actions-no-export.md)
- `software.criacao_ia.tranche01.000069` — [Blender: separar movimento in-place e root motion](../../domains/software-0010/software/criacao-ia/blender-separar-movimento-in-place-e-root-motion.md)
- `software.criacao_ia.tranche01.000070` — [Blender: revisar animação dentro do jogo](../../domains/software-0010/software/criacao-ia/blender-revisar-animacao-dentro-do-jogo.md)

### Cinematics e renders para jogos na Unreal Engine

- [Epic Games — Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) — Explica Level Sequence, Level Sequence Actor, tracks, keyframes e edição de cinematics.
- [Epic Games — Movie Render Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine) — Documenta a renderização de cinematics pela Movie Render Queue e Movie Render Graph.

Notas revisadas:
- `software.criacao_ia.tranche01.000071` — [Unreal Sequencer: distinguir asset e actor](../../domains/software-0010/software/criacao-ia/unreal-sequencer-distinguir-asset-e-actor.md)
- `software.criacao_ia.tranche01.000072` — [Unreal Sequencer: animar com tracks e keyframes](../../domains/software-0010/software/criacao-ia/unreal-sequencer-animar-com-tracks-e-keyframes.md)
- `software.criacao_ia.tranche01.000073` — [Unreal Sequencer: construir cortes de câmera](../../domains/software-0010/software/criacao-ia/unreal-sequencer-construir-cortes-de-camera.md)
- `software.criacao_ia.tranche01.000074` — [Unreal Sequencer: organizar Shots e Sub-Sequences](../../domains/software-0010/software/criacao-ia/unreal-sequencer-organizar-shots-e-sub-sequences.md)
- `software.criacao_ia.tranche01.000075` — [Unreal: capturar Takes com Take Recorder](../../domains/software-0010/software/criacao-ia/unreal-capturar-takes-com-take-recorder.md)
- `software.criacao_ia.tranche01.000076` — [Unreal: acionar Sequencer durante gameplay](../../domains/software-0010/software/criacao-ia/unreal-acionar-sequencer-durante-gameplay.md)
- `software.criacao_ia.tranche01.000077` — [Unreal: montar uma fila de renderização](../../domains/software-0010/software/criacao-ia/unreal-montar-uma-fila-de-renderizacao.md)
- `software.criacao_ia.tranche01.000078` — [Unreal: versionar presets e configurações de render](../../domains/software-0010/software/criacao-ia/unreal-versionar-presets-e-configuracoes-de-render.md)
- `software.criacao_ia.tranche01.000079` — [Unreal: revisar sequência renderizada além do viewport](../../domains/software-0010/software/criacao-ia/unreal-revisar-sequencia-renderizada-alem-do-viewport.md)
- `software.criacao_ia.tranche01.000080` — [Unreal: manter renders rastreáveis](../../domains/software-0010/software/criacao-ia/unreal-manter-renders-rastreaveis.md)

### Workflows de geração de vídeo e assets com ComfyUI

- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros.

Notas revisadas:
- `software.criacao_ia.tranche01.000081` — [ComfyUI: ler um workflow como grafo](../../domains/software-0010/software/criacao-ia/comfyui-ler-um-workflow-como-grafo.md)
- `software.criacao_ia.tranche01.000082` — [ComfyUI: instalar modelos nos caminhos esperados](../../domains/software-0010/software/criacao-ia/comfyui-instalar-modelos-nos-caminhos-esperados.md)
- `software.criacao_ia.tranche01.000083` — [ComfyUI: escolher template antes de montar do zero](../../domains/software-0010/software/criacao-ia/comfyui-escolher-template-antes-de-montar-do-zero.md)
- `software.criacao_ia.tranche01.000084` — [ComfyUI: escolher text-to-video ou image-to-video](../../domains/software-0010/software/criacao-ia/comfyui-escolher-text-to-video-ou-image-to-video.md)
- `software.criacao_ia.tranche01.000085` — [ComfyUI: controlar duração e número de frames](../../domains/software-0010/software/criacao-ia/comfyui-controlar-duracao-e-numero-de-frames.md)
- `software.criacao_ia.tranche01.000086` — [ComfyUI: ajustar prompt sem quebrar o grafo](../../domains/software-0010/software/criacao-ia/comfyui-ajustar-prompt-sem-quebrar-o-grafo.md)
- `software.criacao_ia.tranche01.000087` — [ComfyUI: usar frames de referência com cautela](../../domains/software-0010/software/criacao-ia/comfyui-usar-frames-de-referencia-com-cautela.md)
- `software.criacao_ia.tranche01.000088` — [ComfyUI: salvar e versionar o workflow](../../domains/software-0010/software/criacao-ia/comfyui-salvar-e-versionar-o-workflow.md)
- `software.criacao_ia.tranche01.000089` — [ComfyUI: gerenciar dependências de custom nodes](../../domains/software-0010/software/criacao-ia/comfyui-gerenciar-dependencias-de-custom-nodes.md)
- `software.criacao_ia.tranche01.000090` — [ComfyUI: aprovar asset gerado para produção](../../domains/software-0010/software/criacao-ia/comfyui-aprovar-asset-gerado-para-producao.md)

### Tutoriais e documentação técnica para software, apps e jogos

- [Diátaxis — Start here](https://diataxis.fr/start-here/) — Apresenta as quatro formas documentais: tutorial, how-to, referência e explicação.
- [GitHub Docs — Best practices for GitHub documentation](https://docs.github.com/en/contributing/writing-for-github-docs/best-practices-for-github-docs) — Recomendações oficiais sobre público, objetivo, estrutura, exemplos e manutenção de documentação.

Notas revisadas:
- `software.criacao_ia.tranche01.000091` — [Documentação: escolher entre tutorial e referência](../../domains/software-0010/software/criacao-ia/documentacao-escolher-entre-tutorial-e-referencia.md)
- `software.criacao_ia.tranche01.000092` — [Documentação: declarar leitor e resultado](../../domains/software-0010/software/criacao-ia/documentacao-declarar-leitor-e-resultado.md)
- `software.criacao_ia.tranche01.000093` — [Documentação: fixar versões e pré-requisitos](../../domains/software-0010/software/criacao-ia/documentacao-fixar-versoes-e-pre-requisitos.md)
- `software.criacao_ia.tranche01.000094` — [Tutorial: construir exemplo de ponta a ponta](../../domains/software-0010/software/criacao-ia/tutorial-construir-exemplo-de-ponta-a-ponta.md)
- `software.criacao_ia.tranche01.000095` — [How-to: organizar passos por tarefa](../../domains/software-0010/software/criacao-ia/how-to-organizar-passos-por-tarefa.md)
- `software.criacao_ia.tranche01.000096` — [Referência: descrever campos com precisão](../../domains/software-0010/software/criacao-ia/referencia-descrever-campos-com-precisao.md)
- `software.criacao_ia.tranche01.000097` — [Documentação: tornar resultado e verificação explícitos](../../domains/software-0010/software/criacao-ia/documentacao-tornar-resultado-e-verificacao-explicitos.md)
- `software.criacao_ia.tranche01.000098` — [Documentação: usar imagens acessíveis e úteis](../../domains/software-0010/software/criacao-ia/documentacao-usar-imagens-acessiveis-e-uteis.md)
- `software.criacao_ia.tranche01.000099` — [Documentação: executar exemplos de código](../../domains/software-0010/software/criacao-ia/documentacao-executar-exemplos-de-codigo.md)
- `software.criacao_ia.tranche01.000100` — [Documentação: revisar tutorial gerado por IA](../../domains/software-0010/software/criacao-ia/documentacao-revisar-tutorial-gerado-por-ia.md)

## Resultado

- Notas analisadas: **100/100**.
- Notas com escopo verificável, exemplo e limites registrados: **100/100**.
- Fontes HTTPS primárias específicas: **2 por nota**.
- Revisão factual por IA: `aprovada`; revisor: `Arena.ai Agent Mode`; data: `2026-10-04`.
- Revisão humana: permanece `nao_solicitada`; nenhuma aprovação histórica foi alterada ou estendida.
- O gate estrutural e a reconciliação de contagens são executados separadamente antes do push.

## Limites da revisão

A revisão documental não substitui execução de builds, testes de projeto, teste em hardware final, verificação de licenças específicas de modelos/assets nem aprovação editorial humana. Resultados de IA e políticas de produtos são mutáveis; cada nota aponta a documentação primária a reconsultar. Nenhuma página antiga do site legado do Unity ML-Agents foi usada: as notas citam a documentação atual do pacote 4.0.
