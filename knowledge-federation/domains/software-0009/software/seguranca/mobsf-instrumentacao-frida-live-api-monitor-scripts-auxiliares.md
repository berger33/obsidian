---
id: software.seguranca.tranche11.001035
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
fontes: ["https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md", "https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml", "https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# MobSF **Live API Monitor & Frida Code Editor**: Monitoramento de Criptografia/Rede em Tempo Real e Scripts Auxiliares (`SSL Pinning`, `Root Bypass`, `Hook`)

## Em uma frase
Dentro do **Dynamic Analyzer** do MobSF, duas ferramentas interativas movidas pelo **`frida >= 17.0.0`** permitem dissecar aplicativos complexos sem sair do navegador: o **`Live API Monitor`** e o **`Frida Live Logs / Code Editor`**!

## Por que importa
O **`Live API Monitor`** instala *hooks* dinâmicos sobre as principais classes do framework Android (`javax.crypto.Cipher`, `java.security.MessageDigest`, `javax.crypto.spec.SecretKeySpec`, `android.content.SharedPreferences`, `android.database.sqlite.SQLiteDatabase`, `java.net.URL`, `okhttp3.OkHttpClient`, `android.webkit.WebView`) e exibe na tela, a cada clique que você dá no aplicativo, **os argumentos exatos em texto claro (chaves AES, IVs, payloads antes de criptografar, queries SQL e cabeçalhos HTTP) e o valor de retorno**!

## Como funciona
Além disso, o painel de **Auxiliary Frida Scripts** permite ativar com 1 clique scripts prontos de `Root Detection Bypass`, `SSL Pinning Bypass`, `Debugger Check Bypass`, enumerar todas as classes carregadas no runtime (`Class Loader`) e inspecionar métodos específicos!

## Exemplo
```javascript
// Script Frida customizado no editor do MobSF para interceptar chamadas a javax.crypto.Cipher.doFinal e registrar o texto claro antes da criptografia
Java.perform(function () {
  var Cipher = Java.use("javax.crypto.Cipher");
  Cipher.doFinal.overload("[B").implementation = function (input) {
    var plain = Java.use("java.lang.String").$new(input);
    send("[MobSF Custom Hook] Cipher.doFinal plaintext: " + plain);
    return this.doFinal(input);
  };
});
```

## Limites e trade-offs
Por que interceptar `javax.crypto.Cipher.doFinal` no **Live API Monitor** do MobSF é tão decisivo em pentests de aplicativos bancários e fintechs? Porque muitos apps aplicam uma **segunda camada de criptografia de payload (JWE / AES-GCM na camada de aplicação)** antes de enviar o JSON pelo túnel HTTPS: no proxy (`mitmproxy` / Burp) você vê apenas um blob cifrado ilegível, mas no hook do `Cipher.doFinal` dentro do MobSF você lê e modifica o JSON em texto claro antes da criptografia!

## Como verificar
Guarde os logs do Frida gerados durante a sessão clicando em `Frida Live Logs` no painel de relatório dinâmico.

## Conexões
- [[mobsf-analise-dinamica-android-ios-frida-emulator-corellium-mitm]] — Veja também: MobSF **Dynamic Analyzer**: Instrumentação Interativa com **Frida**, Emuladores Android (**AVD / Genymotion**) e **Corellium iOS** com Interceptação HTTPS.
- [[mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif]] — Veja também: **`mobsfscan` (`MobSF/mobsfscan`)**: SAST Shift-Left de Código-Fonte Mobile (**Java, Kotlin, Android XML, Swift, Objective-C e `Info.plist`**) com Saída **SARIF e SonarQube**.
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.
- [[objection-bypass-ssl-pinning-android-ios-network-security-trustkit]] — Referência cruzada direta com objection-bypass-ssl-pinning-android-ios-network-security-trustkit.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
