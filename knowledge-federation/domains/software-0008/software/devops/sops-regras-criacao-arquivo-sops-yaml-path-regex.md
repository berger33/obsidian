---
id: software.devops.tranche10.000935
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

# SOPS: automação de políticas de chaves e criptografia por diretório com .sops.yaml (creation_rules e path_regex)

## Em uma frase
O arquivo de configuração **`.sops.yaml`** na raiz do repositório define regras declarativas (`creation_rules`) baseadas em `path_regex`, selecionando automaticamente quais chaves KMS/age/PGP e qual `encrypted_regex` aplicar a cada arquivo sem precisar passar flags na linha de comando.

## Por que importa
Passar manualmente ARNs longos do AWS KMS (`--kms arn:aws:kms:...`), chaves públicas `age` (`--age age1...`) e `--encrypted-regex` toda vez que alguém cria um arquivo de segredo para `dev`, `staging` ou `prod` é propenso a erro humano (como criptografar um segredo de produção usando a chave KMS de desenvolvimento).

## Como funciona
Quando o usuário executa `sops encrypt` ou `sops edit <caminho/do/arquivo.yaml>`, o SOPS sobe a árvore de diretórios até encontrar um arquivo **`.sops.yaml`**. Ele avalia a lista **`creation_rules:`** de cima para baixo e aplica a **primeira regra** cujo **`path_regex`** case com o caminho do arquivo: se o arquivo estiver em `clusters/prod/.*\.yaml$`, aplica a chave KMS/age de produção e `encrypted_regex: ^(data|stringData)$`; se estiver em `clusters/dev/.*\.yaml$`, aplica as chaves da equipe de desenvolvimento.

## Exemplo
```yaml
# Exemplo de arquivo .sops.yaml na raiz do repositório diferenciando chaves e regras entre prod e staging
creation_rules:
  - path_regex: clusters/prod/.*\.enc\.yaml$
     encrypted_regex: ^(data|stringData)$
    kms: arn:aws:kms:us-east-1:111122223333:key/prod-key-id
    age: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p

  - path_regex: clusters/staging/.*\.enc\.yaml$
    encrypted_regex: ^(data|stringData)$
    age: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
```

## Limites e trade-offs
Como o SOPS utiliza a **primeira** regra em `creation_rules` cujo `path_regex` casa com o caminho do arquivo (first-match wins), coloque sempre as regras de caminhos mais específicos (`clusters/prod/...`) **acima** de qualquer regra genérica catch-all (`.*\.yaml$`), pois uma regra genérica no topo sombrearia todas as regras subsequentes.

## Como verificar
Crie um `.sops.yaml` com uma regra `path_regex` e `encrypted_regex`, execute `sops encrypt clusters/staging/secret.enc.yaml` sem passar nenhuma flag de chave na CLI e verifique no bloco `sops:` gerado que as chaves do `.sops.yaml` foram aplicadas.

## Conexões
- [[sops-integracao-git-diff-textconv-gitattributes]] — Veja também: SOPS: visualização transparente de diffs em texto claro no Git (.gitattributes e diff.sopsdiffer.textconv).
- [[sops-provedores-identidades-kms-age-pgp-vault]] — Veja também: SOPS: identidades e provedores de chaves mestras (age, PGP, AWS KMS, GCP KMS, Azure Key Vault e HashiCorp Vault).
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[sops-criptografia-parcial-chaves-encrypted-regex-mac]] — Referência cruzada direta com sops-criptografia-parcial-chaves-encrypted-regex-mac.
- [[sops-gerenciamento-chaves-updatekeys-rotate-keygroups]] — Referência cruzada direta com sops-gerenciamento-chaves-updatekeys-rotate-keygroups.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/common-operations/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
