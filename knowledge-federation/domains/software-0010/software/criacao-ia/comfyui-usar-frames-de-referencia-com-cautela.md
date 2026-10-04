---
id: software.criacao_ia.tranche01.000087
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

# ComfyUI: usar frames de referência com cautela

## Em uma frase

Workflows que recebem primeiro ou último frame podem ancorar limites temporais de um clipe quando o modelo documenta essa entrada.

## Por que importa

Referências ajudam orientar composição e transição quando uma sequência precisa começar ou terminar num estado definido.

## Como funciona

Use somente entradas aceitas pelo nó, verifique ordem dos frames e ajuste movimento sem assumir que todos os detalhes serão mantidos.

## Exemplo

Uma cena de porta usa imagem inicial fechada e quadro final aberto para testar transição antes da animação final.

## Limites e trade-offs

Modelos podem distorcer objetos, inventar frames intermediários ou não respeitar exato enquadramento de referência.

## Como verificar

Compare ambos os extremos e inspecione frames intermediários, continuidade de cenário e elementos que deveriam permanecer fixos.

## Conexões
- [[comfyui-ajustar-prompt-sem-quebrar-o-grafo]] — ComfyUI: ajustar prompt sem quebrar o grafo.
- [[comfyui-salvar-e-versionar-o-workflow]] — ComfyUI: salvar e versionar o workflow.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
