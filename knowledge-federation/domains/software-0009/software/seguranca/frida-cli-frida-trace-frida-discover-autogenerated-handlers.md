---
id: software.seguranca.tranche07.000656
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

# Ferramentas CLI do Frida: Rastreamento Instantâneo com **`frida-trace`** (`-i`, `-I`, `-a`, `-j`, `-m`) e **`frida-discover`**

## Em uma frase
O utilitário de linha de comando **`frida-trace`** (`pip install frida-tools`) permite começar a rastrear chamadas de funções nativas, métodos Java ou métodos Objective-C em poucos segundos sem precisar escrever um script do zero: ele gera automaticamente um arquivo JavaScript de *handler* em `__handlers__/` para cada função encontrada e recarrega os handlers ao vivo sempre que você os edita!

## Por que importa
Durante a triagem rápida de um binário desconhecido, rodar `frida-trace -i "open*" -i "connect" -f ./binario` mostra imediatamente na tela, com indentação por profundidade de pilha e cores por thread, todos os arquivos e conexões de rede abertos pelo processo.

## Como funciona
As flags do `frida-trace` cobrem todas as camadas: **`-i <glob>`** (funções C exportadas), **`-I <modulo>`** (todas as exportações de uma biblioteca), **`-a <modulo!offset>`** (funções internas sem símbolo público pelo offset relativo ao módulo!), **`-j <classe!metodo>`** (métodos Java no Android) e **`-m <"-[NS* *]">`** (métodos Objective-C no iOS/macOS).

## Exemplo
```bash
# Rastrear chamadas de abertura de arquivos e resolucao DNS em um binario usando frida-trace
frida-trace -i "open*" -i "getaddrinfo" -f /usr/bin/curl -- https://exemplo.com.br
```

## Limites e trade-offs
Depois que o `frida-trace` criar os arquivos em `./__handlers__/<modulo>/<funcao>.js`, basta editar o `onEnter(log, args, state)` (ex.: adicionando `log("Path: " + args[0].readUtf8String())`) e salvar o arquivo: o `frida-trace` faz *hot-reload* automático sem reiniciar o processo monitorado.

## Como verificar
Inspecione os handlers gerados em `__handlers__/` após rodar o comando acima e verifique a captura do domínio em `getaddrinfo`.

## Conexões
- [[frida-inspecao-memoria-memory-scan-memoryaccessmonitor-apiresolver]] — Veja também: Frida: Varredura de Memória em Tempo Real (`Memory.scan`, `Process.enumerateRanges`), **`MemoryAccessMonitor`** e **`ApiResolver`**.
- [[frida-comunicacao-bidirecional-rpc-exports-send-recv-python-host]] — Veja também: Frida: Comunicação Bidirecional Host-Agente (`send`/`recv`) e Exposição de Funções Internas como **API RPC (`rpc.exports`)** em Python.
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.
- [[frida-hooking-nativo-interceptor-attach-replace-nativefunction-nativepointer]] — Referência cruzada direta com frida-hooking-nativo-interceptor-attach-replace-nativefunction-nativepointer.

## Fontes
- [Frida Official GitHub — Dynamic Instrumentation Toolkit](https://raw.githubusercontent.com/frida/frida/main/README.md) — documentação oficial do Frida cobrindo instalação, bindings Python/Node.js e ferramentas CLI (frida-ps, frida-trace, frida-discover); consultado em 2026-10-03.
- [Frida Official JavaScript API Reference — Interceptor, Stalker, CModule, Java, ObjC & Cloak](https://frida.re/docs/javascript-api/) — referência completa da API JavaScript do Frida para hooking nativo, code tracing Stalker, CModule, pontes mobile e Cloak; consultado em 2026-10-03.
- [Frida Official Documentation — Modes of Operation (Injected, Embedded Gadget, Preloaded)](https://frida.re/docs/modes/) — documentação oficial dos modos de operação do Frida e configuração do frida-gadget; consultado em 2026-10-03.
