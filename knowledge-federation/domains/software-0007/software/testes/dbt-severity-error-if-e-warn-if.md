---
id: software.testes.tranche15.000913
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
fontes: ["https://docs.getdbt.com/reference/resource-configs/severity.md", "https://docs.getdbt.com/reference/data-test-configs?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt data tests: formular limites de erro e warning a partir da contagem de falhas

## Em uma frase
severity, error_if e warn_if determinam se a contagem de falhas de um data test passa, avisa ou falha, com ordem diferente conforme severity seja error ou warn.

## Por que importa
Com severity: error, dbt avalia error_if primeiro; se a condição não for satisfeita, avalia warn_if.

## Como funciona
Com severity: warn, ignora error_if e avalia apenas warn_if. O valor padrão de ambas as condições é != 0.

## Exemplo
Defina `severity: error`, `error_if: "> 10"` e `warn_if: "> 0"` para que violações acima de dez falhem e as demais avisem; se escolher `severity: warn`, configure warn_if sabendo que error_if não participa.

## Limites e trade-offs
Por padrão um warning não falha o job, mas `--warn-error` pode promover todos os warnings e `--warn-error-options` tipos selecionados; a promoção muda o resultado do pipeline, não a contagem da query.

## Como verificar
Use resultados de teste com zero, cinco e onze falhas e verifique classificação sob severity error e warn; repita com --warn-error e confirme a promoção de warnings.

## Conexões
- [[dbt-arguments-obrigatorios-em-data-tests-v2]] — Veja também: dbt v2: colocar argumentos de testes genéricos no bloco arguments.
- [[dbt-store-failures-e-ciclo-de-vida]] — Veja também: dbt data tests: armazenar linhas que falharam para análise controlada.

## Fontes
- [dbt — severity, error_if, and warn_if](https://docs.getdbt.com/reference/resource-configs/severity.md) — ordem de avaliação das condições, diferença entre severity error/warn e promoção por --warn-error; consultado em 2026-10-02.
- [dbt v2 — Data test configurations](https://docs.getdbt.com/reference/data-test-configs?version=2) — severity, error_if, warn_if, store_failures, limit, where e fail_calc; consultado em 2026-10-02.
