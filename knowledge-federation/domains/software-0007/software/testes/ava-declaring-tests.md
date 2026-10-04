---
id: software.testes.tranche21.001473
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

# AVA: declarar testes com título único

## Em uma frase
Um teste é declarado chamando a função test importada do AVA com um título e a implementação, e o título deve ser único dentro de cada arquivo.

## Por que importa
Exigir títulos únicos transforma o nome do caso em endereço estável para filtrar execuções, ler relatórios e localizar a falha no log.

## Como funciona
Importe test de ava, passe título e função, receba o objeto de execução como primeiro argumento e defina todos os testes sincronamente na carga do arquivo.

## Exemplo
test('rejeita data futura', t => t.true(validar('2099-01-01') === false)) declara um caso nomeado com asserção simples.

## Limites e trade-offs
Definições dentro de setTimeout ou setImmediate não funcionam: o AVA precisa conhecer a lista completa de testes antes de agendar qualquer um.

## Como verificar
Renomeie um teste e repita o título em outro caso do arquivo; confirme que o AVA aponta o conflito de título antes de rodar.

## Conexões
- [[ava-setup-npm-init]] — Veja também: AVA: inicializar o projeto com npm init ava.
- [[ava-async-support]] — Veja também: AVA: promessas, async e observáveis.

## Fontes
- [AVA — Guia Writing tests](https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md) — concorrência, modificadores, hooks e isolamento; consultado em 2026-10-03.
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
