---
id: software.testes.tranche21.001527
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/boxed/mutmut", "https://github.com/boxed/mutmut/blob/main/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# mutmut: also_copy e profundidade máxima de pilha

## Em uma frase
Arquivos extras de suporte entram na corrida pela chave also_copy, e max_stack_depth limita a contagem de relevância de um teste à profundidade de pilha dentro do código-fonte.

## Por que importa
Sem also_copy, snapshots e conftest ficam fora da cópia isolada; sem max_stack_depth, funções chamadas por meia suíte geram reteste de centenas de casos irrelevantes.

## Como funciona
Liste os arquivos que o teste precisa além da fonte e defina um teto de pilha que force testes unitários limpos por função.

## Exemplo
also_copy=iommi/snapshots/ com conftest.py no exemplo oficial resolve dependências fora da árvore mutada.

## Limites e trade-offs
O teto baixo demais declara como não-relevante o teste que integrava de propósito, aumentando sobreviventes; o README admite a troca.

## Como verificar
Reduza o max_stack_depth progressivamente e observe mutantes que eram mortos virarem sobreviventes documentados.

## Conexões
- [[mutmut-config-paths]] — Veja também: mutmut: configuração em setup.cfg ou pyproject.
- [[mutmut-mutate-selection]] — Veja também: mutmut: escolher linhas com cobertura ou glob.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
