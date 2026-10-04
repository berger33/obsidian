---
id: software.testes.tranche23.001665
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
fontes: ["https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md", "https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# files, exclude e basePath: minimatch define o que entra na página

## Em uma frase
As opções que listam caminhos de arquivos — files, exclude e preprocessors — usam a biblioteca minimatch para casar padrões como js/*.js; o basePath resolve todos os caminhos relativos definidos nessas listas e, quando relativo, é interpretado a partir do diretório do próprio arquivo de configuração.

## Por que importa
Erros de padrão (esquecer um arquivo, incluir bundle gerado) são a falha mais comum de configuração do Karma; entender a semântica de minimatch evita suítes que rodam com metade dos testes carregados.

## Como funciona
A referência oficial documenta exemplos como **/*.js para todas as subpastas, **/!(jquery).js para negar um arquivo e **/(foo|bar).js para alternativas; esses padrões valem tanto para files quanto para exclude.

## Exemplo
Configure files com um glob que você sabe incluir exatamente os spec; rode karma start e confira na saída a lista de arquivos servidos — qualquer padrão mal formado aparece ali como arquivo faltando.

## Limites e trade-offs
Os padrões controlam apenas o que é servido ao navegador; a ordem de carregamento e a dependência entre arquivos (por exemplo, RequireJS vs globs ingênuos) exigem atenção separada na própria doc.

## Como verificar
Abra a seção "File Patterns" da referência de configuração no repositório e confira os três exemplos de glob listados e o papel do basePath.

## Conexões
- [[karma-config-discovery]] — Veja também: Onde o Karma procura o karma.conf.js (inclusive TypeScript).
- [[karma-browsers-capture]] — Veja também: Captura de navegadores: launchers, a porta 9876 e o timeout de capture.

## Fontes
- [Karma — Configuration file reference](https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md) — descoberta do arquivo, File Patterns e opções do objeto de configuração; consultado em 2026-10-03.
- [Karma — Configuration (intro)](https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md) — assistente karma init, start e overrides de CLI; consultado em 2026-10-03.
