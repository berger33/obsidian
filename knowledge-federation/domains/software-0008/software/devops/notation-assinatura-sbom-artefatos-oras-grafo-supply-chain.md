---
id: software.devops.tranche13.001299
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
fontes: ["https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/", "https://oras.land/docs/category/oras-commands/", "https://raw.githubusercontent.com/notaryproject/notation/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notary Project Notation: Assinatura de SBOMs e Artefatos Anexados via ORAS no Grafo OCI

## Em uma frase
Como o Notation opera sobre qualquer manifesto OCI no registro, ele permite assinar não apenas a imagem de container principal, mas também os artefatos anexados a ela via `oras attach` (como SBOMs SPDX/CycloneDX, relatórios de scan Trivy ou bundles de configuração), criando um grafo de supply chain inteiramente autenticado.

## Por que importa
Se a imagem de container for assinada com `notation sign`, mas o SBOM anexado a ela via OCI Referrers não for assinado, um atacante com acesso ao repositório poderia anexar um SBOM falso ocultando pacotes vulneráveis.

## Como funciona
O fluxo em três etapas publica a imagem e obtém seu digest (`$IMG_DIGEST`), anexa o SBOM com `oras attach` capturando o digest do próprio manifesto do SBOM (`$SBOM_DIGEST`) e executa `notation sign` tanto em `$IMG_DIGEST` quanto em `$SBOM_DIGEST`, formando uma árvore verificável em dois níveis.

## Exemplo
```bash
# 1. Assinar a imagem principal:
notation sign "ghcr.io/org/app@${IMG_DIGEST}"

# 2. Anexar o SBOM e assinar tambem o manifesto do SBOM anexado:
oras attach --artifact-type application/spdx+json "ghcr.io/org/app@${IMG_DIGEST}" sbom.spdx.json
SBOM_DIGEST=$(oras discover "ghcr.io/org/app@${IMG_DIGEST}" -o json | jq -r '.referrers[0].digest')
notation sign "ghcr.io/org/app@${SBOM_DIGEST}"
```

## Limites e trade-offs
Esquecer de habilitar `REGISTRY_STORAGE_DELETE_ENABLED=true` em registros de teste locais (`distribution/distribution`) durante ciclos de assinatura e limpeza impede a remoção de manifestos de assinatura antigos.

## Como verificar
Use `oras discover --format tree` combinado com `notation ls` para visualizar toda a árvore de referrers (SBOMs + assinaturas `application/vnd.cncf.notary.v2.signature`) ligada à imagem.

## Conexões
- [[notation-verificacao-admissao-kubernetes-kyverno-ratify-gatekeeper]] — Veja também: Notary Project Notation: Verificação de Assinaturas na Admissão do Kubernetes com Kyverno e Ratify.
- [[notation-niveis-verificacao-strict-permissive-audit-skip-migracao]] — Veja também: Notary Project Notation: Adoção Gradual com Níveis de Verificação (strict, permissive, audit e skip).

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://oras.land/docs/category/oras-commands/) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
