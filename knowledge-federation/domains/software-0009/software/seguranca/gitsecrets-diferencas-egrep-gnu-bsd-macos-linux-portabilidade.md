---
id: software.seguranca.tranche10.000977
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

# Portabilidade de Expressões Regulares no `git-secrets`: Diferenças entre **GNU `grep -E` (Linux)** e **BSD `grep -E` (macOS)** e Boas Práticas POSIX ERE

## Em uma frase
A documentação oficial do `git-secrets` (seção `Defining prohibited patterns`) destaca uma armadilha técnica importante para equipes onde parte dos desenvolvedores trabalha em **macOS** e parte trabalha em **Linux (Ubuntu/Debian/Fedora)** (ou onde o CI/CD roda em containers Linux): o `git-secrets` delega a avaliação das expressões regulares para o `grep -E` / `git grep -E` nativo do sistema operacional!

## Por que importa
No **Linux (GNU grep)**, extensões como `\s` (espaço em branco), `\w` (caractere de palavra) ou `\d` funcionam em `grep -E`, mas em implementações estritas de **POSIX Extended Regular Expressions (ERE)** ou variações de **BSD `egrep` (macOS)**, sequências PCRE como `\d` ou certos escapes podem se comportar de forma diferente e **deixar um segredo passar em branco no macOS enquanto falha no Linux (ou vice-versa)**!

## Como funciona
Por isso, ao escrever padrões em `git secrets --add` ou no arquivo `.gitallowed`, prefira sempre **Classes de Caracteres POSIX ERE Padrão**: use **`[0-9]`** em vez de `\d`, **`[ \t]`** (ou a classe POSIX `[:space:]`) em vez de `\s`, e **`[A-Za-z0-9_]`** em vez de `\w`!

## Exemplo
```bash
# Escrever padroes 100% portaveis entre macOS (BSD grep) e Linux (GNU grep) usando classes POSIX ERE padrao
git secrets --add 'api_key[ 	]*[:=][ 	]*["'\'']?[A-Za-z0-9_\-]{32,}["'\'']?'
git secrets --scan test/fixtures/sample_config.yaml
```

## Limites e trade-offs
Sempre que adicionar um novo padrão com `git secrets --add` ou uma nova regra de exceção no `.gitallowed`, teste-o imediatamente contra um arquivo de exemplo usando **`git secrets --scan <arquivo>`** tanto em macOS quanto em Linux antes de distribuir para a equipe.

## Como verificar
Observe no código-fonte de `git-secrets` que ele já força `GREP_OPTIONS= LC_ALL=C` em todas as chamadas de `grep`/`git grep` para garantir ordenação de ranges ASCII determinística (`[A-Z]`).

## Conexões
- [[gitsecrets-protecao-env-local-secret-provider-dinamico-vazamento]] — Veja também: Técnica Avançada com `git-secrets`: Usando **`--add-provider`** para Garantir que Nenhum Valor do `.env` Local Seja Copiado para o Código.
- [[gitsecrets-bloqueio-merges-contaminados-prepare-commit-msg-no-ff]] — Veja também: Como o Hook **`prepare-commit-msg`** do `git-secrets` Impede que um **Merge (`--no-ff`)** Contamine a Branch Principal com Histórico Sujo.
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — Referência cruzada direta com gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos.
- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — Referência cruzada direta com gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
