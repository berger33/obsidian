---
id: software.criacao_ia.tranche02.000169
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

# Concept Art com IA: refinar detalhes localizados através de inpainting

## Em uma frase
O inpainting permite corrigir membros, rostos, armas e elementos específicos de uma ilustração sem alterar o restante da composição artística.

## Por que importa
Regenerar a imagem inteira para consertar um detalhe perde variações e poses que já haviam sido aprovadas pela direção de arte.

## Como funciona
Pinte uma máscara sobre a região que contém imperfeições (ex.: dedos extras ou empunhadura torta de espada), descreva a correção no prompt e execute a difusão localizada mantendo as áreas externas intocadas.

## Exemplo
```text
// Fluxo de refinamento por Inpainting
[Concept Art Aprovada com Erro na Mao] ──┐
[Mascara binaria cobrindo a regiao]   ──┼──► [Inpainting Model] ──► [Asset Final Perfeito]
[Prompt: "Mao enluvada segurando arco"] ──┘
```

## Limites e trade-offs
Bordas de máscara mal suavizadas (*feathering*) podem criar descontinuidades visíveis de iluminação ou linhas de corte na imagem final.

## Como verificar
Amplie a área corrigida com zoom de 100% no editor gráfico e confirme a perfeita fusão dos novos pixels com a arte adjacente.

## Conexões
- [[assets-ia-otimizar-compressao-bc7-e-astc-em-vram]] — Veja também: Otimização de Texturas: comprimir mapas PBR em BC7 e ASTC para VRAM.
- [[pipeline-assets-validar-escala-metrica-e-pivots]] — Veja também: Pipeline de Assets: validar escala métrica e pivôs antes do import.
- [[controlnet-guiar-geracao-com-bordas-canny-e-depth]] — Conexão temática direta com controlnet-guiar-geracao-com-bordas-canny-e-depth.
- [[comfyui-ajustar-prompt-sem-quebrar-o-grafo]] — Conexão temática direta com comfyui-ajustar-prompt-sem-quebrar-o-grafo.
- [[documentacao-usar-imagens-acessiveis-e-uteis]] — Conexão temática direta com documentacao-usar-imagens-acessiveis-e-uteis.

## Fontes
- [Blender Manual — Texture Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html) — Documentação técnica cobrindo grafos de textura, nós de bump/normal e mapeamento pbr. Consulta: 2026-10-04.
- [Blender Manual — Texture Painting & Mapping](https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html) — Manual cobrindo projeção de texturas, pintura digital, alinhamento uv e materiais tileáveis. Consulta: 2026-10-04.
