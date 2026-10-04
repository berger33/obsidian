---
id: software.seguranca.tranche11.001047
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

# Auditoria de Memória RAM e Bancos Locais no `objection`: **`memory dump`**, **`memory search`**, **`sqlite connect`** e Proteção de Dados em Repouso (**SQLCipher**)

## Em uma frase
Muitos aplicativos móveis protegem a comunicação de rede com TLS 1.3 e Pinning, mas gravam mensagens, dados pessoais (CPF, cartões, histórico médico) ou tokens JWT diretamente em bancos **SQLite não-criptografados** dentro da pasta privada do app (`/data/data/<pkg>/databases/` no Android ou `Documents/` / `Library/` no iOS) ou mantêm esses segredos em texto claro na memória RAM.

## Por que importa
O `objection` permite auditar tanto os bancos em disco quanto a memória RAM diretamente pelo REPL: **(1) `sqlite connect <arquivo.db>`** abre um console SQL interativo sincronizado com o banco de dados dentro do celular para rodar `tables`, `schema` e `SELECT * FROM ...`; e **(2) `memory list modules`**, **`memory search "<padrao>" --string`** e **`memory dump all <pasta>`** varrem os segmentos de memória do processo em execução em busca de senhas, chaves privadas ou números de cartão que permaneceram residentes na RAM!

## Como funciona
Se um cartão de crédito ou senha digitada na tela de login ainda for encontrado por `memory search` minutos após o login, o aplicativo falha nos controles de higiene de memória do **PCI-DSS / OWASP MASVS-STORAGE**!

## Exemplo
```text
# Buscar strings sensiveis na memoria RAM do processo e inspecionar bancos de dados SQLite locais dentro do sandbox do app
com.empresa.mobileapp on (Android: 14) [usb] # memory search "Bearer eyJ" --string
com.empresa.mobileapp on (Android: 14) [usb] # cd databases
com.empresa.mobileapp on (Android: 14) [usb] # sqlite connect app_cache.db
SQLite @ app_cache.db > tables
```

## Limites e trade-offs
Como proteger bancos SQLite locais em aplicativos Android e iOS para que `sqlite connect` ou o roubo do arquivo `.db` em um backup/dispositivo comprometido não revele nenhum dado? Utilizando **SQLCipher** (criptografia AES-256 de página inteira para SQLite) ou **EncryptedSharedPreferences / Jetpack Security**, com a chave mestre derivada e guardada exclusivamente dentro do **Android Keystore (Hardware-backed / StrongBox)** ou **iOS Keychain (`kSecAttrAccessibleWhenUnlockedThisDeviceOnly`)**!

## Como verificar
Mesmo quando o app usa SQLCipher, lembre-se de que durante a execução a chave passa pela memória para abrir o banco — por isso não armazene localmente no dispositivo dados que poderiam ficar apenas no servidor.

## Conexões
- [[objection-exploracao-ios-keychain-dump-nsuserdefaults-plist-bypasses]] — Veja também: Exploração iOS no `objection`: Dump do **iOS Keychain (`ios keychain dump`)**, **`ios nsuserdefaults get`**, **`ios plist cat`**, **`ios cookies get`** e Bypass de **`TouchID/FaceID`**.
- [[objection-hooking-dinamico-watch-class-method-argumentos-stacktrace]] — Veja também: Engenharia Reversa Dinâmica sem Decompilação no `objection`: Rastreamento de Classes, Argumentos, Retornos e **Stack Traces (`--dump-args --dump-return --dump-backtrace`)**.
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.
- [[objection-inspecao-android-keystore-heap-activities-intents-services]] — Referência cruzada direta com objection-inspecao-android-keystore-heap-activities-intents-services.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
