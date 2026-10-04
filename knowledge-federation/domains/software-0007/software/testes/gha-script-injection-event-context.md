---
id: software.testes.tranche08.000221
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

# GitHub Actions: evitar injeção em scripts com contexto de evento

## Em uma frase
Não interpole diretamente valores controlados por usuário em comando shell; trate contexto de evento como entrada não confiável.

## Por que importa
Título de issue, branch ou comentário pode conter sintaxe interpretada pelo shell quando inserido no script do workflow.

## Como funciona
Passe valores por variável de ambiente ou arquivo com quoting seguro e valide-os antes de uso. Prefira ações que recebam input sem montar comando dinâmico.

## Exemplo
Um workflow extrai nome de branch para env e valida formato antes de usá-lo como parâmetro, sem inserção textual direta no bloco run.

## Limites e trade-offs
Escaping depende de shell e contexto; mover valor para env reduz uma classe de injeção, mas não elimina validação de path ou argumento.

## Como verificar
Use payload de teste com metacaracteres, confirme que não executa comandos e revise todos os contextos `${{ }}` dentro de `run`.

## Conexões
- [[gha-secrets-pull-request-forks]] — Veja também: GitHub Actions: proteger secrets em pull requests externos.
- [[gha-pinning-third-party-actions]] — Veja também: GitHub Actions: fixar e revisar actions de terceiros.

## Fontes
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
- [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) — permissions, concurrency, matrices e configuração dos workflows; consultado em 2026-10-02.
