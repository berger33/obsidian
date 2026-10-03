---
id: software.devops.tranche04.000393
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

# Unidades (units), módulos compartilhados e eliminação de main.tf redundantes com blocos terraform e inputs

## Em uma frase
Na terminologia oficial do Terragrunt, uma **unidade ("unit")** é um diretório que contém um arquivo `terragrunt.hcl` e representa uma única peça de infraestrutura — equivalente a uma instância de um módulo OpenTofu/Terraform. Em vez de duplicar arquivos `main.tf` e declarações `variable` em cada diretório de unidade (`foo` e `bar`) apenas para instanciar um módulo compartilhado (`../shared`), o Terragrunt permite remover completamente os arquivos `main.tf` das unidades e declarar diretamente no `terragrunt.hcl` o bloco **`terraform { source = "../shared" }`** junto com o atributo **`inputs = { ... }`** para passar os valores das variáveis daquela unidade.

## Por que importa
Manter arquivos `main.tf`, `variables.tf` e `terraform.tfvars` repetidos em dezenas de diretórios de ambiente gera centenas de linhas de código boilerplate que precisam ser editadas toda vez que uma nova variável é adicionada ao módulo compartilhado.

## Como funciona
Defina os padrões da sua infraestrutura exclusivamente em módulos `.tf` reutilizáveis e utilize os arquivos `terragrunt.hcl` (com `terraform { source = ... }` e `inputs = { ... }`) para instanciar cada unidade sem arquivos `.tf` duplicados nas pastas de ambiente.

## Exemplo
As unidades `foo/terragrunt.hcl` e `bar/terragrunt.hcl` apontam ambas para `terraform { source = "../shared" }` passando seus respectivos blocos `inputs = { content = "Hello from foo, Terragrunt!" }`, eliminando `foo/main.tf` e `bar/main.tf`.

## Limites e trade-offs
Evite misturar arquivos `.tf` manuais redundantes dentro do diretório da unidade quando já estiver usando `terraform { source = ... }` no `terragrunt.hcl`, mantendo clara a separação entre definição de módulo (`.tf`) e instanciação de unidade (`terragrunt.hcl`).

## Como verificar
Execute `terragrunt plan` em uma unidade contendo apenas `terragrunt.hcl` com `terraform { source = ... }` e `inputs` e confirme que o módulo compartilhado é instanciado com as variáveis corretas.

## Conexões
- [[terragrunt-terragrunt-hcl-auto-init-and-bare-log-format]] — Veja também: Configuração terragrunt.hcl, recurso Auto-init e controle de saída com --log-format bare.
- [[terragrunt-terragrunt-cache-scratch-directory-and-get-terragrunt-dir]] — Veja também: Funcionamento do diretório .terragrunt-cache e uso da função built-in get_terragrunt_dir().

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
