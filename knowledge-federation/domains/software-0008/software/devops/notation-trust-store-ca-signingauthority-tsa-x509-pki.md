---
id: software.devops.tranche13.001293
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
fontes: ["https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/", "https://notaryproject.dev/docs/user-guides/installation/cli/", "https://raw.githubusercontent.com/notaryproject/notation/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notary Project Notation: Gerenciamento de Trust Store (ca, signingAuthority e tsa) e Certificados X.509

## Em uma frase
O modelo de confiança do Notation baseia-se em infraestrutura de chaves públicas X.509 (**PKI**), organizando os certificados confiáveis em uma **Trust Store** local (`notation cert add`, `notation cert ls`, `notation cert show`, `notation cert delete`) dividida por tipos (`ca`, `signingAuthority` e `tsa` para Time Stamping Authorities).

## Por que importa
Diferente de modelos que dependem exclusivamente de chaves avulsas sem hierarquia de certificação, o uso de cadeias X.509 permite que uma organização confie na Autoridade Certificadora (CA) raiz corporativa e revogue certificados folha intermediários sem precisar redistribuir chaves públicas em todos os clusters.

## Como funciona
Os certificados são adicionados a named stores tipadas, como `ca:wabbit-networks.io`, que depois são referenciadas no array `"trustStores"` das políticas de confiança (`trustpolicy.json`). Para testes locais, `notation cert generate-test --default "wabbit-networks.io"` gera um par de chaves RSA de teste e adiciona o certificado autoassinado à trust store.

## Exemplo
```bash
notation cert generate-test --default "wabbit-networks.io"
notation key ls
notation cert ls
```

## Limites e trade-offs
Utilizar certificados autoassinados gerados por `notation cert generate-test` em ambientes de produção viola o modelo de segurança do Notary Project (que alerta explicitamente que certificados de teste são apenas para desenvolvimento).

## Como verificar
Em produção, utilize certificados X.509 emitidos por uma CA privada/corporativa ou por cofres de nuvem (AWS Signer, Azure Key Vault, HashiCorp Vault) e remova qualquer certificado de teste da Trust Store.

## Conexões
- [[notation-formatos-assinatura-jws-vs-cose-rfc8152]] — Veja também: Notary Project Notation: Envelopes de Assinatura JWS (JSON Web Signature) e COSE (RFC 8152).
- [[notation-trust-policy-json-registryscopes-trustedidentities-levels]] — Veja também: Notary Project Notation: Configuração de Trust Policy (trustpolicy.json), Escopos e Níveis de Verificação.

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://notaryproject.dev/docs/user-guides/installation/cli/) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
