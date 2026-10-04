---
id: software.devops.tranche08.000743
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
fontes: ["https://raw.githubusercontent.com/liquibase/liquibase/master/README.md", "https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md", "https://github.com/liquibase/liquibase"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Liquibase 5.0+: remoção de drivers embutidos por padrão e instalação via Liquibase Package Manager (LPM)

## Em uma frase
Como breaking change a partir do Liquibase 5.0, a edição Community e sua imagem Docker (`liquibase/liquibase`) não incluem mais drivers de banco de dados ou extensões por padrão, exigindo adicioná-los explicitamente via Liquibase Package Manager (`lpm add --global`).

## Por que importa
Atualizar a imagem Docker de `liquibase/liquibase:4.x` para `liquibase/liquibase:5.0` ou `:latest` sem ajustar a instalação de drivers JDBC quebrará imediatamente os jobs de migração em produção com erros de driver não encontrado para PostgreSQL, MySQL, SQL Server ou Oracle. A seção `Breaking Change: Drivers and Extensions No Longer Included` em `docker/README.md` documenta exatamente como migrar.

## Como funciona
Para manter a distribuição enxuta e modular no Liquibase 5.0+, os drivers JDBC e extensões foram desacoplados da imagem base `liquibase/liquibase`. Os usuários devem agora adicionar explicitamente os drivers necessários construindo uma imagem derivada com o **Liquibase Package Manager (LPM)** usando `RUN lpm add postgresql --global`, `RUN lpm add mysql --global` ou `RUN lpm add mssql --global` (ou montando os JARs de extensões/drivers no container). Como conveniência adicional, para bancos MySQL ainda é suportada a instalação em tempo de execução passando a variável de ambiente `-e INSTALL_MYSQL=true`.

## Exemplo
```dockerfile
# Dockerfile oficial recomendado para Liquibase 5.0+ adicionando drivers JDBC via LPM
FROM liquibase/liquibase:latest
RUN lpm add postgresql --global && \
    lpm add mysql --global && \
    lpm add mssql --global
```

## Limites e trade-offs
Embora usar `-e INSTALL_MYSQL=true` em tempo de execução no `docker run` funcione para testes rápidos, baixar drivers da internet a cada execução de container em pipelines de CI/CD ou Jobs do Kubernetes adiciona latência e cria dependência de conectividade externa; em produção, construa sempre uma imagem customizada com `RUN lpm add <driver> --global` armazenada no registry interno.

## Como verificar
Construa a imagem derivada com `lpm add` e execute um teste de validação (`liquibase validate`) contra o banco de homologação para confirmar que o driver JDBC é carregado com sucesso.

## Conexões
- [[liquibase-mudancas-versao-5-0-licenca-fsl-community-secure]] — Veja também: Liquibase 5.0+: separação entre Liquibase Community (licença FSL) e Liquibase Secure (comercial).
- [[liquibase-execucao-docker-variaveis-ambiente-registries]] — Veja também: Liquibase: execução em containers Docker, variáveis LIQUIBASE_COMMAND_* e distribuição multi-registry.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
