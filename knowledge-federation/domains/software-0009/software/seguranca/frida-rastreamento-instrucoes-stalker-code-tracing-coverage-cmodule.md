---
id: software.seguranca.tranche07.000653
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/frida/frida/main/README.md", "https://frida.re/docs/javascript-api/", "https://frida.re/docs/modes/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Frida: Rastreamento Dinâmico de Instruções e Cobertura com **`Stalker`** (*Dynamic Binary Translation*) e Alta Performance com **`CModule`**

## Em uma frase
O motor **`Stalker`** do Frida realiza **tradução binária dinâmica (*Dynamic Binary Translation*) no nível de thread**: ele copia os blocos básicos de código da thread monitorada para um cache em memória, instrumenta cada instrução/chamada/salto/retorno (`call`, `ret`, `exec`, `block`, `compile`) e executa o código recompilado sem nunca deixar a thread escapar do monitoramento.

## Por que importa
Enquanto o `Interceptor` exige saber previamente qual endereço de função você quer interceptar, o **`Stalker.follow(threadId, ...)`** rastreia todas as funções, blocos básicos e instruções executadas por uma thread (ideal para *Differential Coverage*, *Fuzzing* e desofuscação de *Control-Flow Flattening* / *OLLVM*).

## Como funciona
Como um callback JavaScript invocado milhões de vezes por segundo pelo `Stalker` ou `Interceptor` causaria lentidão, a classe **`CModule`** compila em tempo real (usando o compilador *TinyCC* embutido no Frida) um trecho de código **C puro** diretamente para código de máquina na memória do processo, executando os callbacks `onEnter` / `transform` na velocidade nativa da CPU!

## Exemplo
```javascript
// Rastrear blocos basicos (compile) executados pela thread principal usando Stalker
const mainThread = Process.enumerateThreads()[0];
Stalker.follow(mainThread.id, {
    events: { compile: true },
    onReceive(events) {
        const parsed = Stalker.parse(events, { annotate: true, stringify: true });
        console.log("[Stalker Blocks] Recebidos: " + parsed.length);
    }
});
```

## Limites e trade-offs
Para encerrar o rastreamento de uma thread limpa e imediatamente, chame `Stalker.unfollow(threadId)` seguido de `Stalker.flush()` e `Stalker.garbageCollect()`.

## Como verificar
Teste `Stalker.follow` em uma função específica (ligando o `Stalker.follow(this.threadId)` no `onEnter` do `Interceptor` e desligando com `Stalker.unfollow(this.threadId)` no `onLeave`) para capturar apenas o rastro exato daquela função.

## Conexões
- [[frida-hooking-nativo-interceptor-attach-replace-nativefunction-nativepointer]] — Veja também: Frida: Hooking de Funções Nativas C/C++/Rust/Go com **`Interceptor.attach`**, `Interceptor.replace`, `NativePointer` e `NativeFunction`.
- [[frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning]] — Veja também: Frida: Auditoria de Segurança Mobile (**OWASP MASVS**) — Pontes **`Java.perform`** (Android ART/Dalvik) e **`ObjC.classes`** (iOS/macOS Objective-C).
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.
- [[ghidra-depurador-dinamico-debugger-gdb-lldb-dbgeng-trace-time-travel]] — Referência cruzada direta com ghidra-depurador-dinamico-debugger-gdb-lldb-dbgeng-trace-time-travel.

## Fontes
- [Frida Official GitHub — Dynamic Instrumentation Toolkit](https://raw.githubusercontent.com/frida/frida/main/README.md) — documentação oficial do Frida cobrindo instalação, bindings Python/Node.js e ferramentas CLI (frida-ps, frida-trace, frida-discover); consultado em 2026-10-03.
- [Frida Official JavaScript API Reference — Interceptor, Stalker, CModule, Java, ObjC & Cloak](https://frida.re/docs/javascript-api/) — referência completa da API JavaScript do Frida para hooking nativo, code tracing Stalker, CModule, pontes mobile e Cloak; consultado em 2026-10-03.
- [Frida Official Documentation — Modes of Operation (Injected, Embedded Gadget, Preloaded)](https://frida.re/docs/modes/) — documentação oficial dos modos de operação do Frida e configuração do frida-gadget; consultado em 2026-10-03.
