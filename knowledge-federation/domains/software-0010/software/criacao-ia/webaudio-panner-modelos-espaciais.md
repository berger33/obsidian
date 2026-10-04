---
id: software.criacao_ia.tranche04.000378
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/PannerNode", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: PannerNode escolhe como o som se move no espaço — pan, equal power ou HRTF

## Em uma frase
O panner de posição 3D tem três modelos de panning (equalpower, HRTF, stereo) e atende por distância com um dos modelos de atenuação (inverse, linear, exponential), todos configuráveis por atributos do nó.

## Por que importa
A 'espacialização' de um jogo web ou de um áudio-imersivo é a soma dessas duas escolhas; o default (equalpower + inverse) é um compromise que soa plano em fones e exagerado em caixas. HRTF dá a direção com as limitações do modelo (CPU, artefatos de front/back); 'stereo' é o modo barato para conteúdo já mixado. É configuração de mixagem, mas feita em código — a API trata como parâmetros de física.

## Como funciona
Crie com ctx.createPanner(); defina panningModel ('HRTF' para fones com custo de CPU, 'equalpower' padrão, 'stereo' para posições pré-mixadas), distanceModel ('inverse' é fisicamente suave; 'linear' para atenuação previsível; 'exponential' para falloff rápido) e a geometria: refDistance, maxDistance, rolloffFactor, cone (coneInnerAngle etc. para diretividade da fonte). A posição da fonte é movida pelo AudioListener (ctx.listener) — a API é source-listener, não camera-trick.

## Exemplo
Um FPS web: footstep = equalpower/inverse com rolloff calibrado, tiros = HRTF (direção importa mais que CPU no momento do combate), ambient loop = stereo sem panner — três modelos no mesmo grafo, cada um no seu custo.

## Limites e trade-offs
HRTF usa respostas medidas (a biblioteca é do projeto FHRT — a página documenta a origem) e a performance por-ouvinte é limitada: não é binauralização de sala (reverberação vem do ConvolverNode, nota separada). Cone angles afetam só a atenuação, não o timbre — 'fonte direcional' é meia-voz. E a posição de listener/panner atualizada por frame é barata em atributos, mas cada mudança pode re-renderizar o quantum — nada de ler sensor em loop apertado sem necessidade.

## Como verificar
Um ABX test entre equalpower e HRTF no mesmo conteúdo fone-ouvinte: a diferença de localizabilidade é audível em material com transient — o teste de escolha é este, não o espectro. Meça CPU por nó (chrome://audits ou flamegraph do performance API) com 50 panners em cada modelo. Um fixture de 'fonte passa pela orelha' valida o cone e o rolloff visualmente no medidor de ganho.

## Conexões
- [[webaudio-worklet-port-fio-da-navalha]] — Web Audio: o port do AudioWorkletNode é o fio da navalha entre página e render.
- [[webaudio-convolver-resposta-ao-impulso]] — Web Audio: ConvolverNode é a reverberação física — e o IR define canal por canal.

## Fontes
- [MDN — PannerNode](https://developer.mozilla.org/en-US/docs/Web/API/PannerNode) — lista modelos de panning, de distância e os parâmetros de geometria Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — as fórmulas de atenuação e os detalhes dos modelos Consulta: 2026-10-04.
