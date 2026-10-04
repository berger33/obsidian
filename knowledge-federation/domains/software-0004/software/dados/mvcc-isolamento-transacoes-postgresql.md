---
id: software.dados.mvcc-isolamento-postgresql.000001
tipo: conceito
dominio: software
subdominio: dados
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://www.postgresql.org/docs/current/mvcc-intro.html", "https://www.postgresql.org/docs/current/transaction-iso.html"]
tags: [dominio/software, subdominio/dados, qualidade/candidata]
aliases: [MVCC, Multiversion Concurrency Control, isolamento de transações PostgreSQL]
lote: software-dados-distribuidos-0004
---

# MVCC e isolamento de transações no PostgreSQL

## Em uma frase
MVCC permite que o PostgreSQL apresente versões visíveis dos dados a cada transação, enquanto o nível de isolamento determina quais mudanças concorrentes essa transação pode observar.

## Por que importa
Operações simultâneas sobre os mesmos dados podem produzir leituras inconsistentes ou atualizações perdidas se a aplicação assumir uma ordem que o banco não garante. Entender snapshots e anomalias ajuda a escolher controles corretos sem recorrer automaticamente a bloqueios amplos. O nome de um nível de isolamento, sozinho, não descreve todas as diferenças de implementação entre bancos.

## Como funciona
No modelo multiversão, uma instrução lê um snapshot lógico dos dados em vez de simplesmente observar todas as gravações concorrentes no instante da leitura. No PostgreSQL, `READ COMMITTED` cria a visão para cada comando; duas consultas na mesma transação podem observar commits diferentes. `REPEATABLE READ` mantém uma visão consistente da transação, mas ainda pode permitir anomalias de serialização específicas. `SERIALIZABLE` procura assegurar um resultado equivalente a alguma execução serial e pode abortar uma transação quando detecta conflito; a aplicação precisa estar preparada para repetir a transação inteira. No PostgreSQL, `READ UNCOMMITTED` comporta-se como `READ COMMITTED`.

## Exemplo
Duas transações tentam reservar a última unidade disponível. Um `SELECT` seguido de uma gravação sem condição atômica pode permitir que ambas ajam com base na mesma observação. Uma atualização condicional, restrição de integridade ou transação serializável pode impedir a violação; a escolha depende da regra de negócio e de como a aplicação trata conflitos e retries.

## Limites e trade-offs
Isolamento serializável não substitui restrições de domínio, autorização ou idempotência. Um conflito de serialização é um resultado esperado que deve ser tratado sem repetir efeitos externos já realizados. Locks explícitos continuam úteis para pontos de conflito específicos, mas podem bloquear concorrentes. O comportamento detalhado é específico do PostgreSQL e de sua versão; não extrapole as garantias para outro banco sem consultar sua documentação.

## Como verificar
Escreva testes concorrentes que controlem a ordem das transações e tentem reproduzir a anomalia relevante. Confirme que violações são recusadas por uma condição, restrição ou erro serializável, e que o caminho de retry repete apenas a unidade transacional segura. Registre a versão do PostgreSQL e o nível configurado no teste.

## Conexões
- [[indice-btree-multicolunas-postgresql]] — índices influenciam o custo das consultas feitas dentro das transações.
- [[explain-analyze-planos-consulta-postgresql]] — planos e medições ajudam a investigar consultas concorrentes sem confundir plano com garantia de consistência.
- [[migracoes-expand-contract]] — alterações de esquema também precisam considerar transações e versões simultâneas da aplicação.

## Fontes
- [PostgreSQL — Introduction to MVCC](https://www.postgresql.org/docs/current/mvcc-intro.html) — snapshots, concorrência e relação entre leituras e gravações; acesso em 2026-10-01.
- [PostgreSQL — Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — níveis implementados, anomalias e falhas serializáveis; acesso em 2026-10-01.
