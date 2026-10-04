---
id: software.criacao_ia.tranche01.000067
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

# Blender: checar compatibilidade de animação glTF

## Em uma frase

A exportação glTF suporta determinados tipos de curvas e objetos, não todos os recursos possíveis do Blender.

## Por que importa

Saber o limite antes da produção reduz retrabalho com drivers, constraints ou propriedades não transferidas.

## Como funciona

Confronte técnicas do rig com a seção de suporte do exportador e converta ou bake apenas o que o destino exigir.

## Exemplo

Uma animação baseada em constraints é testada com bake para keyframes antes de ser entregue ao pipeline de runtime.

## Limites e trade-offs

Bake pode aumentar chaves e ocultar controle editável; suporte varia por objeto e configuração.

## Como verificar

Faça exportação mínima do recurso usado, reimporte e compare movimento no Blender e no visualizador oficial ou engine.

## Conexões
- [[blender-exportar-somente-o-conteudo-necessario]] — Blender: exportar somente o conteúdo necessário.
- [[blender-controlar-multiplas-actions-no-export]] — Blender: controlar múltiplas Actions no export.

## Fontes
- [Blender Manual — Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) — Descreve ações e seu uso para organizar dados de animação no Blender. Consulta: 2026-10-04.
- [Blender Manual — glTF 2.0 export](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html) — Documenta opções, objetos e animações suportados pela exportação glTF do Blender. Consulta: 2026-10-04.
