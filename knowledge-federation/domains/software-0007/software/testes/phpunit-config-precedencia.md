---
id: software.testes.tranche12.000605
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://docs.phpunit.de/en/12.5/configuration.html", "https://docs.phpunit.de/en/12.5/xml-configuration-file.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: resolver configuração efetiva

## Em uma frase
A configuração efetiva é construída dos defaults internos, depois do XML e por fim das opções de CLI.

## Por que importa
Entender precedência facilita reproduzir uma diferença entre execução local e CI sem manter cópias completas de `phpunit.xml`.

## Como funciona
Mantenha defaults compartilhados no XML e passe overrides de escopo restrito na linha de comando; use `--no-configuration` apenas quando quiser ignorar deliberadamente o arquivo padrão.

## Exemplo
Um job pode apontar para uma configuração de integração e alterar o filtro de testes pela CLI sem mudar o XML usado pelos outros jobs.

## Limites e trade-offs
Overrides na linha de comando podem fazer o mesmo script ter resultado diferente do workflow padrão se não forem registrados nos logs do job.

## Como verificar
Execute `--configuration` com e sem override e compare opções de seleção, cache e saída com a configuração declarada no repositório.

## Conexões
- [[phpunit-fixtures-per-test]] — Veja também: PHPUnit 12.5: dimensionar fixtures por teste.
- [[phpunit-selection-filter-group]] — Veja também: PHPUnit 12.5: selecionar testes por suite, grupo ou padrão.

## Fontes
- [PHPUnit 12.5 — Configuration](https://docs.phpunit.de/en/12.5/configuration.html) — precedência entre defaults, XML e opções da linha de comando; consultado em 2026-10-02.
- [PHPUnit 12.5 — XML Configuration](https://docs.phpunit.de/en/12.5/xml-configuration-file.html) — configuração de grupos, isolamento, execução e resultado; consultado em 2026-10-02.
