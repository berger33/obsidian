---
id: software.testes.tranche15.000940
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

# pgTAP: declarar plano para detectar assertions não executadas

## Em uma frase
O plano TAP anuncia quantos testes o script pretende executar; a função `finish()` valida o resultado e encerra a produção de TAP para que casos omitidos não passem despercebidos.

## Por que importa
Plano fixo permite detectar tanto assertion que falhou quanto código que não chegou ao final ou produziu quantidade diferente.

## Como funciona
A alternativa `no_plan()` existe para casos em que a quantidade não é conhecida, mas a própria documentação recomenda evitar enfraquecer essa garantia.

## Exemplo
Abra o script em transação, chame `plan(3)`, execute as três assertions e finalize com `SELECT * FROM finish();` antes do rollback de limpeza.

## Limites e trade-offs
Atualizar uma assertion sem atualizar o número do plano produz falha de protocolo; um bloco de exceção que interrompe o script ainda precisa aparecer no output como erro.

## Como verificar
Remova temporariamente uma assertion e confirme que a checagem do plano falha, depois restaure a contagem e verifique resultado TAP completo.

## Conexões
- [[pgtap-no-plan-enfraquece-contagem-prevista]] — Veja também: pgTAP: reservar no_plan para quantidade realmente indeterminada.

## Fontes
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
