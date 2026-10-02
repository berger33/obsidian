---
id: software.testes.tranche14.000797
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://developer.android.com/training/testing/espresso/accessibility-checking", "https://developer.android.com/training/testing/espresso"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso: executar verificações de acessibilidade junto às ações

## Em uma frase
`AccessibilityChecks.enable()` integra verificações do Android Accessibility Test Framework às ações de view feitas pelos testes Espresso.

## Por que importa
Checagens automatizadas acrescentam feedback sobre problemas perceptíveis sem exigir uma nova suite de UI por regra de acessibilidade.

## Como funciona
Habilite a configuração antes dos testes que farão ações; por padrão, as verificações acompanham as ações definidas por `ViewActions`.

## Exemplo
Um teste de fluxo de boas-vindas pode habilitar checks no setup e acionar os botões para inspecionar findings na hierarquia.

## Limites e trade-offs
A checagem automatizada não prova conformidade completa nem substitui navegação assistiva e avaliação humana.

## Como verificar
Investigue findings gerados por cada ação e complemente com auditoria manual do fluxo e conteúdo acessível.

## Conexões
- [[espresso-recyclerview-actions]] — Veja também: Espresso: usar RecyclerViewActions para itens reciclados.
- [[espresso-suppress-accessibility-narrowly]] — Veja também: Espresso: restringir supressões de findings de acessibilidade.

## Fontes
- [Android — Accessibility checking](https://developer.android.com/training/testing/espresso/accessibility-checking) — execução e supressão estreita de resultados de acessibilidade; consultado em 2026-10-02.
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
