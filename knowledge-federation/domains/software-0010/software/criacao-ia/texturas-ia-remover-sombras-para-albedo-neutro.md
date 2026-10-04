---
id: software.criacao_ia.tranche02.000167
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

# Texturas com IA: remover sombras embutidas para obter albedo neutro

## Em uma frase
A remoção de sombras duras e pontos de iluminação direcional (delighting) é fundamental para que o mapa de albedo responda realisticamente ao motor PBR.

## Por que importa
Texturas que já possuem sombras desenhadas nos pixels criam conflitos visuais quando uma tocha ou o sol do jogo incidem sobre o objeto de outro ângulo.

## Como funciona
Aplique filtros de normalização de luminosidade por alta frequência (*high-pass filter*) ou utilize redes neurais de delighting para equalizar a iluminação e extrair a cor base pura do material.

## Exemplo
```text
// Processo de delighting de textura
[Foto/Textura com Sombra Direcional] ──► [High-Pass / Delight Filter] ──► [Mapa Albedo Neutro PBR]
```

## Limites e trade-offs
Remover excessivamente o contraste pode apagar variações legítimas de cor do material (ex.: manchas naturais da madeira ou mármore).

## Como verificar
Carregue o mapa albedo em uma cena 3D e teste com iluminação dinâmica rotativa para validar a consistência visual em todos os ângulos.

## Conexões
- [[spritesheet-ia-empacotar-e-fatiar-atlas-de-sprites]] — Veja também: Sprite Sheets com IA: empacotar e fatiar atlas com margens uniformes.
- [[assets-ia-otimizar-compressao-bc7-e-astc-em-vram]] — Veja também: Otimização de Texturas: comprimir mapas PBR em BC7 e ASTC para VRAM.
- [[texturas-ia-gerar-padroes-pbr-seamless-tileaveis]] — Conexão temática direta com texturas-ia-gerar-padroes-pbr-seamless-tileaveis.
- [[texturas-ia-derivar-mapas-de-normal-e-roughness]] — Conexão temática direta com texturas-ia-derivar-mapas-de-normal-e-roughness.

## Fontes
- [Blender Manual — Texture Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html) — Documentação técnica cobrindo grafos de textura, nós de bump/normal e mapeamento pbr. Consulta: 2026-10-04.
- [Blender Manual — Texture Painting & Mapping](https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html) — Manual cobrindo projeção de texturas, pintura digital, alinhamento uv e materiais tileáveis. Consulta: 2026-10-04.
