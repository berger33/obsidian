---
id: software.seguranca.tranche07.000652
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

# Frida: Hooking de Funções Nativas C/C++/Rust/Go com **`Interceptor.attach`**, `Interceptor.replace`, `NativePointer` e `NativeFunction`

## Em uma frase
O módulo **`Interceptor`** da API JavaScript do Frida (`frida-gum`) intercepta qualquer função nativa pelo seu endereço de memória (`NativePointer`), permitindo inspecionar/alterar os argumentos na entrada (`onEnter(args)`) e o valor de retorno na saída (`onLeave(retval)`), ou substituir a implementação inteira (`Interceptor.replace`).

## Por que importa
Quando um binário nativo ou biblioteca `libssl.so` / `ncrypt.dll` cifra um payload antes de enviá-lo ao socket, interceptar `SSL_write(ssl, buf, num)` e `SSL_read(ssl, buf, num)` captura o buffer exato em texto claro na memória do processo.

## Como funciona
A classe **`NativePointer`** (`ptr("0x...")`) fornece métodos seguros para leitura e escrita tipada na memória (`readUtf8String()`, `readByteArray(len)`, `readU32()`, `writeByteArray()`), enquanto **`NativeFunction`** permite chamar diretamente qualquer função C exportada pelo processo alvo a partir do JavaScript.

## Exemplo
```javascript
// Interceptar chamadas a SSL_write na libssl.so para auditar payloads antes da criptografia TLS
const sslWritePtr = Module.findExportByName("libssl.so", "SSL_write");
if (sslWritePtr !== null) {
    Interceptor.attach(sslWritePtr, {
        onEnter(args) {
            const buf = args[1];
            const len = args[2].toInt32();
            if (len > 0) {
                console.log("[SSL_write] " + len + " bytes:\n" + hexdump(buf, { length: Math.min(len, 128) }));
            }
        }
    });
}
```

## Limites e trade-offs
O objeto `this` dentro de `onEnter(args)` e `onLeave(retval)` é um armazenamento local por invocação (*thread-local per call*): se você precisar ler em `onLeave` um ponteiro de saída que foi passado como argumento `args[1]` na entrada, salve **`this.outBuf = args[1];`** dentro de `onEnter` e leia `this.outBuf` dentro de `onLeave`!

## Como verificar
Execute o script contra um binário de teste que usa OpenSSL e confirme a impressão do `hexdump` a cada chamada.

## Conexões
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Veja também: Frida: Arquitetura de Instrumentação Dinâmica (`frida-core`, `frida-gum`, Runtimes **QuickJS/V8**) e Modos *Injected*, *Embedded (`frida-gadget`)* e *Preloaded*.
- [[frida-rastreamento-instrucoes-stalker-code-tracing-coverage-cmodule]] — Veja também: Frida: Rastreamento Dinâmico de Instruções e Cobertura com **`Stalker`** (*Dynamic Binary Translation*) e Alta Performance com **`CModule`**.
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Referência cruzada direta com wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab.

## Fontes
- [Frida Official GitHub — Dynamic Instrumentation Toolkit](https://raw.githubusercontent.com/frida/frida/main/README.md) — documentação oficial do Frida cobrindo instalação, bindings Python/Node.js e ferramentas CLI (frida-ps, frida-trace, frida-discover); consultado em 2026-10-03.
- [Frida Official JavaScript API Reference — Interceptor, Stalker, CModule, Java, ObjC & Cloak](https://frida.re/docs/javascript-api/) — referência completa da API JavaScript do Frida para hooking nativo, code tracing Stalker, CModule, pontes mobile e Cloak; consultado em 2026-10-03.
- [Frida Official Documentation — Modes of Operation (Injected, Embedded Gadget, Preloaded)](https://frida.re/docs/modes/) — documentação oficial dos modos de operação do Frida e configuração do frida-gadget; consultado em 2026-10-03.
