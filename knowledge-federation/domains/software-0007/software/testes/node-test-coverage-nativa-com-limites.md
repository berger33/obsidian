---
id: software.testes.tranche15.000939
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
fontes: ["https://nodejs.org/api/cli.html", "https://nodejs.org/api/test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# node:test: gerar cobertura nativa separada por dimensão

## Em uma frase
O test runner do Node expõe coleta e limites nativos para line, branch e function coverage, evitando instalar um instrumentador adicional para métricas básicas.

## Por que importa
Flags de inclusão/exclusão definem o conjunto observado e os thresholds convertem uma medição em status de execução.

## Como funciona
Exclusões e arquivos de teste podem mudar denominador, portanto a política deve ser versionada junto com a suíte.

## Exemplo
Na versão alvo, rode `node --experimental-test-coverage --test-coverage-lines=90 --test-coverage-branches=80 --test-coverage-functions=70 --test`; ajuste cada percentual ao contrato do projeto.

## Limites e trade-offs
Recursos e estabilidade evoluem entre versões do Node; não copie flags experimentais para projeto que roda outra versão, e não interprete percentual alto como prova de assertions úteis.

## Como verificar
Execute um fixture com linha coberta e branch ausente, confirme o relatório por métrica e faça o job falhar ao reduzir o threshold de propósito.

## Conexões
- [[node-test-reporters-e-saidas-de-ci]] — Veja também: node:test: escolher reporter e destino sem perder diagnósticos.

## Fontes
- [Node.js v26.10 — Command-line API](https://nodejs.org/api/cli.html) — flags de execução, seleção, reporters, cobertura e sharding; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
