---
id: software.testes.tranche23.001745
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
fontes: ["https://infection.github.io/guide/command-line-options.html", "https://infection.github.io/guide/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reusar cobertura existente em vez de gerar de novo

## Em uma frase
A justificativa da opção --coverage na doc oficial é de custo puro: quem roda CI com Xdebug/phpdbg para gerar métricas de cobertura e depois roda Infection está executando a suíte com debugger duas vezes, o que "dramatically increases the build time"; com --coverage=<path> o Infection consome os relatórios já gerados.

## Por que importa
O contrato por framework está na página: para PHPUnit e Codeception são necessários os relatórios xml e junit, e um caminho build/coverage deve conter o diretório coverage-xml e o arquivo junit.xml; para PhpSpec basta o xml, com o diretório phpspec-coverage-xml dentro do caminho fornecido.

## Como funciona
A doc fecha o loop com o par de comandos canônico: primeiro vendor/bin/phpunit --coverage-xml=build/coverage/coverage-xml --log-junit=build/coverage/junit.xml, depois infection.phar --coverage=build/coverage — duas fases reutilizáveis em qualquer runner que preserve a árvore.

## Exemplo
Configure a etapa de coverage do seu CI para publicar build/coverage e rode Infection apontando --coverage para o mesmo artefato; compare o tempo do job com e sem a opção para quantificar a frase da doc.

## Limites e trade-offs
Reuso exige que a cobertura seja do mesmo commit e da mesma configuração de testes do run de mutação — a página prescreve a economia, não a invalidação automática de cache velho; cobertura defasada seleciona testes errados por linha mutada.

## Como verificar
Abra a seção --coverage da página Command line options e confirme os requisitos por framework, a árvore de arquivos e o exemplo duplo de comandos.

## Conexões
- [[infection-threads]] — Veja também: --threads: paralelismo primeiro, depois benchmark.
- [[infection-git-diff]] — Veja também: Mutar só a diferença do pull request: --git-diff-filter e --git-diff-lines.

## Fontes
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
- [Infection — Introduction do guia oficial](https://infection.github.io/guide/) — mutation testing, os cinco passos, métricas MSI/MCC e playground; consultado em 2026-10-03.
