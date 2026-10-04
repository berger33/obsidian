---
id: software.testes.tranche07.000149
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://www.postgresql.org/docs/current/applevel-consistency.html", "https://www.postgresql.org/docs/current/ddl-constraints.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de constraints e reconciliação de integridade", "Teste: Teste de constraints e reconciliação de integridade"]
lote: software-testes-2000-0001
---

# Teste de constraints e reconciliação de integridade

## Em uma frase
Verifique invariantes de dados tanto no limite transacional do banco quanto em reconciliações independentes entre fontes ou projeções.

## Por que importa
A inconsistência pode surgir por concorrência, falha parcial, migração ou replicação; uma verificação independente detecta divergências que a aplicação talvez não perceba.

## Como funciona
Teste constraints com entradas inválidas e operações concorrentes; para regras entre tabelas, escolha isolamento ou locks adequados. Depois compare contagens, chaves e agregados entre origem e destino em snapshot coerente, registrando divergências para investigação.

## Exemplo
Execute duas transferências concorrentes contra saldo de teste e confirme invariantes após commit; em seguida reconcilie IDs e totais da tabela principal com projeção analítica na mesma janela de dados.

## Limites e trade-offs
Uma soma sem snapshot coerente pode comparar momentos diferentes e gerar falso alarme. Nem toda regra cabe em CHECK; constraints e Serializable têm custos e escopo próprios.

## Como verificar
Introduza violação controlada para provar que constraint ou teste a detecta; repita concorrência, confirme rollback ou retry documentado e valide que a reconciliação encontra uma divergência inserida em fixture.

## Conexões
- [[mvcc-isolamento-transacoes-postgresql]] — aprofundamento relacionado.
- [[testes-consistencia-eventual-convergencia]] — aprofundamento relacionado.

## Fontes
- [PostgreSQL — Application-Level Data Consistency Checks](https://www.postgresql.org/docs/current/applevel-consistency.html) — anomalias concorrentes e uso de transações serializáveis ou locks; consultado em 2026-10-01.
- [PostgreSQL — Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — constraints declarativas como proteção de integridade no banco; consultado em 2026-10-01.
