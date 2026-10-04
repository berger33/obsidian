---
id: software.criacao_ia.tranche02.000199
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://diataxis.fr/explanation/", "https://diataxis.fr/how-to-guides/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# CI para Documentação: testar snippets de código e validar links quebrados

## Em uma frase
A validação automatizada de snippets e hiperlinks no CI impede que documentações com erros e links mortos cheguem aos usuários.

## Por que importa
Exemplos de código desatualizados ou links quebrados geram frustração imediata e minam a confiança do desenvolvedor no projeto.

## Como funciona
Configure um job no GitHub Actions ou pipeline equivalente utilizando linters de Markdown (ex.: `markdown-link-check` e compiladores de snippets) que executam testes sobre todos os blocos de código documentados.

## Exemplo
```yaml
# Pipeline de validacao de documentacao no GitHub Actions
name: Docs Validation
on: [push, pull_request]
jobs:
  check-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check Broken Markdown Links
        uses: gaurav-nelson/github-action-markdown-link-check@v1
```

## Limites e trade-offs
Verificadores de links podem gerar falhas intermitentes no CI devido a limites de taxa (*rate limiting*) em sites externos.

## Como verificar
Dispare a rotina de validação de documentação no repositório e confirme que todos os links e snippets de teste retornam código de saída zero.

## Conexões
- [[documentacao-manter-guias-de-migracao-e-breaking-changes]] — Veja também: Manutenção de Software: documentar breaking changes e guias de migração.
- [[documentacao-aplicar-checklist-em-tutoriais-gerados-por-ia]] — Veja também: Governança Técnica: aplicar checklist de verificação em tutoriais gerados por IA.
- [[documentacao-executar-exemplos-de-codigo]] — Conexão temática direta com documentacao-executar-exemplos-de-codigo.
- [[documentacao-tornar-resultado-e-verificacao-explicitos]] — Conexão temática direta com documentacao-tornar-resultado-e-verificacao-explicitos.
- [[claude-code-validar-testes-antes-do-commit]] — Conexão temática direta com claude-code-validar-testes-antes-do-commit.

## Fontes
- [Diátaxis Documentation Framework — Explanation](https://diataxis.fr/explanation/) — Especificação formal do quadrante de explicação, arquitetura conceitual e análise de trade-offs. Consulta: 2026-10-04.
- [Diátaxis Documentation Framework — How-to Guides](https://diataxis.fr/how-to-guides/) — Guia para redação de passos orientados a problemas práticos de produção e trabalho diário. Consulta: 2026-10-04.
