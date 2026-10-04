---
id: software.testes.tranche15.000915
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
fontes: ["https://karatelabs.github.io/karate/#data-driven-tests", "https://karatelabs.github.io/karate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: parametrizar cenários com tabelas e arquivos

## Em uma frase
Cenários podem ser repetidos com conjuntos de dados declarados em tabelas, `Examples` ou arquivos externos como CSV, mantendo a lógica única e os dados separados.

## Por que importa
Escrever um cenário por combinação de entrada infla a suíte e faz a manutenção da regra acontecer em vários lugares ao mesmo tempo.

## Como funciona
Declare os dados em tabela quando o conjunto for pequeno e em arquivo quando variar por ambiente, e percorra coleções com laço dentro do cenário.

## Exemplo
Um cenário com `Examples:` lista pares de entrada e resultado esperado, enquanto uma tabela lida de CSV permite reutilizar a mesma massa em várias features.

## Limites e trade-offs
Dados externos precisam ser versionados e estáveis; quando ficam fora do repositório, a suíte passa a depender de um recurso que ninguém sabe reproduzir localmente.

## Como verificar
Rode o cenário parametrizado e confirme no relatório a quantidade de execuções; introduza um caso de fronteira na tabela para verificar a cobertura do novo dado.

## Conexões
- [[karate-parallel-runner]] — Veja também: Karate: executar features em paralelo.
- [[karate-tags-selection]] — Veja também: Karate: selecionar cenários por tags.

## Fontes
- [Karate — Data driven tests](https://karatelabs.github.io/karate/#data-driven-tests) — tabelas, Examples, CSV e laços em feature files; consultado em 2026-10-02.
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
