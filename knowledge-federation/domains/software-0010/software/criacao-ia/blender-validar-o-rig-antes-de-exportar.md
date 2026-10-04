---
id: software.criacao_ia.tranche01.000065
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

# Blender: validar o rig antes de exportar

## Em uma frase

A estrutura do armature, hierarquia e bind pose influenciam se o movimento pode ser reaplicado corretamente no runtime.

## Por que importa

Consertar incompatibilidade no arquivo fonte é mais confiável do que compensar curvas quebradas depois da importação.

## Como funciona

Confirme hierarquia sem ciclos, orientação, nomes de ossos e transforms aplicados conforme o padrão do projeto.

## Exemplo

O personagem usa root separado para deslocamento e ossos deformadores com nomes que o retargeter do projeto reconhece.

## Limites e trade-offs

Aplicar transform ou renomear ossos depois de animar pode mudar offsets e invalidar clips já aprovados.

## Como verificar

Exporte um clip mínimo e confira bind pose, escala, orientação e deformação do mesh no engine alvo.

## Conexões
- [[blender-conferir-intervalos-de-keyframes]] — Blender: conferir intervalos de keyframes.
- [[blender-exportar-somente-o-conteudo-necessario]] — Blender: exportar somente o conteúdo necessário.

## Fontes
- [Blender Manual — Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) — Descreve ações e seu uso para organizar dados de animação no Blender. Consulta: 2026-10-04.
- [Blender Manual — glTF 2.0 export](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html) — Documenta opções, objetos e animações suportados pela exportação glTF do Blender. Consulta: 2026-10-04.
