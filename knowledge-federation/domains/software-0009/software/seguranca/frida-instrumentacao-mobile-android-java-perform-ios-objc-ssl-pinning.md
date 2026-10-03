---
id: software.seguranca.tranche07.000654
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

# Frida: Auditoria de Segurança Mobile (**OWASP MASVS**) — Pontes **`Java.perform`** (Android ART/Dalvik) e **`ObjC.classes`** (iOS/macOS Objective-C)

## Em uma frase
Além da camada nativa C/C++, o Frida fornece pontes completas de tempo de execução (**`Java`** para máquinas virtuais Android ART/Dalvik e JVM, e **`ObjC`** para o runtime Objective-C da Apple em iOS/macOS) para auditar aplicativos mobile segundo o padrão **OWASP MASVS (*Mobile Application Security Verification Standard*)**.

## Por que importa
Permite inspecionar objetos vivos no heap (`Java.choose` / `ObjC.choose`), interceptar métodos Java sobrecarregados (`overload(...)`), auditar armazenamento inseguro no *Keystore/Keychain* e validar a implementação de *Certificate Pinning* e detecção de *Root/Jailbreak* durante pentests mobile autorizados.

## Como funciona
No Android, todo código que interage com a VM Java deve ser envolvido em **`Java.perform(() => { ... })`**, obtendo a referência da classe com **`Java.use("pacote.NomeDaClasse")`** e substituindo `.implementation = function(...) { ... }`; no iOS, **`ObjC.classes.NSURLSession`** expõe diretamente os seletores Objective-C para o `Interceptor.attach`.

## Exemplo
```javascript
// Auditar chamadas de criptografia javax.crypto.Cipher.doFinal na VM Android ART via Java.perform
Java.perform(() => {
    const Cipher = Java.use("javax.crypto.Cipher");
    const doFinalBytes = Cipher.doFinal.overload("[B");
    doFinalBytes.implementation = function (inputBytes) {
        console.log("[Android Cipher] Algoritmo: " + this.getAlgorithm());
        return doFinalBytes.call(this, inputBytes);
    };
});
```

## Limites e trade-offs
Quando um método Java possui múltiplas sobrecargas (*overloads* com assinaturas de parâmetros diferentes), chame explicitamente **`.overload('java.lang.String', 'int')`** antes de atribuir `.implementation`, caso contrário o Frida lançará um erro listando todas as assinaturas disponíveis.

## Como verificar
Execute o script contra um app Android de homologação e confirme a captura do algoritmo retornado por `this.getAlgorithm()`.

## Conexões
- [[frida-rastreamento-instrucoes-stalker-code-tracing-coverage-cmodule]] — Veja também: Frida: Rastreamento Dinâmico de Instruções e Cobertura com **`Stalker`** (*Dynamic Binary Translation*) e Alta Performance com **`CModule`**.
- [[frida-inspecao-memoria-memory-scan-memoryaccessmonitor-apiresolver]] — Veja também: Frida: Varredura de Memória em Tempo Real (`Memory.scan`, `Process.enumerateRanges`), **`MemoryAccessMonitor`** e **`ApiResolver`**.
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.
- [[frida-empacotamento-frida-gadget-configuracao-sem-root-jailbreak]] — Referência cruzada direta com frida-empacotamento-frida-gadget-configuracao-sem-root-jailbreak.
- [[testssl-simulacao-clientes-tls-compatibilidade-navegadores-java-openssl]] — Referência cruzada direta com testssl-simulacao-clientes-tls-compatibilidade-navegadores-java-openssl.

## Fontes
- [Frida Official GitHub — Dynamic Instrumentation Toolkit](https://raw.githubusercontent.com/frida/frida/main/README.md) — documentação oficial do Frida cobrindo instalação, bindings Python/Node.js e ferramentas CLI (frida-ps, frida-trace, frida-discover); consultado em 2026-10-03.
- [Frida Official JavaScript API Reference — Interceptor, Stalker, CModule, Java, ObjC & Cloak](https://frida.re/docs/javascript-api/) — referência completa da API JavaScript do Frida para hooking nativo, code tracing Stalker, CModule, pontes mobile e Cloak; consultado em 2026-10-03.
- [Frida Official Documentation — Modes of Operation (Injected, Embedded Gadget, Preloaded)](https://frida.re/docs/modes/) — documentação oficial dos modos de operação do Frida e configuração do frida-gadget; consultado em 2026-10-03.
