---
id: software.devops.tranche10.000944
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
fontes: ["https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md", "https://www.runatlantis.io/docs/using-atlantis.html", "https://www.runatlantis.io/docs/how-atlantis-works.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Atlantis: configuração de projetos no repositório com atlantis.yaml (projects, workspace, autoplan e when_modified)

## Em uma frase
O arquivo **`atlantis.yaml`** (`version: 3`) na raiz do repositório permite declarar explicitamente cada projeto Terraform (`projects:`), seu diretório (`dir`), seu `workspace`, o `workflow` customizado e as regras de **`autoplan.when_modified`** para disparar planos quando módulos compartilhados são alterados.

## Por que importa
Por padrão, sem um `atlantis.yaml`, o Atlantis detecta projetos apenas no diretório exato onde um arquivo `.tf` foi modificado; porém, se um repositório possui módulos compartilhados em `modules/vpc/` consumidos por `envs/staging/` e `envs/prod/`, alterar um arquivo em `modules/vpc/` precisa disparar automaticamente o `plan` nos diretórios `envs/staging` e `envs/prod`.

## Como funciona
No arquivo **`atlantis.yaml`** (`version: 3`), a lista **`projects:`** define cada unidade de execução com: (1) **`name`**: nome único do projeto para uso com `atlantis plan -p <name>` e `atlantis apply -p <name>`; (2) **`dir`**: diretório relativo à raiz do repositório; (3) **`workspace`**: workspace do Terraform (permitindo declarar múltiplos projetos apontando para o mesmo `dir` com `workspace`s diferentes!); (4) **`terraform_version`**: fixa a versão exata do binário Terraform para aquele projeto; e (5) **`autoplan`**: define `enabled: true` e a lista de globs **`when_modified`** (ex.: `["*.tf", "*.tfvars", "../../modules/**/*.tf"]`) que disparam o plano automático quando alterados em um PR.

## Exemplo
```yaml
# Exemplo de arquivo atlantis.yaml (version 3) definindo projetos por ambiente e rastreamento de módulos compartilhados
version: 3
automerge: false
parallel_plan: true
parallel_apply: false
projects:
  - name: network-staging
    dir: envs/staging/network
    workspace: staging
    terraform_version: v1.9.5
    autoplan:
      when_modified: ["*.tf", "*.tfvars", "../../../modules/vpc/*.tf"]
      enabled: true
```

## Limites e trade-offs
Conforme documenta `Using Atlantis`, quando um projeto é referenciado pelo nome configurado no `atlantis.yaml` via flag **`-p <project>`** (`atlantis plan -p network-staging`), você **não pode** passar simultaneamente as flags `-d` ou `-w`, pois o projeto no `atlantis.yaml` já define fixamente seu diretório e seu workspace.

## Como verificar
Abra um Pull Request alterando um arquivo em `modules/vpc/` listado em `when_modified` do `atlantis.yaml` e confirme que o Atlantis dispara automaticamente o `plan` para os projetos dependentes.

## Conexões
- [[atlantis-bloqueio-diretorio-workspace-locking-unlock]] — Veja também: Atlantis: sistema de Locking por diretório e workspace, Global Apply Lock e relação com o Terraform State Lock.
- [[atlantis-workflows-customizados-repos-yaml-server-side]] — Veja também: Atlantis: configuração server-side (repos.yaml), restrição de allowed_overrides e Custom Workflows ($PLANFILE).
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-comandos-pull-request-plan-apply-flags-workspaces]] — Referência cruzada direta com atlantis-comandos-pull-request-plan-apply-flags-workspaces.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/how-atlantis-works.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
