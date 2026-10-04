---
id: software.criacao_ia.tranche02.000170
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
fontes: ["https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html", "https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Pipeline de Assets: validar escala métrica e pivôs antes do import

## Em uma frase
A padronização de unidades métricas e posicionamento de pontos pivô evita desalinhamentos e problemas de colisão em engines de jogos.

## Por que importa
Modelos ou sprites importados com escalas díspares exigem correções manuais constantes em cada instância na cena do jogo.

## Como funciona
Valide que 1 unidade do software de criação corresponde exatamente a 1 metro na engine (escala 1.0) e posicione o pivô na base do modelo para facilitar o encaixe no chão.

## Exemplo
```python
# Script de validacao de pivot e escala em objetos selecionados no Blender
import bpy

for obj in bpy.context.selected_objects:
    if obj.type == 'MESH':
        print(f"Objeto: {obj.name}

## Limites e trade-offs
Escala: {obj.scale}

## Como verificar
Dimensões: {obj.dimensions}")
        assert obj.scale == (1.0, 1.0, 1.0), f"Escala nao aplicada no objeto {obj.name}"
```

## Conexões
- [[concept-art-ia-refinar-detalhes-com-inpainting]] — Veja também: Concept Art com IA: refinar detalhes localizados através de inpainting.

## Fontes
- [Blender Manual — Texture Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html) — Documentação técnica cobrindo grafos de textura, nós de bump/normal e mapeamento pbr. Consulta: 2026-10-04.
- [Blender Manual — Texture Painting & Mapping](https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html) — Manual cobrindo projeção de texturas, pintura digital, alinhamento uv e materiais tileáveis. Consulta: 2026-10-04.
