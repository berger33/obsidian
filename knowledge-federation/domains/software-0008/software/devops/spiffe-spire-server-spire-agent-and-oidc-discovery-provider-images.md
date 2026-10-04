---
id: software.devops.tranche05.000473
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/spiffe/spire/main/README.md", "https://spiffe.io/spire/try/", "https://github.com/spiffe/spire"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Componentes e imagens oficiais do SPIRE: spire-server, spire-agent e oidc-discovery-provider

## Em uma frase
A seção *Get SPIRE* do README oficial documenta os binários distribuídos nas releases (`github.com/spiffe/spire/releases`) e as três imagens oficiais de contêiner publicadas no GitHub Container Registry: **`ghcr.io/spiffe/spire-server`** (o servidor central que gerencia a autoridade certificadora do domínio de confiança, o registro de entradas de identidade e a atestação dos agentes de nó), **`ghcr.io/spiffe/spire-agent`** (o agente executado em cada nó/host que atesta workloads locais e expõe o socket da SPIFFE Workload API) e **`ghcr.io/spiffe/oidc-discovery-provider`** (que expõe o documento de descoberta OIDC `/.well-known/openid-configuration` e o conjunto de chaves públicas `JWKS` para que sistemas externos validem JWT-SVIDs emitidos pelo SPIRE).

## Por que importa
Compreender a tríade **`spire-server` + `spire-agent` + `oidc-discovery-provider`** esclarece como o SPIRE funciona tanto para mTLS interno entre serviços quanto para federação de identidade com nuvens externas (AWS, GCP, Azure, HashiCorp Vault) que consultam um endpoint OIDC público para validar tokens JWT.

## Como funciona
Implante o `spire-server` em alta disponibilidade no plano de controle, o `spire-agent` como DaemonSet em cada nó trabalhador Kubernetes (ou serviço systemd em VMs) e o `oidc-discovery-provider` quando precisar federar JWT-SVIDs com provedores externos.

## Exemplo
Para eliminar credenciais estáticas de nuvem nos pods Kubernetes, a plataforma implanta `ghcr.io/spiffe/spire-server`, `ghcr.io/spiffe/spire-agent` e `ghcr.io/spiffe/oidc-discovery-provider`, permitindo que o provedor cloud valide os JWT-SVIDs consultando o endpoint JWKS do Discovery Provider.

## Limites e trade-offs
Mantenha as versões de `spire-server` e `spire-agent` alinhadas dentro da política de compatibilidade oficial das releases ao realizar upgrades rolantes da frota.

## Como verificar
Verifique no cluster que os pods `spire-server` e o DaemonSet `spire-agent` estão em estado `Running` e que o `spire-agent` concluiu a atestação de nó junto ao `spire-server`.

## Conexões
- [[spiffe-x509-svid-mtls-and-jwt-svid-authentication]] — Veja também: Documentos de identidade verificáveis SVIDs (X.509 e JWT) para mTLS e autenticação entre serviços.
- [[spiffe-envoy-secret-discovery-service-sds-integration]] — Veja também: Rotação transparente de certificados TLS e trust bundles no Envoy Proxy via SPIRE SDS.

## Fontes
- [SPIRE GitHub — README.md (SPIFFE Runtime Environment, Workload API, SVIDs, Envoy SDS & Security Audits)](https://raw.githubusercontent.com/spiffe/spire/main/README.md) — README oficial do SPIRE (projeto graduado na CNCF sob Apache-2.0) detalhando implementação de produção do SPIFFE, SPIFFE Workload API, emissão de SPIFFE IDs e SVIDs (X.509 mTLS e JWT), imagens spire-server/spire-agent/oidc-discovery-provider, bibliotecas go-spiffe e java-spiffe, integração com Envoy SDS, framework de plugins e auditorias de segurança Cure53 (2021) e CNCF TAG-Security (2018 e 2020).; consultado em 2026-10-03.
- [SPIFFE & SPIRE Official Documentation — Quickstart Guides & Architecture](https://spiffe.io/spire/try/) — Portal oficial do SPIFFE e SPIRE com arquitetura de atestação de nó e workload, guias para Kubernetes/Linux/macOS e o livro gratuito Solving the Bottom Turtle.; consultado em 2026-10-03.
- [SPIRE — Official GitHub Repository](https://github.com/spiffe/spire) — Repositório oficial Apache-2.0 do SPIRE na CNCF.; consultado em 2026-10-03.
