---
id: software.testes.tranche09.000279
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://www.postgresql.org/docs/current/errcodes-appendix.html", "https://www.postgresql.org/docs/current/ddl-constraints.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: afirmar SQLSTATE em vez de texto de erro

## Em uma frase
O SQLSTATE classifica a condição de erro e é mais estável para tratamento programático que a redação localizada da mensagem.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. Assertions pelo texto literal podem quebrar com versão, idioma ou detalhes diferentes sem mudança na classe de falha.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Capture o código e, quando necessário, nome/constraint associado em vez de comparar a mensagem completa.

## Exemplo
Uma inserção duplicada espera a condição de unique violation e verifica a constraint específica definida no schema.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. Não descarte contexto útil: logs podem guardar mensagem completa mesmo quando o teste afirma código estruturado.

## Como verificar
Repita em versões suportadas e locale diferente para confirmar que o teste depende do contrato SQLSTATE esperado.

## Conexões
- [[postgresql-timestamptz-session-timezone]] — Veja também: PostgreSQL: testar timestamptz com timezone explícito.

## Fontes
- [PostgreSQL — Error codes](https://www.postgresql.org/docs/current/errcodes-appendix.html) — SQLSTATEs estáveis para classificar erros do servidor; consultado em 2026-10-02.
- [PostgreSQL — Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — constraints de integridade declaradas no banco; consultado em 2026-10-02.
