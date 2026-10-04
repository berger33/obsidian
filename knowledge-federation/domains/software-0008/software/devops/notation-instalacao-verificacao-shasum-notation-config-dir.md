---
id: software.devops.tranche13.001296
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
fontes: ["https://notaryproject.dev/docs/user-guides/installation/cli/", "https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/", "https://raw.githubusercontent.com/notaryproject/notation/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notary Project Notation: Instalação Verificada por Checksum, Estrutura NOTATION_CONFIG e Estabilidade de Versões

## Em uma frase
A documentação oficial de instalação do Notation recomenda validar a integridade do arquivo tar/zip baixado contra o arquivo `notation_<VERSION>_checksums.txt` usando `shasum --check` antes de extrair o binário, além de configurar o diretório de estado via variável `NOTATION_CONFIG`.

## Por que importa
Baixar binários de segurança de supply chain em runners de CI via `curl` sem verificar o checksum SHA-256 ou instalar versões alpha instáveis (como `2.0.0-alpha.1`) em produção compromete a confiabilidade do pipeline.

## Como funciona
O Notation cria automaticamente o diretório apontado por `NOTATION_CONFIG` (ou o diretório XDG padrão do sistema operacional), onde armazena `config.json`, `trustpolicy.json`, `localkeys/` (apenas para testes), `truststore/x509/` e `plugins/`.

## Exemplo
```bash
export NOTATION_VERSION=1.3.0
curl -LO "https://github.com/notaryproject/notation/releases/download/v${NOTATION_VERSION}/notation_${NOTATION_VERSION}_linux_amd64.tar.gz"
curl -LO "https://github.com/notaryproject/notation/releases/download/v${NOTATION_VERSION}/notation_${NOTATION_VERSION}_checksums.txt"
grep "linux_amd64.tar.gz" "notation_${NOTATION_VERSION}_checksums.txt" | shasum --check
```

## Limites e trade-offs
Usar apenas `notation key delete` e `notation cert delete` para tentar limpar chaves e certificados de teste criados por `notation cert generate-test` não remove os arquivos físicos do disco em `localkeys/`, exigindo limpeza explícita do diretório.

## Como verificar
Defina um `NOTATION_CONFIG` isolado para ambientes de teste e utilize sempre releases estáveis verificadas por `shasum --check` em produção.

## Conexões
- [[notation-plugins-kms-aws-signer-azure-key-vault-vault]] — Veja também: Notary Project Notation: Arquitetura de Plugins KMS (AWS Signer, Azure Key Vault e HashiCorp Vault).
- [[notation-inspect-assinaturas-cadeia-certificados-timestamps]] — Veja também: Notary Project Notation: Inspeção Detalhada de Assinaturas e Cadeias X.509 com notation inspect.

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://notaryproject.dev/docs/user-guides/installation/cli/) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
