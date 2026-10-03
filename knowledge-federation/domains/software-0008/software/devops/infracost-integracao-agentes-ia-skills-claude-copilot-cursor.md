---
id: software.devops.tranche10.000954
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

# Infracost: integração com agentes de codificação de IA (Claude Code, Copilot, Codex, Cursor e Gemini CLI) via Agent Skills

## Em uma frase
O comando **`infracost agent setup`** (e o repositório oficial `infracost/agent-skills`) equipa agentes de codificação de IA (Claude Code, GitHub Copilot, OpenAI Codex, Cursor e Gemini CLI) com acesso em tempo real a preços de nuvem, orçamentos e políticas de FinOps/tagging da organização.

## Por que importa
Quando um desenvolvedor pede a um agente de IA (*"Crie uma aplicação web de 3 camadas na AWS com ECS e Postgres"*), o modelo de linguagem sem contexto de preços pode gerar instâncias superdimensionadas que custam US$ 2.500/mês e violam todas as políticas de tags e regiões da empresa, exigindo retrabalho posterior no PR. A seção `AI Agent` de `infracost.io/docs/` resolve isso na primeira tentativa.

## Como funciona
O desenvolvedor instala as skills no agente usando **`infracost agent setup`** (com suporte aos escopos `--scope user`, `--scope project` ou `--scope local`) ou diretamente pelos instaladores nativos de cada agente (`claude plugin marketplace add infracost/agent-skills` + `claude plugin install infracost@infracost`, `copilot plugin install`, `$skill-installer infracost/agent-skills` no Codex, Rules no Cursor ou `gemini skills install`). Uma vez instaladas, as skills ficam disponíveis como slash commands (`/infracost:<skill>`) e também são invocadas automaticamente quando o usuário pede ao agente para estimar custos, corrigir violações de tagging ou gerar infraestrutura dentro de um orçamento específico (ex.: *"...que custe menos de $400/mês e cumpra todas as políticas FinOps"*).

## Exemplo
```bash
# Instalar as skills do Infracost para agentes de IA no escopo do projeto atual ou via plugin do Claude Code
infracost agent setup --scope project
claude plugin marketplace add infracost/agent-skills
claude plugin install infracost@infracost
```

## Limites e trade-offs
Conforme observa a nota da documentação oficial para o **OpenAI Codex**, o instalador padrão do Codex espera um único skill por repositório; como `infracost/agent-skills` define múltiplos skills especializados, caso o Codex informe que não é um único skill, basta instruí-lo no prompt a instalar todas as skills do repositório.

## Como verificar
Execute `infracost agent setup --scope project` e peça ao agente de IA um detalhamento de custos do diretório Terraform atual usando `/infracost`.

## Conexões
- [[infracost-politicas-finops-tagging-guardrails-orcamentos]] — Veja também: Infracost: governança com FinOps Policies, Tagging Policies, Cost Budgets e Cost Guardrails.
- [[infracost-extensoes-ide-code-lens-vscode-jetbrains-neovim]] — Veja também: Infracost: estimativas de custo inline em tempo real na IDE (Code Lens no VS Code, Cursor, JetBrains, Neovim e Zed).
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.
- [[infracost-comandos-cli-scan-inspect-price-flags-globais]] — Referência cruzada direta com infracost-comandos-cli-scan-inspect-price-flags-globais.
- [[mirrord-agentes-ia-claude-code-cursor-codex-testes-cluster]] — Referência cruzada direta com mirrord-agentes-ia-claude-code-cursor-codex-testes-cluster.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
