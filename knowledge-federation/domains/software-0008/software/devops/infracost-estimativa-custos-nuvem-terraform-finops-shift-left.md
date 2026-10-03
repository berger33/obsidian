---
id: software.devops.tranche10.000951
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

# Infracost: estimativa de custos de nuvem e FinOps Shift-Left para Infraestrutura como Código

## Em uma frase
O **Infracost** (`infracost.io/docs/`) desloca os custos de nuvem para a esquerda (*shifts cloud costs left*) no fluxo de engenharia, analisando arquivos de Infraestrutura como Código (Terraform, Terragrunt, CloudFormation e AWS CDK) em AWS, Azure e Google Cloud para calcular custos e detectar violações de FinOps antes do deploy.

## Por que importa
Tradicionalmente, engenheiros alteram tipos de instâncias EC2/RDS, provisionam NAT Gateways ou discos provisionados IOPS no Terraform e só descobrem que aumentaram a fatura mensal em US$ 15.000 trinta dias depois, quando a fatura da nuvem chega ao financeiro. Segundo a página oficial `Get started` (`infracost.io/docs/`), o Infracost mostra o impacto financeiro na IDE, no agente de IA e no Pull Request antes que o código seja aplicado.

## Como funciona
Quando o desenvolvedor executa a CLI do Infracost (versão `2.16.3+`, configurada rapidamente via **`infracost setup`**), a ferramenta analisa localmente os arquivos de IaC do projeto para determinar os tipos de recursos e quantidades que seriam criados, consulta os preços das nuvens e avalia as políticas da organização. Crucialmente, conforme destaca a nota de segurança da documentação oficial: **nenhuma credencial ou segredo de nuvem é enviado à API de preços**, e o Infracost **não faz nenhuma alteração** no seu estado do Terraform nem nos recursos da nuvem.

## Exemplo
```bash
# Instalar a CLI do Infracost, executar o assistente interativo de configuração e escanear o diretório Terraform atual
brew install infracost
infracost setup
infracost scan
```

## Limites e trade-offs
Como o Infracost calcula as estimativas analisando estaticamente o código IaC local (ou o JSON de um plano Terraform) sem conectar-se à sua conta real da AWS/Azure/GCP por padrão, recursos cujo custo depende fortemente de métricas variáveis de tráfego/consumo (como gigabytes transferidos no S3/CloudFront ou milhões de invocações no AWS Lambda) são estimados com base nas configurações e parâmetros de uso informados.

## Como verificar
Execute `infracost --version` e rode `infracost scan` na raiz de um projeto Terraform para visualizar o detalhamento de custos por recurso diretamente no terminal.

## Conexões
- [[infracost-comandos-cli-scan-inspect-price-flags-globais]] — Veja também: Infracost: análise de infraestrutura via CLI (infracost scan, inspect, price) e flags globais (--json, --llm, --currency).
- [[infracost-politicas-finops-tagging-guardrails-orcamentos]] — Referência cruzada direta com infracost-politicas-finops-tagging-guardrails-orcamentos.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
