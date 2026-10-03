---
id: software.devops.tranche08.000751
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

# Redgate Flyway: controle de versão para bancos de dados baseado em migrações e tabela flyway_schema_history

## Em uma frase
O Flyway (da Redgate, código aberto sob licença Apache-2.0) traz controle de versão para bancos de dados com simplicidade e convenção sobre configuração, rastreando mudanças de esquema na tabela `flyway_schema_history`.

## Por que importa
Enquanto o código de aplicação é versionado em Git com histórico claro de commits e tags, esquemas de banco de dados frequentemente sofrem alterações ad-hoc sem rastreabilidade, tornando impossível recriar o estado exato de um ambiente do zero ou saber quais scripts já rodaram em cada servidor. Segundo o README oficial e a documentação `Getting started with Flyway`, o Flyway permite evoluir o esquema do banco com confiança e facilidade em todas as instâncias.

## Como funciona
Conforme explica a seção `How does Flyway work?` do README oficial: (1) no cenário mais simples, o Flyway conecta-se a um banco de dados vazio e localiza a tabela de histórico (criando a tabela **`flyway_schema_history`** por padrão se ela ainda não existir) para rastrear o estado do banco; (2) em seguida, o Flyway varre o sistema de arquivos ou o classpath da aplicação procurando migrações disponíveis (que podem ser escritas em **SQL** ou **Java**); (3) as migrações são comparadas com a tabela de histórico; e (4) qualquer migração cuja versão seja superior à versão marcada como atual no banco é considerada uma **migração pendente** (`pending migration`), sendo ordenada pelo número de versão e executada sequencialmente enquanto `flyway_schema_history` é atualizada a cada passo.

## Exemplo
```bash
# Verificar o estado das migrações aplicadas e pendentes no banco e executar flyway migrate
flyway -url="jdbc:postgresql://localhost:5432/appdb" -user="postgres" -locations="filesystem:./sql" info
flyway -url="jdbc:postgresql://localhost:5432/appdb" -user="postgres" -locations="filesystem:./sql" migrate
```

## Limites e trade-offs
Como o Flyway registra na `flyway_schema_history` um checksum CRC32 de cada script de migração versionada aplicado, alterar mesmo um comentário ou espaço em branco em um arquivo `V1__...sql` que já foi executado em produção fará com que a próxima verificação de integridade (`flyway validate` ou `flyway migrate`) falhe por divergência de checksum; correções futuras devem sempre ser criadas como uma nova versão sequencial (`V2__...sql`, `V3__...sql`).

## Como verificar
Execute `flyway info` após rodar `flyway migrate` e confirme na tabela impressa que todas as migrações listadas apresentam `State: Success` e constam na tabela `flyway_schema_history`.

## Conexões
- [[flyway-modos-execucao-cli-docker-java-api-maven-gradle]] — Veja também: Redgate Flyway: 5 formas de execução (Command-line, Docker, Java API, Maven e Gradle).
- [[flyway-bancos-suportados-relacionais-cloud-data-warehouses]] — Referência cruzada direta com flyway-bancos-suportados-relacionais-cloud-data-warehouses.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
