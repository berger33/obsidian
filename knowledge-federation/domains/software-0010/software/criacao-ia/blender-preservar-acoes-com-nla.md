---
id: software.criacao_ia.tranche01.000063
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.blender.org/manual/en/latest/animation/actions.html", "https://docs.blender.org/manual/en/latest/editors/nla/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender: preservar ações com NLA

## Em uma frase

NLA permite organizar e combinar strips de Action na linha do tempo e manter clips disponíveis para o pipeline.

## Por que importa

A organização evita perder ações que não estão ativas no momento da exportação e torna visível a sequência pretendida.

## Como funciona

Stash ou organize Actions conforme fluxo usado, ajuste strips e confirme opções de exportação antes de gerar o arquivo.

## Exemplo

Um artista mantém idle e walk separados no NLA para revisar a transição sem fundir as curvas num único clip.

## Limites e trade-offs

Comportamento de exportação depende de ações ativas, faixas NLA e opções; estado do editor pode afetar o resultado.

## Como verificar

Faça uma exportação de teste com cada configuração e verifique quantidade, nomes e duração das animações importadas.

## Conexões
- [[blender-nomear-actions-para-o-pipeline]] — Blender: nomear Actions para o pipeline.
- [[blender-conferir-intervalos-de-keyframes]] — Blender: conferir intervalos de keyframes.

## Fontes
- [Blender Manual — Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) — Descreve ações e seu uso para organizar dados de animação no Blender. Consulta: 2026-10-04.
- [Blender Manual — Nonlinear Animation Editor](https://docs.blender.org/manual/en/latest/editors/nla/index.html) — Apresenta faixas, strips e ações no editor de animação não linear. Consulta: 2026-10-04.
