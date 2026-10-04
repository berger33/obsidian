---
id: software.seguranca.tranche10.000936
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

# Apktool (`b` / `build`) + **`zipalign`** + **`apksigner` (v1/v2/v3/v4)**: O Pipeline Completo de Recompilação e Assinatura para Android 11–15+

## Em uma frase
Um erro muito comum de iniciantes após rodar `apktool b pasta_decodificada -o app_mod.apk` é tentar instalar o `app_mod.apk` diretamente com `adb install` e receber o erro `INSTALL_PARSE_FAILED_NO_CERTIFICATES` ou `INSTALL_PARSE_FAILED_MANIFEST_MALFORMED` (no Android 11+ / API 30+, que exige obrigatoriamente **APK Signature Scheme v2 ou v3** e alinhamento de 4 bytes das bibliotecas não-comprimidas!).

## Por que importa
O `apktool b` apenas remonta os arquivos `.dex` e `resources.arsc` em um pacote `.apk` não-assinado (em `dist/`); para que o Android aceite instalá-lo, você **DEVE executar na ordem exata**: **(1) `apktool b`** (usando `--use-aapt2` nas versões 2.x; no Apktool 2.9+/3.x o `aapt2` já é o padrão!), **(2) `zipalign -p -f -v 4`** (alinhando arquivos `.so` em limites de página de 4 KiB e demais recursos em 4 bytes **ANTES** de assinar com o `apksigner`!) e **(3) `apksigner sign`**!

## Como funciona
Nota vital: com o antigo `jarsigner` (esquema v1), o `zipalign` rodava *depois* da assinatura; mas com o moderno **`apksigner` (esquemas v2/v3/v4, que assinam o bloco binário inteiro do arquivo ZIP!)**, se você rodar `zipalign` depois do `apksigner`, você **invalidará a assinatura v2/v3**! Portanto: **`apktool b` -> `zipalign` -> `apksigner sign` -> `apksigner verify`**!

## Exemplo
```bash
# Pipeline completo para recompilar com Apktool, alinhar em limites de pagina (zipalign) e assinar nos esquemas v2/v3 (apksigner)
apktool b /cases/mobile/apk_edit_xml_only -o /cases/mobile/app_unaligned.apk

zipalign -p -f -v 4 /cases/mobile/app_unaligned.apk /cases/mobile/app_aligned.apk

apksigner sign --ks /cases/mobile/pentest_release.jks \
  --ks-pass pass:SenhaForteDoKeystore123 \
  --out /cases/mobile/app_patched_signed.apk \
  /cases/mobile/app_aligned.apk

apksigner verify --verbose /cases/mobile/app_patched_signed.apk
```

## Limites e trade-offs
Se durante o `apktool b` o `aapt2` reclamar de atributos privados ou flags inválidas nos recursos, tente adicionar a flag **`-nc` / `--no-crunch`** (para desabilitar o re-processamento de imagens PNG) ou verifique a lista `doNotCompress` dentro do `apktool.yml`.

## Como verificar
Confirme sempre que `apksigner verify --verbose` exibe `Verified using v2 scheme (APK Signature Scheme v2): true` e `Verified using v3 scheme: true` antes de rodar `adb install`.

## Conexões
- [[apktool-injecao-frida-gadget-so-smali-dispositivos-sem-root]] — Veja também: Apktool + **`frida-gadget.so`**: Como Embutir o Frida Dentro de um APK via `System.loadLibrary` em Smali para Instrumentação em **Aparelhos Sem Root**.
- [[apktool-gestao-frameworks-if-install-framework-roms-fabricantes]] — Veja também: Apktool (`if` / `install-framework`): Gestão de **APKs de Framework (`framework-res.apk`)** para Aplicativos de Sistema de Fabricantes (Samsung / Xiaomi / AOSP).
- [[apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali]] — Referência cruzada direta com apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali.
- [[apktool-controles-decodificacao-no-src-no-res-only-main-classes]] — Referência cruzada direta com apktool-controles-decodificacao-no-src-no-res-only-main-classes.
- [[apktool-defesas-anti-repackaging-assinatura-play-integrity-auditoria]] — Referência cruzada direta com apktool-defesas-anti-repackaging-assinatura-play-integrity-auditoria.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
