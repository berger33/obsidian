---
id: software.seguranca.tranche10.000938
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

# Auditoria de **Split APKs / Android App Bundles (`.aab`, `.apks`, `.xapk`)** com Apktool: Como Decodificar e Fundir Múltiplos Splits (`base.apk` + `split_config.*.apk`)

## Em uma frase
Desde que a Google Play Store tornou obrigatório o formato **Android App Bundle (`.aab`)**, quando você extrai um aplicativo instalado de um celular moderno via `adb shell pm path <pacote>`, o Android não devolve mais um único `base.apk`: ele devolve **vários arquivos Split APK** (`base.apk`, `split_config.arm64_v8a.apk`, `split_config.pt.apk`, `split_config.xxhdpi.apk`)!

## Por que importa
Se você modificar e re-assinar apenas o `base.apk` com sua chave de pentest, o Android recusará instalá-lo ao lado dos outros splits porque **todos os Split APKs de uma mesma sessão `adb install-multiple` precisam estar assinados exatamente com o mesmo certificado**!

## Como funciona
Você tem duas estratégias limpas para auditar Split APKs com o Apktool: **(1)** re-assinar **todos os arquivos `split_config.*.apk`** com o mesmo keystore (`pentest_release.jks`) usado no `base.apk` modificado e instalá-los juntos via **`adb install-multiple base_signed.apk split_arm64_signed.apk ...`**; ou **(2)** decodificar os splits e fundir as bibliotecas nativas (`lib/arm64-v8a/`) e recursos no `base.apk` (removendo os atributos `android:isSplitRequired="true"` e `com.android.vending.splits.required` do `AndroidManifest.xml`)!

## Exemplo
```bash
# Re-assinar tanto o base.apk modificado pelo Apktool quanto o split nativo arm64 com a mesma chave e instalar via adb install-multiple
apksigner sign --ks /cases/mobile/pentest_release.jks --ks-pass pass:SenhaForteDoKeystore123 \
  --out /cases/mobile/base_mod_signed.apk /cases/mobile/base_mod_aligned.apk

apksigner sign --ks /cases/mobile/pentest_release.jks --ks-pass pass:SenhaForteDoKeystore123 \
  --out /cases/mobile/split_arm64_signed.apk /cases/mobile/split_config.arm64_v8a.apk

adb install-multiple -r /cases/mobile/base_mod_signed.apk /cases/mobile/split_arm64_signed.apk
```

## Limites e trade-offs
A Estratégia 1 (re-assinar os `split_config.*.apk` originais com a mesma chave do `base.apk` modificado e usar `adb install-multiple`) é muito mais rápida e livre de erros de merge de recursos do que tentar fundir manualmente 5 splits em um APK monolítico!

## Como verificar
Lembre-se de desinstalar a versão original da Play Store (`adb uninstall <pacote>`) antes de rodar `adb install-multiple` devido à troca da chave de assinatura.

## Conexões
- [[apktool-gestao-frameworks-if-install-framework-roms-fabricantes]] — Veja também: Apktool (`if` / `install-framework`): Gestão de **APKs de Framework (`framework-res.apk`)** para Aplicativos de Sistema de Fabricantes (Samsung / Xiaomi / AOSP).
- [[apktool-anatomia-apktool-yml-sdkinfo-donotcompress-unkownfiles]] — Veja também: Apktool: Anatomia do Arquivo de Controle **`apktool.yml`** (`sdkInfo`, `versionInfo`, `doNotCompress` e `unknownFiles`).
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Referência cruzada direta com apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3.
- [[apktool-modificacao-androidmanifest-debuggable-network-security-config]] — Referência cruzada direta com apktool-modificacao-androidmanifest-debuggable-network-security-config.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
