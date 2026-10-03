---
id: software.devops.tranche04.000399
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md", "https://docs.terragrunt.com/getting-started/quick-start/", "https://github.com/gruntwork-io/terragrunt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Automação GitOps em CI/CD (plan no PR e apply no merge) e Terragrunt Scale

## Em uma frase
O passo 8 do Quick Start oficial enfatiza que, assim que infraestrutura real e mais de um engenheiro estão envolvidos, as operações do Terragrunt devem deixar de ser executadas manualmente em laptops e passar a rodar em **pipelines de CI/CD**: isso coloca um `plan` revisável em cada pull request, torna a branch `main` a fonte única da verdade para o que está implantado e permite que os jobs de CI autentiquem-se com **credenciais de curta duração** (short-lived credentials) em vez de chaves permanentes em máquinas locais. Para acelerar essa adoção, a Gruntwork disponibiliza o **Terragrunt Scale** (`docs.terragrunt.com/terragrunt-scale/`) e o guia oficial *Continuous Integration with Terragrunt* (`docs.terragrunt.com/guides/ci-with-terragrunt/`), que configuram fluxos de plan-on-pull-request e apply-on-merge dentro do próprio GitHub Actions ou GitLab CI respeitando o DAG da stack.

## Por que importa
Executar `terragrunt apply` a partir de máquinas de desenvolvedores com credenciais administrativas de longa duração impede revisão por pares do plano de execução e cria risco de conflitos concorrentes e vazamento de chaves.

## Como funciona
Configure seus pipelines no GitHub Actions ou GitLab CI para autenticar via OIDC com credenciais efêmeras, executar `terragrunt run --all plan` automaticamente em cada pull request e executar `terragrunt run --all --non-interactive apply` apenas após o merge na branch principal.

## Exemplo
Quando um engenheiro abre um PR alterando um módulo compartilhado e duas unidades em `staging`, o workflow no GitHub Actions assume uma role temporária via OIDC, calcula o DAG da stack e publica o resultado do `plan` no PR; após aprovação e merge, o pipeline aplica as unidades na ordem do DAG.

## Limites e trade-offs
Nunca armazene chaves estáticas de longa duração (`AWS_SECRET_ACCESS_KEY`) nos runners ou laptops para rodar o Terragrunt em produção; utilize federação de identidade OIDC com credenciais de curta duração nos jobs de CI.

## Como verificar
Valide no pipeline de CI que qualquer alteração em arquivos `.tf` ou `terragrunt.hcl` dispara automaticamente o plano em ordem de DAG no PR antes de permitir o merge.

## Conexões
- [[terragrunt-unapplied-dependencies-and-mock-outputs-in-plan]] — Veja também: Tratamento de dependências ainda não aplicadas durante o plan com mock_outputs e mock_outputs_allowed_terraform_commands.
- [[terragrunt-documentation-fixtures-and-incremental-adoption]] — Veja também: Adoção incremental do Terragrunt e uso das fixtures oficiais test/fixtures/docs/01-quick-start.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
