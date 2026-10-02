---
id: software.dados.indices-compostos-postgresql.000001
tipo: tecnica
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
fontes: ["https://www.postgresql.org/docs/current/indexes-multicolumn.html", "https://www.postgresql.org/docs/current/indexes-types.html"]
tags: [dominio/software, subdominio/dados, qualidade/candidata]
aliases: [Índice composto, Índice multicoluna, Índice B-tree composto]
lote: software-dados-distribuidos-0004
---

# Índices B-tree multicoluna no PostgreSQL

## Em uma frase
Um índice B-tree multicoluna organiza chaves numa ordem definida e costuma ser mais eficiente quando as condições da consulta restringem as colunas líderes dessa ordem.

## Por que importa
Índices podem reduzir leituras de tabela, mas um índice composto não é uma promessa de aceleração para qualquer consulta que mencione uma de suas colunas. A ordem das chaves, a seletividade, o tamanho da tabela e os dados determinam se o planejador consegue reduzir trabalho. Índices também consomem armazenamento e aumentam o custo de gravações e manutenção.

## Como funciona
Considere um índice `(tenant_id, created_at)`. Uma busca que filtra por `tenant_id` e restringe `created_at` pode aproveitar a ordenação das duas chaves. Em B-tree, restrições de igualdade nas colunas líderes, seguidas de uma restrição de intervalo na primeira coluna sem igualdade, limitam diretamente a faixa percorrida. Condições em colunas mais à direita ainda podem ser avaliadas no índice, mas podem não reduzir a faixa lida. A documentação atual do PostgreSQL também descreve a otimização skip scan, que pode tornar certos predicados sem a primeira chave úteis quando o planejador estima poucas combinações distintas. Outros métodos, como GIN e BRIN, têm regras diferentes para índices compostos.

## Exemplo
Uma aplicação lista os pedidos de um cliente em ordem temporal. Um índice `(customer_id, created_at)` corresponde ao filtro por cliente e ao ordenamento por data; um índice `(created_at, customer_id)` não é automaticamente equivalente para esse padrão. O resultado deve ser confirmado pelo plano e por uma carga representativa, não apenas pela leitura do nome do índice.

## Limites e trade-offs
A regra de coluna líder é uma orientação para B-tree, não uma lei universal para todos os métodos de índice ou versões do PostgreSQL. A otimização skip scan é dependente da distribuição e da estimativa do planejador. Um índice redundante pode elevar custo de escrita, autovacuum e armazenamento sem melhorar a consulta. Não crie índices para todo filtro hipotético.

## Como verificar
Liste consultas prioritárias, seus filtros e `ORDER BY`; verifique se a ordem das colunas do índice corresponde a esses padrões. Compare planos e buffers com `EXPLAIN (ANALYZE, BUFFERS)` usando volume e distribuição realistas. Observe também o custo de `INSERT`, `UPDATE` e manutenção depois de implantar o índice.

## Conexões
- [[explain-analyze-planos-consulta-postgresql]] — mede o efeito do índice no plano executado.
- [[mvcc-isolamento-transacoes-postgresql]] — índices servem consultas em transações, mas não substituem o isolamento necessário.
- [[paginacao-por-cursor-api]] — uma ordenação indexável pode ser parte de uma paginação por chave.

## Fontes
- [PostgreSQL — Multicolumn Indexes](https://www.postgresql.org/docs/current/indexes-multicolumn.html) — regras para B-tree e demais índices compostos; acesso em 2026-10-01.
- [PostgreSQL — Index Types](https://www.postgresql.org/docs/current/indexes-types.html) — diferenças entre métodos de índice; acesso em 2026-10-01.
