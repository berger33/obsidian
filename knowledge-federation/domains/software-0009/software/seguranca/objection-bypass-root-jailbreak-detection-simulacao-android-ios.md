---
id: software.seguranca.tranche11.001044
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

# Auditoria de Detecção de **Root e Jailbreak** no `objection`: Comandos **`disable`** vs **`simulate`** para Testar a Resiliência da Defesa do Aplicativo

## Em uma frase
O `objection` possui uma dupla de comandos genial para avaliar controles de **Detecção de Root (Android)** e **Detecção de Jailbreak (iOS)**: não apenas o comando **`disable`** (para quando você está em um aparelho *rooted/jailbroken* e quer esconder isso do app), mas também o comando **`simulate`** (para quando você está em um aparelho comum *sem root/jailbreak* e quer testar se o código de detecção do aplicativo realmente funciona!)!

## Por que importa
Quando você executa **`android root disable`** ou **`ios jailbreak disable`**, o agente Frida do `objection` intercepta chamadas como `File.exists()`, `Runtime.exec("which su")`, `PackageManager.getPackageInfo("com.topjohnwu.magisk")`, `NSFileManager.fileExistsAtPath_("/Applications/Cydia.app")`, `canOpenURL("cydia://")` e `fopen()`, retornando `false` sempre que o app procura por binários `su`, Magisk, Frida ou Cydia!

## Como funciona
Inversamente, quando você executa **`android root simulate`** ou **`ios jailbreak simulate`** em um aparelho limpo, o `objection` responde **`true`** para essas mesmas checagens — permitindo que o auditor de AppSec verifique em 5 segundos se o aplicativo realmente detecta e bloqueia a execução como prometido!

## Exemplo
```text
# Testar se o mecanismo anti-root do aplicativo funciona (simulate) e depois contorna-lo (disable) no REPL do objection
com.empresa.mobileapp on (Android: 14) [usb] # android root simulate
com.empresa.mobileapp on (Android: 14) [usb] # android root disable
```

## Limites e trade-offs
Para equipes de **Engenharia Mobile Defensiva (MASVS-RESILIENCE)**: como os comandos `android root disable` e `ios jailbreak disable` interceptam APIs de alto nível da VM Java (`java.io.File`) e do Objective-C Runtime (`NSFileManager`), verificações de integridade mais resistentes devem combinar chamadas de sistema nativas diretas via **JNI / Syscalls assembly (`faccessat` / `openat` em C/C++)** com atestação criptográfica remota via **Google Play Integrity API** e **Apple App Attest (`DCAppAttestService`)**!

## Como verificar
Valide sempre a eficácia da sua biblioteca de RASP / Anti-Root rodando o `objection` com `-s "android root disable"` no início do processo.

## Conexões
- [[objection-bypass-ssl-pinning-android-ios-network-security-trustkit]] — Veja também: Bypass Universal de **SSL/TLS Certificate Pinning** no `objection`: **`android sslpinning disable`** e **`ios sslpinning disable`** (`OkHttp3`, `Conscrypt`, `TrustKit`, `NSURLSession`).
- [[objection-inspecao-android-keystore-heap-activities-intents-services]] — Veja também: Exploração Android no `objection`: Auditoria do **Android Keystore (`android keystore list`)**, Manipulação de **Objetos na Heap (`android heap`)** e Lançamento de **Activities/Intents**.
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.
- [[apktool-defesas-anti-repackaging-assinatura-play-integrity-auditoria]] — Referência cruzada direta com apktool-defesas-anti-repackaging-assinatura-play-integrity-auditoria.
- [[mobsf-instrumentacao-frida-live-api-monitor-scripts-auxiliares]] — Referência cruzada direta com mobsf-instrumentacao-frida-live-api-monitor-scripts-auxiliares.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
