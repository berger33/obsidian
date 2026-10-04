---
id: software.criacao_ia.tranche04.000377
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/AudioWorkletNode", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: o port do AudioWorkletNode é o fio da navalha entre página e render

## Em uma frase
A única via de estado entre a página e um AudioWorkletProcessor é a porta de mensagens (node.port / this.port), com postMessage/onmessage — e é aí que se resolve 'como passar o áudio para o DSP'.

## Por que importa
O modelo shared-memory não existe (nem deve): o DSP roda no render thread sem GC nem lock. Passar samples por mensagem é possível e caro; a decisão de arquitetura — controle por mensagem, streaming por outro mecanismo (ex.: SharedArrayBuffer, com as regras de COOP/COEP) — precisa ser tomada cedo, porque refatorar DSP é caro. O port é o único canal garantido.

## Como funciona
No main thread: node.port.postMessage({type:'config', tempo: 0.25}); node.port.onmessage = ev => {...}. No processor: this.port.onmessage trata a fila; o que for estado por-amostra vai num objeto mutável local (this.tempo = ...) que process() lê. Mensagens são assíncronas e podem chegar em qualquer ponto entre quanta — trate como fila de comandos idempotente. Transferência de ownership (transfer list) é como se passa um ArrayBuffer grande sem cópia — no sentido main→worklet e vice-versa.

## Exemplo
Um visualizador com DSP em worklet envia o 'frame rate alvo' por port a cada config change, e recebe do worklet um resumo por quadro (RMS, peak) por postMessage — os samples nunca cruzam a fronteira; a análise que precisa dos buffers usa SharedArrayBuffer como exceção consciente.

## Limites e trade-offs
PortMessage tem latência de estrutura (clonagem): streaming de áudio por port vira GC no render thread — o anti-padrão exato que a API desencoraja. SharedArrayBuffer resolve throughput mas impõe isolamento de contexto (cross-origin isolation) — uma decisão de deploy, não de código. E mensagens não têm ordem garantida com o processo de render — estados transitórios (fade) devem ser interpolados no processador, não esperados prontos.

## Como verificar
Um teste de ida-e-volta: main envia N configs, worklet ecoa o hash do estado final; o resultado é determinístico apesar de timing — prova de que o design de fila funciona. Meça o custo de postMessage com buffers grandes vs. a abordagem resumo-por-quadro — o argumento anti-padrão vira número. No CI, uma verificação de crossOriginIsolated quando o produto usa SAB.

## Conexões
- [[webaudio-audioworklet-modulos-processador]] — Web Audio: AudioWorklet é módulo separado com o seu próprio global scope.
- [[webaudio-panner-modelos-espaciais]] — Web Audio: PannerNode escolhe como o som se move no espaço — pan, equal power ou HRTF.

## Fontes
- [MDN — AudioWorkletNode](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorkletNode) — descreve o port de mensagem do node e o par com o processor Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — a definição normativa do MessagePort do worklet Consulta: 2026-10-04.
