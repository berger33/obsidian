---
id: software.criacao_ia.tranche01.000062
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
fontes: ["https://docs.blender.org/manual/en/latest/animation/actions.html", "https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender: nomear Actions para o pipeline

## Em uma frase

Nomes de ação explícitos ajudam artistas e ferramentas a identificar clips depois de exportar e importar.

## Por que importa

Nomes genéricos como `Action.003` dificultam mapear animação para estados de gameplay e detectar substituições acidentais.

## Como funciona

Adote uma convenção curta por personagem e intenção, mantendo nomes compatíveis com limites do engine alvo.

## Exemplo

Um conjunto pode usar `hero_locomotion_run` e `hero_combat_hit`, incluindo variante somente quando necessária.

## Limites e trade-offs

Convenções extensas podem divergir entre times; nomes não substituem metadados de rig e documentação de importação.

## Como verificar

Exporte uma amostra e compare nomes recebidos no engine com a tabela de clips aprovada pela equipe.

## Conexões
- [[blender-organizar-clips-como-actions]] — Blender: organizar clips como Actions.
- [[blender-preservar-acoes-com-nla]] — Blender: preservar ações com NLA.

## Fontes
- [Blender Manual — Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) — Descreve ações e seu uso para organizar dados de animação no Blender. Consulta: 2026-10-04.
- [Blender Manual — glTF 2.0 export](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html) — Documenta opções, objetos e animações suportados pela exportação glTF do Blender. Consulta: 2026-10-04.
