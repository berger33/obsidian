---
id: software.criacao_ia.tranche04.000369
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.blender.org/manual/en/latest/editors/preferences/system.html", "https://docs.blender.org/manual/en/latest/interface/undo_redo.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender 5.2: os limites de memória do System — undo, shaders, geometry nodes — e seus efeitos colaterais

## Em uma frase
O painel Memory & Limits centraliza tetos que parecem cosméticos mas mudam comportamento: Undo Memory Limit, Texture/VBO Time Out com Garbage Collection Rate, Shader Compilation Method e Geometry Nodes Stack Limit.

## Por que importa
Cada um tem um trade-off documentado na página: Global Undo desligado economiza memória mas 'stops the Adjust Last Operation panel from functioning, also preventing tool options from being changed in some cases'; Subprocess na compilação de shaders acelera 'at the cost of higher memory usage'; e subir o stack limit de Geometry Nodes 'can result in crashes caused by running out of stack memory'. O painel é uma negociação de recursos, não um menu de prefs.

## Como funciona
Undo Steps/Undo Memory Limit (MB, 0 ilimitado) dimensionam o histórico — time com cenas de simulação longa aumenta; Texture Time Out controla quando a GL texture não-usada é liberada (0 mantém alocadas — o caminho do VRAM apertado é timeout baixo, não 'menos undo'). Shader Compilation Method Thread (memory-efficient, mais lento) vs. Subprocess (mais rápido em cores altas, RAM alta) é escolha por perfil da estação; a página nota que não há opção em macOS e que exige backend OpenGL, e requer restart. Stack Limit é o teto das node groups aninhadas — aumente com um crash de teste na cena, não por intuição.

## Exemplo
Um pipeline de look-dev que recompila shaders a cada nó novo adota Subprocess nas estações de 16 cores e volta a Thread nas laptops de review de 8 GB — a própria doc dá a regra de decisão.

## Limites e trade-offs
Essas prefs são da instalação, não do arquivo .blend: config de estação vive no doc de setup do estúdio, não no projeto. A dependência OpenGL do método de shader-compile significa que a pilha Vulkan da nota anterior remove esse dial — os dois painéis competem. Os timeouts de GL texturas não governam memória de render engine; para Cycles, os budget próprios estão nas suas páginas (a mesma página só faz o link do assunto).

## Como verificar
Meça o tempo de 'novo material com nó' nos dois métodos de compilação numa estação real — é o critério da doc para a escolha. Force o stack limit baixo e confirme que a cena de aninhamento profundo falha (crash controlado vira teste); restaure e valide. Reproduza o efeito colateral do Global Undo desligado (Adjust Last Operation morto) para que o time saiba por que ele fica ligado.

## Conexões
- [[blender-backend-vulkan-interface-52]] — Blender 5.2: o backend da interface é escolha (OpenGL × Vulkan) com custo de reinicialização.
- [[blender-proxy-setup-automatico-vs-manual]] — Blender VSE: Proxy Setup Automatic gera sozinho, Manual delega à farm — a decisão é de pipeline.

## Fontes
- [Blender — Preferences: System](https://docs.blender.org/manual/en/latest/editors/preferences/system.html) — as seções Memory & Limits e seus textos de trade-off, na íntegra Consulta: 2026-10-04.
- [Blender — Undo and Redo](https://docs.blender.org/manual/en/latest/interface/undo_redo.html) — a página see-also da própria System para os limites e o Global Undo Consulta: 2026-10-04.
