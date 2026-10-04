---
id: software.testes.tranche21.001474
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

# AVA: promessas, async e observáveis

## Em uma frase
O AVA aguarda promessas retornadas pelo teste e falha o caso se a promessa rejeitar, com suporte nativo a funções async e consumo automático de observáveis até o fim.

## Por que importa
Esquecer o await é o flaky silencioso mais comum em JavaScript: sem retorno de promessa, o teste passaria cedo demais, e o AVA fecha essa porta.

## Como funciona
Retorne a promessa encadeada ou marque a função como async com await interno; ao devolver um observável, o AVA o consome inteiro antes de encerrar o teste.

## Exemplo
Um teste que consulta a API pode ser async t => t.is(await buscar().nome, 'unicorn') sem callbacks nem done.

## Limites e trade-offs
Testes observáveis só terminam se o stream emitir complete ou error; um stream suspenso segura o teste até o timeout.

## Como verificar
Faça um teste async esquecer um await em um caminho de erro e confirme que o teste falha em vez de passar silenciosamente.

## Conexões
- [[ava-declaring-tests]] — Veja também: AVA: declarar testes com título único.
- [[ava-serial-modifier]] — Veja também: AVA: casos .serial antes dos concorrentes.

## Fontes
- [AVA — Guia Writing tests](https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md) — concorrência, modificadores, hooks e isolamento; consultado em 2026-10-03.
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
