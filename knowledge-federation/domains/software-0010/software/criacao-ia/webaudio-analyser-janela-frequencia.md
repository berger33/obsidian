---
id: software.criacao_ia.tranche04.000380
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: AnalyserNode dá o espectro com janela e suavização — não a FFT crua

## Em uma frase
O analyser entrega os dados de frequência/tempo via FFT sobre uma janela (Blackman default) com smoothingTimeConstant — o buffer é um snapshot suavizado, não o bin de cada bloco.

## Por que importa
Visualizações 'que tremem' e 'que lagam' são os dois sintomas de ignorar os dois knobs: sem smoothing os bins saltam entre frames; com smoothing demais a barra não acompanha o transient. E a geometria (fftSize → frequencyBinCount = fftSize/2) define o custo e a resolução ao mesmo tempo — quem 'só quer uma barra bonita' escolhe sem querer os dois.

## Como funciona
Crie com ctx.createAnalyser(), conecte no caminho pós-efeitos (a leitura do que você quer ver, não do dry). Ajuste fftSize (potência de 2, de 32 a 32768; default 2048) — a resolução por bin é sampleRate/fftSize, e getByteFrequencyData preenche Uint8Array de length frequencyBinCount. smoothingTimeConstant (0..1, default 0.8) é a média exponencial temporal; 0 é instantâneo. Para forma de onda no tempo, getByteTimeDomainData no mesmo buffer duplo do lado temporal.

## Exemplo
Um equalizer de visualização reage ao kick sem tremor: fftSize 1024 (bins ~43 Hz a 44.1k), smoothing 0,6 (mais rápido que o default para o transient), e as barras acima de 1 kHz vêm de getByteFrequencyData com índice pré-computado do bin-alvo.

## Limites e trade-offs
Os dados são 8 bits (0–255) com mapeamento por dB — não use para medição precisa (para isso o caminho é getFloatFrequencyData, que devolve dB reais no buffer float). min/maxDecibels (default -100/-30) definem a escala do byte; fora da janela tudo satura branco/preto e a 'forma' vira mentira. O analyser tem tap pass-through (não afeta o áudio, mas cada bloco de FFT custa CPU — 128 canais de análise é budget real). Não há janelas de FFT custom: o type é fixo — a especificação define o processamento interno.

## Como verificar
Um tom puro de 440 Hz no grafo: o pico deve estar no bin round(440/binHz) — a calibração da geometria. Varie smoothingTimeConstant num loop de teste e meça o desvio-std do bin entre frames: é a curva que o knob controla. Compare getByteFrequencyData vs. getFloatFrequencyData no mesmo quadro para validar a decisão de escala.

## Conexões
- [[webaudio-convolver-resposta-ao-impulso]] — Web Audio: ConvolverNode é a reverberação física — e o IR define canal por canal.

## Fontes
- [MDN — AnalyserNode](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode) — documenta fftSize/frequencyBinCount, os getters byte/float e os knobs de suavização/dB Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — a definição do processamento interno de FFT e janela Consulta: 2026-10-04.
