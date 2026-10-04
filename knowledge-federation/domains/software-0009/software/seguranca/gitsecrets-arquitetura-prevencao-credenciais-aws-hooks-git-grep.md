---
id: software.seguranca.tranche10.000971
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

# **awslabs `git-secrets` (`awslabs/git-secrets`)**: Arquitetura dos **3 Hooks Git (`pre-commit`, `commit-msg`, `prepare-commit-msg`)** e Subcomando Nativo `git secrets`

## Em uma frase
Criado pela equipe de segurança da **Amazon Web Services (`awslabs/git-secrets`, licença Apache 2.0)**, o **`git-secrets`** é um utilitário leve e sem dependências externas pesadas (escrito em Bash POSIX integrado diretamente ao `git-sh-setup` e `git grep`) projetado para **impedir que credenciais da AWS e padrões proibidos entrem em um repositório Git**.

## Por que importa
O que diferencia o `git-secrets` de hooks que olham apenas os arquivos em *stage* (`pre-commit`)? Conforme mostra o código-fonte oficial `git-secrets`, ao rodar **`git secrets --install`**, ele instala **TRÊS hooks Git distintos**: **(1) `pre-commit`** (verifica todos os arquivos adicionados, copiados, modificados ou mesclados no índice `--cached` via `git diff-index --diff-filter 'ACMU'`); **(2) `commit-msg`** (verifica a **própria mensagem do commit**, impedindo que um desenvolvedor cole uma chave ou token na descrição do `git commit -m "..."`!); e **(3) `prepare-commit-msg`** (invocado em **merges non-fast-forward (`--no-ff`)**, inspecionando `git log destino..origem -p` para impedir que um merge traga histórico contaminado de outra branch!)!

## Como funciona
Por ser instalado no `$PATH` com o nome `git-secrets`, o próprio binário `git` o reconhece automaticamente como o subcomando nativo **`git secrets`**!

## Exemplo
```bash
# Instalar os 3 hooks do git-secrets (pre-commit, commit-msg, prepare-commit-msg) no repositorio atual e registrar padroes AWS
git secrets --install
git secrets --register-aws
git secrets --list
```

## Limites e trade-offs
Repare na importância do hook **`commit-msg`**: em muitos incidentes reais, desenvolvedores colam um comando `curl -H "Authorization: ..."` ou variáveis de ambiente no texto explicativo da mensagem de commit, onde scanners que só olham arquivos da árvore de trabalho nunca procuram!

## Como verificar
Se o repositório utilizar subdiretórios estilo Debian (`.git/hooks/pre-commit.d`), o `git secrets --install` detecta e instala os scripts automaticamente dentro desses diretórios.

## Conexões
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — Veja também: `git-secrets` **`--register-aws` & `--aws-provider`**: Detecção de Prefixos IAM (`AKIA`, `ASIA`, `AROA`), Chaves **Amazon Bedrock (`ABSK`)** e Leitura de `~/.aws/credentials`.
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — Referência cruzada direta com gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos.
- [[talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog]] — Referência cruzada direta com talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
