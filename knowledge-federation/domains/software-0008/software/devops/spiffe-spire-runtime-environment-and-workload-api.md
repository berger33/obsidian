---
id: software.devops.tranche05.000471
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

# SPIRE como ambiente de execução SPIFFE graduado na CNCF e exposição da SPIFFE Workload API

## Em uma frase
O **SPIRE** (*the SPIFFE Runtime Environment*), projeto **graduado na CNCF** sob licença Apache-2.0, é uma cadeia de ferramentas e APIs para estabelecer confiança criptográfica entre sistemas de software através de uma ampla variedade de plataformas de hospedagem (Kubernetes, máquinas virtuais Linux, bare-metal, nuvens públicas). Conforme define o README oficial, o SPIRE expõe a **SPIFFE Workload API** (`workload.proto`), que atesta sistemas de software em execução e emite **SPIFFE IDs** (`spiffe://trust-domain/workload-identifier`) e **SVIDs** (*SPIFFE Verifiable Identity Documents*) para eles, permitindo que duas cargas de trabalho estabeleçam confiança mútua sem segredos estáticos.

## Por que importa
Autenticar microsserviços distribuindo senhas, chaves de API ou certificados de longa duração em variáveis de ambiente e arquivos estáticos cria o problema da "tartaruga de baixo" (*the bottom turtle*: como autenticar o processo que busca o primeiro segredo?). O SPIRE resolve esse problema atestando dinamicamente o processo junto ao kernel/kubelet/nuvem e entregando identidades criptográficas de curta duração via socket local.

## Como funciona
Implante o SPIRE para emitir identidades verificáveis padronizadas (`SPIFFE IDs`) para workloads que precisam estabelecer conexões **mTLS**, assinar e verificar tokens **JWT**, ou autenticar-se com segurança em cofres de segredos, bancos de dados e serviços de provedores de nuvem sem credenciais gravadas em disco.

## Exemplo
Dois microsserviços rodando um em um cluster Kubernetes on-premises e outro em uma VM na nuvem recebem seus SVIDs da SPIFFE Workload API local e estabelecem uma conexão mTLS autenticada pela identidade `spiffe://empresa.com/pagamentos/api` sem compartilhar nenhuma senha estática.

## Limites e trade-offs
Lembre-se de que a SPIFFE Workload API é projetada para ser consumida localmente no mesmo host/nó via Unix Domain Socket sem exigir que a aplicação apresente um token inicial: a identidade da aplicação é descoberta pelo próprio `spire-agent` inspecionando os metadados do processo chamador no kernel e no runtime de contêiner.

## Como verificar
Consulte os recursos da API ou execute o cliente da SPIFFE Workload API em um workload registrado e confirme o recebimento do `SPIFFE ID` e do SVID válido.

## Conexões
- [[spiffe-x509-svid-mtls-and-jwt-svid-authentication]] — Veja também: Documentos de identidade verificáveis SVIDs (X.509 e JWT) para mTLS e autenticação entre serviços.

## Fontes
- [SPIRE GitHub — README.md (SPIFFE Runtime Environment, Workload API, SVIDs, Envoy SDS & Security Audits)](https://raw.githubusercontent.com/spiffe/spire/main/README.md) — README oficial do SPIRE (projeto graduado na CNCF sob Apache-2.0) detalhando implementação de produção do SPIFFE, SPIFFE Workload API, emissão de SPIFFE IDs e SVIDs (X.509 mTLS e JWT), imagens spire-server/spire-agent/oidc-discovery-provider, bibliotecas go-spiffe e java-spiffe, integração com Envoy SDS, framework de plugins e auditorias de segurança Cure53 (2021) e CNCF TAG-Security (2018 e 2020).; consultado em 2026-10-03.
- [SPIFFE & SPIRE Official Documentation — Quickstart Guides & Architecture](https://spiffe.io/spire/try/) — Portal oficial do SPIFFE e SPIRE com arquitetura de atestação de nó e workload, guias para Kubernetes/Linux/macOS e o livro gratuito Solving the Bottom Turtle.; consultado em 2026-10-03.
- [SPIRE — Official GitHub Repository](https://github.com/spiffe/spire) — Repositório oficial Apache-2.0 do SPIRE na CNCF.; consultado em 2026-10-03.
