---
id: software.dados.migracoes.expand-contract.000001
tipo: tecnica
dominio: software
subdominio: dados
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: pendente
revisor: ""
fontes: ["https://docs.gitlab.com/development/database/avoiding_downtime_in_migrations/", "https://docs.gitlab.com/development/migration_style_guide/"]
tags: [dominio/software, subdominio/dados, qualidade/candidata]
aliases: [Migração expand-contract, Migração de banco sem downtime]
---

# Migrações de banco com expand-contract

## Em uma frase
Expand-contract separa uma mudança incompatível de schema em etapas compatíveis, permitindo que versões antigas e novas do aplicativo coexistam durante o deploy.

## Por que importa
Em produção, deploy da aplicação e alteração do banco raramente são atômicos. Instâncias antigas podem continuar processando tráfego enquanto novas instâncias sobem; workers, jobs agendados e processos de rollback também podem usar o schema antigo. Remover ou renomear uma coluna cedo demais pode transformar uma alteração simples em indisponibilidade.

## Como funciona
Na fase de expansão, adicione estruturas novas sem remover as antigas e mantenha compatibilidade com o código em execução. Faça backfill de forma controlada, monitore progresso e verifique consistência. Implante código que consiga operar durante a transição e, quando necessário, leia temporariamente ambas as representações. Depois de confirmar que nenhum consumidor depende do formato antigo, mude a leitura e escrita definitivamente. Só então contraia o schema removendo a coluna, índice ou tabela antiga em uma etapa posterior.

## Exemplo
Para trocar `users.name` por `users.display_name`, crie a coluna nova, atualize escritores para manter ambas coerentes, preencha registros existentes e migre leitores. Observe erros e divergências durante o período de convivência. Em um release posterior, pare de usar a coluna antiga e remova-a após confirmar que aplicações e jobs antigos já foram encerrados.

## Limites e trade-offs
A estratégia cria estados intermediários e código temporário, aumenta a complexidade de rollback e exige observabilidade do backfill. DDL e lock behavior variam por banco e operação; “adicionar uma coluna” não é universalmente sem risco. Migrações de dados grandes podem precisar de lotes pequenos, limitação de carga e retomada idempotente. Siga as recomendações específicas do banco e da plataforma.

## Como verificar
Teste a sequência com versões antiga e nova da aplicação, incluindo workers atrasados. Meça locks, duração, lag de replicação, erros e divergência entre colunas. Confirme que o rollback continua possível antes da contração e que a remoção só ocorre quando nenhuma versão suportada lê o schema antigo.

## Conexões
- [[contract-testing-consumer-provider]] — consumidores e produtores também precisam de compatibilidade durante a migração.
- [[gates-de-qualidade-no-merge]] — validações de migration devem ser bloqueantes no fluxo de entrega.
- [[sli-slo-orcamento-de-erro]] — monitore impacto de latência e erros durante o backfill.

## Fontes
- [GitLab — Avoiding downtime in migrations](https://docs.gitlab.com/development/database/avoiding_downtime_in_migrations/) — exemplos de mudanças compatíveis e etapas de migração; acesso em 2026-10-01.
- [GitLab — Migration Style Guide](https://docs.gitlab.com/development/migration_style_guide/) — categorias, limites e práticas específicas do GitLab; acesso em 2026-10-01.
