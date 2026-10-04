---
id: software.devops.tranche08.000742
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

# Liquibase 5.0+: separação entre Liquibase Community (licença FSL) e Liquibase Secure (comercial)

## Em uma frase
A partir do Liquibase 5.0, o projeto estabeleceu uma separação clara entre a edição `liquibase/liquibase` (Liquibase Community, licenciada sob Functional Source License — FSL) e a edição comercial `liquibase/liquibase-secure` (antigo Pro), mantendo a série 4.x sob Apache-2.0.

## Por que importa
Equipes de arquitetura, DevOps e compliance jurídico que atualizam pipelines de CI/CD ou imagens Docker do Liquibase 4.x para o Liquibase 5.0+ precisam compreender as mudanças de licenciamento (de Apache 2.0 na 4.x para FSL na 5.0 Community) e a mudança do nome da imagem comercial (de `liquibase-pro` para `liquibase-secure`). O README principal e o `docker/README.md` oficial do Liquibase detalham essa matriz.

## Como funciona
De acordo com a documentação oficial de licenciamento no repositório: (1) **Liquibase 4 (`4.x`)**: permanece sob licença **Apache 2.0** e continua disponível como imagem oficial do Docker Hub (`docker pull liquibase:4.x` ou `liquibase/liquibase:4.x`); (2) **Liquibase 5.0+ Community (`liquibase/liquibase`)**: distribuído sob a **Functional Source License (FSL)** (`FSL-1.1-ALv2`), que permite uso gratuito para migrações de banco de dados com acesso total ao código-fonte, proíbe uso comercial que concorra com produtos/serviços da Liquibase e converte-se automaticamente para Apache 2.0 após dois anos; e (3) **Liquibase 5.0+ Secure (`liquibase/liquibase-secure`)**: edição comercial que exige uma chave de licença válida e adiciona recursos empresariais como Policy Checks, Quality Checks e Advanced Rollback.

## Exemplo
```bash
# Pull explícito da imagem Liquibase 5.0+ Community (FSL) versus Liquibase 4.x (Apache 2.0)
docker pull liquibase/liquibase:5.0.1
docker pull liquibase:4.x
```

## Limites e trade-offs
Conforme documentado na matriz de disponibilidade de imagens (`docker/README.md`), para o Liquibase 5.0+ a imagem não está disponível na biblioteca oficial raiz do Docker (`_/liquibase`), devendo-se puxar obrigatoriamente do namespace da comunidade (`liquibase/liquibase`, `ghcr.io/liquibase/liquibase` ou `public.ecr.aws/liquibase/liquibase`); além disso, clientes que possuem chave de licença comercial não devem mais injetar a chave na imagem Community, devendo migrar para a imagem `liquibase/liquibase-secure`.

## Como verificar
Verifique nos Dockerfiles e pipelines de CI/CD qual tag de imagem está sendo utilizada (`liquibase:4.x`, `liquibase/liquibase:5.0` ou `liquibase/liquibase-secure:5.0`) e confirme a conformidade com o modelo de licença da organização.

## Conexões
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Veja também: Liquibase: plataforma de versionamento, rastreamento e implantação de mudanças de esquema de banco de dados.
- [[liquibase-gerenciamento-drivers-lpm-breaking-change-5-0]] — Veja também: Liquibase 5.0+: remoção de drivers embutidos por padrão e instalação via Liquibase Package Manager (LPM).
- [[liquibase-cadencia-releases-trimestrais-nightly-builds]] — Referência cruzada direta com liquibase-cadencia-releases-trimestrais-nightly-builds.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
