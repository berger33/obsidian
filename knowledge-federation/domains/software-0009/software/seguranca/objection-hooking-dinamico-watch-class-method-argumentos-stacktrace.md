---
id: software.seguranca.tranche11.001048
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/sensepost/objection/master/README.md", "https://github.com/sensepost/objection/wiki/Patching-Android-Applications"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Engenharia Reversa Dinâmica sem Decompilação no `objection`: Rastreamento de Classes, Argumentos, Retornos e **Stack Traces (`--dump-args --dump-return --dump-backtrace`)**

## Em uma frase
Quando você analisa um aplicativo Android ou iOS altamente ofuscado (onde o R8/DexGuard ou um ofuscador LLVM renomeou pacotes e embaralhou o fluxo de controle), tentar seguir a lógica apenas lendo o código estático pode levar dias.

## Por que importa
No `objection`, os comandos **`android hooking search classes <termo>`** / **`ios hooking search classes <termo>`** e **`watch class_method`** transformam o próprio runtime do aplicativo em um oráculo: você pede para o `objection` observar uma classe inteira (`watch class`) ou um método específico com as três flags **`--dump-args`**, **`--dump-return`** e **`--dump-backtrace`**!

## Como funciona
No exato instante em que você toca no botão da interface do aplicativo, o `objection` imprime no terminal **quais valores foram passados nos argumentos, qual valor o método retornou e a pilha completa de chamadas (*Backtrace / Call Stack*) mostrando qual método ofuscado `a.b.c()` chamou aquela função**!

## Exemplo
```text
# Rastrear um metodo no Android imprimindo automaticamente seus argumentos, valor de retorno e a pilha de chamadas (backtrace)
com.empresa.mobileapp on (Android: 14) [usb] # android hooking search methods gerarAssinaturaHmac
com.empresa.mobileapp on (Android: 14) [usb] # android hooking watch class_method com.empresa.crypto.Signer.gerarAssinaturaHmac --dump-args --dump-return --dump-backtrace
```

## Limites e trade-offs
Combine esse workflow do `objection` com o **JADX (`jadx-gui`)**: use o `watch class_method ... --dump-backtrace` no `objection` para descobrir exatamente quais classes são executadas quando você realiza uma transação no app, e então abra diretamente aquelas classes no `jadx-gui` para analisar a implementação!

## Como verificar
No iOS, a sintaxe equivalente para rastrear métodos Objective-C com argumentos e backtrace é `ios hooking watch method "+[NSURL urlWithString:]" --dump-args --dump-return --dump-backtrace`.

## Conexões
- [[objection-inspecao-memoria-memory-dump-search-write-sqlite-files]] — Veja também: Auditoria de Memória RAM e Bancos Locais no `objection`: **`memory dump`**, **`memory search`**, **`sqlite connect`** e Proteção de Dados em Repouso (**SQLCipher**).
- [[objection-sistema-plugins-customizados-importacao-scripts-frida-api]] — Veja também: Extensibilidade do `objection`: Sistema de **Plugins (`plugin load`)**, Execução de Scripts Frida (`import`) e API REST (`--api-host` / `--api-port`).
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.
- [[jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin]] — Referência cruzada direta com jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
