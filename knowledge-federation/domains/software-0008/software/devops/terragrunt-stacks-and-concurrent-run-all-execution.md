---
id: software.devops.tranche04.000395
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

# Gerenciamento de Stacks e execução concorrente com terragrunt run --all e --non-interactive

## Em uma frase
No contexto do Terragrunt, uma **stack (pilha)** é uma coleção de unidades que são gerenciadas em conjunto — representando, por exemplo, um ambiente inteiro (`dev`, `staging`, `prod`) ou um projeto completo. Executando **`terragrunt run --all apply`** (ou `plan`) no diretório pai acima das unidades, o Terragrunt descobre todas as unidades da stack, exibe os grupos de execução planejados, pede confirmação interativa para comandos potencialmente destrutivos (que pode ser suprimida em automações com a flag **`--non-interactive`**) e executa os comandos **concorrentemente** nas unidades independentes, prefixando cada linha de log com o nome da unidade (como `[foo]` e `[bar]`).

## Por que importa
Atualizar 30 unidades de um ambiente entrando pasta por pasta manualmente é lento e propenso a esquecimentos. O comando `terragrunt run --all` paraleliza a execução das unidades independentes e desambigua os logs de cada módulo no terminal.

## Como funciona
Em pipelines de CI/CD ou operações de ambiente, utilize `terragrunt run --all plan` para revisar mudanças de toda a stack e `terragrunt run --all --non-interactive apply` para aplicar alterações de forma automatizada sem travar em prompts interativos.

## Exemplo
No diretório raiz que contém as unidades `foo` e `bar`, o operador executa `terragrunt run --all --non-interactive apply`; o Terragrunt agrupa ambas no `Group 1`, executa o `apply` em paralelo e exibe os logs identificados por `[foo] tofu:` e `[bar] tofu:`.

## Limites e trade-offs
Cuidado ao executar `terragrunt run --all destroy` ou `apply` a partir do diretório raiz errado do repositório; revise sempre a lista de módulos (`Group 1`, `Group 2`...) exibida pelo Terragrunt antes de confirmar a operação interativa.

## Como verificar
Execute `terragrunt run --all plan` no diretório pai de múltiplas unidades de teste e confirme a exibição dos grupos de processamento e dos logs prefixados por unidade.

## Conexões
- [[terragrunt-terragrunt-cache-scratch-directory-and-get-terragrunt-dir]] — Veja também: Funcionamento do diretório .terragrunt-cache e uso da função built-in get_terragrunt_dir().
- [[terragrunt-directed-acyclic-graph-dag-and-execution-order]] — Veja também: Grafo Acíclico Direcionado (DAG) no Terragrunt para ordenação automática de runs na stack.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
