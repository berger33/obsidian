---
id: software.testes.tranche21.001475
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
fontes: ["https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md", "https://github.com/avajs/ava/blob/main/readme.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AVA: casos .serial antes dos concorrentes

## Em uma frase
O modificador .serial força testes que não podem dividir o processo a rodarem em sequência, sempre antes dos testes concorrentes do mesmo arquivo.

## Por que importa
Arquivos inteiros em série desperdiçam o modelo do AVA; o modificador por teste deixa o gargalo explícito e pequeno.

## Como funciona
Aplique test.serial nos casos que manipulam recursos globais e deixe os demais concorrentes; também funciona com hooks e com .todo().

## Exemplo
O teste que grava no diretório temporário único do pacote fica .serial, e os outros nove continuam em paralelo.

## Limites e trade-offs
A serialização vale só dentro do arquivo: o AVA ainda roda arquivos diferentes ao mesmo tempo, a menos que o flag --serial da CLI limite isso.

## Como verificar
Rode um arquivo com um caso .serial e confirme no relatório que ele executou antes dos concorrentes.

## Conexões
- [[ava-async-support]] — Veja também: AVA: promessas, async e observáveis.
- [[ava-only-skip-todo-failing]] — Veja também: AVA: only, skip, todo e failing.

## Fontes
- [AVA — Guia Writing tests](https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md) — concorrência, modificadores, hooks e isolamento; consultado em 2026-10-03.
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
