---
id: software.devops.tranche13.001292
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

# Notary Project Notation: Envelopes de Assinatura JWS (JSON Web Signature) e COSE (RFC 8152)

## Em uma frase
O Notation suporta dois formatos padronizados de envelope criptográfico para as assinaturas Notary v2: **JWS (JSON Web Signature)**, utilizado por padrão, e **COSE (CBOR Object Signing and Encryption — RFC 8152)**, selecionável via flag `--signature-format cose`.

## Por que importa
Ambientes corporativos e dispositivos de borda com requisitos específicos de serialização binária compacta (CBOR/RFC 8152) ou integração com cadeias de certificados X.509 precisam escolher o formato de envelope compatível com seus validadores.

## Como funciona
Ao executar `notation sign $IMAGE`, o Notation gera uma assinatura JWS contendo o descritor OCI assinado, atributos de timestamp/expiração e a cadeia de certificados X.509; passando `notation sign --signature-format cose $IMAGE`, o envelope é codificado no padrão binário COSE, mantendo o mesmo fluxo de listagem (`notation ls`) e verificação (`notation verify`).

## Exemplo
```bash
# Assinar imagem utilizando o formato padrao JWS ou o formato binario COSE:
notation sign "$IMAGE"
notation sign --signature-format cose "$IMAGE"
notation ls "$IMAGE"
```

## Limites e trade-offs
Usar versões muito antigas de plugins de verificação ou controladores de admissão que suportavam apenas JWS ao validar imagens assinadas com `--signature-format cose` causa falha de parsing na verificação.

## Como verificar
Mantenha o binário `notation` e os validadores de cluster (Ratify / Kyverno) atualizados para suportar tanto envelopes `jws` quanto `cose`.

## Conexões
- [[notation-arquitetura-notary-project-assinatura-artefatos-oci]] — Veja também: Notary Project Notation: Arquitetura CNCF Incubating para Assinatura e Verificação de Artefatos OCI.
- [[notation-trust-store-ca-signingauthority-tsa-x509-pki]] — Veja também: Notary Project Notation: Gerenciamento de Trust Store (ca, signingAuthority e tsa) e Certificados X.509.

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://notaryproject.dev/docs/user-guides/installation/cli/) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
