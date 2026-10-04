---
id: software.devops.tranche10.000952
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

# Infracost: análise de infraestrutura via CLI (infracost scan, inspect, price) e flags globais (--json, --llm, --currency)

## Em uma frase
Conforme a referência oficial `CLI commands` (`infracost.io/docs/features/cli_commands/`), a análise de custos na CLI divide-se entre **`infracost scan`** (que avalia um diretório IaC ou arquivo `tfplan.json` e faz cache local), **`infracost inspect`** (que filtra e agrupa instantaneamente o último scan) e **`infracost price`** (que precifica IaC recebido via `stdin`).

## Por que importa
Em repositórios grandes com centenas de recursos, reexecutar o parser completo do IaC toda vez que você quer agrupar os custos por serviço, filtrar apenas recursos caros ou exportar para um prompt de LLM desperdiçaria tempo; separar `scan` (com cache local) de `inspect` e `price` torna a exploração interativa instantânea.

## Como funciona
Os comandos do grupo *Analyze infrastructure* operam da seguinte forma: (1) **`infracost scan [caminho|tfplan.json]`**: autodetecta o tipo de IaC no diretório (Terraform, Terragrunt, CloudFormation, CDK) ou lê um arquivo JSON gerado por `terraform show -json`, calcula os custos, avalia as políticas FinOps/tagging, exibe o relatório e salva os resultados no cache local (aceitando `--currency EUR|BRL|USD`); (2) **`infracost inspect`**: filtra, agrupa e resume os resultados do último `scan` em cache instantaneamente; (3) **`infracost price`**: estima o custo de trechos de IaC passados diretamente via pipe no `stdin`; e (4) **Flags globais**: todos os comandos aceitam `--org <slug>`, `--json` (saída estruturada JSON) e **`--llm`** (formato compacto e eficiente em tokens projetado para prompts de LLMs).

## Exemplo
```bash
# Escanear o diretório ./terraform na moeda BRL, exportar em JSON ou formato compacto para LLM (--llm)
infracost scan ./terraform --currency BRL
infracost scan ./terraform --llm
infracost inspect
```

## Limites e trade-offs
Quando seu código Terraform utiliza expressões dinâmicas que só são resolvidas em tempo de `terraform plan` (como `data` sources externos consultados na nuvem ou módulos remotos complexos no HCP Terraform / Terraform Enterprise), conforme aponta a documentação oficial, passe o plano compilado em JSON (**`infracost scan tfplan.json`**) em vez de apontar apenas para o diretório estático.

## Como verificar
Execute `infracost scan --json > /tmp/infracost.json` e verifique a estrutura JSON gerada contendo a lista de recursos, custos mensais e resultados de políticas.

## Conexões
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Veja também: Infracost: estimativa de custos de nuvem e FinOps Shift-Left para Infraestrutura como Código.
- [[infracost-politicas-finops-tagging-guardrails-orcamentos]] — Veja também: Infracost: governança com FinOps Policies, Tagging Policies, Cost Budgets e Cost Guardrails.
- [[infracost-integracao-agentes-ia-skills-claude-copilot-cursor]] — Referência cruzada direta com infracost-integracao-agentes-ia-skills-claude-copilot-cursor.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
