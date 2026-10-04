---
id: software.devops.tranche10.000934
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

# SOPS: visualização transparente de diffs em texto claro no Git (.gitattributes e diff.sopsdiffer.textconv)

## Em uma frase
Conforme documenta a seção `Showing diffs in cleartext in git` de `Common operations`, configurar um filtro `diff=sopsdiffer` no `.gitattributes` junto com `git config diff.sopsdiffer.textconv "sops decrypt"` permite que o `git diff` exiba automaticamente as diferenças em texto claro entre versões de arquivos criptografados.

## Por que importa
Embora o SOPS mantenha os nomes das chaves em texto claro, quando um valor criptografado é alterado (ou quando a DEK do arquivo é rotacionada), o `git diff` padrão mostra apenas a mudança de uma string Base64 `ENC[AES256_GCM,...]` para outra, exigindo que o revisor descriptografe manualmente as duas versões para saber qual era o valor antigo e qual é o novo.

## Como funciona
O Git possui o recurso nativo `textconv` para converter arquivos binários ou cifrados em texto antes de calcular o diff visual na tela. Ao adicionar **`*.enc.yaml diff=sopsdiffer`** (ou `*.yaml diff=sopsdiffer` na pasta de segredos) no arquivo **`.gitattributes`** na raiz do repositório e executar **`git config diff.sopsdiffer.textconv "sops decrypt"`** no repositório local, toda chamada ao comando `git diff` (ou `git log -p` e interfaces gráficas de clientes Git) invoca `sops decrypt` em memória sobre a versão anterior e a versão atual do arquivo antes de exibir o diff colorido linha a linha.

## Exemplo
```bash
# Configurar o repositório Git local para exibir diffs de arquivos *.enc.yaml descriptografados automaticamente
echo "*.enc.yaml diff=sopsdiffer" >> .gitattributes
git config diff.sopsdiffer.textconv "sops decrypt"
git diff secrets.enc.yaml
```

## Limites e trade-offs
O filtro `textconv` do Git altera exclusivamente a **exibição visual** do `git diff` e `git log -p` na máquina do desenvolvedor que possui a chave de descriptografia; ele nunca altera o conteúdo gravado nos commits (`git add` / `git commit` continuam gravando apenas o arquivo criptografado no repositório).

## Como verificar
Verifique a configuração no `.git/config` com `git config --get diff.sopsdiffer.textconv` e execute `git diff` após alterar um segredo com `sops set` para confirmar a visualização do diff em texto claro.

## Conexões
- [[sops-criptografia-parcial-chaves-encrypted-regex-mac]] — Veja também: SOPS: criptografia seletiva de campos (--encrypted-regex, _unencrypted, --encrypted-suffix) e integridade MAC.
- [[sops-regras-criacao-arquivo-sops-yaml-path-regex]] — Veja também: SOPS: automação de políticas de chaves e criptografia por diretório com .sops.yaml (creation_rules e path_regex).
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[sops-operacoes-arvore-extract-set-unset-in-place]] — Referência cruzada direta com sops-operacoes-arvore-extract-set-unset-in-place.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/common-operations/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
