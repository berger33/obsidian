---
id: software.criacao_ia.tranche01.000081
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

# ComfyUI: ler um workflow como grafo

## Em uma frase

Um workflow ComfyUI conecta nós tipados para carregar modelos, transformar dados, amostrar resultados e salvar saídas.

## Por que importa

Visualizar dependências ajuda localizar onde texto, imagem, modelo ou parâmetro influencia o vídeo final.

## Como funciona

Siga conexões da entrada até os nós de salvamento e leia tipo e valor de cada nó antes de mudar configurações.

## Exemplo

Num fluxo text-to-video, prompt, carregadores e latentes alimentam amostragem, decodificação e nó que grava o clipe.

## Limites e trade-offs

Nós customizados podem mudar comportamento e dependências; um grafo não é portátil só por ser um arquivo JSON.

## Como verificar

Abra workflow sem executar, confira nós ausentes e compare parâmetros com o exemplo documentado para a versão instalada.

## Conexões
- [[unreal-manter-renders-rastreaveis]] — Unreal: manter renders rastreáveis.
- [[comfyui-instalar-modelos-nos-caminhos-esperados]] — ComfyUI: instalar modelos nos caminhos esperados.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
