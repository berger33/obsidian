---
id: software.testes.tranche09.000273
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
fontes: ["https://www.postgresql.org/docs/current/ddl-constraints.html", "https://www.postgresql.org/docs/current/errcodes-appendix.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: validar unicidade sob inserções concorrentes

## Em uma frase
Uma constraint UNIQUE é a autoridade final para impedir duplicidade mesmo quando duas transações verificam ausência antes de inserir.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. Uma consulta prévia seguida de insert pode ter race e não garante unicidade por si só.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Abra duas conexões, sincronize a tentativa de inserir a mesma chave e trate o resultado do banco como contrato.

## Exemplo
Dois workers reservam o mesmo identificador; exatamente um commit é aceito e o outro recebe violação de unicidade.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. Índices, NULLs e regras de unicidade parcial alteram o que é considerado duplicado e devem refletir o schema real.

## Como verificar
Verifique o estado final, a constraint nomeada e o código de erro, não apenas que algum insert falhou.

## Conexões
- [[postgresql-mvcc-concurrent-read-write]] — Veja também: PostgreSQL: testar visibilidade MVCC entre conexões.
- [[postgresql-row-lock-skip-locked-queue]] — Veja também: PostgreSQL: testar filas com FOR UPDATE SKIP LOCKED.

## Fontes
- [PostgreSQL — Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — constraints de integridade declaradas no banco; consultado em 2026-10-02.
- [PostgreSQL — Error codes](https://www.postgresql.org/docs/current/errcodes-appendix.html) — SQLSTATEs estáveis para classificar erros do servidor; consultado em 2026-10-02.
