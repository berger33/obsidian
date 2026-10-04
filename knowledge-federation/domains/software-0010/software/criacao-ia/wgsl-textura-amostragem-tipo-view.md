---
id: software.criacao_ia.tranche04.000317
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
fontes: ["https://www.w3.org/TR/WGSL/", "https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: amostrar uma textura exige ver o tipo certo, não só o binding

## Em uma frase
A expressão do tipo da textura no shader (f32, i32, u32, depth) precisa coincidir com o viewSampleType do layout — depth texturas só se amostram por comparação.

## Por que importa
Dois bugs clássicos de sampling têm a mesma raiz: declarar 'texture_2d<f32>' sobre uma view de profundidade, ou 'textureSample' sem gradientes controlados dentro de laço divergente. A especificação resolve ambos com tipos de view explícitos e funções separadas (sample vs. sampleCompare vs. load), eliminando a mágica de GL.

## Como funciona
Para cor: textureSample(t, s, uv) em 'texture_2d<f32>'. Para profundidade com shadow map: a textura é 'texture_depth_2d' e só existe textureSampleCompare(t, s, uv, ref). Para leitura sem filtro (manipulação, formato R32*): textureLoad(t, coord, level) com viewSampleType float|sint|uint coerente. Combine com o sampler (filtering, address modes) declarado como entry separada do mesmo grupo — o layout amarra os dois.

## Exemplo
Um PCF 3x3 usa textureSampleCompareLoop num laço de offsets; cada iteração lê uma vizinhança do depth map, e a média vira o termo de sombra — sem o tipo depth no shader, a compilação nem começaria.

## Limites e trade-offs
textureSample com derivação implícita de mip em fluxo divergente é indefinido no fragment — troque por sampleLevel. A restrição de comparação (sem filtro manual) vale só para views de profundidade; formatos de integer exigem minFilter magFilter 'nearest' no sampler para coerência com sample não-comparativo onde a plataforma o permite. A origem (0,0) é o canto superior esquerdo em ambas as APIs — coordenadas de textura vs. framebuffer.

## Como verificar
Troque intencionalmente o viewSampleType do layout e confirme a falha de compatibilidade no createRenderPipeline. Renderize um quad de teste com gradientes conhecidos e leia os deltas de mip via staging para validar a escolha sampleLevel vs. sample. Compare os resultados do seu PCF com uma referência por CPU num mapa pequeno.

## Conexões
- [[wgsl-atomicos-compare-loop]] — WGSL: atômicos só em memória de escrita explícita, e CAS é loop manual.
- [[wgsl-builtins-estagios-corte]] — WGSL: cada estágio expõe apenas os embutidos que fazem sentido para ele.

## Fontes
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — define texturas amostráveis por tipo, sampling de comparação e as funções de load Consulta: 2026-10-04.
- [MDN — WebGPU API (guia)](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) — panorama do pipeline de amostragem: samplers, texturas e bindings Consulta: 2026-10-04.
