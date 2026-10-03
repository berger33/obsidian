---
id: software.devops.tranche04.000392
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

# Configuração terragrunt.hcl, recurso Auto-init e controle de saída com --log-format bare

## Em uma frase
O Quick Start oficial demonstra que integrar um projeto OpenTofu/Terraform existente ao Terragrunt pode começar simplesmente criando um arquivo vazio `touch terragrunt.hcl` no diretório do projeto. Apenas com esse arquivo, o usuário já passa a contar com o recurso **Auto-init** (`docs.terragrunt.com/features/units/auto-init/`): não é mais necessário executar `tofu init` ou `terraform init` manualmente antes de `terragrunt apply`, pois o Terragrunt executa `init` automaticamente sempre que necessário. Além disso, como o log padrão do Terragrunt adiciona prefixos de horário, stream (`STDOUT`) e contexto para facilitar execuções em escala, pode-se usar a flag **`--log-format bare`** (ou a variável de ambiente **`TG_LOG_FORMAT=bare`**) quando se desejar uma saída idêntica à do `tofu`/`terraform` puro.

## Por que importa
Esquecer de rodar `init` após adicionar um módulo ou alterar configuração de backend é uma falha constante em fluxos manuais e scripts de CI; o Auto-init elimina essa etapa repetitiva, enquanto `TG_LOG_FORMAT=bare` preserva compatibilidade com ferramentas que leem a saída limpa do plano.

## Como funciona
Use `terragrunt apply` / `terragrunt plan` diretamente sem chamadas prévias manuais de `init` e configure `TG_LOG_FORMAT=bare` (ou `--log-format bare`) quando desejar saída enxuta em execuções de uma única unidade.

## Exemplo
Em um diretório `foo` contendo um `main.tf` novo ainda não inicializado, o engenheiro cria `foo/terragrunt.hcl` e executa imediatamente `terragrunt apply -auto-approve`; o Terragrunt inicializa o backend e o provedor `hashicorp/local`, gera `.terraform.lock.hcl` e aplica o recurso em um único comando.

## Limites e trade-offs
Não remova o arquivo `.terraform.lock.hcl` gerado durante o Auto-init: conforme lembra a própria saída do OpenTofu no guia, versione `.terraform.lock.hcl` no controle de versão para garantir seleções determinísticas de provedores nas execuções futuras.

## Como verificar
Em um diretório de teste sem `.terraform` inicializado, crie um `terragrunt.hcl` vazio, execute `terragrunt plan` e confirme que o Auto-init baixa os provedores automaticamente antes de gerar o plano.

## Conexões
- [[terragrunt-orchestration-for-opentofu-and-terraform-at-scale]] — Veja também: Terragrunt como orquestrador flexível para escalar projetos em OpenTofu e Terraform.
- [[terragrunt-units-shared-modules-and-inputs-blocks]] — Veja também: Unidades (units), módulos compartilhados e eliminação de main.tf redundantes com blocos terraform e inputs.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
