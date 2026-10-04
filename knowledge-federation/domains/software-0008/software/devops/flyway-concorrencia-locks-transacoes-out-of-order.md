---
id: software.devops.tranche08.000759
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/flyway/flyway/main/README.md", "https://documentation.red-gate.com/flyway/getting-started-with-flyway", "https://github.com/flyway/flyway"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Redgate Flyway: controle de concorrência, escopo de transações (group) e migrações fora de ordem (outOfOrder)

## Em uma frase
O Flyway utiliza locks nativos do banco de dados sobre a tabela `flyway_schema_history` para serializar execuções concorrentes, executa cada migração em sua própria transação por padrão (ou agrupadas com `group=true`) e permite controlar branches paralelas com `outOfOrder`.

## Por que importa
Em equipes grandes onde múltiplos desenvolvedores criam branches em paralelo (ex.: a branch A cria `V4__...sql` e é mesclada depois que a branch B já levou `V5__...sql` para homologação), entender como o Flyway lida com migrações fora de ordem e como agrupa transações evita bloqueios inesperados no pipeline. A documentação oficial do Flyway cobre esses comportamentos de execução.

## Como funciona
(1) **Concorrência**: diferentemente de ferramentas que gravam uma flag booleana permanente em uma tabela de lock, o Flyway adquire locks em nível de banco de dados (como `SELECT ... FOR UPDATE` ou advisory locks do SGBD, liberados automaticamente caso a conexão TCP caia) para coordenar múltiplos nós chamando `migrate` ao mesmo tempo; (2) **Escopo transacional**: por padrão (`group=false`), cada migração `V` roda em sua própria transação independente (se a `V5` falhar após a `V4` ter sucesso, a `V4` permanece aplicada e registrada); se `group=true` for configurado (em bancos com DDL transacional como PostgreSQL), todas as migrações pendentes rodam em uma única transação atômica tudo-ou-nada; e (3) **Ordem de versão**: por padrão (`outOfOrder=false`), o Flyway rejeita uma migração `V4` se a `V5` já foi aplicada; ativar `outOfOrder=true` permite aplicar a `V4` atrasada em ambientes de integração.

## Exemplo
```bash
# Executar flyway migrate agrupando todas as migrações pendentes em uma única transação atômica (PostgreSQL)
flyway -url="jdbc:postgresql://localhost:5432/appdb" \
  -user="postgres" \
  -group="true" \
  migrate
```

## Limites e trade-offs
Algumas instruções SQL específicas (como `CREATE INDEX CONCURRENTLY` ou `VACUUM` no PostgreSQL) são proibidas pelo próprio SGBD de rodar dentro de um bloco de transação (`BEGIN ... COMMIT`); para esses scripts específicos, o Flyway detecta automaticamente (ou permite configurar `executeInTransaction=false` por script) para executá-los fora de uma transação, o que é incompatível com `group=true` para aquele lote.

## Como verificar
Verifique na coluna `State` de `flyway info` se alguma migração foi aplicada como `Out of Order` (`Out of order` vs `Success`) antes de promover a release para produção.

## Conexões
- [[flyway-configuracao-toml-conf-variaveis-ambiente-precedencia]] — Veja também: Redgate Flyway: configuração declarativa (flyway.toml e flyway.conf), variáveis FLYWAY_* e precedência.
- [[flyway-edicoes-community-apache2-teams-enterprise-redgate]] — Veja também: Redgate Flyway: código aberto Apache-2.0 no repositório flyway/flyway e ecossistema Redgate.
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.
- [[flyway-bancos-suportados-relacionais-cloud-data-warehouses]] — Referência cruzada direta com flyway-bancos-suportados-relacionais-cloud-data-warehouses.
- [[flyway-comandos-ciclo-vida-info-validate-migrate-baseline-repair]] — Referência cruzada direta com flyway-comandos-ciclo-vida-info-validate-migrate-baseline-repair.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
