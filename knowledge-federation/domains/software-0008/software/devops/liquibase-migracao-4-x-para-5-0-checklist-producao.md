---
id: software.devops.tranche08.000749
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

# Liquibase: guia prático de atualização do Liquibase 4.x para 5.0+ em pipelines e produção

## Em uma frase
A migração do Liquibase 4.x para 5.0+ segue um roteiro de 6 etapas documentado oficialmente: revisão de licença (Apache 2.0 vs FSL/Comercial), escolha da edição (`liquibase/liquibase` vs `liquibase/liquibase-secure`), atualização de referência de imagem, adição de drivers via LPM, validação em não-produção e rollout em produção.

## Por que importa
Organizações que possuem dezenas de pipelines usando `FROM liquibase/liquibase:4.x` ou `FROM liquibase/liquibase-pro:4.x` precisam de um procedimento passo a passo para atualizar para a geração 5.0 sem interromper deploys de banco de dados. A seção `Upgrading from Liquibase 4 to 5.0` em `docker/README.md` descreve exatamente essas 6 etapas.

## Como funciona
O procedimento oficial compreende: **Step 1**: entender os requisitos de licença (4.x é Apache 2.0; 5.0 Community é FSL; 5.0 Secure é comercial); **Step 2**: escolher a edição (Community se não precisar de recursos enterprise e aceitar a FSL; Secure se tiver licença comercial e precisar de Policy Checks, Quality Checks ou Advanced Rollback); **Step 3**: atualizar a referência da imagem (`liquibase/liquibase:4.x` -> `liquibase/liquibase:5.0`, ou `liquibase/liquibase-pro:4.x` -> `liquibase/liquibase-secure:5.0`); **Step 4**: atualizar a instalação de drivers adicionando `RUN lpm add <db> --global` no Dockerfile (já que a 5.0+ não inclui drivers por padrão); **Step 5**: testar primeiro em não-produção executando `liquibase:5.0 validate` contra um banco de teste; e **Step 6**: concluir a migração em produção.

## Exemplo
```bash
# Etapa 5 do guia oficial de migração: validar changelogs existentes contra um banco de teste usando Liquibase 5.0
docker run --rm \
  -v $(pwd)/changelog:/liquibase/changelog \
  -e LIQUIBASE_COMMAND_URL="jdbc:postgresql://test-db:5432/testdb" \
  -e LIQUIBASE_COMMAND_USERNAME="username" \
  -e LIQUIBASE_COMMAND_PASSWORD="password" \
  meu-registry.interno/liquibase-com-drivers:5.0 validate
```

## Limites e trade-offs
Se uma organização não puder adotar a Functional Source License (FSL) da versão 5.0 Community por políticas internas que exigem estritamente licenças aprovadas pela OSI no momento imediato da adoção (sem aguardar a conversão de 2 anos da FSL para Apache 2.0) e não possuir licença comercial do Liquibase Secure, ela pode permanecer na série `liquibase:4.x` (Apache 2.0) ou avaliar ferramentas sob Apache 2.0.

## Como verificar
Após atualizar a imagem para `5.0` com os drivers instalados via LPM, execute `liquibase validate` e `liquibase status` em ambiente de staging e confirme zero regressões na leitura da tabela `DATABASECHANGELOG` existente.

## Conexões
- [[liquibase-estrategias-rollback-reversao-segura-mudancas]] — Veja também: Liquibase: estratégias de reversão de esquema (rollback por tag, contagem ou data) e validação prévia.
- [[liquibase-governanca-publicacao-sonatype-aprovadores]] — Veja também: Liquibase: governança de publicação de releases no Sonatype/Maven Central com gate de múltiplos aprovadores.
- [[liquibase-mudancas-versao-5-0-licenca-fsl-community-secure]] — Referência cruzada direta com liquibase-mudancas-versao-5-0-licenca-fsl-community-secure.
- [[liquibase-gerenciamento-drivers-lpm-breaking-change-5-0]] — Referência cruzada direta com liquibase-gerenciamento-drivers-lpm-breaking-change-5-0.
- [[liquibase-execucao-docker-variaveis-ambiente-registries]] — Referência cruzada direta com liquibase-execucao-docker-variaveis-ambiente-registries.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
