---
id: software.testes.tranche15.000930
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nodejs.org/api/test.html", "https://nodejs.org/api/cli.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# node:test: compreender o isolamento padrão entre arquivos de teste

## Em uma frase
Com isolamento em processo, o runner executa cada arquivo descoberto num processo filho; quando esse modo é desligado, os módulos compartilham o processo e contexto do runner.

## Por que importa
Isolamento reduz interferência por globals e estado de módulo entre arquivos, mas acrescenta custo e não elimina dependências externas compartilhadas como banco ou porta TCP.

## Como funciona
`--test-isolation=none` muda o contrato e deve ser escolhido deliberadamente.

## Exemplo
Rode `node --test` no modo padrão para arquivos independentes e compare com `node --test --test-isolation=none` ao diagnosticar inicialização cara ou estado global.

## Limites e trade-offs
Código executado ao importar um arquivo ainda pode ter side effects e processos independentes podem disputar o mesmo serviço; isolamento do runner não equivale a sandbox de rede.

## Como verificar
Crie dois arquivos que alteram o mesmo global e execute nos dois modos, verificando se o resultado ilustra o limite esperado e se teardown fecha recursos externos.

## Conexões
- [[node-test-concurrency-por-arquivo-e-por-caso]] — Veja também: node:test: separar concorrência de arquivos e subtestes.

## Fontes
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
- [Node.js v26.10 — Command-line API](https://nodejs.org/api/cli.html) — flags de execução, seleção, reporters, cobertura e sharding; consultado em 2026-10-02.
