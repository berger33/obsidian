---
id: software.devops.tranche13.001291
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/notaryproject/notation/main/README.md", "https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/", "https://notaryproject.dev/docs/user-guides/installation/cli/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notary Project Notation: Arquitetura CNCF Incubating para Assinatura e Verificação de Artefatos OCI

## Em uma frase
O **Notation** (`notaryproject/notation`, projeto **CNCF Incubating**) é a CLI e biblioteca oficial que implementa as especificações do **Notary Project (Notary v2)** para assinar e verificar criptograficamente imagens de containers e artefatos genéricos como itens padrão no ecossistema de registros OCI.

## Por que importa
Enquanto o Notary v1 legado usava um servidor TUF separado incompatível com a portabilidade de artefatos entre registros, o Notation armazena as assinaturas diretamente no próprio registro OCI vinculadas ao digest da imagem.

## Como funciona
O Notation assina sempre o **digest imutável** (`@sha256:...`) do artefato (resolvendo tags para digest antes de assinar) e publica um artefato de assinatura com media type `application/vnd.cncf.notary.v2.signature` anexado à imagem no registry, que pode ser listado com `notation ls` e validado com `notation verify`.

## Exemplo
```bash
IMAGE="localhost:5001/net-monitor@sha256:073b75987e95b89f187a89809f08a32033972bb63cda279db8a9ca16b7ff555a"
notation sign "$IMAGE"
notation ls "$IMAGE"
notation verify "$IMAGE"
```

## Limites e trade-offs
Passar uma tag mutável (`localhost:5001/net-monitor:v1`) para `notation sign` e continuar usando a tag nos manifestos de deploy permite que a tag seja apontada para outra imagem entre o build e o deploy.

## Como verificar
Referencie sempre o digest imutável (`@sha256:...`) tanto ao assinar com `notation sign` quanto ao verificar com `notation verify` e implantar no Kubernetes.

## Conexões
- [[notation-formatos-assinatura-jws-vs-cose-rfc8152]] — Veja também: Notary Project Notation: Envelopes de Assinatura JWS (JSON Web Signature) e COSE (RFC 8152).

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://notaryproject.dev/docs/user-guides/installation/cli/) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
