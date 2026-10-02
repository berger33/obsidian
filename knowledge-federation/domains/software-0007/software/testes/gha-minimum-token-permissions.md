---
id: software.testes.tranche08.000220
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.github.com/en/actions/reference/security/secure-use", "https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitHub Actions: limitar permissões do token GITHUB_TOKEN

## Em uma frase
Conceda a cada workflow ou job somente as permissões necessárias e faça a configuração explícita no YAML.

## Por que importa
Token excessivamente amplo aumenta impacto de workflow comprometido ou de código não confiável executado em pull request.

## Como funciona
Declare permissions no menor escopo possível, mantenha leitura como padrão quando aplicável e revise elevações por job e evento.

## Exemplo
Job de lint só lê conteúdo; job de release recebe permissão de escrita estritamente no job protegido que publica artefato.

## Limites e trade-offs
Permissões YAML não restringem credenciais externas ou token fornecido por ação de terceiros; revise todas as fontes de segredo e acesso.

## Como verificar
Inspecione permissões efetivas em cada evento, tente operação proibida em job de leitura e verifique que não há elevação herdada sem necessidade.

## Conexões
- [[gha-script-injection-event-context]] — Veja também: GitHub Actions: evitar injeção em scripts com contexto de evento.
- [[gha-environment-protection-gates]] — Veja também: GitHub Actions: verificar gates de environment antes do deploy.

## Fontes
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
- [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) — permissions, concurrency, matrices e configuração dos workflows; consultado em 2026-10-02.
