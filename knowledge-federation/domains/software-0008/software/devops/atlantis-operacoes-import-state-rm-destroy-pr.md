---
id: software.devops.tranche10.000947
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

# Atlantis: importação de recursos (atlantis import), remoção de estado (state rm) e planos destrutivos (-destroy) via PR

## Em uma frase
Além de `plan` e `apply`, o Atlantis suporta importar recursos existentes para o estado do Terraform (**`atlantis import ADDRESS ID`**), gerenciar recursos no state e gerar planos de destruição controlada (**`atlantis plan -- -destroy`**) diretamente por comentários no Pull Request sem precisar de acesso local ao `.tfstate`.

## Por que importa
Em equipes que bloquearam o acesso de escrita direto ao bucket S3 do `.tfstate` a partir das máquinas dos desenvolvedores (permitindo escrita apenas pela IAM Role do servidor Atlantis), importar um recurso criado manualmente no console da nuvem exigiria abrir exceções de segurança se o Atlantis não tivesse suporte nativo ao comando `atlantis import`.

## Como funciona
Conforme documenta o README oficial (`Runs terraform plan, import, apply remotely`) e o guia `Using Atlantis`: (1) **`atlantis import [options] ADDRESS ID`**: o desenvolvedor adiciona o bloco `resource "..." "..."` no código `.tf` do Pull Request e comenta `atlantis import -d <dir> -w <workspace> aws_s3_bucket.logs meu-bucket-existente`; o Atlantis executa `terraform import` no workspace bloqueado e posta o resultado no PR; e (2) **Planos destrutivos (`-destroy`)**: comentar **`atlantis plan -d dir -- -destroy`** gera um plano de destruição (`destroy plan`) em `$PLANFILE` que, após revisão cuidadosa da equipe no comentário do PR, pode ser efetivado com `atlantis apply -d dir`.

## Exemplo
```text
# Importar um recurso existente para o estado do Terraform pelo PR e rodar um novo plano para confirmar zero diffs
atlantis import -d infra/storage -w production aws_s3_bucket.audit_logs empresa-audit-logs-prod
atlantis plan -d infra/storage -w production
```

## Limites e trade-offs
Como o comando `atlantis import` altera imediatamente o arquivo `.tfstate` remoto adicionando o recurso importado antes mesmo do `atlantis apply`, após rodar `atlantis import` com sucesso execute sempre um `atlantis plan` em seguida no mesmo PR para verificar que o código `.tf` escrito no PR corresponde exatamente aos atributos do recurso importado na nuvem e faça o merge do PR.

## Como verificar
Após executar `atlantis import ADDRESS ID` no comentário do PR, rode `atlantis plan` no mesmo projeto e confirme que o plano reporta `No changes. Your infrastructure matches the configuration`.

## Conexões
- [[atlantis-automerge-apply-requirements-protecao-branches]] — Veja também: Atlantis: Automerging de Pull Requests, método de merge (--auto-merge-method) e requisito undiverged.
- [[atlantis-verificacao-politicas-policy-checking-conftest-opa]] — Veja também: Atlantis: avaliação automatizada de políticas sobre planos Terraform (Policy Checking com Conftest / OPA Rego).
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-comandos-pull-request-plan-apply-flags-workspaces]] — Referência cruzada direta com atlantis-comandos-pull-request-plan-apply-flags-workspaces.
- [[atlantis-bloqueio-diretorio-workspace-locking-unlock]] — Referência cruzada direta com atlantis-bloqueio-diretorio-workspace-locking-unlock.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/locking.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
