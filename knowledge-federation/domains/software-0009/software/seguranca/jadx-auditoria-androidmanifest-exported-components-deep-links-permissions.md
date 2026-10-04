---
id: software.seguranca.tranche10.000924
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

# Auditoria de Superfície de Ataque Android no JADX: **`AndroidManifest.xml`**, Componentes Exportados (`exported="true"`), **Intent Filters / Deep Links** e `allowBackup`

## Em uma frase
Toda auditoria de segurança Android (seguindo o **OWASP MASTG / MASVS-PLATFORM**) começa abrindo o **`AndroidManifest.xml`** decodificado pelo JADX para mapear a **Superfície de Ataque IPC (*Inter-Process Communication*)** exposta pelo aplicativo para outros apps instalados no mesmo celular ou para links web.

## Por que importa
Quais atributos do `AndroidManifest.xml` devem ser inspecionados imediatamente? **(1) `android:debuggable="true"`** (permite anexar `jdb` / `run-as` sem root!); **(2) `android:allowBackup="true"`** (permite extrair o banco SQLite e `SharedPreferences` via `adb backup` se não houver regras de exclusão); **(3) `android:usesCleartextTraffic="true"`** (permite tráfego `http://` em texto claro sem TLS!); e **(4) Componentes Exportados (`<activity>`, `<service>`, `<receiver>`, `<provider>`)**!

## Como funciona
Atenção à regra do Android: qualquer componente que declare explicitamente **`android:exported="true"`** — ou que em APIs antigas possua um bloco **`<intent-filter>`** sem declarar `android:exported="false"` e sem exigir uma `android:permission` com `protectionLevel="signature"` — **pode ser invocado por qualquer outro aplicativo malicioso instalado no aparelho**!

## Exemplo
```bash
# Extrair apenas os recursos (-s / --no-src) em 2 segundos com o JADX e auditar componentes exportados e Deep Links no AndroidManifest.xml
jadx --no-src -d /cases/mobile/manifest_only /cases/mobile/target_app.apk
grep -En 'android:(exported="true"|debuggable="true"|allowBackup="true"|usesCleartextTraffic="true"|scheme=|host=)' \
  /cases/mobile/manifest_only/resources/AndroidManifest.xml
```

## Limites e trade-offs
No `jadx-gui`, você pode segurar **`Ctrl` e clicar diretamente no nome de qualquer `Activity`, `Service`, `BroadcastReceiver` ou `ContentProvider` dentro do `AndroidManifest.xml`** para saltar instantaneamente para a classe Java que processa aquela `Intent` (`onCreate()`, `onNewIntent()`, `onReceive()`, `query()`, `openFile()`)!

## Como verificar
Audite todo `ContentProvider` exportado procurando por vulnerabilidades de **SQL Injection** em `query()` e **Path Traversal** em `openFile()` (`ParcelFileDescriptor`).

## Conexões
- [[jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin]] — Veja também: JADX: Desofuscação Automática (**`--deobf`**, `.jobf`), Importação de Mapas **ProGuard/R8 (`--mappings-path`)** e Metadados **Kotlin (`kotlin.Metadata`)**.
- [[jadx-auditoria-segredos-hardcoded-strings-xml-buildconfig-native-libs]] — Veja também: JADX: Caça a **Segredos Hardcoded, Chaves de API, URLs de Homologação e Credenciais** em `BuildConfig.java`, `res/values/strings.xml` e `assets/`.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.
- [[jadx-auditoria-webview-javascriptinterface-ssl-pinning-criptografia]] — Referência cruzada direta com jadx-auditoria-webview-javascriptinterface-ssl-pinning-criptografia.
- [[apktool-modificacao-androidmanifest-debuggable-network-security-config]] — Referência cruzada direta com apktool-modificacao-androidmanifest-debuggable-network-security-config.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
