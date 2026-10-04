---
id: software.criacao_ia.tranche01.000084
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

# ComfyUI: escolher text-to-video ou image-to-video

## Em uma frase

Workflows de texto e de imagem oferecem formas diferentes de condicionar conteúdo temporal no exemplo Wan documentado.

## Por que importa

Escolher modalidade conforme material disponível ajuda manter direção visual ou explorar cenas ainda sem imagem inicial.

## Como funciona

Use texto para partir de descrição e image-to-video quando a cena deve começar a partir de frame de referência; confira nó e modelo correspondentes.

## Exemplo

Um storyboard fornece frame inicial a animar, enquanto uma prévia de cenário pode nascer de descrição textual.

## Limites e trade-offs

Condicionamento por imagem não garante identidade perfeita nem preservação de todos os detalhes ao longo dos frames.

## Como verificar

Compare primeiro frame, sequência completa e prompt e registre artefatos de personagem, fundo e composição.

## Conexões
- [[comfyui-escolher-template-antes-de-montar-do-zero]] — ComfyUI: escolher template antes de montar do zero.
- [[comfyui-controlar-duracao-e-numero-de-frames]] — ComfyUI: controlar duração e número de frames.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
