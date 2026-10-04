---
id: software.devops.tranche10.000948
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

# Atlantis: avaliação automatizada de políticas sobre planos Terraform (Policy Checking com Conftest / OPA Rego)

## Em uma frase
O recurso de **Policy Checking** do Atlantis executa o **Conftest** (Open Policy Agent / Rego) contra o arquivo JSON do plano gerado pelo `terraform show -json $PLANFILE`, bloqueando o `atlantis apply` até que todas as políticas passem ou que um revisor autorizado emita `atlantis approve_policies`.

## Por que importa
Revisão humana de planos Terraform de 500 linhas em comentários de PR frequentemente deixa passar erros de conformidade (como um bucket S3 público, um Security Group abrindo `0.0.0.0/0` na porta 22 ou ausência de tags obrigatórias de centro de custo). Integrar Policy Checking no próprio fluxo do Atlantis transforma políticas Rego em um gate obrigatório antes do `apply`.

## Como funciona
Quando `--enable-policy-checks` está habilitado no servidor Atlantis e conjuntos de políticas (`policy_sets` do Conftest/OPA) estão configurados no `repos.yaml`: (1) logo após o estágio `plan` gerar o `$PLANFILE`, o Atlantis converte o plano binário para JSON (`$SHOWFILE`) e executa o estágio **`policy_check`** rodando `conftest test`; (2) o resultado da avaliação das políticas é comentado no PR ao lado do plano; e (3) se `policy_check` estiver em `apply_requirements` e alguma política falhar, o `atlantis apply` é bloqueado a menos que o código seja corrigido ou que um membro da equipe listada em `owners` aprove explicitamente a exceção com **`atlantis approve_policies`**.

## Exemplo
```text
# Aprovar excepcionalmente um plano que falhou em uma política não-bloqueante (exige usuário listado em owners do policy_set)
atlantis approve_policies -d envs/staging/network -w staging
```

## Limites e trade-offs
Como um novo `atlantis plan` invalida aprovações anteriores, qualquer execução de `atlantis approve_policies` vale exclusivamente para o plano atual; se um novo commit for enviado ao PR ou um novo `atlantis plan` for rodado, as políticas serão reavaliadas do zero.

## Como verificar
Adicione `policy_check` na lista `apply_requirements` do `repos.yaml` e verifique no comentário do PR a seção `Policy Check Results` gerada após cada `atlantis plan`.

## Conexões
- [[atlantis-operacoes-import-state-rm-destroy-pr]] — Veja também: Atlantis: importação de recursos (atlantis import), remoção de estado (state rm) e planos destrutivos (-destroy) via PR.
- [[atlantis-seguranca-webhooks-segredos-autenticacao-implantacao]] — Veja também: Atlantis: modelo de segurança do servidor, proteção contra PRs maliciosos, Drift Detection API e implantação em Kubernetes.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-workflows-customizados-repos-yaml-server-side]] — Referência cruzada direta com atlantis-workflows-customizados-repos-yaml-server-side.
- [[infracost-politicas-finops-tagging-guardrails-orcamentos]] — Referência cruzada direta com infracost-politicas-finops-tagging-guardrails-orcamentos.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/how-atlantis-works.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
