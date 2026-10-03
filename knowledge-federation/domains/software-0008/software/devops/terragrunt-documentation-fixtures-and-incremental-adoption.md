---
id: software.devops.tranche04.000400
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

# Adoção incremental do Terragrunt e uso das fixtures oficiais test/fixtures/docs/01-quick-start

## Em uma frase
O Quick Start oficial destaca que todas as etapas do tutorial possuem exemplos completos e prontos para execução disponíveis no repositório oficial em **`github.com/gruntwork-io/terragrunt/tree/main/test/fixtures/docs/01-quick-start`**, e recomenda uma estratégia de **adoção incremental**: começar pequeno (por exemplo, adicionando `terragrunt.hcl` para aproveitar o Auto-init e gerenciamento de unidades simples) e introduzir gradualmente recursos mais avançados como módulos compartilhados, blocos `inputs`, stacks com `run --all`, DAG de dependências com `dependency`/`mock_outputs` e automação de CI/CD.

## Por que importa
Tentar reescrever de uma só vez toda a árvore de repositórios Terraform de uma empresa para usar todos os recursos avançados do Terragrunt simultaneamente gera resistência da equipe e alto risco operacional. A adoção gradual preserva a estabilidade enquanto reduz o boilerplate passo a passo.

## Como funciona
Use as fixtures oficiais de `test/fixtures/docs/01-quick-start` como referência de estrutura de diretórios ao treinar a equipe e migre um ambiente não produtivo primeiro (de `terragrunt.hcl` básico até stacks com DAG completo) antes de expandir o padrão.

## Exemplo
Para capacitar uma equipe que operava dezenas de pastas Terraform independentes, o arquiteto reproduz localmente os passos de `test/fixtures/docs/01-quick-start` usando apenas o provedor `hashicorp/local` (sem precisar de conta de nuvem) e em seguida guia a migração incremental do ambiente de desenvolvimento.

## Limites e trade-offs
Evite criar hierarquias excessivamente profundas e complexas logo no primeiro dia de uso do Terragrunt; consulte a página oficial de *Terminology* (`docs.terragrunt.com/getting-started/terminology/`) para alinhar os conceitos de *unit* e *stack* na equipe.

## Como verificar
Reproduza localmente a estrutura de duas unidades (`foo` e `bar`) com módulo compartilhado (`shared`) e dependência DAG das fixtures do Quick Start e confirme que `terragrunt run --all apply` converge sem erros.

## Conexões
- [[terragrunt-ci-cd-gitops-workflows-and-terragrunt-scale]] — Veja também: Automação GitOps em CI/CD (plan no PR e apply no merge) e Terragrunt Scale.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
