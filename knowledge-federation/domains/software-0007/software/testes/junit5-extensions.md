---
id: software.testes.tranche18.001182
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

# JUnit 5: estender comportamento com extensões

## Em uma frase
As extensões podem interceptar fases do ciclo de vida e resolver parâmetros, sendo registradas por anotação, por anotação composta ou por configuração global.

## Por que importa
Comportamentos transversais como preparação de recursos externos ficam separados dos testes e reutilizáveis entre projetos.

## Como funciona
Registre a extensão no escopo mais estreito que cobrir o caso, documente os recursos que ela gerencia e evite estado global implícito.

## Exemplo
Uma extensão pode criar recurso temporário antes de cada caso e liberá-lo ao final, sem código de preparação no teste.

## Limites e trade-offs
Extensões globais afetam toda a suíte sem que o autor do teste perceba, e várias extensões concorrentes exigem compreensão da ordem de execução.

## Como verificar
Desabilite temporariamente a extensão e confirme que os casos que dependem dela falham de forma clara, evidenciando a responsabilidade.

## Conexões
- [[junit5-dynamic-tests]] — Veja também: JUnit 5: gerar testes em tempo de execução.
- [[junit5-dependency-injection]] — Veja também: JUnit 5: receber parâmetros resolvidos.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
