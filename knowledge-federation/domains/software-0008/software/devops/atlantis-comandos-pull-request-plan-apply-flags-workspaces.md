---
id: software.devops.tranche10.000942
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
fontes: ["https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md", "https://www.runatlantis.io/docs/using-atlantis.html", "https://www.runatlantis.io/docs/locking.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Atlantis: comandos de comentário em PR (atlantis plan e apply), seleção de projeto (-d, -p, -w) e arquivos env/{workspace}.tfvars

## Em uma frase
Conforme documenta a página oficial `Using Atlantis` (`runatlantis.io/docs/using-atlantis.html`), os comentários `atlantis plan` e `atlantis apply` aceitam filtros por diretório (`-d`), projeto (`-p`) e workspace (`-w`), flags extras do Terraform após `--` e carregam automaticamente arquivos `env/{workspace}.tfvars`.

## Por que importa
Em um repositório Git que contém múltiplos diretórios Terraform ou utiliza múltiplos workspaces (`default`, `staging`, `production`), os engenheiros precisam saber como planejar e aplicar um único projeto/workspace específico, passar variáveis pontuais (`-target` ou `-destroy`) e organizar variáveis por ambiente sem repetição manual de `-var-file`.

## Como funciona
Nos comentários do Pull Request: (1) **`atlantis plan`** (sem flags) roda o plano para todos os projetos modificados no PR, enquanto **`atlantis plan -d <dir> -w <workspace>`** ou **`atlantis plan -p <project>`** planeja apenas o alvo especificado; (2) **Automatic Environment Variable Files**: ao rodar `atlantis plan` para um workspace `<workspace>`, o Atlantis verifica automaticamente se existe o arquivo **`env/{workspace}.tfvars`** relativo ao diretório do projeto (ex.: `env/default.tfvars`, `env/staging.tfvars`, `env/production.tfvars`) e o inclui automaticamente via `-var-file`; (3) **Flags extras do Terraform**: qualquer argumento após `--` é repassado ao Terraform (ex.: `atlantis plan -d dir -- -var foo='bar'` ou `atlantis plan -- -destroy`); e (4) **`atlantis apply`** (sem flags) aplica **todos os planos ainda não aplicados daquele PR**.

## Exemplo
```text
# Planejar e aplicar um workspace específico (carregando automaticamente env/staging.tfvars) ou passar flags extras após --
atlantis plan -d infra/network -w staging
atlantis plan -d infra/network -- -target=aws_security_group.web
atlantis apply -d infra/network -w staging
```

## Limites e trade-offs
Conforme alerta uma nota importante na documentação oficial `Using Atlantis`, executar um **`atlantis plan` sem flags** (assim como um autoplan disparado por novo commit) **descarta todos os planos criados anteriormente com flags manuais `-p` / `-d` / `-w`** naquele PR; portanto, se você planeja múltiplos workspaces manualmente com `-w staging` e `-w production`, aplique-os antes de rodar um `atlantis plan` geral sem flags.

## Como verificar
Crie a pasta `env/staging.tfvars` dentro de um diretório de projeto Terraform e comente `atlantis plan -w staging` no PR, verificando na saída comentada pelo Atlantis a inclusão automática de `-var-file=env/staging.tfvars`.

## Conexões
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Veja também: Atlantis: automação self-hosted de fluxos Terraform em Pull Requests via webhooks.
- [[atlantis-bloqueio-diretorio-workspace-locking-unlock]] — Veja também: Atlantis: sistema de Locking por diretório e workspace, Global Apply Lock e relação com o Terraform State Lock.
- [[atlantis-configuracao-repositorio-atlantis-yaml-autoplan-when-modified]] — Referência cruzada direta com atlantis-configuracao-repositorio-atlantis-yaml-autoplan-when-modified.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/locking.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
