---
id: software.testes.tranche15.000914
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
fontes: ["https://docs.getdbt.com/reference/resource-configs/store_failures.md", "https://docs.getdbt.com/reference/resource-configs/limit.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt data tests: armazenar linhas que falharam para análise controlada

## Em uma frase
`store_failures` persiste os registros devolvidos pela query de teste como uma relation, permitindo investigar evidências depois da execução.

## Por que importa
A relation facilita triagem em dados volumosos, mas pode conter informações sensíveis e precisa de schema, retenção, permissões e limpeza definidos.

## Como funciona
Em cada execução que armazena falhas, o resultado anterior do mesmo teste é substituído; com limit, a relation também fica sujeita ao limite.

## Exemplo
Ative `store_failures: true` apenas para a regra que precisa de investigação, configure schema ou alias apropriado e conceda acesso mínimo ao time responsável pela triagem.

## Limites e trade-offs
A relation é um retrato da execução, não um log append-only; uma nova execução substitui o resultado anterior e pode deixar um conjunto vazio após correção. Limite acesso e retenção e não dependa dela como histórico contínuo.

## Como verificar
Rode um caso com falhas, consulte a relation, corrija os dados e execute novamente; confirme que a nova execução substitui o conjunto anterior e que limit controla as linhas retornadas/armazenadas.

## Conexões
- [[dbt-severity-error-if-e-warn-if]] — Veja também: dbt data tests: formular limites de erro e warning a partir da contagem de falhas.
- [[dbt-where-limita-populacao-sem-mudar-regra]] — Veja também: dbt data tests: usar where para limitar a população avaliada.

## Fontes
- [dbt — store_failures](https://docs.getdbt.com/reference/resource-configs/store_failures.md) — substituição dos resultados da execução anterior e interação com limit; consultado em 2026-10-02.
- [dbt — limit](https://docs.getdbt.com/reference/resource-configs/limit.md) — limite de registros de falha retornados pela query e relação com armazenamento; consultado em 2026-10-02.
