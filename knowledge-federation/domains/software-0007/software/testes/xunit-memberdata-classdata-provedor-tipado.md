---
id: software.testes.tranche11.000502
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://xunit.net/docs/getting-started/v3/getting-started", "https://xunit.net/docs/config-xunit-runner-json"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# xUnit: mover dados reutilizáveis para MemberData ou ClassData

## Em uma frase
Theories podem obter dados de membros ou classes provedoras, separando matriz de argumentos da lógica do teste.

## Por que importa
xUnit.net cria casos a partir de Facts/Theories e gerencia instâncias e fixtures com regras próprias de escopo e paralelismo; o nome familiar de um atributo não dispensa entender o lifecycle. Um atributo com dezenas de valores comprime manutenção e pode levar casos diferentes a compartilhar estado mutável.

## Como funciona
Use test class instance para estado novo por caso, fixtures compartilhadas só quando o custo justificar, dados nomeáveis e determinísticos e coleções para proteger recursos compartilhados. Use provedor determinístico, descreva cada linha e devolva objetos novos quando mutabilidade fizer parte do teste.

## Exemplo
Três classes testam um parser com MemberData compartilhado que fornece strings e resultado esperado por linha.

## Limites e trade-offs
Detalhes de fixtures, runner e modos de paralelismo variam entre xUnit v2 e v3 e entre versões do runner. Compartilhar fixture não a torna thread-safe, e ordem do teste não é contrato entre casos. Descoberta de dados e serialização de argumentos dependem do runner e da versão xUnit utilizada.

## Como verificar
Rode discovery no runner de CI e confirme que cada linha é descobrível e reexecutável com argumento registrado.

## Conexões
- [[xunit-inline-data-casos-visíveis]] — Veja também: xUnit: manter InlineData pequeno e representar cada linha no relatório.
- [[xunit-constructor-dispose-instancia-por-teste]] — Veja também: xUnit: usar constructor e Dispose para contexto novo por caso.

## Fontes
- [xUnit.net v3 — Getting Started](https://xunit.net/docs/getting-started/v3/getting-started) — Fact, Theory, dados inline, descoberta e execução de casos; consultado em 2026-10-02.
- [xUnit.net — Configuration Files](https://xunit.net/docs/config-xunit-runner-json) — opções de runner, execução paralela e configuração por assembly; consultado em 2026-10-02.
