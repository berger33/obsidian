---
id: software.seguranca.tranche11.001046
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

# Exploração iOS no `objection`: Dump do **iOS Keychain (`ios keychain dump`)**, **`ios nsuserdefaults get`**, **`ios plist cat`**, **`ios cookies get`** e Bypass de **`TouchID/FaceID`**

## Em uma frase
No **Apple iOS**, onde o aplicativo armazena seus segredos, tokens de sessão, cookies e preferências locais? Em quatro repositórios nativos que o `objection` audita com comandos de uma linha!

## Por que importa
Primeiro, **`ios keychain dump`** (e `ios keychain dump --json keychain.json`): como o `objection` roda **dentro do próprio processo assinado do aplicativo**, ele possui automaticamente os *Entitlements* (`keychain-access-groups`) daquele app e chama `SecItemCopyMatching` para extrair **todos os itens que o aplicativo guardou no iOS Keychain**, exibindo inclusive os atributos de proteção **`kSecAttrAccessible`** (`WhenUnlocked`, `AfterFirstUnlock`, `WhenPasscodeSetThisDeviceOnly`) e flags de Access Control (Biometria)!

## Como funciona
Segundo, **`ios nsuserdefaults get`** imprime todas as chaves/valores salvos no `NSUserDefaults`; terceiro, **`ios plist cat <arquivo.plist>`** converte arquivos Binary Plist em XML legível sem tirá-los do celular; quarto, **`ios cookies get`** extrai o `NSHTTPCookieStorage`; e quinto, **`ios ui biometrics_bypass`** intercepta `LAContext evaluatePolicy:` para contornar validações locais puramente booleanas de TouchID / FaceID!

## Exemplo
```text
# Auditar o armazenamento seguro de um aplicativo iOS: extrair Keychain, NSUserDefaults, Cookies e testar bypass de LAContext
com.empresa.iosapp on (iPhone: 17.4) [usb] # ios keychain dump
com.empresa.iosapp on (iPhone: 17.4) [usb] # ios nsuserdefaults get
com.empresa.iosapp on (iPhone: 17.4) [usb] # ios cookies get
com.empresa.iosapp on (iPhone: 17.4) [usb] # ios ui biometrics_bypass
```

## Limites e trade-offs
Por que o comando **`ios ui biometrics_bypass`** funciona contra implementações ingênuas de TouchID/FaceID e como corrigi-lo segundo o **OWASP MASTG**? Se o desenvolvedor apenas chama `LAContext.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics)` e, no callback `if (success) { ... }`, libera a tela, um hook no Objective-C força `success = YES`! A forma criptograficamente segura no iOS é atrelar uma chave no **Keychain / Secure Enclave** com a flag **`kSecAccessControlBiometryCurrentSet`**: assim, o hardware do Secure Enclave só libera a chave criptográfica se o sensor biométrico físico realmente validar a digital/rosto!

## Como verificar
Verifique na coluna `Accessible` do `ios keychain dump` se todas as credenciais sensíveis usam `*ThisDeviceOnly` (impedindo que os tokens vazem em backups do iTunes/Finder).

## Conexões
- [[objection-inspecao-android-keystore-heap-activities-intents-services]] — Veja também: Exploração Android no `objection`: Auditoria do **Android Keystore (`android keystore list`)**, Manipulação de **Objetos na Heap (`android heap`)** e Lançamento de **Activities/Intents**.
- [[objection-inspecao-memoria-memory-dump-search-write-sqlite-files]] — Veja também: Auditoria de Memória RAM e Bancos Locais no `objection`: **`memory dump`**, **`memory search`**, **`sqlite connect`** e Proteção de Dados em Repouso (**SQLCipher**).
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.
- [[mobsf-analise-estatica-ios-ipa-plist-ats-macho-pie-arc-canary]] — Referência cruzada direta com mobsf-analise-estatica-ios-ipa-plist-ats-macho-pie-arc-canary.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
