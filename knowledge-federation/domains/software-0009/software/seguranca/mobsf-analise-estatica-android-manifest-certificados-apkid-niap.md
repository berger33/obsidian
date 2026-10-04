---
id: software.seguranca.tranche11.001032
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

# MobSF **Android Static Analyzer**: Auditoria de Assinaturas (`apksigtool` v1–v4), Detecção de Packers (**`APKiD`**), `AndroidManifest.xml`, **NIAP** e Bibliotecas `.so` (`LIEF`)

## Em uma frase
Quando você envia um arquivo `.apk` ou `.aab` para o **Static Analyzer** do MobSF, ele executa uma bateria de verificações estáticas que iriam requerer meia dúzia de ferramentas manuais.

## Por que importa
Primeiro, com **`apksigtool`** e `asn1crypto`, ele valida se o pacote está assinado com os esquemas **v1 (JAR), v2 (APK Signature Scheme v2), v3 (Key Rotation) e v4**, alertando imediatamente se o aplicativo estiver vulnerável à falha histórica **`Janus` (`CVE-2017-13156`, quando um APK usa apenas assinatura v1 em Android antigo)** ou se foi assinado com o certificado público de debug do AOSP!

## Como funciona
Segundo, com **`APKiD`**, ele identifica compiladores, ofuscadores (ProGuard, R8, DexGuard) e *packers* comerciais/maliciosos; terceiro, com **`LIEF`**, analisa todas as bibliotecas nativas C/C++ (`lib/<abi>/*.so`) verificando se foram compiladas com **NX, Stack Canary, RELRO, PIE e Fortify**; e quarto, decompila o DEX com JADX/Baksmali e avalia o código contra o **OWASP MASVS / MSTG** e o perfil governamental **NIAP (`Protection Profile for Application Software`)**!

## Exemplo
```bash
# Enviar um pacote APK para analise estatica automatizada no MobSF via API REST e salvar o hash MD5 retornado
MOBSF_API_KEY="sua_chave_api_mobsf_aqui"
curl -sS -F "file=@/cases/mobile/app-release.apk" \
  -H "Authorization: ${MOBSF_API_KEY}" \
  http://127.0.0.1:8000/api/v1/upload | jq .
```

## Limites e trade-offs
Preste muita atenção à tabela **`Shared Library Binary Analysis`** no relatório do MobSF: muitas equipes de segurança auditam apenas o código Java/Kotlin decompilado e esquecem que bibliotecas nativas `.so` compiladas pelo Android NDK sem `PIE`, sem `Stack Canary` ou sem `Full RELRO` abrem portas para exploração de corrupção de memória!

## Como verificar
Após o `/api/v1/upload` retornar o `hash` do arquivo, dispare o processamento com `POST /api/v1/scan` passando `hash=<md5>`.

## Conexões
- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — Veja também: **Mobile Security Framework (`MobSF`)**: Arquitetura da Plataforma All-in-One de **SAST, DAST e Análise de Malware Mobile** (`APK`, `AAB`, `XAPK`, `IPA`, `APPX`).
- [[mobsf-analise-estatica-ios-ipa-plist-ats-macho-pie-arc-canary]] — Veja também: MobSF **iOS Static Analyzer**: Auditoria de Pacotes `.ipa`, **`Info.plist` (`App Transport Security / ATS`)**, Entitlements e Binários **Mach-O (`PIE`, `ARC`, `Canary`)**.
- [[jadx-auditoria-androidmanifest-exported-components-deep-links-permissions]] — Referência cruzada direta com jadx-auditoria-androidmanifest-exported-components-deep-links-permissions.
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Referência cruzada direta com apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
