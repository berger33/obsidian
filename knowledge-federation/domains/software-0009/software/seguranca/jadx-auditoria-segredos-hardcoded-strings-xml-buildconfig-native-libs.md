---
id: software.seguranca.tranche10.000925
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

# JADX: Caça a **Segredos Hardcoded, Chaves de API, URLs de Homologação e Credenciais** em `BuildConfig.java`, `res/values/strings.xml` e `assets/`

## Em uma frase
Desenvolvedores mobile frequentemente acreditam erroneamente que variáveis definidas no `build.gradle` (`buildConfigField`), no arquivo `res/values/strings.xml` (`google_api_key`, `firebase_database_url`, `aws_cognito_pool_id`) ou constantes `private static final String` no código Java ficam invisíveis após compilar o `.apk`.

## Por que importa
Ao decompilar o APK com o JADX, todas as constantes de `build.gradle` aparecem em texto claro na classe **`BuildConfig.java`**, e todas as strings de recursos aparecem em **`resources/res/values/strings.xml`** e **`resources/assets/`** (que muitas vezes contêm arquivos `.env`, `.json`, `.p12`, `.pem` ou chaves privadas embutidas)!

## Como funciona
Combinar a decompilação do JADX (`jadx -d out app.apk`) com varredura automatizada pelo **Gitleaks (`gitleaks dir out`)**, **TruffleHog (`trufflehog filesystem out`)** ou buscas no `jadx-gui` revela chaves de API da AWS, tokens de bots do Slack/Telegram, chaves do Stripe/SendGrid e endpoints internos de staging!

## Exemplo
```bash
# Decompilar o APK com o JADX e passar o Gitleaks sobre o codigo Java reconstruido e os arquivos XML/assets decodificados
jadx -d /cases/mobile/app_unpacked -j 16 /cases/mobile/target_app.apk
gitleaks dir /cases/mobile/app_unpacked \
  --report-format json \
  --report-path /cases/mobile/apk_hardcoded_secrets.json
```

## Limites e trade-offs
E quando a equipe de desenvolvimento move o segredo do Java para uma biblioteca nativa C/C++ (`.so` em `resources/lib/arm64-v8a/libnative-keys.so`) chamada via **JNI (`System.loadLibrary("native-keys")`)**? No JADX você localiza a declaração `public native String getApiSecret();` e, em seguida, abre o arquivo `libnative-keys.so` no **Ghidra** ou **Radare2** (procurando a função `Java_com_empresa_..._getApiSecret`)!

## Como verificar
Verifique no `strings.xml` se a URL do **Firebase Realtime Database (`https://*.firebaseio.com/.json`)** está exposta e se permite leitura anônima sem autenticação.

## Conexões
- [[jadx-auditoria-androidmanifest-exported-components-deep-links-permissions]] — Veja também: Auditoria de Superfície de Ataque Android no JADX: **`AndroidManifest.xml`**, Componentes Exportados (`exported="true"`), **Intent Filters / Deep Links** e `allowBackup`.
- [[jadx-auditoria-webview-javascriptinterface-ssl-pinning-criptografia]] — Veja também: Auditoria de Código no JADX (**OWASP MASVS-CODE & CRYPTO**): **WebViews Inseguras (`addJavascriptInterface`)**, **`X509TrustManager` Vazio** e Criptografia Fraca.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
