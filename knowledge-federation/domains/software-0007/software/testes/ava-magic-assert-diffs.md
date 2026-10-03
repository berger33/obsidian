---
id: software.testes.tranche21.001478
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
fontes: ["https://github.com/avajs/ava/blob/main/readme.md", "https://github.com/avajs/ava/blob/main/docs/03-assertions.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AVA: diagnóstico de falha com magic assert

## Em uma frase
O AVA amplia as falhas de asserção com trechos de código e diffs limpos entre real e esperado, destacando apenas a diferença em objetos e arrays.

## Por que importa
Em teste unitário, a mensagem de erro é o produto; reler stack trace de um deep-equal falho custa minutos por dia e desanima o ciclo interno.

## Como funciona
Escreva asserções normais de t (t.deepEqual, t.is) e deixe o relatório formatar o contraste; as linhas do próprio AVA saem do stack trace.

## Exemplo
A falha de um objeto aninhado mostra só a chave divergente com sinalização de mais e menos, em vez dos dois objetos inteiros.

## Limites e trade-offs
O diff bonito não transforma asserção vaga em bom teste: comparar JSON inteiro esconde a intenção que t.get deveria expressar.

## Como verificar
Quebre uma chave de um objeto esperado e confirme que o relatório destaca exatamente o par divergente.

## Conexões
- [[ava-hooks-lifecycle]] — Veja também: AVA: ganchos before, after e always.
- [[ava-parallel-ci-watch]] — Veja também: AVA: distribuição na CI e modo watch.

## Fontes
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
- [AVA — Guia Assertions](https://github.com/avajs/ava/blob/main/docs/03-assertions.md) — asserções nativas e mensagens aprimoradas; consultado em 2026-10-03.
