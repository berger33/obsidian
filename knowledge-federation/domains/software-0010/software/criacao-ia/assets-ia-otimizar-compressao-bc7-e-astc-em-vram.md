---
id: software.criacao_ia.tranche02.000168
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

# Otimização de Texturas: comprimir mapas PBR em BC7 e ASTC para VRAM

## Em uma frase
A compressão em formatos de bloco de GPU (BC7 para desktop e ASTC para mobile) reduz o consumo de memória de vídeo sem perda perceptível de qualidade.

## Por que importa
Texturas salvas em PNG ou JPG descompactam integralmente na VRAM, esgotando rapidamente os limites de hardware gráfico em cenas densas.

## Como funciona
Configure o pipeline de importação da engine para converter mapas de cor para BC7/ASTC e mapas de normal para formatos com preservação de dois canais (BC5 / RGTC).

## Exemplo
```bash
# Inspecionar propriedades de compressao de textura no projeto
# No Unity: TextureImporter.textureCompression = TextureImporterCompression.CompressedHQ
# No Unreal Engine: Texture.CompressionSettings = TC_Default (BC7) / TC_Normalmap (BC5)
```

## Limites e trade-offs
A compressão por blocos pode introduzir pequenos artefatos em gradientes suaves ou textos finos incluídos em interfaces gráficas.

## Como verificar
Verifique o uso de memória no profiler gráfico da engine para confirmar a redução do consumo de textura por cena.

## Conexões
- [[texturas-ia-remover-sombras-para-albedo-neutro]] — Veja também: Texturas com IA: remover sombras embutidas para obter albedo neutro.
- [[concept-art-ia-refinar-detalhes-com-inpainting]] — Veja também: Concept Art com IA: refinar detalhes localizados através de inpainting.
- [[texturas-ia-derivar-mapas-de-normal-e-roughness]] — Conexão temática direta com texturas-ia-derivar-mapas-de-normal-e-roughness.
- [[pipeline-assets-validar-escala-metrica-e-pivots]] — Conexão temática direta com pipeline-assets-validar-escala-metrica-e-pivots.
- [[blender-exportar-somente-o-conteudo-necessario]] — Conexão temática direta com blender-exportar-somente-o-conteudo-necessario.

## Fontes
- [Blender Manual — Texture Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html) — Documentação técnica cobrindo grafos de textura, nós de bump/normal e mapeamento pbr. Consulta: 2026-10-04.
- [Blender Manual — Texture Painting & Mapping](https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html) — Manual cobrindo projeção de texturas, pintura digital, alinhamento uv e materiais tileáveis. Consulta: 2026-10-04.
