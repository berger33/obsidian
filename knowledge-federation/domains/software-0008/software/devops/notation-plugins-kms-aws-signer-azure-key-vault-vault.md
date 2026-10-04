---
id: software.devops.tranche13.001295
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

# Notary Project Notation: Arquitetura de Plugins KMS (AWS Signer, Azure Key Vault e HashiCorp Vault)

## Em uma frase
O Notation possui uma arquitetura extensível de plugins (`notation plugin ls`) que delega a operação criptográfica de assinatura para serviços de KMS e HSM em nuvem — como **AWS Signer**, **Azure Key Vault (AKV)**, **Google Cloud KMS** e **HashiCorp Vault** — sem que a chave privada jamais saia do HSM.

## Por que importa
Gerar e armazenar chaves privadas de assinatura em arquivos locais no disco do runner de CI/CD cria o risco de exfiltração da chave privada caso o runner sofra comprometimento.

## Como funciona
Com o plugin instalado no diretório de plugins de `NOTATION_CONFIG`, o operador registra a chave externa com `notation key add --plugin <nome-do-plugin> --id <key-arn-ou-uri>`. Durante `notation sign`, o Notation envia apenas o digest a ser assinado para a API do KMS/Signer (autenticado via OIDC/IAM role do runner) e anexa a assinatura retornada ao registry OCI.

## Exemplo
```bash
notation plugin ls
notation key ls
```

## Limites e trade-offs
Conceder a permissão IAM de `signer:SignPayload` ou acesso de assinatura no Key Vault para jobs de Pull Request não revisados (em vez de restringir aos workflows de release da branch protegida) permite que código de PR receba assinatura oficial de produção.

## Como verificar
Restrinja a identidade IAM/OIDC autorizada a invocar o plugin KMS do Notation exclusivamente aos pipelines de release de tags/branches protegidas.

## Conexões
- [[notation-trust-policy-json-registryscopes-trustedidentities-levels]] — Veja também: Notary Project Notation: Configuração de Trust Policy (trustpolicy.json), Escopos e Níveis de Verificação.
- [[notation-instalacao-verificacao-shasum-notation-config-dir]] — Veja também: Notary Project Notation: Instalação Verificada por Checksum, Estrutura NOTATION_CONFIG e Estabilidade de Versões.

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://notaryproject.dev/docs/user-guides/installation/cli/) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
