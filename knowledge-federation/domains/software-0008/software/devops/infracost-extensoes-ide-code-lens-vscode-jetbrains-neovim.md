---
id: software.devops.tranche10.000955
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

# Infracost: estimativas de custo inline em tempo real na IDE (Code Lens no VS Code, Cursor, JetBrains, Neovim e Zed)

## Em uma frase
A extensão de IDE do Infracost (configurável via **`infracost ide setup`** para VS Code, Cursor, JetBrains, VSCodium, Theia, Neovim e Zed) executa um Language Server local que exibe estimativas de custo, violações de FinOps e problemas de tags como **Code Lenses** diretamente acima de cada bloco `resource` enquanto você edita o arquivo.

## Por que importa
Descobrir o custo de um recurso apenas depois de fazer `git commit`, `git push` e abrir um Pull Request ainda exige vários minutos de espera pelo CI; ver um Code Lens inline dizendo `Monthly cost: $142.50 | 1 FinOps issue` no exato segundo em que você digita `instance_type = "m5.2xlarge"` no editor permite corrigir o código antes mesmo do primeiro commit.

## Como funciona
Conforme documenta a seção `IDE` em `infracost.io/docs/`, após instalar a extensão (`ext install Infracost.infracost` no VS Code `v1.75.0+`, plugin `24761-infracost` nas IDEs JetBrains como IntelliJ/GoLand/PyCharm, `infracost/infracost.nvim` no Neovim ou extensão nativa no Zed/Cursor) e autenticar na barra lateral, o Language Server do Infracost escaneia o workspace local continuamente. Acima de cada bloco de recurso Terraform ou CloudFormation, ele renderiza uma linha clicável (**Code Lens**); clicar no Code Lens abre a visão detalhada com a decomposição de custos (computação, armazenamento, IOPS) e as violações de políticas FinOps e tagging daquele recurso específico.

## Exemplo
```bash
# Iniciar o assistente interativo para instalar a extensão do Infracost na sua IDE ou instalar via CLI do VS Code
infracost ide setup
code --install-extension Infracost.infracost
```

## Limites e trade-offs
Em ambientes corporativos restritos onde a IDE não tem acesso direto ao Marketplace público na internet, a documentação oficial orienta baixar o arquivo `.vsix` da página de releases `infracost/vscode-infracost` (instalando via `code --install-extension infracost-<version>-<platform>.vsix`) ou o `.zip` do JetBrains Marketplace (*Install Plugin from Disk...*).

## Como verificar
Abra um arquivo `main.tf` no VS Code ou JetBrains com a extensão Infracost ativa e verifique a exibição do Code Lens de custo mensal acima das declarações `resource`.

## Conexões
- [[infracost-integracao-agentes-ia-skills-claude-copilot-cursor]] — Veja também: Infracost: integração com agentes de codificação de IA (Claude Code, Copilot, Codex, Cursor e Gemini CLI) via Agent Skills.
- [[infracost-integracao-cicd-pull-requests-infracost-ci-setup]] — Veja também: Infracost: comentários automáticos de diff de custos em Pull Requests (infracost ci setup e pipelines CI/CD).
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
