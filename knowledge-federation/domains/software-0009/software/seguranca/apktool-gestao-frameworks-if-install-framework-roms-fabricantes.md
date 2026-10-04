---
id: software.seguranca.tranche10.000937
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

# Apktool (`if` / `install-framework`): Gestão de **APKs de Framework (`framework-res.apk`)** para Aplicativos de Sistema de Fabricantes (Samsung / Xiaomi / AOSP)

## Em uma frase
Ao tentar decodificar um aplicativo de sistema pré-instalado em uma ROM customizada de fabricante (como apps de sistema da Samsung OneUI, Xiaomi HyperOS/MIUI, Motorola ou dispositivos IoT/POS embarcados em Android), o `apktool d` pode falhar com erros `Could not decode attr value, using undecoded value instead: ns=android, name=...`.

## Por que importa
Por que isso acontece? Porque aplicativos comuns usam apenas os recursos padrão do Android SDK (ID de pacote `0x01`, embutido no próprio Apktool como `1.apk`), mas aplicativos de sistema de fabricantes referenciam recursos compartilhados de pacotes de framework proprietários instalados em `/system/framework/` do aparelho (IDs de pacote `0x02`, `0x03`, etc., como `framework-res.apk`, `twframework-res.apk` ou `miui.apk`)!

## Como funciona
Para que o Apktool resolva perfeitamente essas referências, você extrai o `framework-res.apk` do dispositivo via `adb pull /system/framework/framework-res.apk` e o registra no Apktool usando **`apktool if framework-res.apk -t <tag>`** (*install-framework*)!

## Exemplo
```bash
# Extrair os frameworks proprietarios do dispositivo via adb, instala-los no Apktool com a tag 'vendor-rom' e decodificar o app de sistema
adb pull /system/framework/framework-res.apk /cases/mobile/
apktool if /cases/mobile/framework-res.apk -p /cases/mobile/frameworks -t vendor-rom

apktool d /cases/mobile/VendorSystemService.apk \
  -p /cases/mobile/frameworks \
  -t vendor-rom \
  -o /cases/mobile/vendor_service_decoded
```

## Limites e trade-offs
Use **`apktool empty-framework-dir`** (eventualmente com `--force`) sempre que atualizar a versão do Apktool na sua estação de trabalho para limpar o cache antigo de `1.apk` e forçar a extração do framework atualizado!

## Como verificar
Verifique no `apktool.yml` gerado na seção `usesFramework: ids: [1, 2]` quais IDs de framework foram utilizados na decodificação.

## Conexões
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Veja também: Apktool (`b` / `build`) + **`zipalign`** + **`apksigner` (v1/v2/v3/v4)**: O Pipeline Completo de Recompilação e Assinatura para Android 11–15+.
- [[apktool-aplicativos-split-apks-app-bundles-aab-fusao-reconstrucao]] — Veja também: Auditoria de **Split APKs / Android App Bundles (`.aab`, `.apks`, `.xapk`)** com Apktool: Como Decodificar e Fundir Múltiplos Splits (`base.apk` + `split_config.*.apk`).
- [[apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali]] — Referência cruzada direta com apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali.
- [[apktool-controles-decodificacao-no-src-no-res-only-main-classes]] — Referência cruzada direta com apktool-controles-decodificacao-no-src-no-res-only-main-classes.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
