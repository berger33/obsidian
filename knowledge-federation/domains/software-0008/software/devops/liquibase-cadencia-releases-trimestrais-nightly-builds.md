---
id: software.devops.tranche08.000745
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

# Liquibase: cadência de releases trimestrais da comunidade (Fev, Mai, Ago, Nov) e Nightly Builds da branch main

## Em uma frase
A partir da versão 5.0.2, o Liquibase Community opera com duas vias de distribuição: builds contínuos da branch `main` no GitHub (`releases/tag/nightly`) para acesso antecipado e releases estáveis trimestrais (fevereiro, maio, agosto e novembro) para produção.

## Por que importa
Equipes corporativas de banco de dados precisam de um calendário previsível de lançamentos estáveis para planejar janelas de atualização e homologação, enquanto desenvolvedores que aguardam uma correção de bug recém-mesclada precisam testar o binário imediatamente sem esperar meses. A seção `Release Cadence and Access` do README oficial do Liquibase documenta esse modelo duplo.

## Como funciona
(1) **Quarterly Community Releases**: lançadas trimestralmente nos meses de **fevereiro, maio, agosto e novembro** (como a `v5.0.3` em maio de 2026 e a release planejada de agosto de 2026), fornecendo versões estáveis prontas para produção em todos os canais oficiais (GitHub Releases, Maven Central, gerenciadores de pacotes e registries de containers); e (2) **Main Branch Builds on GitHub (Nightly builds)**: atualizadas automaticamente após cada execução bem-sucedida de testes na branch padrão `main`, publicando `liquibase-nightly.tar.gz` (Linux/macOS) e `liquibase-nightly.zip` (Windows) na tag `https://github.com/liquibase/liquibase/releases/tag/nightly`.

## Exemplo
```bash
# Atualizar um clone local antigo da branch master para a nova branch padrão main conforme instrução oficial do README
git branch -m master main && git fetch origin && git branch -u origin/main main
```

## Limites e trade-offs
Os artefatos `liquibase-nightly` refletem o estado mais recente da branch `main` e destinam-se exclusivamente a testes antecipados e feedback comunitário; em pipelines de produção e dependências Maven/Gradle de aplicações críticas, fixe sempre uma versão trimestral estável (como `5.0.3`).

## Como verificar
Consulte `liquibase --version` no seu ambiente e verifique na página de releases do GitHub se a versão instalada corresponde à release trimestral estável vigente.

## Conexões
- [[liquibase-execucao-docker-variaveis-ambiente-registries]] — Veja também: Liquibase: execução em containers Docker, variáveis LIQUIBASE_COMMAND_* e distribuição multi-registry.
- [[liquibase-integracoes-maven-gradle-spring-boot-cicd]] — Veja também: Liquibase: automação e integrações com Maven, Gradle, Ant, Spring Boot, GitHub Actions e Spinnaker.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.
- [[liquibase-mudancas-versao-5-0-licenca-fsl-community-secure]] — Referência cruzada direta com liquibase-mudancas-versao-5-0-licenca-fsl-community-secure.
- [[liquibase-governanca-publicacao-sonatype-aprovadores]] — Referência cruzada direta com liquibase-governanca-publicacao-sonatype-aprovadores.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
