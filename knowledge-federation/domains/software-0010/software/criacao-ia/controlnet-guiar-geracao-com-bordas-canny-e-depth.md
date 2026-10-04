---
id: software.criacao_ia.tranche02.000163
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

# ControlNet: guiar geração de assets com mapas de borda Canny e profundidade

## Em uma frase
O ControlNet condiciona a síntese generativa a restrições estruturais de geometria através de detectores de borda e mapas de profundidade.

## Por que importa
A geração pura baseada em texto livre altera a silhueta, escala e contornos fundamentais de modelos e concept arts a cada iteração.

## Como funciona
Extraia as bordas de uma malha 3D com o filtro Canny ou renderize o buffer de profundidade (*Z-Depth*) da câmera para guiar a síntese de novos estilos sem perder a proporção original do objeto.

## Exemplo
```text
// Pipeline de composicao com ControlNet
[Render 3D de Referencia] ──► [Preprocessador Canny] ──┐
                                                      ▼
[Prompt: "Textura de madeira envelhecida"] ──► [ControlNet + SD] ──► [Asset Texturizado]
```

## Limites e trade-offs
Pesos de ControlNet muito elevados (`weight > 1.2`) provocam saturação de cores e artefatos escuros ao redor das linhas de borda.

## Como verificar
Renderize o asset gerado sobre a malha original no Blender e verifique se as linhas e cantos coincidem perfeitamente com a geometria.

## Conexões
- [[texturas-ia-derivar-mapas-de-normal-e-roughness]] — Veja também: Texturas com IA: derivar mapas de normal e roughness de alturas.
- [[controlnet-fixar-postura-de-sprites-com-openpose]] — Veja também: ControlNet: fixar postura anatômica de sprites 2D com OpenPose.
- [[concept-art-ia-refinar-detalhes-com-inpainting]] — Conexão temática direta com concept-art-ia-refinar-detalhes-com-inpainting.
- [[blender-exportar-somente-o-conteudo-necessario]] — Conexão temática direta com blender-exportar-somente-o-conteudo-necessario.

## Fontes
- [Blender Manual — Texture Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html) — Documentação técnica cobrindo grafos de textura, nós de bump/normal e mapeamento pbr. Consulta: 2026-10-04.
- [Blender Manual — Texture Painting & Mapping](https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html) — Manual cobrindo projeção de texturas, pintura digital, alinhamento uv e materiais tileáveis. Consulta: 2026-10-04.
