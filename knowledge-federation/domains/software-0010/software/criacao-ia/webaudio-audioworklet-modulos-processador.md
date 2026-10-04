---
id: software.criacao_ia.tranche04.000376
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet/registerProcessor", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: AudioWorklet é módulo separado com o seu próprio global scope

## Em uma frase
O processador de áudio via worklet é registrado por addModule(num arquivo JS) no audioWorklet — um scope dedicado, fora do main thread, com AudioWorkletProcessor de onde o laço process() sai.

## Por que importa
Substituir o ScriptProcessorNode (deprecated) não é copiar código: o modelo é outro — o arquivo do processador é um módulo carregado no contexto de render, onde o main thread não pode bloqueá-lo. Quem envia o closure 'que já estava pronto' da página descobre que nada é visível ali dentro: o módulo é fronteira física.

## Como funciona
Estrutura mínima: um .js exportando 'class MeuProcessador extends AudioWorkletProcessor { process(inputs, outputs, parameters) { ...; return true; } }; registerProcessor("meu-processador", MeuProcessador);', carregado com await ctx.audioWorklet.addModule('/meu-processador.js'), instanciado com new AudioWorkletNode(ctx, 'meu-processador'). O laço process() roda a cada quantum (128 amostras), recebe os canais de entrada e escreve nos de saída; retornar true mantém vivo, false finaliza o node. Parâmetros AudioParam vêm no terceiro argumento, já atualizados.

## Exemplo
Um delay com feedback que precisa de jitter-zero: o main thread só muda o parâmetro de tempo (setTargetAtTime no AudioParam exposto), e o processador consome o valor por amostra no quantum — zero dependência do timing de eventos do navegador.

## Limites e trade-offs
O scope do worklet não tem DOM nem a maior parte das APIs web; ele processa áudio. Comunicação com a página é port (nota separada) — variáveis compartilhadas não existem. O quantum é fixo (128 frames) e a latência do laço é o quantum, não o que você espera do 'tempo real do SO'. addModule resolve URLs como módulos ES (export/import funcionam), e o arquivo precisa ser CORS-correct — CDNs sem CORS quebram o carregamento com erro de módulo, não de áudio.

## Como verificar
Um fixture mínimo que ecoa entrada em saída e roda numa suíte Playwright: se o audio render funciona e o main thread fica livre (o FPS da página não cai com o nó ativo), o modelo está correto. Return false no process: o node finaliza e para de consumir — o teste do contrato. Um módulo cross-origin sem CORS: confirme a falha de addModule documentada e a mensagem.

## Conexões
- [[webaudio-decodeaudiodata-ressample-completo]] — Web Audio: decodeAudioData ressampleia para o contexto e exige o dado completo.
- [[webaudio-worklet-port-fio-da-navalha]] — Web Audio: o port do AudioWorkletNode é o fio da navalha entre página e render.

## Fontes
- [MDN — AudioWorklet: registerProcessor()](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet/registerProcessor) — o registro do processor class no contexto de áudio Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — define o modelo de worklet, o quantum e o contrato process() Consulta: 2026-10-04.
