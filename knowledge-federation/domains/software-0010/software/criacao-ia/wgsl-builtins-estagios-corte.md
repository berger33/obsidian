---
id: software.criacao_ia.tranche04.000318
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://www.w3.org/TR/WGSL/", "https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: cada estágio expõe apenas os embutidos que fazem sentido para ele

## Em uma frase
Variáveis @builtin dão ao shader posições e índices do sistema, mas a lista disponível é por estágio e o espaço de coordenadas muda na saída do vertex.

## Por que importa
Assumir que 'position' significa o mesmo nas três funções de um material é fonte de bugs de culling e de profundidade: na saída do vertex é clip space; no fragment é coordenada de framebuffer com Y para baixo; e o espaço de profundidade da WebGPU vai de 0 a 1, diferente do GL [-1,1] que muitos portadores carregam na memória muscular.

## Como funciona
Vertex: entrada @builtin(vertex_index)/@builtin(instance_index) com draw procedimental; saída com position em clip space (w implícito) e dados interpolados anotados @location(n). Fragment: @builtin(position) é a coordenada framebuffer (origin no canto superior esquerdo, y crescente para baixo) e @builtin(front_facing)/@builtin(sample_index) onde habilitado. Compute: @builtin(global_invocation_id/local_invocation_id/workgroup_id) mais num_workgroups no dispatch. Profundidade fora de [-1,1] exige reescalonamento manual em port de GL.

## Exemplo
O quad fullscreen de pós-processamento não lê buffer de vértices: usa @builtin(vertex_index) num draw de 3 triângulos e deriva UV de 'position.xy' já na resolução do canvas.

## Limites e trade-offs
Nem todo builtin existe em todo estágio (sample_index só com multisample; frag_depth só quando o render pass o aceita), e usar um não-disponível é erro de compilação, não de link de runtime. O Y invertido em fragment position pega portadores de GL de surpresa — a correção de eixo deve estar centralizada.

## Como verificar
Escreva um programa mínimo que grava @builtin(position) numa textura de debug e confirme a origem/escala na janela do dispositivo. Num port GL, compare o resultado da sombra com a fórmula reescalada de profundidade antes e depois. A listagem de builtins por estágio na especificação serve como checklist de revisão.

## Conexões
- [[wgsl-textura-amostragem-tipo-view]] — WGSL: amostrar uma textura exige ver o tipo certo, não só o binding.
- [[wgsl-uniformidade-amostragem]] — WGSL: fluxo divergente e operações uniformes — uma análise, não uma sugestão.

## Fontes
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — lista de builtins por estágio e espaços de coordenadas normativos Consulta: 2026-10-04.
- [MDN — GPUShaderModule](https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule) — exemplo canônico usa @builtin(position) e @location na estrutura de pipeline básico Consulta: 2026-10-04.
