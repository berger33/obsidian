---
id: software.criacao_ia.tranche04.000379
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: ConvolverNode é a reverberação física — e o IR define canal por canal

## Em uma frase
O convolver aplica a resposta-ao-impulso carregada como AudioBuffer; o layout de canais do IR decide o que é mono, estéreo ou surround, e o buffer precisa ter 1, 2 ou 4 canais.

## Por que importa
É a diferença entre 'um reverb' e 'o reverb daquela sala': a API não sintetiza espaço, ela convoluciona — o que o IR medir, o nó entrega. O erro clássico de import (IR estéreo com o normalize ligado que engole a diferença de nível entre salas, ou IR surround de 4 canais montado errado) é decisão de pipeline de assets, não de código de runtime.

## Como funciona
Carregue o WAV/ogg do IR via fetch + decodeAudioData (o ressample para o rate do contexto ocorre ali — nota decodeAudioData), atribua convolver.buffer = irBuffer e ajuste 'normalize' (default true: a convolução é renormalizada para manter o nível; para IRs com ganho autoral, desligue). Canais: 1 = mono-in/mono-out; 2 = estéreo; 4 = a fonte interpreta os dois primeiros canais como o par estéreo do dry... e as duas extras completam o surround (a página documenta o layout esperado). Dry/wet fica fora do nó — faça no grafo (gain em paralelo).

## Exemplo
Um configurador de produto 'em espaços reais': cada sala do configurador troca apenas o buffer do convolver (mesmo grafo, normalize off, levelagem autoral embutida nos IRs ensaiados); o wet/dry por sala é um crossfade no grafo.

## Limites e trade-offs
Convolution é cara (FFT por bloco) — um convolver por grafo estende-se melhor que N por fonte; a atenuação por distância não é dele (combine com panner antes/depois, e decida o routing). IRs longos (>2 s de cauda) aumentam latência de bloco e custo por amostra. O 'normalize' booleano não substitui o headroom da mix — ganho de convolução é conteúdo, não mixagem; um IR 'quente' clipa igual com o normalize on.

## Como verificar
Compare o mesmo IR com normalize on/off num medidor de saída: a diferença de nível é a função documentada. Um sweep mono através do convolver e a medição da resposta confirmam o layout de canais (canal 2 de um IR estéreo deve sair no out L/R como esperado). Meça o custo por cauda (IR de 0,5 s vs 3 s) para dimensionar o budget do produto.

## Conexões
- [[webaudio-panner-modelos-espaciais]] — Web Audio: PannerNode escolhe como o som se move no espaço — pan, equal power ou HRTF.
- [[webaudio-analyser-janela-frequencia]] — Web Audio: AnalyserNode dá o espectro com janela e suavização — não a FFT crua.

## Fontes
- [MDN — ConvolverNode](https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode) — define o papel do buffer de IR, o normalize e o mapeamento de canais Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — as regras de tamanho/canal do AudioBuffer de convolução Consulta: 2026-10-04.
