---
id: software.devops.tranche10.000957
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

# Infracost: gerenciamento de autenticação (auth login, device flow, token cache) e múltiplas organizações (infracost org)

## Em uma frase
A CLI do Infracost gerencia identidades via **`infracost auth`** (`login` com OAuth PKCE ou `--oauth-use-device-flow` para terminais remotos, `whoami` e `logout`) e permite alternar ou fixar organizações por repositório com **`infracost org`** (`list`, `current`, `switch --repo`).

## Por que importa
Consultores de DevOps, engenheiros de plataforma em holdings com várias empresas ou desenvolvedores trabalhando via SSH/containers remotos (sem navegador local) precisam autenticar via Device Flow e fixar qual organização do Infracost (com suas respectivas tabelas de descontos corporativos e políticas FinOps) deve ser usada em cada repositório Git.

## Como funciona
Conforme especifica a referência `CLI commands` (`Auth` e `Org`): (1) **Autenticação**: `infracost auth login` realiza login OAuth PKCE via navegador e armazena o token no cache local (`--access-token-use-cache`, padrão `true`). Quando executado em um servidor remoto sem navegador/localhost (como SSH, DevContainer ou WSL sem GUI), passar a flag global **`--oauth-use-device-flow`** exibe um código de dispositivo para autorizar em qualquer navegador; e (2) **Organizações (`infracost org`)**: `infracost org list` lista todas as organizações do usuário, `infracost org switch <slug>` troca a organização ativa globalmente e **`infracost org switch <slug> --repo`** fixa a organização especificamente para o repositório Git atual (ou usa-se `--org <slug>` por comando).

## Exemplo
```bash
# Autenticar em um servidor remoto usando OAuth Device Flow e fixar a organização ativa para o repositório atual
infracost auth login --oauth-use-device-flow
infracost auth whoami
infracost org switch minha-empresa --repo
```

## Limites e trade-offs
Se o token em cache expirar ou apresentar problemas de permissão após uma alteração de papéis na organização, você pode forçar uma renovação limpa desativando temporariamente o cache com `--access-token-use-cache=false` ou executando `infracost auth logout` seguido de `infracost auth login`.

## Como verificar
Execute `infracost auth whoami` e `infracost org current` para confirmar o usuário autenticado e a organização ativa aplicada ao diretório atual.

## Conexões
- [[infracost-integracao-cicd-pull-requests-infracost-ci-setup]] — Veja também: Infracost: comentários automáticos de diff de custos em Pull Requests (infracost ci setup e pipelines CI/CD).
- [[infracost-manutencao-diagnostico-doctor-update-config-yml]] — Veja também: Infracost: configuração multi-projeto com infracost.yml e diagnóstico/manutenção da CLI (infracost doctor e update).
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.
- [[infracost-comandos-cli-scan-inspect-price-flags-globais]] — Referência cruzada direta com infracost-comandos-cli-scan-inspect-price-flags-globais.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
