---
id: software.seguranca.tranche11.001049
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

# Extensibilidade do `objection`: Sistema de **Plugins (`plugin load`)**, Execução de Scripts Frida (`import`) e API REST (`--api-host` / `--api-port`)

## Em uma frase
Além dos comandos nativos embutidos, o `objection` possui três mecanismos de extensão e automação documentados na wiki oficial (`Plugins`, `Working with Jobs`): **(1) `import <script.js>`** — carrega e injeta qualquer script JavaScript customizado do Frida (por exemplo, um script baixado do *Frida CodeShare*) dentro da sessão atual do `objection`;

## Por que importa
**(2) Sistema de Plugins (`plugin load <pasta>`)** — permite empacotar um script TypeScript/JavaScript Frida junto com uma classe Python (`Plugin`) que registra novos subcomandos nativos no menu do `objection` (como o famoso plugin **`Wallbreaker`** para inspeção profunda de objetos Java na memória ou **`flexdecrypt`** no iOS!); e **(3) Servidor de API HTTP do `objection`**!

## Como funciona
Ao iniciar o `objection` no modo API ou invocar o endpoint RPC do agente, você pode disparar chamadas para métodos internos do aplicativo móvel diretamente a partir de scripts Python externos ou do **Burp Suite / `sqlmap`**!

## Exemplo
```text
# Carregar um script Frida customizado ou um plugin externo dentro de uma sessao ativa do objection
com.empresa.mobileapp on (Android: 14) [usb] # import /cases/mobile/custom_protobuf_decoder.js
com.empresa.mobileapp on (Android: 14) [usb] # plugin load /opt/objection-plugins/Wallbreaker
```

## Limites e trade-offs
Por que expor uma função interna de assinatura criptográfica do app via RPC do Frida/`objection` para um script Python (ou para o `mitmproxy`) é uma técnica tão poderosa em pentests de API? Se o aplicativo móvel assina cada requisição HTTP com uma chave ou algoritmo ofuscado dentro de uma biblioteca nativa `.so`, em vez de reimplementar o algoritmo em Python, você faz o seu script no `mitmproxy` pedir para o próprio aplicativo aberto no celular calcular a assinatura válida para o payload modificado pelo pentester!

## Como verificar
Verifique sempre o código-fonte de qualquer script do Frida CodeShare ou plugin de terceiros antes de carregá-lo com `import` ou `plugin load`.

## Conexões
- [[objection-hooking-dinamico-watch-class-method-argumentos-stacktrace]] — Veja também: Engenharia Reversa Dinâmica sem Decompilação no `objection`: Rastreamento de Classes, Argumentos, Retornos e **Stack Traces (`--dump-args --dump-return --dump-backtrace`)**.
- [[objection-protecao-ui-flag-secure-screenshots-clipboard-backgrounding]] — Veja também: Auditoria de Proteções de Interface e Vazamento em Background no `objection`: **`android ui FLAG_SECURE`**, Pasteboard/Clipboard e Snapshots de Tela.
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
