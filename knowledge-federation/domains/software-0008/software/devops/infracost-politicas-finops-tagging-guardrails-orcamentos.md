---
id: software.devops.tranche10.000953
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

# Infracost: governança com FinOps Policies, Tagging Policies, Cost Budgets e Cost Guardrails

## Em uma frase
Além de estimar o valor em dólares de cada recurso, o Infracost valida automaticamente o código IaC contra **FinOps Policies** (ex.: tipos de instância e gerações recomendadas), **Tagging Policies** (tags obrigatórias), **Budgets** e **Guardrails**, consultáveis via `infracost policies`, `budgets` e `guardrails`.

## Por que importa
Saber apenas que um módulo custa US$ 800/mês não diz ao desenvolvedor que ele está usando volumes EBS `gp2` antigos em vez de `gp3` (que são mais baratos e rápidos), instâncias AWS de geração antiga (`m5` em vez de `m6i`/`m7g`) ou que esqueceu a tag `CostCenter` obrigatória para alocação contábil.

## Como funciona
Conforme documenta a página `Get started` e a seção `Organization settings` em `CLI commands`, a organização configura suas regras centralizadamente e a CLI as aplica durante o `infracost scan` (e na IDE / Pull Requests): (1) **`infracost policies`**: lista todas as **FinOps policies** (regras de eficiência de custo, regiões preferidas e tipos de instâncias) e **Tagging policies** (chaves e valores válidos de tags obrigatórias) ativas na organização; (2) **`infracost budgets`**: lista os orçamentos de custo configurados; e (3) **`infracost guardrails`**: lista os limites de alerta/bloqueio (guardrails de aumento percentual ou valor absoluto em dólares) aplicáveis ao repositório atual.

## Exemplo
```bash
# Listar as políticas de FinOps/Tagging, os orçamentos e os guardrails ativos para o repositório atual
infracost policies
infracost budgets
infracost guardrails
```

## Limites e trade-offs
Ao implantar **Tagging Policies** e **FinOps Policies** pela primeira vez em um repositório legado grande que já possui centenas de recursos em produção sem tags padronizadas, configurar os guardrails de PR para bloquear qualquer falha no repositório inteiro travará os desenvolvedores; avalie apenas os recursos novos/modificados no diff do Pull Request enquanto corrige o passivo gradualmente.

## Como verificar
Execute `infracost policies --json` e `infracost scan` em um projeto de teste para confirmar que violações de políticas FinOps e de tags aparecem destacadas ao lado da estimativa de custo.

## Conexões
- [[infracost-comandos-cli-scan-inspect-price-flags-globais]] — Veja também: Infracost: análise de infraestrutura via CLI (infracost scan, inspect, price) e flags globais (--json, --llm, --currency).
- [[infracost-integracao-agentes-ia-skills-claude-copilot-cursor]] — Veja também: Infracost: integração com agentes de codificação de IA (Claude Code, Copilot, Codex, Cursor e Gemini CLI) via Agent Skills.
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.
- [[atlantis-verificacao-politicas-policy-checking-conftest-opa]] — Referência cruzada direta com atlantis-verificacao-politicas-policy-checking-conftest-opa.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
