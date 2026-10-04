---
id: software.devops.tranche10.000956
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

# Infracost: comentários automáticos de diff de custos em Pull Requests (infracost ci setup e pipelines CI/CD)

## Em uma frase
O comando **`infracost ci setup`** conecta o repositório ao Infracost (via App Integration recomendada ou gerando workflows de CI com `--ci-pipeline`) para que todo Pull Request receba automaticamente um comentário mostrando o diff de custo mensal, violações de FinOps e problemas de tags introduzidos pela mudança.

## Por que importa
Mesmo que um desenvolvedor individual não tenha instalado a extensão na IDE, o Pull Request é o ponto de controle obrigatório onde toda a equipe e os revisores avaliam a mudança: ter uma tabela automática no PR mostrando `+$320/mês (+14%)` junto com o diff de código faz com que o impacto financeiro seja discutido durante o code review.

## Como funciona
Conforme descrevem as seções `CI/CD` (`infracost.io/docs/`) e `CI` (`infracost.io/docs/features/cli_commands/#ci`), existem duas formas de habilitar a verificação em Pull Requests (GitHub, GitLab, Azure DevOps, Bitbucket): (1) **Infracost App Integration (recomendada)**: rodar `infracost ci setup` conecta o repositório diretamente à integração de nuvem do Infracost em poucos minutos sem precisar manter scripts complexos de runner; ou (2) **CI Pipeline (`infracost ci setup --ci-pipeline`)**: gera o arquivo de workflow para GitHub Actions / GitLab CI usando um token de serviço configurado na variável de ambiente **`INFRACOST_CLI_AUTHENTICATION_TOKEN`**.

## Exemplo
```bash
# Conectar o repositório atual à integração de Pull Requests do Infracost ou gerar um workflow de pipeline CI/CD
infracost ci setup
infracost ci setup --ci-pipeline --yes
```

## Limites e trade-offs
Em ambientes não-interativos de CI/CD, o runner não possui navegador web para executar o login OAuth interativo (`infracost auth login`); portanto, conforme documenta a seção `Auth` de `CLI commands`, nos runners de CI você deve sempre autenticar definindo a variável de ambiente secreta **`INFRACOST_CLI_AUTHENTICATION_TOKEN`** com um token de conta de serviço ou personal access token.

## Como verificar
Abra um Pull Request alterando o tamanho de uma instância em um arquivo `.tf` e confirme que o comentário automático do Infracost aparece no PR detalhando a diferença de custo mensal antes e depois da mudança.

## Conexões
- [[infracost-extensoes-ide-code-lens-vscode-jetbrains-neovim]] — Veja também: Infracost: estimativas de custo inline em tempo real na IDE (Code Lens no VS Code, Cursor, JetBrains, Neovim e Zed).
- [[infracost-autenticacao-oauth-pkce-device-flow-organizacoes]] — Veja também: Infracost: gerenciamento de autenticação (auth login, device flow, token cache) e múltiplas organizações (infracost org).
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.
- [[infracost-politicas-finops-tagging-guardrails-orcamentos]] — Referência cruzada direta com infracost-politicas-finops-tagging-guardrails-orcamentos.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
