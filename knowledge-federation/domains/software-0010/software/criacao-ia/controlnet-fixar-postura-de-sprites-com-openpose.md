---
id: software.criacao_ia.tranche02.000164
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

# ControlNet: fixar postura anatômica de sprites 2D com OpenPose

## Em uma frase
O modelo OpenPose extrai e fixa esqueletos anatômicos de personagens para orientar a geração de quadros de spritesheets 2D.

## Por que importa
Gerar poses sequenciais para sprites 2D sem controle esquelético resulta em membros com comprimentos variáveis e proporções corporais inconsistentes.

## Como funciona
Capture a pose desejada a partir de uma gravação real ou boneco 3D de referência, gere o esqueleto colorido OpenPose e envie-o como entrada de controle para sintetizar o personagem no estilo artístico pretendido.

## Exemplo
```text
// Pipeline de geracao de sprite com OpenPose
[Esqueleto OpenPose (Keyframe de Corrida)] ──┐
                                            ▼
[Prompt: "Guerreiro medieval pixel art"] ──► [ControlNet OpenPose] ──► [Sprite do Quadro]
```

## Limites e trade-offs
O OpenPose pode falhar na detecção de dedos finos, armas longas ou sobreposições complexas de braços na frente do torso.

## Como verificar
Confira a anatomia das juntas geradas e ajuste manualmente os pontos esqueléticos caso haja deslocamento nas mãos ou pés.

## Conexões
- [[controlnet-guiar-geracao-com-bordas-canny-e-depth]] — Veja também: ControlNet: guiar geração de assets com mapas de borda Canny e profundidade.
- [[pixel-art-ia-alinhar-a-grade-e-limitar-paleta]] — Veja também: Pixel Art com IA: alinhar arte à grade de pixels e limitar contagem de cores.
- [[spritesheet-ia-empacotar-e-fatiar-atlas-de-sprites]] — Conexão temática direta com spritesheet-ia-empacotar-e-fatiar-atlas-de-sprites.
- [[blender-validar-o-rig-antes-de-exportar]] — Conexão temática direta com blender-validar-o-rig-antes-de-exportar.

## Fontes
- [Blender Manual — Texture Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html) — Documentação técnica cobrindo grafos de textura, nós de bump/normal e mapeamento pbr. Consulta: 2026-10-04.
- [Blender Manual — Texture Painting & Mapping](https://docs.blender.org/manual/en/latest/sculpt_paint/painting/texture_paint/index.html) — Manual cobrindo projeção de texturas, pintura digital, alinhamento uv e materiais tileáveis. Consulta: 2026-10-04.
