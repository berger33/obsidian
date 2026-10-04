---
id: software.devops.tranche10.000959
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
fontes: ["https://www.infracost.io/docs/", "https://www.infracost.io/docs/features/cli_commands/", "https://github.com/infracost/infracost"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Infracost: suporte multi-ferramenta de IaC (Terraform, Terragrunt, CloudFormation e AWS CDK) e multi-cloud

## Em uma frase
O Infracost autodetecta e analisa projetos escritos em **Terraform**, **Terragrunt**, **AWS CloudFormation** e **AWS CDK** (em AWS, Azure e Google Cloud), suportando tanto a leitura estática rápida do código-fonte quanto a avaliação de planos compilados (`tfplan.json`).

## Por que importa
Organizações raramente usam uma única ferramenta de IaC em todas as equipes: a equipe de plataforma pode usar Terraform/Terragrunt para redes e clusters EKS/AKS/GKE, enquanto equipes de desenvolvimento serverless usam AWS CDK (TypeScript/Python) ou CloudFormation. Ter uma única ferramenta de FinOps e políticas de tagging que compreende todas essas linguagens evita silos de governança.

## Como funciona
Quando você aponta **`infracost scan <diretório>`** para uma pasta (ou usa `infracost price` via stdin), a CLI inspeciona os arquivos presentes para identificar automaticamente a ferramenta de IaC: (1) em projetos **Terraform** e **Terragrunt**, analisa os arquivos `.tf` / `terragrunt.hcl` e módulos locais/remotos diretamente em segundos sem precisar rodar `terraform init`/`plan` na nuvem; (2) em projetos **CloudFormation** e **AWS CDK**, sintetiza/analisa os templates dos recursos AWS; e (3) caso o projeto dependa de valores gerados apenas no momento do plano (como no HCP Terraform), aceita o arquivo JSON do plano (`infracost scan tfplan.json`).

## Exemplo
```bash
# Gerar um arquivo JSON de plano do Terraform e escaneá-lo diretamente com o Infracost
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary > tfplan.json
infracost scan tfplan.json
```

## Limites e trade-offs
Analisar diretamente o diretório de código-fonte (`infracost scan .`) é muito mais rápido e não exige credenciais de nuvem (sendo o modo padrão usado na IDE, nos agentes de IA e no scan local); já o modo baseado em `tfplan.json` exige executar `terraform init` e `terraform plan` com acesso ao estado e à nuvem antes do `infracost scan`, sendo reservado para pipelines de CI que já geram o `tfplan.binary` como parte do deploy.

## Como verificar
Execute `infracost scan` sobre um diretório contendo arquivos `.tf` sem ter variáveis `AWS_ACCESS_KEY_ID` exportadas no shell e confirme que o cálculo de custos ocorre 100% localmente sem acessar a conta da AWS.

## Conexões
- [[infracost-manutencao-diagnostico-doctor-update-config-yml]] — Veja também: Infracost: configuração multi-projeto com infracost.yml e diagnóstico/manutenção da CLI (infracost doctor e update).
- [[infracost-filtragem-agrupamento-inspect-stdin-price-automacao]] — Veja também: Infracost: consultas instantâneas sobre resultados em cache (infracost inspect) e precificação via pipe (infracost price).
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.
- [[infracost-comandos-cli-scan-inspect-price-flags-globais]] — Referência cruzada direta com infracost-comandos-cli-scan-inspect-price-flags-globais.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
