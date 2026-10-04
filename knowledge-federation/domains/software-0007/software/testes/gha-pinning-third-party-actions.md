---
id: software.testes.tranche08.000222
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

# GitHub Actions: fixar e revisar actions de terceiros

## Em uma frase
Fixe dependências de actions em referência imutável aprovada e mantenha processo de atualização revisada.

## Por que importa
Uma tag móvel pode apontar para código diferente do que foi auditado, alterando o comportamento de pipeline sem mudança local visível.

## Como funciona
Use SHA completo conforme política, registre versão legível em comentário quando útil e atualize por revisão que examine diff, permissões e origem.

## Exemplo
Atualização automatizada propõe SHA novo com release correspondente; revisão verifica mudanças e teste do workflow antes de aceitar.

## Limites e trade-offs
Pinning não torna action confiável por si só; uma versão imutável ainda pode conter vulnerabilidade ou receber acesso excessivo.

## Como verificar
Varra workflows por tags mutáveis, confirme SHA e provenance segundo política e reavalie permissões consumidas por cada action.

## Conexões
- [[gha-minimum-token-permissions]] — Veja também: GitHub Actions: limitar permissões do token GITHUB_TOKEN.
- [[gha-job-output-untrusted-artifacts]] — Veja também: GitHub Actions: não confiar em artifacts de execução não privilegiada.

## Fontes
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
- [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) — permissions, concurrency, matrices e configuração dos workflows; consultado em 2026-10-02.
