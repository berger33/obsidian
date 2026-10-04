---
id: software.seguranca.tranche11.001043
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

# Bypass Universal de **SSL/TLS Certificate Pinning** no `objection`: **`android sslpinning disable`** e **`ios sslpinning disable`** (`OkHttp3`, `Conscrypt`, `TrustKit`, `NSURLSession`)

## Em uma frase
Quando um pentester configura o proxy **Burp Suite** ou **`mitmproxy`** no celular para auditar as chamadas de API de um aplicativo móvel, aplicativos que implementam **SSL/TLS Certificate Pinning** rejeitam o certificado da CA do proxy e abortam a conexão TLS.

## Por que importa
Em vez de procurar manualmente onde o pinning foi programado, os comandos **`android sslpinning disable`** (no Android) e **`ios sslpinning disable`** (no iOS) do `objection` instalam *hooks* simultâneos em todas as bibliotecas e APIs padrão de validação de certificado da plataforma!

## Como funciona
No **Android**, o `android sslpinning disable` intercepta `SSLContext`, `TrustManagerImpl` (Android 7+ Conscrypt / `network_security_config.xml`), `OkHttp3 CertificatePinner`, `HttpsURLConnection`, `WebViewClient`, `Appcelerator`, `PhoneGap` e `IBM WorkLight`. Já no **iOS**, o `ios sslpinning disable` intercepta `SecTrustEvaluate` / `SecTrustEvaluateWithError`, `NSURLSession`, `AFNetworking` e `TrustKit`, substituindo a decisão de validação por sucesso!

## Exemplo
```text
# No prompt REPL do objection: desabilitar SSL Pinning em tempo real e listar os jobs de hook ativos
com.empresa.mobileapp on (Android: 14) [usb] # android sslpinning disable
(agent) Custom TrustManager ready, overriding SSLContext.init()
(agent) Found okhttp3.CertificatePinner, overriding check()
(agent) Job: 948102 - Starting: android sslpinning disable

com.empresa.mobileapp on (Android: 14) [usb] # jobs list
```

## Limites e trade-offs
E se o aplicativo mobile não usar as bibliotecas Java/Objective-C do sistema para TLS, mas sim uma engine nativa compilada em C/C++/Go/Rust/Flutter (como **`libflutter.so` com BoringSSL** ou **`Cronet`**)? Nesse caso, `android sslpinning disable` não verá a chamada Java; você deve combinar o `objection` com um hook nativo sobre a função C `ssl_crypto_x509_session_verify_cert_chain` na `libflutter.so` via `frida`!

## Como verificar
Passe `--quiet` (`android sslpinning disable --quiet`) quando quiser suprimir as mensagens de log no console a cada requisição HTTPS interceptada.

## Conexões
- [[objection-patchapk-patchipa-instrumentacao-sem-root-jailbreak]] — Veja também: Instrumentação Sem Root/Jailbreak com **`objection patchapk`** e **`objection patchipa`**: Automação do `frida-gadget` e Configurações de Script.
- [[objection-bypass-root-jailbreak-detection-simulacao-android-ios]] — Veja também: Auditoria de Detecção de **Root e Jailbreak** no `objection`: Comandos **`disable`** vs **`simulate`** para Testar a Resiliência da Defesa do Aplicativo.
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
