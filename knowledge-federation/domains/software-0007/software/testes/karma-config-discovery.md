---
id: software.testes.tranche23.001664
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md", "https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Onde o Karma procura o karma.conf.js (inclusive TypeScript)

## Em uma frase
O CLI do Karma aceita o caminho do arquivo como primeiro argumento e, sem ele, procura em ordem: karma.conf.js, karma.conf.coffee, karma.conf.ts, e depois os mesmos nomes dentro de .config/. A função exportada recebe o objeto de configuração e chama config.set.

## Por que importa
Encontrar o arquivo de configuração automaticamente permite rodar karma start em qualquer estrutura de projeto sem repetir parâmetros, e a variante .config/ mantém a raiz limpa.

## Como funciona
O arquivo pode ser JavaScript, CoffeeScript ou TypeScript, carregado como módulo Node comum; desde a versão 6.3 também pode ser uma função async, e o uso de TypeScript depende de ts-node — se o tsconfig usar módulos ES, é preciso forçar module commonjs.

## Exemplo
Execute karma start my.conf.js para passar o caminho explicitamente e karma start para a descoberta automática; confira o log, que ecoa qual arquivo de configuração foi lido.

## Limites e trade-offs
A configuração async é um recurso da série 6.3 — projetos travados em versões antigas do Karma não a têm — e o erro típico de TypeScript (SyntaxError: Unexpected token) exige o registro manual do ts-node.

## Como verificar
Abra a página de configuração e a referência de configuration file no repositório e confirme a lista de nomes procurados e o bloco async da versão 6.3.

## Conexões
- [[karma-init-wizard]] — Veja também: karma init: um assistente que escreve o arquivo de configuração.
- [[karma-file-patterns]] — Veja também: files, exclude e basePath: minimatch define o que entra na página.

## Fontes
- [Karma — Configuration (intro)](https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md) — assistente karma init, start e overrides de CLI; consultado em 2026-10-03.
- [Karma — Configuration file reference](https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md) — descoberta do arquivo, File Patterns e opções do objeto de configuração; consultado em 2026-10-03.
