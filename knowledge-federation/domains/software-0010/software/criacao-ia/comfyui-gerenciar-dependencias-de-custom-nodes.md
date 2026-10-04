---
id: software.criacao_ia.tranche01.000089
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

# ComfyUI: gerenciar dependências de custom nodes

## Em uma frase

Workflows podem depender de nós fornecidos por extensões e não apenas das operações nativas do ComfyUI.

## Por que importa

Identificar dependências evita que outro artista receba grafo com funções ausentes ou comportamento alterado silenciosamente.

## Como funciona

Registre nome e versão das extensões, evite atualizar no meio de uma revisão e teste upgrades em cópia isolada.

## Exemplo

Uma equipe trava versão do node pack de vídeo antes de renderizar sequência que precisa ser repetida por vários artistas.

## Limites e trade-offs

Extensões podem introduzir código de terceiros, incompatibilidade e alterações de licença ou segurança.

## Como verificar

Compare lista de nós instalados com workflow e documentação e rode render de referência depois de qualquer atualização.

## Conexões
- [[comfyui-salvar-e-versionar-o-workflow]] — ComfyUI: salvar e versionar o workflow.
- [[comfyui-aprovar-asset-gerado-para-producao]] — ComfyUI: aprovar asset gerado para produção.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
