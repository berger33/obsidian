---
id: software.testes.tranche18.001181
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://junit.org/junit5/docs/current/user-guide/", "https://github.com/junit-team/junit5"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit 5: gerar testes em tempo de execução

## Em uma frase
Métodos de fábrica podem produzir casos dinamicamente, com nome e conteúdo definidos a partir de dados disponíveis apenas durante a execução.

## Por que importa
Alguns cenários dependem de dados externos ou de coleções geradas, e a declaração estática não conseguiria expressá-los.

## Como funciona
Gere os casos com nome descritivo, mantenha cada caso independente e limite o uso a situações que realmente exigem geração.

## Exemplo
Uma fábrica pode criar um caso por arquivo encontrado em diretório, nomeando cada um pelo arquivo de origem.

## Limites e trade-offs
Casos dinâmicos escapam a algumas verificações estáticas e exigem mais cuidado com limpeza, já que o número é conhecido só em execução.

## Como verificar
Gere um caso adicional na fábrica e confirme que ele aparece individualmente no relatório com resultado próprio.

## Conexões
- [[junit5-parameterized]] — Veja também: JUnit 5: variar entradas com testes parametrizados.
- [[junit5-extensions]] — Veja também: JUnit 5: estender comportamento com extensões.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
