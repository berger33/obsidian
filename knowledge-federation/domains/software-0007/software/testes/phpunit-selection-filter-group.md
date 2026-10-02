---
id: software.testes.tranche12.000606
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
fontes: ["https://docs.phpunit.de/en/12.5/configuration.html", "https://docs.phpunit.de/en/12.5/textui.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: selecionar testes por suite, grupo ou padrão

## Em uma frase
O runner oferece opções para selecionar suite, grupo ou padrão de nome sem precisar editar a descoberta da classe.

## Por que importa
Filtros aceleram investigação e permitem separar categorias de execução, mas uma suite parcial não demonstra que o restante foi executado.

## Como funciona
Use `--testsuite`, `--group` ou `--filter` para o alvo pretendido, e `--list-tests` para inspecionar a seleção antes de um job caro.

## Exemplo
Um desenvolvedor pode rodar apenas os testes do grupo `database` ao alterar um repositório e executar a suíte completa antes da integração.

## Limites e trade-offs
Padrões de filtro e nomes podem deixar de selecionar um caso após refatoração, convertendo a execução rápida em falsa confirmação se zero testes passarem sem falha.

## Como verificar
Revise quantidade e nomes encontrados pelo filtro e configure a pipeline para falhar quando a suite crítica não descobrir testes.

## Conexões
- [[phpunit-config-precedencia]] — Veja também: PHPUnit 12.5: resolver configuração efetiva.
- [[phpunit-random-seed-repro]] — Veja também: PHPUnit 12.5: reproduzir falhas por ordem aleatória.

## Fontes
- [PHPUnit 12.5 — Configuration](https://docs.phpunit.de/en/12.5/configuration.html) — precedência entre defaults, XML e opções da linha de comando; consultado em 2026-10-02.
- [PHPUnit 12.5 — Text UI](https://docs.phpunit.de/en/12.5/textui.html) — ordenação, seleção, sementes aleatórias e saída do test runner; consultado em 2026-10-02.
