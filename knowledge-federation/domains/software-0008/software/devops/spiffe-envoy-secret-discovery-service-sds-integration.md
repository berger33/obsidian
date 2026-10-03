---
id: software.devops.tranche05.000474
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

# Rotação transparente de certificados TLS e trust bundles no Envoy Proxy via SPIRE SDS

## Em uma frase
A seção *Integrate with SPIRE* do README oficial destaca que o SPIRE fornece uma implementação nativa do **Secret Discovery Service (SDS)** do **Envoy Proxy** (`spiffe.io/spire/docs/envoy/`). Ao conectar o Envoy diretamente ao socket do `spire-agent` via protocolo SDS, o SPIRE **instala e rotaciona transparentemente os certificados TLS (X.509-SVIDs) e os pacotes de confiança (trust bundles) dentro do Envoy em memória**, sem que a aplicação principal precise conhecer a biblioteca SPIFFE ou gerenciar recarregamento de arquivos TLS.

## Por que importa
Muitas aplicações legadas ou escritas em diversas linguagens não podem ter seu código-fonte alterado para chamar diretamente a SPIFFE Workload API. Colocar um sidecar ou gateway Envoy consumindo o SDS do SPIRE adiciona mTLS autenticado por SPIFFE ID e rotação automática de certificados sem tocar em uma única linha de código da aplicação.

## Como funciona
Configure os clusters e listeners TLS do Envoy Proxy para buscar seus certificados (`tls_certificate_sds_secret_config`) e contextos de validação (`validation_context_sds_secret_config`) dinamicamente via gRPC SDS apontando para o socket Unix do `spire-agent`.

## Exemplo
Em uma malha de serviços baseada em Envoy e SPIRE, o `spire-agent` rotaciona os certificados X.509-SVID a cada poucas horas e empurra os novos pares de chaves automaticamente para o Envoy via stream SDS sem derrubar conexões TCP ativas.

## Limites e trade-offs
Certifique-se de configurar no filtro de validação do Envoy a checagem explícita do Subject Alternative Name (`match_typed_subject_alt_names`) para aceitar apenas os `SPIFFE IDs` autorizados a se comunicar com aquele serviço.

## Como verificar
Inspecione o endpoint `/certs` da interface de administração local do Envoy e confirme que o certificado X.509 carregado via SDS possui o `SPIFFE ID` esperado e validade atualizada.

## Conexões
- [[spiffe-spire-server-spire-agent-and-oidc-discovery-provider-images]] — Veja também: Componentes e imagens oficiais do SPIRE: spire-server, spire-agent e oidc-discovery-provider.
- [[spiffe-go-spiffe-and-java-spiffe-client-libraries]] — Veja também: Bibliotecas clientes oficiais go-spiffe e java-spiffe para consumo direto da SPIFFE Workload API.

## Fontes
- [SPIRE GitHub — README.md (SPIFFE Runtime Environment, Workload API, SVIDs, Envoy SDS & Security Audits)](https://raw.githubusercontent.com/spiffe/spire/main/README.md) — README oficial do SPIRE (projeto graduado na CNCF sob Apache-2.0) detalhando implementação de produção do SPIFFE, SPIFFE Workload API, emissão de SPIFFE IDs e SVIDs (X.509 mTLS e JWT), imagens spire-server/spire-agent/oidc-discovery-provider, bibliotecas go-spiffe e java-spiffe, integração com Envoy SDS, framework de plugins e auditorias de segurança Cure53 (2021) e CNCF TAG-Security (2018 e 2020).; consultado em 2026-10-03.
- [SPIFFE & SPIRE Official Documentation — Quickstart Guides & Architecture](https://spiffe.io/spire/try/) — Portal oficial do SPIFFE e SPIRE com arquitetura de atestação de nó e workload, guias para Kubernetes/Linux/macOS e o livro gratuito Solving the Bottom Turtle.; consultado em 2026-10-03.
- [SPIRE — Official GitHub Repository](https://github.com/spiffe/spire) — Repositório oficial Apache-2.0 do SPIRE na CNCF.; consultado em 2026-10-03.
