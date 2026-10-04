---
id: software.criacao_ia.tranche02.000162
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

# Texturas com IA: derivar mapas de normal e roughness de alturas

## Em uma frase
A conversão de mapas de altura gerados por IA em mapas de normais tangentes e rugosidade completa a criação de materiais PBR.

## Por que importa
Superfícies que utilizam apenas o canal difuso sem dados de relevo e refletividade parecem plásticas e sem profundidade sob a iluminação do engine.

## Como funciona
Alimente o mapa de altura (*heightmap*) em nós de filtro Sobel ou plugins de texturização para calcular os gradientes espaciais em RGB (espaço tangente) e inverta tons para derivar a rugosidade (*roughness*).

## Exemplo
```text
// Grafo de geracao de Normal Map no Shader Editor do Blender
[Height / Bump Texture]
        │
        ▼
   [Bump Node] ──► Normal Output ──► [Principled BSDF (Normal)]
```

## Limites e trade-offs
Mapas de normais derivados de fotos com sombras duras criam relevos invertidos e falsas elevações onde havia apenas escuridão visual.

## Como verificar
Inspecione o material sob uma luz rotacional e confirme se as saliências e ranhuras reagem corretamente à direção dos raios de luz.

## Conexões
- [[texturas-ia-gerar-padroes-pbr-seamless-tileaveis]] — Veja também: Texturas com IA: gerar padrões PBR contínuos e sem emendas.
- [[controlnet-guiar-geracao-com-bordas-canny-e-depth]] — Veja também: ControlNet: guiar geração de assets com mapas de borda Canny e profundidade.
- [[texturas-ia-remover-sombras-para-albedo-neutro]] — Conexão temática direta com texturas-ia-remover-sombras-para-albedo-neutro.
- [[assets-ia-otimizar-compressao-bc7-e-astc-em-vram]] — Conexão temática direta com assets-ia-otimizar-compressao-bc7-e-astc-em-vram.

## Fontes
- [Blender Manual — Texture Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html) — Documentação técnica cobrindo grafos de textura, nós de bump/normal e mapeamento pbr. Consulta: 2026-10-04.
- [Blender Manual — Texture Painting & Mapping](https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html) — Manual cobrindo projeção de texturas, pintura digital, alinhamento uv e materiais tileáveis. Consulta: 2026-10-04.
