---
id: software.testes.tranche24.001819
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/google/syzkaller/master/README.md", "https://github.com/google/syzkaller"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Badges públicos e o disclaimer de que não é produto Google

## Em uma frase
O README fecha com a frase de status — "This is NOT an official Google product" — e abre com a fileira de badges verificáveis: CI do GitHub Actions, build do OSS-Fuzz (com o link para a lista de issues filtrada por Proj-syzkaller no tracker), Go Report Card, codecov e GoDoc, sob licença Apache 2.0 — informação suficiente para inferir a natureza do projeto (Go, qualidade medida publicamente, uso real no OSS-Fuzz).

## Por que importa
O fuzzer alimenta o pipeline de segurança do OSS-Fuzz para kernels — o badge com link para o bug tracker público é a auditoria contínua do próprio projeto; o disclaimer define expectativas jurídicas: código de pesquisa de qualidade de produção, sem contrato de suporte.

## Como funciona
Ao avaliar adoção, use os fatos públicos: o tracker do OSS-Fuzz com a label Proj-syzkaller mostra o estado atual dos bugs encontrados; o CI badge, a disciplina de regressão; o Go Report Card, a saúde estática — três links diretos na abertura do README.

## Exemplo
A coluna "Found bugs" no README e o dashboard do OSS-Fuzz servem como due diligence contínua para quem roda o syzkaller em kernel próprio: a ferramenta é julgada pelos achados visíveis.

## Limites e trade-offs
Badges e disclaimers descrevem o momento da consulta; nenhum deles atesta suporte a versão específica de kernel — a matriz de suporte está na própria lista do README, que esta nota cobre separadamente.

## Como verificar
Os badges, o link OSS-Fuzz e o disclaimer final foram lidos na página oficial do repositório google/syzkaller.

## Conexões
- [[syzkaller-bug-reporting]] — Veja também: Onde reportar: found_bugs por SO e o guia Linux.

## Fontes
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
- [Repositório oficial google/syzkaller](https://github.com/google/syzkaller) — Repositório oficial do syzkaller no GitHub com código-fonte, descrições de syscalls, integração OSS-Fuzz e documentação.; consultado em 2026-10-03.
