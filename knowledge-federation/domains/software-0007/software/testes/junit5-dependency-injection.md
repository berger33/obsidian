---
id: software.testes.tranche18.001183
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

# JUnit 5: receber parâmetros resolvidos

## Em uma frase
Construtores e métodos de teste podem receber parâmetros resolvidos por extensões registradas, incluindo informações do teste corrente e recursos preparados.

## Por que importa
A injeção evita preparação manual repetida e deixa explícitas as dependências de cada caso.

## Como funciona
Aceite apenas os parâmetros realmente necessários, prefira resolvedores documentados e mantenha os resolvedores próprios testados como código comum.

## Exemplo
Um caso pode receber o diretório temporário e o relatório do teste corrente sem preparar nada manualmente.

## Limites e trade-offs
Resolvedores personalizados escondem dependências que o leitor não vê no corpo do teste, e erros de resolução só aparecem em execução.

## Como verificar
Introduza um parâmetro sem resolvedor correspondente e confirme que a falha aponta claramente a assinatura problemática.

## Conexões
- [[junit5-extensions]] — Veja também: JUnit 5: estender comportamento com extensões.
- [[junit5-parallel-execution]] — Veja também: JUnit 5: habilitar execução paralela.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
