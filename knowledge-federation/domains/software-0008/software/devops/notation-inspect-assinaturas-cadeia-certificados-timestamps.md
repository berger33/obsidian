---
id: software.devops.tranche13.001297
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
fontes: ["https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/", "https://raw.githubusercontent.com/notaryproject/notation/main/README.md", "https://notaryproject.dev/docs/user-guides/installation/cli/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notary Project Notation: Inspeção Detalhada de Assinaturas e Cadeias X.509 com notation inspect

## Em uma frase
O comando `notation inspect <imagem@sha256:...>` decodifica e exibe em formato legível (árvore ou JSON) todos os metadados internos de cada assinatura anexada a um artefato OCI, incluindo algoritmo de assinatura, atributos assinados (`expiry`, `signingScheme`), timestamps e o `Subject`/`Issuer`/validade de cada certificado da cadeia X.509.

## Por que importa
Quando `notation verify` falha por expiração de certificado, incompatibilidade de `trustedIdentities` ou ausência de carimbo de tempo (RFC 3161 TSA), `notation ls` mostra apenas os digests das assinaturas sem revelar qual certificado assinou o artefato.

## Como funciona
Ao executar `notation inspect $IMAGE` (ou `notation inspect --output json $IMAGE`), o engenheiro inspeciona exatamente o `Media type` (`application/vnd.cncf.notary.v2.signature`), o algoritmo (`ECDSA-SHA-256`, `RSASSA-PSS-SHA-256`), o `Signed attributes` e a cadeia completa de certificados embutida no envelope JWS ou COSE.

## Exemplo
```bash
notation ls "$IMAGE"
notation inspect "$IMAGE"
```

## Limites e trade-offs
Assinar imagens de produção com certificados folha de curta duração sem anexar um carimbo de tempo confiável (TSA — Time Stamping Authority) faz com que `notation verify` passe a rejeitar a imagem em produção assim que o certificado expirar.

## Como verificar
Configure um endpoint TSA RFC 3161 ao assinar artefatos de longa duração e audite os atributos do carimbo de tempo com `notation inspect`.

## Conexões
- [[notation-instalacao-verificacao-shasum-notation-config-dir]] — Veja também: Notary Project Notation: Instalação Verificada por Checksum, Estrutura NOTATION_CONFIG e Estabilidade de Versões.
- [[notation-verificacao-admissao-kubernetes-kyverno-ratify-gatekeeper]] — Veja também: Notary Project Notation: Verificação de Assinaturas na Admissão do Kubernetes com Kyverno e Ratify.

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://notaryproject.dev/docs/user-guides/installation/cli/) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
