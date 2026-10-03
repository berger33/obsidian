---
id: software.testes.tranche15.000942
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
fontes: ["https://pgtap.org/documentation.html", "https://pgtap.org/pg_prove.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pgTAP: verificar contrato de schema com assertions específicas

## Em uma frase
pgTAP oferece funções como `has_table`, `has_column` e `col_type_is` para testar existência e tipo de estruturas, produzindo diagnósticos vinculados ao catálogo do PostgreSQL.

## Por que importa
Uma assertion de tipo pode falhar porque tabela ou coluna não existe, então testar presença antes do detalhe melhora o diagnóstico e separa ausência de incompatibilidade.

## Como funciona
Verificações de schema complementam testes de dados, não afirmam que as linhas da tabela satisfazem a regra.

## Exemplo
Valide `has_table('public', 'orders')`, depois `has_column` e `col_type_is` para a chave que a aplicação consome.

## Limites e trade-offs
Nome de tipo, schema de busca e versão do PostgreSQL podem alterar a representação; use a assinatura adequada e não faça o teste depender de search_path implícito sem declarar isso.

## Como verificar
Remova uma coluna num banco de teste e confirme que a falha aponta a expectativa correta; execute novamente com schema explicitamente configurado.

## Conexões
- [[pgtap-no-plan-enfraquece-contagem-prevista]] — Veja também: pgTAP: reservar no_plan para quantidade realmente indeterminada.
- [[pgtap-results-eq-semantica-de-conjunto-e-ordem]] — Veja também: pgTAP: escolher comparação de resultados que corresponda ao contrato.

## Fontes
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
