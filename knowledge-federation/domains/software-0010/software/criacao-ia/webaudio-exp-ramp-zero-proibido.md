---
id: software.criacao_ia.tranche04.000374
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/AudioParam/exponentialRampToValueAtTime", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: exponentialRampToValueAtTime não passa por zero — nem começando nem terminando nele

## Em uma frase
A rampa exponencial exige que o valor atual e o alvo sejam ambos não-zero (e de mesmo sinal); zero em qualquer ponta lança exceção — a matemática da interpolação multiplicativa não tem porta para o nada.

## Por que importa
Fade-out exponencial é a curva 'musical' padrão (o ouvido responde log), e o primeiro reflexo é 'ramp to 0' — que é justamente o caso ilegal. O segundo reflexo de alguns (ramp from 0) também é ilegal. Conhecer a dupla restrição evita a gambiarra do '0.0001' que, somada ao linearRamp, aparece em todo codebase de áudio web não revisado.

## Como funciona
Padrão correto do fade-out exponencial: um valor inicial não-zero (ex.: 0.001 como piso prático, não o 0 matemático) → ramp até lá com exponentialRamp, e setValueAtTime(0, fim) discreto para o corte — o salto audível de 0.001 em ganho é inaudível por definição. Para fades simétricos, use a mesma técnica espelhada, ou OfflineAudioContext para gerar a curva na mão. A restrição é documentada como 'throw' — capturar a exceção e não o bug é antipadrão: valide antes de agendar.

## Exemplo
Um synth polifônico que aplica 'release' com setTargetAtTime(0.0005, now, dt) seguido de stop no nó após a cauda — sem exceção, sem clique, sem mágica de -60 dB hardcoded.

## Limites e trade-offs
A regra de mesmo sinal (não ir de positivo a negativo pela rampa) pega quem tenta crossfade direcional. O 'piso 0.0001' não é norma da API — é convenção; o corte final real depende do stop agendado do source, não do parâmetro. Em parâmetros de filtro (frequency, Q), o zero tem outro significado (freq ≥ nyquist/Nyquist-clamping) — a técnica do piso não é portátil entre AudioParams.

## Como verificar
Um teste unitário que chama exponentialRamp para 0 e afirma a exceção — a regra como assert. Renderize o fade via OfflineAudioContext e meça o último bloco: a queda de 0.001→0 não deve produzir clique (RMS do jump < limiar). Um lint caseiro nos agendamentos (procurar expRamp com target 0) pega o reflexo no code review.

## Conexões
- [[webaudio-settargetattime-constante-tempo]] — Web Audio: setTargetAtTime é o easing exponencial — a constante define 63%, não o fim.
- [[webaudio-decodeaudiodata-ressample-completo]] — Web Audio: decodeAudioData ressampleia para o contexto e exige o dado completo.

## Fontes
- [MDN — AudioParam: exponentialRampToValueAtTime()](https://developer.mozilla.org/en-US/docs/Web/API/AudioParam/exponentialRampToValueAtTime) — documenta as exceções por valor zero nos dois lados da rampa Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — a restrição de sinal das exponenciais na automação Consulta: 2026-10-04.
