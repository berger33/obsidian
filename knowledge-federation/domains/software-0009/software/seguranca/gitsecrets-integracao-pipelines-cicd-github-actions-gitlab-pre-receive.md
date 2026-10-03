---
id: software.seguranca.tranche10.000979
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

# Implantação de `git-secrets` em **Pipelines CI/CD** e **Hooks Server-Side (`pre-receive`)** para Impedir Bypass com `git commit --no-verify`

## Em uma frase
Por que nenhum controle de segurança executado apenas no cliente (`pre-commit`, `commit-msg`, `prepare-commit-msg`) pode ser considerado uma barreira de segurança definitiva sozinho? Porque no Git qualquer desenvolvedor pode passar a flag **`git commit --no-verify` (ou `-n`)**, que instrui o Git a pular 100% dos hooks locais da pasta `.git/hooks/`!

## Por que importa
Para tornar a política do `git-secrets` **incontornável**, replique a mesma configuração (`git secrets --register-aws` + padrões corporativos + `.gitallowed`) em dois pontos do servidor: **(1) Em um Hook `pre-receive` no servidor Git autohospedado (GitLab Self-Managed / Gitea / Gerrit)**, que rejeita o `git push` de forma síncrona antes que os commits sejam aceitos no repositório central; e **(2) Em um Job Obrigatório de Branch Protection no CI/CD (`git secrets --scan-history` ou range do PR)**!

## Como funciona
Como o `git-secrets` é apenas um script Bash que usa `git grep`, ele roda em menos de 1 segundo em qualquer container Linux de CI/CD!

## Exemplo
```bash
# Em um pipeline de CI/CD: configurar os padroes do git-secrets e auditar todos os commits introduzidos pelo Pull Request
git secrets --register-aws
git secrets --add '(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}'
git log "${BASE_SHA}..${HEAD_SHA}" -p | git secrets --scan -
```

## Limites e trade-offs
Ao manter o arquivo **`.gitallowed`** versionado na raiz do repositório e protegido pelo `.github/CODEOWNERS` do time de Segurança, tanto o `git secrets` na máquina do desenvolvedor quanto o `git secrets` no pipeline de CI/CD aplicarão exatamente a mesma lista de exceções auditadas!

## Como verificar
Combine o `git-secrets` no CI/CD com o **Gitleaks** e o **TruffleHog** para cobrir mais de 800 provedores SaaS além da AWS.

## Conexões
- [[gitsecrets-bloqueio-merges-contaminados-prepare-commit-msg-no-ff]] — Veja também: Como o Hook **`prepare-commit-msg`** do `git-secrets` Impede que um **Merge (`--no-ff`)** Contamine a Branch Principal com Histórico Sujo.
- [[gitsecrets-eliminacao-credenciais-estaticas-aws-oidc-sso-iam-roles]] — Veja também: Além do `git-secrets`: Como Eliminar 100% as Chaves Estáticas `AKIA...` nas Estações e no CI/CD com **AWS IAM Identity Center (SSO)** e **OIDC Federation**.
- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — Referência cruzada direta com gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep.
- [[talisman-auditoria-seguranca-talismanrc-codeowners-bypass-detection]] — Referência cruzada direta com talisman-auditoria-seguranca-talismanrc-codeowners-bypass-detection.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
