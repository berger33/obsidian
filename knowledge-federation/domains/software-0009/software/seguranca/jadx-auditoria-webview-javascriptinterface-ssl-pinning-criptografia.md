---
id: software.seguranca.tranche10.000926
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/skylot/jadx/master/README.md", "https://github.com/skylot/jadx/wiki/jadx-gui-features-overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria de Código no JADX (**OWASP MASVS-CODE & CRYPTO**): **WebViews Inseguras (`addJavascriptInterface`)**, **`X509TrustManager` Vazio** e Criptografia Fraca

## Em uma frase
Com o código Java reconstruído pelo JADX, você pode auditar sistematicamente as três falhas de código mais críticas do **OWASP Mobile Top 10 / MASVS**: **(1) Configurações Inseguras de `WebView`**, **(2) Validação TLS Quebrada (`TrustManager` / `HostnameVerifier`)** e **(3) Criptografia e Armazenamento Local Inseguro (`MASVS-CRYPTO` / `MASVS-STORAGE`)**!

## Por que importa
Em **WebViews**, procure chamadas para `setJavaScriptEnabled(true)` combinadas com **`addJavascriptInterface(...)`** (que expõe métodos Java nativos do celular para qualquer código JavaScript carregado na WebView!), `setAllowFileAccessFromFileURLs(true)` e `setAllowUniversalAccessFromFileURLs(true)` (que permitem a um HTML local ler arquivos privados `/data/data/<pkg>/shared_prefs/*.xml` do aplicativo via XSS ou Deep Link!).

## Como funciona
Em **Rede/TLS**, procure implementações de **`X509TrustManager`** cujo método `checkServerTrusted()` esteja **vazio**, `HostnameVerifier` que retorna sempre **`return true;`** ou `WebViewClient.onReceivedSslError()` que chama **`handler.proceed()`** (aceitando qualquer certificado TLS falsificado por um atacante Man-in-the-Middle!)!

## Exemplo
```bash
# Auditar estaticamente no codigo Java decompilado pelo JADX padroes perigosos de WebView, TLS TrustManager e Criptografia (ECB/Hardcoded IV)
grep -rnE 'addJavascriptInterface|setAllowUniversalAccessFromFileURLs|checkServerTrusted|ALLOW_ALL_HOSTNAME_VERIFIER|onReceivedSslError|Cipher\.getInstance\("AES(/ECB)?'\
  /cases/mobile/app_unpacked/sources/
```

## Limites e trade-offs
Em **Criptografia (`javax.crypto.Cipher`)**, procure por `Cipher.getInstance("AES")` (que em Java/Android usa por padrão o modo inseguro **`AES/ECB/PKCS5Padding`** quando o modo não é especificado!), `SecretKeySpec` inicializado com bytes constantes no código, `IvParameterSpec` com vetor de inicialização fixo (`new byte[16]`) ou uso de `java.util.Random` em vez de `SecureRandom`!

## Como verificar
Ao encontrar um método de **SSL Pinning** customizado (ex.: `CertificatePinner` do OkHttp) no JADX, copie a assinatura exata da classe e dos argumentos do método para criar em 30 segundos o hook de bypass correspondente no **Frida (`Java.use(...)`)**!

## Conexões
- [[jadx-auditoria-segredos-hardcoded-strings-xml-buildconfig-native-libs]] — Veja também: JADX: Caça a **Segredos Hardcoded, Chaves de API, URLs de Homologação e Credenciais** em `BuildConfig.java`, `res/values/strings.xml` e `assets/`.
- [[jadx-exportacao-grafos-fluxo-controle-cfg-call-graph-dot-json]] — Veja também: JADX: Exportação de **Control Flow Graphs (`--cfg`, `--raw-cfg`)**, **Grafo de Chamadas (`--call-graph json|dot`)** e Saída Estruturada (`--output-format json`).
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.
- [[mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile]] — Referência cruzada direta com mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
