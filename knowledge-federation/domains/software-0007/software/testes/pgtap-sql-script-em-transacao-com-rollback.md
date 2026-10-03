---
id: software.testes.tranche15.000946
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
fontes: ["https://pgtap.org/pg_prove.html", "https://pgtap.org/documentation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pgTAP: isolar efeitos de script com transação e rollback

## Em uma frase
Scripts SQL de teste podem iniciar transação, declarar plano, executar assertions, finalizar e fazer rollback, de forma que alterações transitórias não contaminem o banco de desenvolvimento.

## Por que importa
O exemplo de `pg_prove` demonstra o ciclo explícito do script, mas não é seguro assumir que todo efeito externo ou operação não transacional seja desfeito.

## Como funciona
A fixture de banco ainda precisa começar em estado conhecido e ser exclusiva ao job.

## Exemplo
Envolva DDL e DML de teste em `BEGIN` e `ROLLBACK`, configure o target do pg_prove como banco descartável e mantenha criação de extensão ou instalação de funções fora do escopo do teste se precisar persistir.

## Limites e trade-offs
Rollback não desfaz chamadas externas, sequences têm particularidades e extensões podem exigir permissões; escolha um banco isolado para impedir que falha de teardown danifique dados reais.

## Como verificar
Verifique a contagem antes/depois da execução no banco temporário, teste a saída do script após falha e assegure que rollback ocorreu mesmo quando assertions não passam.

## Conexões
- [[pgtap-skip-e-todo-explicam-excecoes-do-plano]] — Veja também: pgTAP: representar temporariamente testes ignorados ou conhecidos como TODO.
- [[pgtap-pg-prove-e-tap-harness]] — Veja também: pg_prove: usar TAP::Harness para agregar scripts de teste.

## Fontes
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
