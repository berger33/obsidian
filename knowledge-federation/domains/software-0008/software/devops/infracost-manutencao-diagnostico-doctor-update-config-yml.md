---
id: software.devops.tranche10.000958
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

# Infracost: configuração multi-projeto com infracost.yml e diagnóstico/manutenção da CLI (infracost doctor e update)

## Em uma frase
Para repositórios que contêm múltiplos projetos ou workspaces de IaC, o arquivo **`infracost.yml`** coordena o escaneamento unificado, enquanto os comandos **`infracost doctor`** e **`infracost update`** diagnosticam/reparam a instalação e atualizam o binário da CLI.

## Por que importa
Em monorepos de infraestrutura com dezenas de pastas (`envs/prod/vpc`, `envs/prod/eks`, `envs/prod/rds`) ou múltiplos arquivos de variáveis `.tfvars`, rodar `infracost scan` sem informar como os projetos e variáveis se relacionam pode deixar pastas de fora; além disso, diagnosticar rapidamente falhas de rede/certificados/plugins com `infracost doctor` economiza tempo de suporte.

## Como funciona
Conforme documenta a página `CLI commands`: (1) **Multi-projeto (`infracost.yml`)**: quando o repositório possui múltiplos projetos ou workspaces, declará-los em um arquivo `infracost.yml` na raiz faz com que um único `infracost scan` avalie todos os projetos em conjunto; (2) **`infracost doctor`**: executa uma bateria de verificações de saúde na instalação local da CLI (conectividade, autenticação, extensões, variáveis) e pode reparar problemas automaticamente; e (3) **`infracost update`**, `infracost version` e `infracost completion`: mantêm o binário atualizado na versão mais recente e geram scripts de autocompletar para o shell (`bash`, `zsh`, `fish`).

## Exemplo
```bash
# Diagnosticar e reparar problemas na instalação local do Infracost e atualizar o binário da CLI
infracost doctor
infracost update
infracost version
```

## Limites e trade-offs
Caso você tenha instalado o Infracost através de um gerenciador de pacotes do sistema operacional (como `brew install infracost` no macOS/Linux ou `choco install infracost` no Windows), prefira atualizá-lo pelo próprio gerenciador (`brew upgrade infracost` ou `choco upgrade infracost`) conforme recomendado na seção `Install the CLI` para manter o registro de versões do gerenciador consistente.

## Como verificar
Execute `infracost doctor` no seu ambiente de desenvolvimento e confirme que todas as verificações de saúde da CLI e de autenticação passam sem alertas.

## Conexões
- [[infracost-autenticacao-oauth-pkce-device-flow-organizacoes]] — Veja também: Infracost: gerenciamento de autenticação (auth login, device flow, token cache) e múltiplas organizações (infracost org).
- [[infracost-suporte-multiac-terraform-terragrunt-cloudformation-cdk]] — Veja também: Infracost: suporte multi-ferramenta de IaC (Terraform, Terragrunt, CloudFormation e AWS CDK) e multi-cloud.
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.
- [[infracost-comandos-cli-scan-inspect-price-flags-globais]] — Referência cruzada direta com infracost-comandos-cli-scan-inspect-price-flags-globais.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
