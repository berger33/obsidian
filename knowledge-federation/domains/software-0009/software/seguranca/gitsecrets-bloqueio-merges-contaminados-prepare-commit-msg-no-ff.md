---
id: software.seguranca.tranche10.000978
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst", "https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Como o Hook **`prepare-commit-msg`** do `git-secrets` Impede que um **Merge (`--no-ff`)** Contamine a Branch Principal com Histórico Sujo

## Em uma frase
Analise um cenário sutil que engana muitos hooks simples de `pre-commit`: um desenvolvedor terceirizado cria uma branch `feature/login`, faz um commit `A` adicionando uma chave `AKIA...` da AWS e, no commit seguinte `B`, percebe o erro e apaga a chave (`git rm`).

## Por que importa
Na árvore final do commit `B`, a chave não existe mais — portanto, um scanner que olha apenas o snapshot atual dos arquivos na hora do merge não vê nada de errado! Porém, quando o mantenedor executa **`git merge --no-ff feature/login`** na branch `main`, **o commit `A` (que contém a chave!) entra inteiro para dentro do histórico da branch `main`**!

## Como funciona
É exatamente para barrar esse vetor que o `git-secrets` instala o hook **`prepare-commit-msg`**: conforme implementado na função `prepare_commit_msg_hook()` do código-fonte oficial, ao detectar um merge (`case "$2,$3" in merge,)`), ele extrai o SHA da branch que está sendo mesclada (`GITHEAD_<sha>`) e executa **`git log "${dest}".."${sha}" -p | scan_with_fn_or_die "scan" -`** — varrendo o diff de **TODOS os commits intermediários da branch recebida** e abortando o merge na hora se qualquer commit passado contiver um segredo!

## Exemplo
```bash
# Simular a verificacao que o hook prepare-commit-msg do git-secrets realiza antes de aceitar o merge de uma branch
git log main..feature/nova-integracao -p | git secrets --scan -
```

## Limites e trade-offs
Essa verificação `git log main..HEAD -p | git secrets --scan -` também é o comando exato mais rápido para colocar em jobs de **Pull Request no GitHub Actions / GitLab CI**: ela analisa todos os commits do PR em menos de 1 segundo!

## Como verificar
Se um PR falhar nessa verificação porque o autor adicionou e depois removeu uma chave em commits separados da mesma branch, oriente-o a revogar a chave e fazer um `git rebase -i` (*squash/drop*) na branch antes do merge.

## Conexões
- [[gitsecrets-diferencas-egrep-gnu-bsd-macos-linux-portabilidade]] — Veja também: Portabilidade de Expressões Regulares no `git-secrets`: Diferenças entre **GNU `grep -E` (Linux)** e **BSD `grep -E` (macOS)** e Boas Práticas POSIX ERE.
- [[gitsecrets-integracao-pipelines-cicd-github-actions-gitlab-pre-receive]] — Veja também: Implantação de `git-secrets` em **Pipelines CI/CD** e **Hooks Server-Side (`pre-receive`)** para Impedir Bypass com `git commit --no-verify`.
- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — Referência cruzada direta com gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep.
- [[gitsecrets-modos-varredura-scan-cached-untracked-no-index-history]] — Referência cruzada direta com gitsecrets-modos-varredura-scan-cached-untracked-no-index-history.
- [[talisman-resposta-incidente-vazamento-revogacao-git-filter-repo]] — Referência cruzada direta com talisman-resposta-incidente-vazamento-revogacao-git-filter-repo.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
