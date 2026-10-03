---
id: software.testes.tranche15.000912
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
fontes: ["https://docs.getdbt.com/reference/resource-properties/data-tests?version=2", "https://docs.getdbt.com/reference/data-test-configs?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt v2: colocar argumentos de testes genéricos no bloco arguments

## Em uma frase
A sintaxe de parâmetros de generic data tests em dbt v2 exige que os valores fiquem sob `arguments`, em vez de aparecerem como propriedades irmãs do nome do teste.

## Por que importa
Projetos com YAML escrito para versões anteriores podem receber erro de validação ao atualizar.

## Como funciona
A mudança separa argumentos de entrada de opções de configuração e metadados do teste.

## Exemplo
Atualize `accepted_values` para `arguments: {values: [...]}` e mantenha `config:` para `severity`, `where` ou outras opções da instância.

## Limites e trade-offs
O formato depende da versão-alvo declarada no projeto e do caminho de atualização; não misture exemplos de releases antigas sem comparar com a documentação v2.

## Como verificar
Execute validação de parse após a conversão, inclua um teste com argumentos e outro com configuração, e revise a saída compilada antes de disparar consultas no warehouse.

## Conexões
- [[dbt-singular-e-generic-com-fronteiras-de-reuso]] — Veja também: dbt data tests: decidir quando um teste singular deve virar genérico.
- [[dbt-severity-error-if-e-warn-if]] — Veja também: dbt data tests: formular limites de erro e warning a partir da contagem de falhas.

## Fontes
- [dbt v2 — Data test properties](https://docs.getdbt.com/reference/resource-properties/data-tests?version=2) — sintaxe YAML e propriedades de testes genéricos; consultado em 2026-10-02.
- [dbt v2 — Data test configurations](https://docs.getdbt.com/reference/data-test-configs?version=2) — severity, error_if, warn_if, store_failures, limit, where e fail_calc; consultado em 2026-10-02.
