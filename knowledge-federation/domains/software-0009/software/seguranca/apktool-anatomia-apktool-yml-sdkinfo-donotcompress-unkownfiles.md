---
id: software.seguranca.tranche10.000939
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
fontes: ["https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md", "https://apktool.org/wiki/the-basics/intro/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Apktool: Anatomia do Arquivo de Controle **`apktool.yml`** (`sdkInfo`, `versionInfo`, `doNotCompress` e `unknownFiles`)

## Em uma frase
Dentro da pasta gerada por `apktool d`, o arquivo **`apktool.yml`** é o cérebro que instrui o `apktool b` sobre como remontar o aplicativo.

## Por que importa
Quatro seções do `apktool.yml` resolvem problemas reais durante pentests mobile: **(1) `sdkInfo` (`minSdkVersion`, `targetSdkVersion`)** — permite ajustar versões de SDK se você estiver testando o APK em um emulador de API anterior; **(2) `doNotCompress`** — lista extensões e caminhos de arquivos (como `resources.arsc`, `.so`, `.mp3`, `.webp` ou bancos de dados em `assets/`) que **NÃO podem ser comprimidos com DEFLATE dentro do ZIP** porque o código Android os lê via `mmap()` direto (`openRawResourceFd`); **(3) `unknownFiles`** — preserva arquivos fora do padrão Android (como metadados de frameworks multiplataforma Flutter/React Native/Cordova/Kotlin Multiplatform) na posição exata dentro do APK; e **(4) `isFrameworkApk`**!

## Como funciona
Se após recompilar um APK com `apktool b` o aplicativo fechar sozinho (*crash*) no início reclamando de `FileNotFoundException: This file can not be opened as a file descriptor; it is probably compressed`, basta adicionar a extensão ou caminho daquele arquivo na lista **`doNotCompress:`** do `apktool.yml`!

## Exemplo
```yaml
# Trecho de apktool.yml — Garantindo que bibliotecas nativas (.so), resources.arsc e assets especificos nao sejam comprimidos no build
version: 2.10.0
apkFileName: target_app.apk
isFrameworkApk: false
sdkInfo:
  minSdkVersion: '26'
  targetSdkVersion: '34'
doNotCompress:
- resources.arsc
- so
- png
- assets/flutter_assets/kernel_blob.bin
```

## Limites e trade-offs
Nunca apague a seção `unknownFiles:` do `apktool.yml` ao auditar aplicativos híbridos (React Native `index.android.bundle`, Flutter, Unity ou Xamarin), pois muitos arquivos de configuração desses motores residem fora das pastas padrão `res/` e `assets/`.

## Como verificar
Verifique com `zipinfo /cases/mobile/app_aligned.apk | grep '\.so$'` que as bibliotecas `.so` estão listadas como `stor` (*stored / uncompressed*) e não `defN` (*deflated*).

## Conexões
- [[apktool-aplicativos-split-apks-app-bundles-aab-fusao-reconstrucao]] — Veja também: Auditoria de **Split APKs / Android App Bundles (`.aab`, `.apks`, `.xapk`)** com Apktool: Como Decodificar e Fundir Múltiplos Splits (`base.apk` + `split_config.*.apk`).
- [[apktool-defesas-anti-repackaging-assinatura-play-integrity-auditoria]] — Veja também: Engenharia Defensiva Mobile (**OWASP MASVS-RESILIENCE**): Detecção de **Repackaging (`Apktool`)**, Verificação de Certificado de Assinatura e **Play Integrity API**.
- [[apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali]] — Referência cruzada direta com apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali.
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Referência cruzada direta com apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3.
- [[apktool-injecao-frida-gadget-so-smali-dispositivos-sem-root]] — Referência cruzada direta com apktool-injecao-frida-gadget-so-smali-dispositivos-sem-root.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
