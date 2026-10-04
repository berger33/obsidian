---
id: software.criacao_ia.tranche01.000086
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

# ComfyUI: ajustar prompt sem quebrar o grafo

## Em uma frase

Prompt descreve conteúdo e movimento, enquanto as conexões do workflow controlam modelos e transformação de dados.

## Por que importa

Separar alterações semânticas de alterações estruturais facilita saber se a mudança veio do texto ou da configuração.

## Como funciona

Mude primeiro uma característica do prompt, mantenha seed e nós relevantes estáveis quando suportado e compare resultados lado a lado.

## Exemplo

Para um plano do jogo, altere apenas direção do movimento de câmera mantendo design do cenário aprovado.

## Limites e trade-offs

Prompt não controla com precisão cada frame; uma mudança pequena pode gerar composição ou identidade muito diferente.

## Como verificar

Guarde prompt e workflow de cada render e avalie a sequência inteira, não apenas thumbnail inicial.

## Conexões
- [[comfyui-controlar-duracao-e-numero-de-frames]] — ComfyUI: controlar duração e número de frames.
- [[comfyui-usar-frames-de-referencia-com-cautela]] — ComfyUI: usar frames de referência com cautela.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
