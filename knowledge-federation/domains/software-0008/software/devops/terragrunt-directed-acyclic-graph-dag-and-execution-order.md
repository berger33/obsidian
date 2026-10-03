---
id: software.devops.tranche04.000396
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

# Grafo Acíclico Direcionado (DAG) no Terragrunt para ordenação automática de runs na stack

## Em uma frase
O Quick Start oficial explica que o Terragrunt constrói um **Directed Acyclic Graph (DAG — Grafo Acíclico Direcionado)** que representa os relacionamentos de dependência entre todas as unidades da stack. Quando o usuário executa um comando em toda a stack (como `terragrunt run --all plan` ou `apply`), o Terragrunt analisa o DAG para determinar exatamente a ordem dos grupos de execução (`Group 1`, `Group 2`, etc.), garantindo que as unidades das quais outras dependem sejam processadas primeiro e que suas saídas (`outputs`) estejam prontas antes de iniciar as unidades dependentes.

## Por que importa
Em uma infraestrutura real onde o cluster EKS/Kubernetes (`bar`) depende da VPC e das sub-redes (`foo`), tentar aplicar o cluster antes da rede falha imediatamente, e tentar destruir a rede antes do cluster trava por recursos em uso. O DAG resolve automaticamente a ordem de criação e a ordem reversa de destruição.

## Como funciona
Declare explicitamente as relações entre unidades no `terragrunt.hcl` (usando `dependency` quando precisar consumir outputs ou `dependencies` quando precisar apenas de ordenação) para que o DAG do Terragrunt orquestre os grupos de execução sem scripts externos.

## Exemplo
Quando a unidade `bar` declara dependência da unidade `foo`, a saída de `terragrunt run --all plan` mostra `Group 1: - Module ./foo` seguido de `Group 2: - Module ./bar`, provando que o DAG escalonou `foo` antes de `bar`.

## Limites e trade-offs
Nunca crie dependências circulares entre duas unidades (por exemplo, `foo` dependendo de `bar` e `bar` dependendo de `foo`), pois isso viola a propriedade acíclica do DAG e impede o Terragrunt de calcular uma ordem válida de execução.

## Como verificar
Inspecione o cabeçalho `The stack at . will be processed in the following order` ao rodar `terragrunt run --all plan` e confirme que os grupos refletem fielmente a topologia de dependências.

## Conexões
- [[terragrunt-stacks-and-concurrent-run-all-execution]] — Veja também: Gerenciamento de Stacks e execução concorrente com terragrunt run --all e --non-interactive.
- [[terragrunt-dependency-blocks-and-dynamic-cross-unit-inputs]] — Veja também: Passagem dinâmica de outputs entre unidades com o bloco dependency no Terragrunt.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
