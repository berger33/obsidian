---
id: software.devops.tranche11.001005
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://www.keycloak.org/guides", "https://raw.githubusercontent.com/keycloak/keycloak/main/README.md", "https://www.keycloak.org/server/configuration-production"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Keycloak Operator no Kubernetes: CRDs para implantação declarativa, importação de Realms e gestão de Clients

## Em uma frase
O Keycloak Operator (distribuído no OperatorHub/Artifact Hub para Kubernetes e OpenShift) automatiza o ciclo de vida do servidor, a importação declarativa de Realms e o gerenciamento de Clients OIDC e SAML por meio de Custom Resource Definitions (CRDs), além de suportar imagens customizadas pré-otimizadas (`kc.sh build`) e rolling updates sem downtime.

## Por que importa
Gerenciar instâncias do Keycloak, realms e dezenas de clientes OIDC manualmente pela interface gráfica viola os princípios de GitOps e dificulta a reprodutibilidade entre ambientes de staging e produção. O Operator permite versionar toda a topologia de identidade como manifestos Kubernetes reconciliados continuamente.

## Como funciona
Conforme listado na seção *Operator* do portal oficial de guias (`keycloak.org/guides`), o Keycloak Operator oferece: (1) instalação declarativa do cluster Keycloak via recurso customizado (`Keycloak`), configurando banco de dados, TLS, recursos e réplicas; (2) importação automatizada de Realms (`KeycloakRealmImport`) a partir de especificações declarativas; (3) gerenciamento declarativo de clientes OIDC e SAML (`KeycloakClient`); (4) uso de imagens customizadas otimizadas (`kc.sh build`), evitando recompilação de providers/temas na inicialização do pod; e (5) verificação de compatibilidade de rolling updates (`Checking if rolling updates are possible`) para evitar indisponibilidade ao atualizar configurações ou versões.

## Exemplo
```dockerfile
# Construir uma imagem customizada e pré-otimizada do Keycloak (kc.sh build) para inicialização rápida no Kubernetes
FROM quay.io/keycloak/keycloak:latest AS builder
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true
ENV KC_DB=postgres
RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak/ /opt/keycloak/
ENTRYPOINT ["/opt/keycloak/bin/kc.sh", "start", "--optimized"]
```

## Limites e trade-offs
Quando você passa a flag `--optimized` para acelerar o boot dos pods no Kubernetes, o Keycloak ignora opções de tempo de build (`build options` como `--db`, `--health-enabled` ou `--features`) se elas não tiverem sido gravadas previamente durante a etapa `kc.sh build` da imagem.

## Como verificar
Execute `/opt/keycloak/bin/kc.sh show-config` dentro do container construído para inspecionar todas as propriedades gravadas na etapa de build (`Runtime` vs `Build time` configuration).

## Conexões
- [[keycloak-cluster-alta-disponibilidade-infinispan-jgroups-banco]] — Veja também: Keycloak em cluster de alta disponibilidade: JGroups, caches distribuídos Infinispan, banco relacional e pilha IPv4/IPv6.
- [[keycloak-observabilidade-opentelemetry-metricas-sli-jfr]] — Veja também: Observabilidade no Keycloak: OpenTelemetry tracing, métricas de eventos, SLIs/SLOs, Exemplars e Java Flight Recorder.
- [[keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf]] — Referência cruzada direta com keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/guides) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://www.keycloak.org/server/configuration-production) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
