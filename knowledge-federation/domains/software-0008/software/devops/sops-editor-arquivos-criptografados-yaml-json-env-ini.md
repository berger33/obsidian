---
id: software.devops.tranche10.000931
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
fontes: ["https://raw.githubusercontent.com/getsops/sops/main/README.rst", "https://getsops.io/docs/usage/common-operations/", "https://getsops.io/docs/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SOPS (Secrets OPerationS): editor de arquivos criptografados estruturados (YAML, JSON, ENV, INI e BINARY)

## Em uma frase
O **SOPS** (`getsops/sops`, criado na Mozilla em 2015 e doado à CNCF como projeto Sandbox sob licença MPL-2.0) é um editor de arquivos criptografados que suporta formatos **YAML, JSON, ENV, INI e BINARY**, criptografando valores com AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud KMS, **age** e **PGP**.

## Por que importa
Quando se criptografa um arquivo YAML ou JSON inteiro como um bloco binário opaco (por exemplo, com `gpg -c secrets.yaml` ou `openssl enc`), torna-se impossível ver no `git diff` ou em um Pull Request **qual chave** foi alterada ou adicionada sem descriptografar o arquivo inteiro. Segundo o `README.rst` oficial e a documentação em `getsops.io/docs/`, o SOPS preserva as chaves do documento em texto claro e criptografa apenas os valores.

## Como funciona
Quando você criptografa um arquivo estruturado (`YAML`, `JSON`, `ENV` ou `INI`) com **`sops encrypt`** (ou o edita diretamente com **`sops edit arquivo.yaml`**), o SOPS gera uma chave de criptografia de dados simétrica (**Data Encryption Key — DEK**), cifra individualmente cada valor da árvore mantendo os nomes das chaves em texto claro, cifra a DEK usando uma ou mais chaves mestras configuradas (KMS de nuvem, `age` ou `PGP`) e adiciona ao final do arquivo um bloco de metadados chamado **`sops:`** contendo as chaves mestras cifradas, o timestamp `lastmodified` e um código de autenticação de mensagem (**`mac`**) que protege a integridade de todo o arquivo.

## Exemplo
```bash
# Criptografar um arquivo existente em um novo arquivo e descriptografá-lo no stdout usando a CLI sops
sops encrypt secrets.plain.yaml > secrets.enc.yaml
sops decrypt secrets.enc.yaml
```

## Limites e trade-offs
Como o SOPS mantém os **nomes das chaves** (e a estrutura de indentação do YAML/JSON) em texto claro para viabilizar code review e diffs legíveis no Git, nunca coloque o próprio segredo dentro do *nome* de uma chave YAML; caso você precise ocultar até mesmo a estrutura e os nomes das chaves do arquivo, criptografe-o usando o formato `binary` (`--input-type binary --output-type binary`).

## Como verificar
Inspecione um arquivo criptografado `secrets.enc.yaml` com `cat` e confirme que os valores apareceram no formato `ENC[AES256_GCM,data:...,iv:...,tag:...,type:str]` e que a seção final `sops:` contém o `mac` e os receptores de chave.

## Conexões
- [[sops-operacoes-arvore-extract-set-unset-in-place]] — Veja também: SOPS: edição in-place (-i) e manipulação cirúrgica da árvore do documento (--extract, sops set e sops unset).
- [[sops-criptografia-parcial-chaves-encrypted-regex-mac]] — Referência cruzada direta com sops-criptografia-parcial-chaves-encrypted-regex-mac.
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/common-operations/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
