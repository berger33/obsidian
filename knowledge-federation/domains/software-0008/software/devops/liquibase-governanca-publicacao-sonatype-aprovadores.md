---
id: software.devops.tranche08.000750
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

# Liquibase: governança de publicação de releases no Sonatype/Maven Central com gate de múltiplos aprovadores

## Em uma frase
O pipeline de publicação de releases do Liquibase (`/workflow/release-published.yml`) implementa um controle de governança onde a publicação de uma release no GitHub pausa após a etapa `Setup` e exige a aprovação manual de no mínimo 2 aprovadores antes de liberar o deploy no Maven Central/Sonatype e registries.

## Por que importa
Em ferramentas de banco de dados baixadas milhões de vezes do Maven Central e Docker Hub para rodar com credenciais administrativas de produção, proteger o pipeline de release contra publicações acidentais ou comprometimento de uma única conta de mantenedor (princípio dos quatro olhos / two-person rule) é uma prática exemplar de segurança de engenharia de release. A seção `Publish Release Manual Trigger to Sonatype` do README oficial do Liquibase documenta esse mecanismo.

## Como funciona
Quando um Product Owner (PO) ou Team Leader publica uma release em `github.com/liquibase/liquibase/releases/`, o workflow `release-published.yml` é disparado. O workflow para imediatamente após a etapa `Setup` e envia um e-mail para a lista de `approvers` configurada no job `manual_trigger_deployment`. É obrigatório um **mínimo de 2 aprovadores** (`minimum of 2 approvers`) verificando a versão exata no PR (como `Deploying vX.Y.Z to sonatype`) para que os jobs subsequentes — `deploy_maven`, `deploy_javadocs`, `publish_to_github_packages`, entre outros — sejam autorizados a executar.

## Exemplo
```yaml
# Padrão de governança de release inspirado no workflow release-published.yml do Liquibase (exigindo 2 aprovadores no environment)
jobs:
  deploy_maven:
    needs: [setup, manual_trigger_deployment]
    environment:
      name: sonatype-production-release
```

## Limites e trade-offs
Exigir aprovação manual síncrona de pelo menos dois mantenedores seniores adiciona uma etapa de coordenação humana entre a criação da tag e a disponibilidade imediata dos artefatos no Maven Central, mas elimina o risco de que um disparo equivocado publique pacotes imutáveis incorretos nos repositórios globais.

## Como verificar
Ao consumir uma nova release do Liquibase a partir do Maven Central ou GitHub Releases, verifique a conclusão de todos os jobs do workflow `release-published.yml` e a integridade dos pacotes publicados.

## Conexões
- [[liquibase-migracao-4-x-para-5-0-checklist-producao]] — Veja também: Liquibase: guia prático de atualização do Liquibase 4.x para 5.0+ em pipelines e produção.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.
- [[liquibase-cadencia-releases-trimestrais-nightly-builds]] — Referência cruzada direta com liquibase-cadencia-releases-trimestrais-nightly-builds.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
