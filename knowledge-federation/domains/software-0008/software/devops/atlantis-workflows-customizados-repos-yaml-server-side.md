---
id: software.devops.tranche10.000945
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

# Atlantis: configuração server-side (repos.yaml), restrição de allowed_overrides e Custom Workflows ($PLANFILE)

## Em uma frase
Para governança centralizada de segurança, o administrador do servidor Atlantis utiliza a configuração server-side (**`repos.yaml`** / `--repo-config`) para definir requisitos de aprovação (`apply_requirements`), controlar quais chaves o `atlantis.yaml` do repositório pode sobrescrever (`allowed_overrides`) e definir **Custom Workflows** usando `$PLANFILE`.

## Por que importa
Se qualquer desenvolvedor puder editar o `atlantis.yaml` dentro da branch do seu próprio Pull Request para definir um workflow customizado que executa `curl | bash` ou desabilita requisitos de aprovação antes do `apply`, um PR não revisado poderia exfiltrar as credenciais de nuvem do servidor Atlantis.

## Como funciona
O arquivo server-side **`repos.yaml`** (montado no servidor Atlantis via `--repo-config=repos.yaml`) define políticas por repositório (`id: /.*/` ou `id: github.com/minha-org/infra`): (1) **`apply_requirements: [approved, mergeable, undiverged]`**: exige que o PR esteja aprovado no Git, sem conflitos de merge e atualizado com a branch base antes de aceitar `atlantis apply`; (2) **`allowed_overrides`**: restringe exatamente o que o `atlantis.yaml` do repositório pode customizar; e (3) **`workflows`**: permite customizar os estágios `plan` e `apply` (ex.: rodar Terragrunt, OpenTofu, TFLint ou scripts de preparação), onde o passo de plano **deve** gravar o arquivo de saída na variável de ambiente **`$PLANFILE`** (ex.: `terraform plan -out $PLANFILE`) para que os comandos do Atlantis funcionem.

## Exemplo
```yaml
# Exemplo de repos.yaml server-side exigindo PR aprovado, mergeable e atualizado antes de permitir atlantis apply
repos:
  - id: /.*/
    branch: /^main$/
    apply_requirements: [approved, mergeable, undiverged]
    allowed_overrides: [workflow, apply_requirements]
    allow_custom_workflows: false
```

## Limites e trade-offs
Como o comando `atlantis plan` roda automaticamente assim que um Pull Request é aberto (antes mesmo de qualquer revisor humano ter aprovado o código do PR!), nunca habilite `allow_custom_workflows: true` no `repos.yaml` nem permita que PRs não confiáveis executem código arbitrário durante o `plan` (como providers maliciosos ou `external` data sources sem revisão) em servidores Atlantis com credenciais de produção.

## Como verificar
Com `apply_requirements: [approved, mergeable]` configurado no `repos.yaml`, tente comentar `atlantis apply` em um PR ainda não aprovado no GitHub/GitLab e confirme que o Atlantis bloqueia a execução.

## Conexões
- [[atlantis-configuracao-repositorio-atlantis-yaml-autoplan-when-modified]] — Veja também: Atlantis: configuração de projetos no repositório com atlantis.yaml (projects, workspace, autoplan e when_modified).
- [[atlantis-automerge-apply-requirements-protecao-branches]] — Veja também: Atlantis: Automerging de Pull Requests, método de merge (--auto-merge-method) e requisito undiverged.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-verificacao-politicas-policy-checking-conftest-opa]] — Referência cruzada direta com atlantis-verificacao-politicas-policy-checking-conftest-opa.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/how-atlantis-works.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
