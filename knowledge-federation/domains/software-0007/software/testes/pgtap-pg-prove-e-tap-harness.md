---
id: software.testes.tranche15.000947
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

# pg_prove: usar TAP::Harness para agregar scripts de teste

## Em uma frase
`pg_prove` executa scripts SQL ou funções xUnit, coleta o output TAP e usa um harness para resumir sucesso e falha da coleção.

## Por que importa
Organização por arquivos permite dividir responsabilidades e relatório por script, enquanto o resumo agrega número de arquivos e assertions.

## Como funciona
Opções de concorrência e seleção mudam quais scripts chegam ao harness, então o comando deve ser reproduzível.

## Exemplo
Execute `pg_prove tests/` apontando explicitamente para o banco de testes e publique o sumário junto do log detalhado quando um script falhar.

## Limites e trade-offs
O harness não cria automaticamente uma base de dados segura nem instala a extensão correta; conexão, schema e permissões continuam pré-requisitos externos.

## Como verificar
Execute uma coleção com script bom e outro com falha controlada, confirme que o status global é não-zero e que o relatório identifica o arquivo responsável.

## Conexões
- [[pgtap-sql-script-em-transacao-com-rollback]] — Veja também: pgTAP: isolar efeitos de script com transação e rollback.
- [[pgtap-runtests-xunit-setup-e-teardown]] — Veja também: pgTAP: organizar funções xUnit com runtests e lifecycle explícito.

## Fontes
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
