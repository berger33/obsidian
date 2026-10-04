---
id: software.devops.tranche10.000933
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

# SOPS: criptografia seletiva de campos (--encrypted-regex, _unencrypted, --encrypted-suffix) e integridade MAC

## Em uma frase
Para arquivos que misturam metadados públicos e segredos (como manifestos `Kind: Secret` do Kubernetes), o SOPS permite criptografar apenas chaves específicas usando **`--encrypted-regex`** (ex.: `'^(data|stringData)$'`), sufixos **`_unencrypted`** ou **`--encrypted-suffix`**, mantendo o restante em texto claro mas protegido pelo **MAC** de integridade.

## Por que importa
Se você passar um manifesto `Secret` do Kubernetes para o `sops encrypt` sem filtros, o SOPS criptografará também os valores de `apiVersion: v1`, `kind: Secret` e `metadata.name`, impedindo que ferramentas de validação e indexação identifiquem qual recurso Kubernetes aquele arquivo representa antes da descriptografia. A seção `Encrypting only parts of a file` de `Common operations` resolve isso.

## Como funciona
O SOPS oferece três mecanismos para criptografar apenas parte de um arquivo YAML/JSON/ENV/INI: (1) **Sufixo `_unencrypted`** (customizável com `--unencrypted-suffix`): qualquer chave cujo nome termine em `_unencrypted` (e tudo abaixo dela) permanece em texto claro; (2) **`--encrypted-suffix`**: inverte a lógica para criptografar apenas chaves que terminem no sufixo escolhido; e (3) **`--encrypted-regex`**: criptografa exclusivamente os valores sob chaves que casem com a expressão regular fornecida — por exemplo, **`--encrypted-regex '^(data|stringData)$'`** em um `Secret` Kubernetes deixa `apiVersion`, `kind`, `metadata` e `type` em texto claro e criptografa apenas `data` e `stringData`. Crucialmente, mesmo os campos deixados em texto claro entram no cálculo do checksum **`mac`** do arquivo!

## Exemplo
```bash
# Criptografar apenas os blocos data e stringData de um Secret Kubernetes mantendo apiVersion, kind e metadata legíveis
sops encrypt --encrypted-regex '^(data|stringData)$' k8s-secret.yaml > k8s-secret.enc.yaml
```

## Limites e trade-offs
Como todos os valores do arquivo — inclusive os valores em texto claro fora de `encrypted-regex` ou marcados com `_unencrypted` — são incluídos por padrão no cálculo do **MAC (Message Authentication Code)** do SOPS, se alguém editar manualmente no editor de texto uma label ou o `metadata.name` em texto claro sem usar o `sops`, a descriptografia falhará com erro de verificação de integridade (`MAC mismatch`); caso você realmente precise permitir edição externa dos campos não criptografados, deve ativar explicitamente **`--mac-only-encrypted`**.

## Como verificar
Criptografe um manifesto Kubernetes com `--encrypted-regex '^(data|stringData)$'`, tente alterar manualmente `metadata.name` com `sed` e execute `sops decrypt` para observar a proteção do MAC bloqueando a adulteração.

## Conexões
- [[sops-operacoes-arvore-extract-set-unset-in-place]] — Veja também: SOPS: edição in-place (-i) e manipulação cirúrgica da árvore do documento (--extract, sops set e sops unset).
- [[sops-integracao-git-diff-textconv-gitattributes]] — Veja também: SOPS: visualização transparente de diffs em texto claro no Git (.gitattributes e diff.sopsdiffer.textconv).
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[sops-regras-criacao-arquivo-sops-yaml-path-regex]] — Referência cruzada direta com sops-regras-criacao-arquivo-sops-yaml-path-regex.
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/common-operations/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
