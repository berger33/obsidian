---
id: software.seguranca.tranche10.000974
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

# `git-secrets` em Escala Corporativa: Configuração de **Templates Globais do Git (`init.templateDir`)** e Injeção Retroativa em Repositórios Existentes

## Em uma frase
Como o aviso em destaque no `README.rst` do `git-secrets` lembra: apenas instalar o binário `git-secrets` com `brew install git-secrets` ou `make install` **não protege nenhum repositório automaticamente** até que os hooks sejam instalados em `.git/hooks/`!

## Por que importa
Para automatizar 100% essa proteção na máquina de todos os engenheiros, combine o registro global de padrões (`git secrets --register-aws --global`) com o **Diretório de Templates Globais do Git (`init.templateDir`)**: ao rodar **`git secrets --install ~/.git-templates/git-secrets`** e **`git config --global init.templateDir ~/.git-templates/git-secrets`**, qualquer `git clone` ou `git init` futuro já nascerá com os três hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`) instalados!

## Como funciona
E para os repositórios que o desenvolvedor **já havia clonado antes** de configurar o `init.templateDir`? Conforme documenta o manual do Git citado pelo `git-secrets`, rodar `git init` (ou `git secrets --install -f <dir>`) dentro de um repositório já existente é totalmente seguro e copia os novos hooks do template sem apagar nenhum commit!

## Exemplo
```bash
# Configurar o template global do Git com git-secrets e instalar retroativamente em todos os repositorios locais de ~/projetos
git secrets --register-aws --global
git secrets --install ~/.git-templates/git-secrets
git config --global init.templateDir ~/.git-templates/git-secrets

find ~/projetos -name ".git" -type d -prune | while read -r gitdir; do
  git secrets --install -f "$(dirname "$gitdir")"
done
```

## Limites e trade-offs
O comando `find ... -name ".git"` acima resolve em 2 segundos o problema clássico de estações de trabalho veteranas: ele percorre todos os repositórios já clonados no disco do desenvolvedor e instala os hooks do `git-secrets` em cada um deles!

## Como verificar
Verifique em qualquer repositório clonado que os arquivos `.git/hooks/pre-commit`, `.git/hooks/commit-msg` e `.git/hooks/prepare-commit-msg` estão presentes e executáveis (`-rwxr-xr-x`).

## Conexões
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — Veja também: `git-secrets`: Adição de Padrões Proibidos (`--add`), Literais (`--literal`), Exceções (`.gitallowed` / `--allowed`) e **Secret Providers (`--add-provider`)**.
- [[gitsecrets-modos-varredura-scan-cached-untracked-no-index-history]] — Veja também: `git-secrets` Modos de Varredura: **`--scan`** (`--cached`, `--untracked`, `--no-index`, `-r`, `stdin`) vs **`--scan-history`** em Todo o Histórico Git.
- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — Referência cruzada direta com gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep.
- [[talisman-instalacao-global-git-template-framework-pre-commit-husky]] — Referência cruzada direta com talisman-instalacao-global-git-template-framework-pre-commit-husky.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
