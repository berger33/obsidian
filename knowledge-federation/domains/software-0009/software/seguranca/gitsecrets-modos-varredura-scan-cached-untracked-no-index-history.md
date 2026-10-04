---
id: software.seguranca.tranche10.000975
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

# `git-secrets` Modos de Varredura: **`--scan`** (`--cached`, `--untracked`, `--no-index`, `-r`, `stdin`) vs **`--scan-history`** em Todo o Histórico Git

## Em uma frase
Além de atuar nos hooks de commit, o `git-secrets` possui cinco modos de varredura sob demanda para auditoria local e pipelines de CI/CD.

## Por que importa
Quando você executa **`git secrets --scan`** sem argumentos dentro de um repositório Git, ele usa internamente `LC_ALL=C git grep -nwHEI` para varrer ultrarrapidamente todos os arquivos rastreados (`git ls-files`). Você pode refinar o escopo de `--scan` com: **(1) `--cached`** (varre apenas os blobs registrados na área de stage / index); **(2) `--untracked`** (inclui também arquivos novos ainda não adicionados ao Git, como um arquivo `.bak` ou `.env` esquecido na pasta!); **(3) `--no-index`** ou **`-r <diretorio>`** (varre diretórios comuns fora do Git); e **(4) `-` (`stdin`)** (lê e audita um fluxo canalizado via pipe, ex.: `git diff | git secrets --scan -`)!

## Como funciona
E antes de tornar qualquer repositório privado em público (Open-Source) ou em auditorias de CI/CD, **`git secrets --scan-history`** usa `git log --all -G"<padroes>"` seguido de `git grep` sobre todas as revisões encontradas em todo o histórico!

## Exemplo
```bash
# Auditar simultaneamente arquivos rastreados e nao-rastreados (--untracked) e depois varrer todo o historico de revisoes (--scan-history)
git secrets --scan --untracked
git secrets --scan-history
```

## Limites e trade-offs
Olhe a inteligência de performance na função `scan_history()` do código-fonte do `git-secrets`: em vez de rodar `git grep` cegamente sobre cada um dos 50.000 commits de um repositório grande, ele primeiro filtra com **`git log --all -G"${combined_patterns}" --pretty=%H`** apenas os hashes de commits cujos diffs tocaram em algum padrão proibido e, só então, executa `git grep` nessas revisões específicas!

## Como verificar
Use `git secrets --scan -r /caminho/pasta` para auditar diretórios de artefatos de build ou pacotes extraídos que não possuem `.git`.

## Conexões
- [[gitsecrets-instalacao-hooks-locais-templates-globais-init-templatedir]] — Veja também: `git-secrets` em Escala Corporativa: Configuração de **Templates Globais do Git (`init.templateDir`)** e Injeção Retroativa em Repositórios Existentes.
- [[gitsecrets-protecao-env-local-secret-provider-dinamico-vazamento]] — Veja também: Técnica Avançada com `git-secrets`: Usando **`--add-provider`** para Garantir que Nenhum Valor do `.env` Local Seja Copiado para o Código.
- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — Referência cruzada direta com gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep.
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — Referência cruzada direta com gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
