---
id: software.seguranca.tranche07.000658
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

# Frida: Instrumentação sem Root/Jailbreak com **`frida-gadget`** e Modos de Operação (`listen`, `connect`, `script`, `script-directory`)

## Em uma frase
Quando o dispositivo iOS ou Android de teste não possui *jailbreak*/*root* (ou quando se testa um perfil corporativo MDM onde o `frida-server` não pode rodar como `root`), o Frida opera em modo **Embedded** através da biblioteca compartilhada **`frida-gadget`** (`libfrida-gadget.so` no Android, `FridaGadget.dylib` no iOS/macOS, `frida-gadget.dll` no Windows).

## Por que importa
Ao adicionar uma dependência `DT_NEEDED` (via `patchelf --add-needed libfrida-gadget.so` ou `System.loadLibrary("frida-gadget")` no Smali) e re-assinar o APK/IPA de homologação, o próprio aplicativo carrega o `frida-gadget` no seu próprio espaço de memória com as permissões do próprio app.

## Como funciona
O comportamento do `frida-gadget` é controlado por um arquivo de configuração JSON com o mesmo nome (`libfrida-gadget.config.so`), que suporta quatro modos de **`interaction.type`**: **`listen`** (abre socket local/USB aguardando o cliente Frida), **`connect`** (conecta de saída a um `frida-portal`), **`script`** (executa um arquivo `.js` embutido de forma autônoma) e **`script-directory`**.

## Exemplo
```json
{
  "interaction": {
    "type": "script",
    "path": "/data/local/tmp/autonomous_audit.js",
    "on_change": "reload"
  }
}
```

## Limites e trade-offs
Usar `"type": "script"` no arquivo de configuração do `frida-gadget` renomeado evita abrir a porta TCP padrão `27042` do Frida (que muitos SDKs anti-tampering procuram via scan de portas local).

## Como verificar
Verifique com `frida-ps -U` a conexão ao aplicativo instrumentado com o `frida-gadget` em um dispositivo Android sem root.

## Conexões
- [[frida-comunicacao-bidirecional-rpc-exports-send-recv-python-host]] — Veja também: Frida: Comunicação Bidirecional Host-Agente (`send`/`recv`) e Exposição de Funções Internas como **API RPC (`rpc.exports`)** em Python.
- [[frida-desempacotamento-memoria-malware-dex-pe-elf-dumping]] — Veja também: Frida: Extração Dinâmica de Payloads Desempacotados em Memória (DEX Android, Módulos PE/ELF e Strings Decifradas).
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.
- [[frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning]] — Referência cruzada direta com frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning.
- [[frida-furtividade-cloak-anti-frida-deteccao-defesa-runtimes]] — Referência cruzada direta com frida-furtividade-cloak-anti-frida-deteccao-defesa-runtimes.

## Fontes
- [Frida Official GitHub — Dynamic Instrumentation Toolkit](https://raw.githubusercontent.com/frida/frida/main/README.md) — documentação oficial do Frida cobrindo instalação, bindings Python/Node.js e ferramentas CLI (frida-ps, frida-trace, frida-discover); consultado em 2026-10-03.
- [Frida Official JavaScript API Reference — Interceptor, Stalker, CModule, Java, ObjC & Cloak](https://frida.re/docs/javascript-api/) — referência completa da API JavaScript do Frida para hooking nativo, code tracing Stalker, CModule, pontes mobile e Cloak; consultado em 2026-10-03.
- [Frida Official Documentation — Modes of Operation (Injected, Embedded Gadget, Preloaded)](https://frida.re/docs/modes/) — documentação oficial dos modos de operação do Frida e configuração do frida-gadget; consultado em 2026-10-03.
