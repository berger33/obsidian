---
id: software.dados.explain-analyze-postgresql.000001
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
fontes: ["https://www.postgresql.org/docs/current/using-explain.html", "https://www.postgresql.org/docs/current/sql-explain.html"]
tags: [dominio/software, subdominio/dados, qualidade/candidata]
aliases: [EXPLAIN, EXPLAIN ANALYZE, plano de consulta PostgreSQL]
lote: software-dados-distribuidos-0004
---

# Planos de consulta com EXPLAIN ANALYZE no PostgreSQL

## Em uma frase
`EXPLAIN` mostra o plano escolhido pelo PostgreSQL, enquanto `EXPLAIN ANALYZE` executa a instrução e acrescenta medidas observadas daquela execução.

## Por que importa
Uma consulta lenta pode decorrer de estimativas incorretas, leitura excessiva, ordenação, junções ou limitações que só aparecem com o formato real dos dados. O plano ajuda a formular hipóteses com evidências, mas não é um veredito isolado: estatísticas, cache, concorrência e ambiente afetam o resultado. Medir uma consulta em produção sem entender a semântica do comando também pode alterar dados.

## Como funciona
`EXPLAIN` apresenta nós do plano, custos estimados, cardinalidade estimada e largura média. Esses custos são unidades internas do planejador, não milissegundos. `EXPLAIN ANALYZE` roda o comando e informa linhas, loops e tempos observados por nó; em instruções que alteram dados, os efeitos acontecem como numa execução normal. A documentação descreve usar uma transação e revertê-la para testar certas alterações, mas isso não desfaz efeitos externos executados por funções ou integrações. A medição também tem overhead e, por padrão, não inclui o custo de enviar resultados pela rede ao cliente.

## Exemplo
Para uma consulta de leitura, compare linhas estimadas com linhas reais e examine os nós mais caros antes de adicionar um índice. Em uma atualização de teste, avalie cuidadosamente se o ambiente é isolado e se a transação pode ser revertida; não execute `EXPLAIN ANALYZE` de DML em dados reais supondo que o prefixo `EXPLAIN` torne a instrução inofensiva.

## Limites e trade-offs
Uma execução mede apenas um conjunto de parâmetros, dados e condições de cache. Não compare custos de planos entre servidores como se fossem tempo de relógio. Nós de loops repetidos podem multiplicar trabalho; entenda `loops` e linhas por loop. A análise não inclui automaticamente latência de aplicação, rede ou disputa de recursos externa ao comando.

## Como verificar
Use dados representativos, atualize estatísticas quando apropriado e compare estimativas com linhas reais. Observe buffers e loops quando disponíveis, repita medições com cautela e valide que uma alteração melhora o objetivo de latência ou recursos sob carga realista. Para DML, use um banco descartável ou um plano de teste controlado e confira efeitos colaterais antes de executar.

## Conexões
- [[indice-btree-multicolunas-postgresql]] — planos ajudam a medir se um índice composto favorece a consulta real.
- [[sql-parametrizacao-consultas]] — manter parâmetros seguros continua necessário ao investigar consultas com entrada externa.
- [[gates-de-qualidade-no-merge]] — medições de desempenho devem ser repetíveis e ligadas a mudanças específicas.

## Fontes
- [PostgreSQL — Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — estrutura de planos, `EXPLAIN ANALYZE` e ressalvas da medição; acesso em 2026-10-01.
- [PostgreSQL — EXPLAIN command](https://www.postgresql.org/docs/current/sql-explain.html) — opções, execução de instruções e semântica do comando; acesso em 2026-10-01.
