---
id: software.seguranca.tranche11.001045
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

# Exploração Android no `objection`: Auditoria do **Android Keystore (`android keystore list`)**, Manipulação de **Objetos na Heap (`android heap`)** e Lançamento de **Activities/Intents**

## Em uma frase
Em avaliações de segurança Android (seguindo o guia **OWASP MASTG**), o `objection` oferece quatro famílias de comandos específicos para o runtime Android (`Dalvik` / `ART`):

## Por que importa
A primeira é **`android keystore list`** e **`android keystore watch`**: interroga a API `java.security.KeyStore` (`AndroidKeyStore`) dentro do processo do aplicativo para listar todos os *aliases* de chaves criptográficas pertencentes àquele app, verificar se exigem autenticação biométrica e monitorar seu uso em tempo real!

## Como funciona
A segunda é **`android hooking`** (`list activities`, `list services`, `list receivers`, `watch class`, `watch class_method`, `set return_value`): permite forçar um método booleano como `isPremiumUser()` ou `verifyPin()` a retornar sempre `true` com 1 comando! A terceira é **`android intent launch_activity <classe>`** (abre qualquer tela do aplicativo diretamente, inclusive telas administrativas não-exportadas!). E a quarta é **`android heap search instances <classe>`** + **`android heap execute <hashcode> <metodo>`**, que localiza objetos vivos na memória RAM e invoca métodos neles!

## Exemplo
```text
# Listar chaves no Android Keystore, buscar instancias vivas na Heap e forcar o retorno de um metodo booleano
com.empresa.mobileapp on (Android: 14) [usb] # android keystore list
com.empresa.mobileapp on (Android: 14) [usb] # android heap search instances com.empresa.mobileapp.auth.SessionManager
com.empresa.mobileapp on (Android: 14) [usb] # android hooking set return_value com.empresa.mobileapp.auth.BiometricHelper.isAuthenticated true
```

## Limites e trade-offs
Compreenda por que **`android heap search instances`** é tão revelador: mesmo que o desenvolvedor não salve um token ou senha em disco (`SharedPreferences`), se o objeto Java/Kotlin que guarda a sessão ou a senha em memória continuar vivo na Heap após o login, `android heap evaluate <hashcode>` permite inspecionar todos os campos privados daquela instância em memória!

## Como verificar
Para proteger dados críticos em memória no Android, prefira arrays `char[]` / `byte[]` zerados imediatamente após o uso (`Arrays.fill(secret, (byte) 0)`) em vez de objetos `java.lang.String` imutáveis.

## Conexões
- [[objection-bypass-root-jailbreak-detection-simulacao-android-ios]] — Veja também: Auditoria de Detecção de **Root e Jailbreak** no `objection`: Comandos **`disable`** vs **`simulate`** para Testar a Resiliência da Defesa do Aplicativo.
- [[objection-exploracao-ios-keychain-dump-nsuserdefaults-plist-bypasses]] — Veja também: Exploração iOS no `objection`: Dump do **iOS Keychain (`ios keychain dump`)**, **`ios nsuserdefaults get`**, **`ios plist cat`**, **`ios cookies get`** e Bypass de **`TouchID/FaceID`**.
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.
- [[jadx-auditoria-androidmanifest-exported-components-deep-links-permissions]] — Referência cruzada direta com jadx-auditoria-androidmanifest-exported-components-deep-links-permissions.
- [[mobsf-instrumentacao-frida-live-api-monitor-scripts-auxiliares]] — Referência cruzada direta com mobsf-instrumentacao-frida-live-api-monitor-scripts-auxiliares.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
