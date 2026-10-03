---
id: software.devops.tranche04.000391
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

# Terragrunt como orquestrador flexível para escalar projetos em OpenTofu e Terraform

## Em uma frase
O Terragrunt, mantido pela Gruntwork (`gruntwork.io`) sob licença MIT, é uma ferramenta flexível de orquestração projetada para permitir que Infraestrutura como Código (IaC) escrita em **OpenTofu** (`>= 1.6.0`) ou **Terraform** (`>= 0.12.0`) escale em produção. Conforme documentado no Quick Start oficial, o Terragrunt nasceu organicamente da experiência de suportar equipes operando código Terraform em larga escala, resolvendo problemas recorrentes como duplicação de código entre ambientes, inicialização manual repetitiva, passagem dinâmica de saídas entre módulos e execução ordenada de pilhas multi-unidades.

## Por que importa
À medida que uma organização cresce de um único estado monolítico para dezenas ou centenas de módulos isolados em múltiplos ambientes (`dev`, `staging`, `prod`) e contas de nuvem, gerenciar variáveis estáticas `.tfvars` e rodar comandos manualmente na ordem correta torna-se inviável sem uma camada de orquestração.

## Como funciona
Adote o Terragrunt sobre seus módulos OpenTofu ou Terraform existentes (consultando a documentação de `tf-path` caso ambos os binários `tofu` e `terraform` estejam instalados na mesma máquina) para padronizar unidades, dependências e execuções em lote.

## Exemplo
Uma equipe de plataforma que migrou parte de seus repositórios para OpenTofu 1.8 enquanto mantém projetos legados em Terraform utiliza o Terragrunt como interface única de orquestração em ambos os ambientes.

## Limites e trade-offs
Quando tanto `tofu` quanto `terraform` estiverem instalados no ambiente de CI ou na máquina local, configure explicitamente o binário desejado conforme a documentação oficial de `tf-path` para evitar ambiguidade na seleção do executável.

## Como verificar
Execute `terragrunt --version` no ambiente e confirme a detecção correta do binário subjacente (`tofu` ou `terraform`).

## Conexões
- [[terragrunt-terragrunt-hcl-auto-init-and-bare-log-format]] — Veja também: Configuração terragrunt.hcl, recurso Auto-init e controle de saída com --log-format bare.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
