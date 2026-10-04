---
id: software.devops.tranche10.000932
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

# SOPS: edição in-place (-i) e manipulação cirúrgica da árvore do documento (--extract, sops set e sops unset)

## Em uma frase
Conforme documenta a página oficial `Common operations` (`getsops.io/docs/usage/common-operations/`), o SOPS permite criptografar/descriptografar arquivos in-place (`-i`), extrair apenas uma sub-árvore ou chave específica (`sops decrypt --extract`) e alterar ou remover valores sem abrir editor interativo (`sops set` e `sops unset`).

## Por que importa
Em scripts de automação e pipelines de CI/CD (onde não há humano para interagir com o editor `$EDITOR` aberto pelo `sops edit`), frequentemente é necessário extrair apenas uma chave específica (ex.: uma chave privada RSA dentro do YAML) sem precisar instalar `yq`/`jq` ou atualizar um único valor criptografado via linha de comando.

## Como funciona
O SOPS utiliza uma sintaxe de caminho de árvore estilo dicionário Python (`'["chavePai"]["chaveFilha"]'` para objetos e `'["meu_array"][1]'` para índices de listas): (1) **Extração (`--extract`)**: `sops decrypt --extract '["app2"]["key"]' example.yaml` descriptografa e imprime exclusivamente aquele valor no `stdout`; (2) **Atualização não-interativa (`sops set`)**: `sops set example.yaml '["app2"]["key"]' '"novoValorJson"'` (ou lendo de arquivo com `--value-file` ou stdin com `--value-stdin`) descriptografa a DEK, atualiza apenas aquela folha da árvore, recalcula o `mac` e regrava o arquivo criptografado; (3) **Remoção (`sops unset`)**: `sops unset example.yaml '["app2"]["key"]'` remove a chave da árvore; e (4) **In-place (`-i` / `--in-place`)**: `sops encrypt -i file.yaml` substitui o próprio arquivo.

## Exemplo
```bash
# Extrair uma chave específica e atualizar outra chave diretamente na árvore criptografada sem abrir editor
sops decrypt --extract '["database"]["password"]' secrets.enc.yaml
sops set secrets.enc.yaml '["database"]["password"]' '"novaSenhaRotacionada2026"'
```

## Limites e trade-offs
Conforme alerta a seção `Saving Output to a File` da documentação oficial, passar simultaneamente as flags `--in-place` (`-i`) e `--output` no mesmo comando resulta em erro; além disso, lembre-se de que no comando `sops set <arquivo> <caminho> <valor>`, o `<valor>` passado como argumento na CLI **deve ser formatado como JSON válido** (portanto, uma string simples precisa de aspas duplas internas, como `'"meu_texto"'`).

## Como verificar
Execute `sops set secrets.enc.yaml '["app"]["env"]' '"staging"'` e em seguida `sops decrypt --extract '["app"]["env"]' secrets.enc.yaml` para confirmar que o valor retornado é `staging`.

## Conexões
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Veja também: SOPS (Secrets OPerationS): editor de arquivos criptografados estruturados (YAML, JSON, ENV, INI e BINARY).
- [[sops-criptografia-parcial-chaves-encrypted-regex-mac]] — Veja também: SOPS: criptografia seletiva de campos (--encrypted-regex, _unencrypted, --encrypted-suffix) e integridade MAC.
- [[sops-integracao-git-diff-textconv-gitattributes]] — Referência cruzada direta com sops-integracao-git-diff-textconv-gitattributes.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/common-operations/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
