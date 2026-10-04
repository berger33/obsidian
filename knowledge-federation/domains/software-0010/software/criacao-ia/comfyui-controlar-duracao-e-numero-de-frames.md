---
id: software.criacao_ia.tranche01.000085
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

# ComfyUI: controlar duração e número de frames

## Em uma frase

Tamanho do vídeo depende de resolução e contagem de frames configuradas no workflow, sujeitas ao modelo usado.

## Por que importa

Ajustar duração e dimensões ao objetivo equilibra legibilidade, tempo de inferência e recursos de hardware.

## Como funciona

Comece com configuração conservadora, mude uma dimensão por rodada e conte frames e taxa pretendida antes de ampliar.

## Exemplo

Um animatic curto gera menos frames para revisão de câmera antes de produzir sequência mais longa para trailer.

## Limites e trade-offs

Mais frames ou resolução elevam custo e não asseguram coerência temporal ou detalhe útil.

## Como verificar

Registre resolução, frames, duração e tempo de execução; reproduza saída e confirme que o player interpreta taxa esperada.

## Conexões
- [[comfyui-escolher-text-to-video-ou-image-to-video]] — ComfyUI: escolher text-to-video ou image-to-video.
- [[comfyui-ajustar-prompt-sem-quebrar-o-grafo]] — ComfyUI: ajustar prompt sem quebrar o grafo.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
