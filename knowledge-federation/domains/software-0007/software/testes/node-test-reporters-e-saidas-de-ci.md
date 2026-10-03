---
id: software.testes.tranche15.000938
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

# node:test: escolher reporter e destino sem perder diagnósticos

## Em uma frase
O CLI aceita reporter de teste e destino do reporter, permitindo separar saída humana de logs estruturados para ferramentas de integração.

## Por que importa
Um job que descarta stdout ou envia tudo a uma única tela pode perder detalhes úteis em falha.

## Como funciona
Formatos diferentes servem objetivos distintos, e o destino deve ser mantido como artifact.

## Exemplo
Configure `--test-reporter` e `--test-reporter-destination` para emitir a representação esperada pelo CI, deixando a saída normal legível para desenvolvimento local.

## Limites e trade-offs
Nem todo reporter contém o mesmo nível de informação ou é aceito em toda versão; mantenha o formato em sincronia com o parser que consome o artifact.

## Como verificar
Gere um caso que passa e outro que falha, confira o XML ou TAP salvo e valide que o sistema de CI extrai estado, nome, duração e mensagem.

## Conexões
- [[node-test-shard-distribuicao-de-arquivos]] — Veja também: node:test: coordenar shards sem sobrepor arquivos entre jobs.
- [[node-test-coverage-nativa-com-limites]] — Veja também: node:test: gerar cobertura nativa separada por dimensão.

## Fontes
- [Node.js v26.10 — Command-line API](https://nodejs.org/api/cli.html) — flags de execução, seleção, reporters, cobertura e sharding; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
