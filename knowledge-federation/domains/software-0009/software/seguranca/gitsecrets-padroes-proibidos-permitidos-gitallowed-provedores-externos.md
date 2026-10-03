---
id: software.seguranca.tranche10.000973
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

# `git-secrets`: Adição de Padrões Proibidos (`--add`), Literais (`--literal`), Exceções (`.gitallowed` / `--allowed`) e **Secret Providers (`--add-provider`)**

## Em uma frase
Para proteger credenciais de outros provedores além da AWS (como tokens internos, chaves do GCP/Azure, strings de conexão PostgreSQL/MongoDB ou senhas corporativas), o `git-secrets` oferece três mecanismos de extensão.

## Por que importa
Primeiro, **`git secrets --add '<regex>'`** (com `--global` para aplicar a todos os repositórios da máquina, ou **`-l` / `--literal`** quando você quer buscar uma string exata escapando caracteres especiais como `+` ou `.`). Segundo, **`git secrets --add --allowed '<regex>'`** — ou, melhor ainda para compartilhar com toda a equipe via Git, o arquivo **`.gitallowed`** na raiz do repositório!

## Como funciona
E terceiro, **`git secrets --add-provider -- <comando> [args]`**: um **Secret Provider** é qualquer executável ou script que, ao ser invocado pelo `git-secrets`, imprime no `stdout` uma lista de padrões ou segredos proibidos separados por quebra de linha (permitindo buscar padrões atualizados de um repositório corporativo central ou ler arquivos locais `.env` para garantir que nenhum valor do `.env` seja copiado para arquivos rastreados pelo Git!)!

## Exemplo
```bash
# Adicionar padroes proibidos para chaves privadas PEM, strings de conexao com senha e um provedor de arquivo central
git secrets --add --global '-----BEGIN (RSA|EC|DSA|OPENSSH|PGP|PRIVATE) KEY'
git secrets --add --global '(postgres|mysql|mongodb|redis)://[^:]+:[^@]+@'
git secrets --add-provider -- cat /etc/secops/prohibited-corporate-patterns.txt
```

## Limites e trade-offs
Como funciona exatamente o algoritmo de filtragem de falsos positivos (`process_output` no código-fonte de `git-secrets`)? Primeiro, ele extrai todas as linhas no formato `arquivo:linha:conteudo` que casaram com algum padrão proibido; depois, ele passa essas linhas por `grep -Ev "${allowed}"` (combinando `secrets.allowed` do `git config` com as linhas não-comentadas do arquivo **`.gitallowed`**): o commit só é aprovado se **todas** as linhas suspeitas forem explicitamente canceladas por um padrão permitido!

## Como verificar
Nota técnica importante: se o padrão permitido em `.gitallowed` incluir o prefixo `caminho/do/arquivo.ext:numero_linha:` (ou `caminho/do/arquivo.ext:.*padrao`), você restringe a exceção apenas àquele arquivo específico!

## Conexões
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — Veja também: `git-secrets` **`--register-aws` & `--aws-provider`**: Detecção de Prefixos IAM (`AKIA`, `ASIA`, `AROA`), Chaves **Amazon Bedrock (`ABSK`)** e Leitura de `~/.aws/credentials`.
- [[gitsecrets-instalacao-hooks-locais-templates-globais-init-templatedir]] — Veja também: `git-secrets` em Escala Corporativa: Configuração de **Templates Globais do Git (`init.templateDir`)** e Injeção Retroativa em Repositórios Existentes.
- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — Referência cruzada direta com gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep.
- [[gitsecrets-modos-varredura-scan-cached-untracked-no-index-history]] — Referência cruzada direta com gitsecrets-modos-varredura-scan-cached-untracked-no-index-history.
- [[talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity]] — Referência cruzada direta com talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
