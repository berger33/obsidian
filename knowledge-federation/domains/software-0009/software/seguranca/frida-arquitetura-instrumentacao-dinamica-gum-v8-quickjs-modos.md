---
id: software.seguranca.tranche07.000651
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

# Frida: Arquitetura de Instrumentação Dinâmica (`frida-core`, `frida-gum`, Runtimes **QuickJS/V8**) e Modos *Injected*, *Embedded (`frida-gadget`)* e *Preloaded*

## Em uma frase
**Frida** (`frida/frida`, wxWindows Library Licence, criado por Ole André Vadla Ravnås) é o toolkit multiplataforma de instrumentação dinâmica que permite injetar scripts JavaScript/TypeScript (executados pelo motor leve **QuickJS** por padrão ou **V8**) dentro de processos nativos e gerenciados em Windows, macOS, Linux, iOS, Android, watchOS, tvOS e QNX.

## Por que importa
Permite que pesquisadores de segurança, analistas de malware e auditores de aplicações mobile (OWASP MASVS) inspecionem e modifiquem argumentos de funções, valores de retorno, memória RAM e tráfego criptografado em tempo real sem precisar do código-fonte.

## Como funciona
O motor de baixo nível em C (**`frida-gum`**) realiza a reescrita de instruções em memória (`Inline Hooking` e *Code Tracing*), operando em três modos: **(1) Injected** (`frida-server` ou daemon local injeta `frida-agent` em um processo em execução ou via *spawn* `-f`), **(2) Embedded** (embutindo a biblioteca compartilhada **`frida-gadget.so` / `.dylib` / `.dll`** dentro do APK/IPA para dispositivos sem root/jailbreak) e **(3) Preloaded** (`LD_PRELOAD` / `DYLD_INSERT_LIBRARIES`).

## Exemplo
```bash
# Listar processos ativos no dispositivo local ou USB (-U) e anexar script de instrumentacao via CLI do Frida
frida-ps -Uai
frida -U -f com.exemplo.appcorporativo -l /cases/pentest/audit_hooks.js
```

## Limites e trade-offs
Ao usar `frida -f <binario>` (*Spawn Mode*), o Frida cria o processo suspenso na primeira instrução, injeta o agente e aplica todos os seus ganchos **antes** que `main()` ou inicializadores estáticos rodem, garantindo que verificações de inicialização não escapem.

## Como verificar
Verifique `Frida.version` e `Script.runtime` (`"QJS"` ou `"V8"`) no console interativo do Frida para validar o ambiente do agente.

## Conexões
- [[frida-hooking-nativo-interceptor-attach-replace-nativefunction-nativepointer]] — Veja também: Frida: Hooking de Funções Nativas C/C++/Rust/Go com **`Interceptor.attach`**, `Interceptor.replace`, `NativePointer` e `NativeFunction`.
- [[frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning]] — Referência cruzada direta com frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning.
- [[radare2-depuracao-reversivel-checkpoints-dts-rarun2-gdb-frida]] — Referência cruzada direta com radare2-depuracao-reversivel-checkpoints-dts-rarun2-gdb-frida.

## Fontes
- [Frida Official GitHub — Dynamic Instrumentation Toolkit](https://raw.githubusercontent.com/frida/frida/main/README.md) — documentação oficial do Frida cobrindo instalação, bindings Python/Node.js e ferramentas CLI (frida-ps, frida-trace, frida-discover); consultado em 2026-10-03.
- [Frida Official JavaScript API Reference — Interceptor, Stalker, CModule, Java, ObjC & Cloak](https://frida.re/docs/javascript-api/) — referência completa da API JavaScript do Frida para hooking nativo, code tracing Stalker, CModule, pontes mobile e Cloak; consultado em 2026-10-03.
- [Frida Official Documentation — Modes of Operation (Injected, Embedded Gadget, Preloaded)](https://frida.re/docs/modes/) — documentação oficial dos modos de operação do Frida e configuração do frida-gadget; consultado em 2026-10-03.
