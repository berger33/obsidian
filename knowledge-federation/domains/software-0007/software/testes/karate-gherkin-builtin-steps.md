---
id: software.testes.tranche15.000910
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://karatelabs.github.io/karate/", "https://karatelabs.github.io/karate/#data-driven-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: escrever API tests em Gherkin com steps embutidos

## Em uma frase
Arquivos de feature usam sintaxe Gherkin, mas os passos de HTTP, asserção e manipulação de dados já vêm implementados no framework.

## Por que importa
Sem step definitions próprios, a especificação fica mais próxima do domínio e o time não mantém uma camada de cola entre frase e código.

## Como funciona
Estruture o cenário com `url`, `path`, `method` e `status`, usando `match` para verificar o corpo e variáveis para reaproveitar dados.

## Exemplo
`Given url 'https://api.exemplo.com'`, `And path 'usuarios/1'`, `When method get`, `Then status 200` descreve uma chamada completa.

## Limites e trade-offs
Steps embutidos não cobrem toda lógica de domínio; regras complexas continuam exigindo features reutilizáveis ou código auxiliar, e a liberdade do DSL pede disciplina de escrita.

## Como verificar
Execute a feature com o runner e confirme que cada linha aparece no relatório com o resultado da verificação correspondente.

## Conexões
- [[karate-match-assertions]] — Veja também: Karate: usar match e marcadores fuzzy.

## Fontes
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
- [Karate — Data driven tests](https://karatelabs.github.io/karate/#data-driven-tests) — tabelas, Examples, CSV e laços em feature files; consultado em 2026-10-02.
