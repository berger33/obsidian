---
id: software.criacao_ia.tranche01.000068
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

# Blender: controlar múltiplas Actions no export

## Em uma frase

Uma armature pode conter diversas Actions, e as opções de exportação determinam quais clips são gravados.

## Por que importa

Configuração incorreta pode produzir somente o clip ativo ou um conjunto duplicado e difícil de usar.

## Como funciona

Ative a estratégia de exportação adequada às Actions presentes e confirme que nomes e ranges são independentes.

## Exemplo

O rig de um inimigo exporta patrulha e ataque como dois clips sem mesclar intervalos nem duplicar root motion.

## Limites e trade-offs

Nomes que colidem ou strips sobrepostos podem impedir associação intuitiva no destino.

## Como verificar

Conte clips após importação e valide que cada nome aciona a animação prevista sem referência ao estado original do arquivo.

## Conexões
- [[blender-checar-compatibilidade-de-animacao-gltf]] — Blender: checar compatibilidade de animação glTF.
- [[blender-separar-movimento-in-place-e-root-motion]] — Blender: separar movimento in-place e root motion.

## Fontes
- [Blender Manual — Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) — Descreve ações e seu uso para organizar dados de animação no Blender. Consulta: 2026-10-04.
- [Blender Manual — glTF 2.0 export](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html) — Documenta opções, objetos e animações suportados pela exportação glTF do Blender. Consulta: 2026-10-04.
