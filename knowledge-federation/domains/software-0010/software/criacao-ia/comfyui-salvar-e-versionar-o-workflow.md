---
id: software.criacao_ia.tranche01.000088
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.comfy.org/basic-concepts/workflow", "https://docs.comfy.org/tutorials/video/wan/wan2_2"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: salvar e versionar o workflow

## Em uma frase

Salvar o grafo junto a prompt e parâmetros permite reconstruir um experimento e investigar por que um resultado mudou.

## Por que importa

Sem workflow preservado, um arquivo de vídeo isolado raramente explica modelos, nós e configurações que o produziram.

## Como funciona

Salve JSON do fluxo, anote versões do ComfyUI e nós, modelos e parâmetros e vincule cada vídeo ao identificador do projeto.

## Exemplo

Um clip de teste inclui JSON exportado, lista de modelos e observação sobre GPU usada, sem embutir credenciais privadas.

## Limites e trade-offs

Workflow pode conter caminhos locais ou identificadores sensíveis; pesos de terceiros podem não ser redistribuíveis.

## Como verificar

Abra uma cópia limpa do workflow e confirme nós, entradas e capacidade de reexecução conforme licenças e dependências disponíveis.

## Conexões
- [[comfyui-usar-frames-de-referencia-com-cautela]] — ComfyUI: usar frames de referência com cautela.
- [[comfyui-gerenciar-dependencias-de-custom-nodes]] — ComfyUI: gerenciar dependências de custom nodes.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
