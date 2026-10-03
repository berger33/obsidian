---
id: software.devops.tranche04.000398
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

# Tratamento de dependências ainda não aplicadas durante o plan com mock_outputs e mock_outputs_allowed_terraform_commands

## Em uma frase
O Quick Start oficial demonstra um cenário fundamental do ciclo de vida IaC: quando uma stack inteira ainda **não foi aplicada** (`foo` nunca rodou `apply`) e o engenheiro executa `terragrunt run --all plan`, a unidade dependente `bar` falha com o erro `./foo/terragrunt.hcl is a dependency of ./bar/terragrunt.hcl but detected no outputs`, pois o Terragrunt tenta buscar `terragrunt output` de `foo` antes que `foo` tenha estado criado. Para permitir que o `plan` de uma stack nova funcione do início ao fim, configura-se o atributo **`mock_outputs`** dentro do bloco `dependency` e restringe-se seu uso exclusivamente à fase de planejamento com **`mock_outputs_allowed_terraform_commands = ["plan"]`**.

## Por que importa
Sem `mock_outputs`, é impossível rodar `terragrunt run --all plan` em um pull request que cria duas unidades novas encadeadas (`vpc` + `cluster`) antes do primeiro `apply`. E restringir com `mock_outputs_allowed_terraform_commands = ["plan"]` garante que valores falsos de mock jamais sejam usados acidentalmente durante um `apply` real.

## Como funciona
Adicione sempre `mock_outputs = { ... }` com valores sintaticamente válidos para os validadores dos provedores e inclua `mock_outputs_allowed_terraform_commands = ["plan"]` em todos os blocos `dependency` das unidades da stack.

## Exemplo
No `bar/terragrunt.hcl`, a equipe define `dependency "foo" { config_path = "../foo", mock_outputs = { content = "Mocked content from foo" }, mock_outputs_allowed_terraform_commands = ["plan"] }`; o `terragrunt run --all plan` emite um `WARN` informando o uso do mock e conclui o plano de `foo` e `bar` com sucesso, enquanto o `apply` subsequente usa o valor real de `foo`.

## Limites e trade-offs
Forneça em `mock_outputs` valores que respeitem o formato esperado pelo provedor de nuvem (por exemplo, um ARN ou ID com formato válido na AWS), caso contrário a validação sintática do provedor durante o `plan` rejeitará o valor mockado.

## Como verificar
Execute `terragrunt run --all plan` em uma stack ainda não aplicada com `mock_outputs` configurado e confirme a emissão do aviso `mock outputs provided and returning those in dependency output` e o sucesso do plano.

## Conexões
- [[terragrunt-dependency-blocks-and-dynamic-cross-unit-inputs]] — Veja também: Passagem dinâmica de outputs entre unidades com o bloco dependency no Terragrunt.
- [[terragrunt-ci-cd-gitops-workflows-and-terragrunt-scale]] — Veja também: Automação GitOps em CI/CD (plan no PR e apply no merge) e Terragrunt Scale.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
