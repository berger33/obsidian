---
id: software.devops.tranche04.000397
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

# Passagem dinâmica de outputs entre unidades com o bloco dependency no Terragrunt

## Em uma frase
Para que uma unidade consuma valores produzidos por outra unidade da stack, o Terragrunt oferece o bloco **`dependency "<nome>" { config_path = "../<unidade>" }`**. Uma vez declarado, as saídas (`output`) expostas pelo módulo da unidade alvo ficam acessíveis dinamicamente dentro do bloco `inputs` da unidade dependente por meio da expressão **`dependency.<nome>.outputs.<nome_do_output>`** (por exemplo, `content = "Foo content: ${dependency.foo.outputs.content}"`). Por baixo dos panos, o Terragrunt resolve a dependência executando `terragrunt output` na unidade referenciada e injetando o valor retornado como input dinâmico.

## Por que importa
Essa capacidade supera uma das maiores limitações dos arquivos estáticos `terraform.tfvars`: como `bar` depende de um valor que só é conhecido após `foo` ser criado, arquivos `.tfvars` estáticos exigiriam scripts manuais ou cópia de IDs entre pastas, além de dispensar a configuração complexa de múltiplos data sources `terraform_remote_state` no código `.tf`.

## Como funciona
Exponha os identificadores necessários como `output` nos módulos compartilhados e conecte as unidades consumidoras usando blocos `dependency` e referências `dependency.<nome>.outputs.<campo>` dentro de `inputs` no `terragrunt.hcl`.

## Exemplo
O módulo de rede `vpc` expõe `output "vpc_id"`; na unidade `eks/terragrunt.hcl`, o bloco `dependency "vpc" { config_path = "../vpc" }` permite passar `vpc_id = dependency.vpc.outputs.vpc_id` diretamente em `inputs`.

## Limites e trade-offs
Se uma unidade depende da existência de outra apenas para ordem de execução mas **não consome nenhum output** dela, o próprio diagnóstico do Terragrunt recomenda usar o bloco `dependencies` em vez de `dependency`.

## Como verificar
Após aplicar a unidade fornecedora e a unidade consumidora com `terragrunt run --all apply`, verifique no recurso criado pela unidade consumidora que o valor real do output foi interpolado corretamente.

## Conexões
- [[terragrunt-directed-acyclic-graph-dag-and-execution-order]] — Veja também: Grafo Acíclico Direcionado (DAG) no Terragrunt para ordenação automática de runs na stack.
- [[terragrunt-unapplied-dependencies-and-mock-outputs-in-plan]] — Veja também: Tratamento de dependências ainda não aplicadas durante o plan com mock_outputs e mock_outputs_allowed_terraform_commands.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
