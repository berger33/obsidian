---
id: software.devops.tranche10.000936
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/getsops/sops/main/README.rst", "https://getsops.io/docs/usage/", "https://getsops.io/docs/usage/common-operations/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SOPS: identidades e provedores de chaves mestras (age, PGP, AWS KMS, GCP KMS, Azure Key Vault e HashiCorp Vault)

## Em uma frase
O SOPS suporta criptografia envelope multi-receptor combinando chaves assimétricas locais modernas (**age** e **PGP**) com serviços gerenciados de KMS em nuvem (**AWS KMS**, **GCP KMS**, **Azure Key Vault**, **HuaweiCloud KMS**) e o motor Transit do **HashiCorp Vault**.

## Por que importa
Em equipes reais e clusters GitOps, um único arquivo criptografado precisa poder ser aberto tanto pelo controlador do Flux/Argo CD rodando na AWS (via IAM Role no AWS KMS ou chave `age`) quanto por um engenheiro sênior de plantão (via sua chave `age` ou `PGP` de emergência) caso o provedor de nuvem esteja indisponível. A seção `Identities` de `getsops.io/docs/usage/` documenta esse suporte.

## Como funciona
O SOPS nunca usa o KMS ou a chave `age`/`PGP` para criptografar diretamente todos os valores do arquivo: ele usa **Envelope Encryption**. Uma única **Data Encryption Key (DEK)** simétrica AES-256-GCM criptografa os valores do documento, e essa DEK de 32 bytes é criptografada separadamente para cada chave mestra listada (`kms`, `gcp_kms`, `azure_kv`, `hc_vault`, `age`, `pgp`). Para descriptografar o arquivo (`sops decrypt`), o cliente precisa ter acesso a **apenas uma** das chaves mestras registradas no bloco `sops:` do arquivo (a menos que `key_groups` com `shamir_threshold` seja configurado).

## Exemplo
```bash
# Criptografar um arquivo usando uma chave pública moderna 'age' (definida via flag --age ou variável SOPS_AGE_RECIPIENTS)
export SOPS_AGE_RECIPIENTS="age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p"
sops encrypt secrets.yaml > secrets.enc.yaml
```

## Limites e trade-offs
Na comunidade Cloud Native e GitOps (como no guia oficial do Flux CD), a ferramenta **`age`** (`FiloSottile/age`) substituiu amplamente o legado `PGP`/`GnuPG` para chaves locais ou em-cluster porque possui chaves públicas compactas de uma única linha (`age1...`), zero configuração de anel de chaves complexo (`gpg-agent`) e criptografia moderna (`X25519` + `ChaCha20-Poly1305`).

## Como verificar
Verifique no bloco final `sops:` do arquivo criptografado as listas `kms:`, `age:` ou `pgp:`, onde cada entrada armazena sua própria cópia cifrada (`enc:`) da mesma chave de dados do arquivo.

## Conexões
- [[sops-regras-criacao-arquivo-sops-yaml-path-regex]] — Veja também: SOPS: automação de políticas de chaves e criptografia por diretório com .sops.yaml (creation_rules e path_regex).
- [[sops-gerenciamento-chaves-updatekeys-rotate-keygroups]] — Veja também: SOPS: rotação da chave de dados (sops rotate), sincronização de receptores (sops updatekeys) e Key Groups (Shamir).
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[vault-criptografia-como-servico-transit-data-encryption]] — Referência cruzada direta com vault-criptografia-como-servico-transit-data-encryption.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/usage/common-operations/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
