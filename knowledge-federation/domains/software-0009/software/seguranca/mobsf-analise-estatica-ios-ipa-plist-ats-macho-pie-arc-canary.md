---
id: software.seguranca.tranche11.001033
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

# MobSF **iOS Static Analyzer**: Auditoria de Pacotes `.ipa`, **`Info.plist` (`App Transport Security / ATS`)**, Entitlements e Binários **Mach-O (`PIE`, `ARC`, `Canary`)**

## Em uma frase
Como auditar a segurança de um aplicativo **Apple iOS (`.ipa` ou código-fonte Swift / Objective-C)** sem precisar de um iPhone com jailbreak para a fase estática?

## Por que importa
Ao receber um arquivo **`.ipa`** (que internamente é um arquivo ZIP contendo `Payload/<App>.app/`), o **iOS Static Analyzer** do MobSF extrai e analisa quatro pilares fundamentais da segurança iOS:

## Como funciona
**(1) `Info.plist` & `App Transport Security (ATS)`** — verifica se o desenvolvedor desabilitou a proteção TLS obrigatória da Apple usando `NSAllowsArbitraryLoads = true` ou `NSAllowsArbitraryLoadsInWebContent = true`, e audita Custom URL Schemes (`CFBundleURLTypes`); **(2) `Entitlements` e Provisioning Profile** — verifica se o binário possui `get-task-allow: true` (que permite anexar um debugger em dispositivos comuns!); **(3) Análise Binária Mach-O (`macholib` & `LIEF`)** — verifica no executável nativo iOS se **PIE (`MH_PIE`)**, **Stack Canary (`___stack_chk_guard`)**, **ARC (`_objc_release` — *Automatic Reference Counting*)** e criptografia FairPlay (`LC_ENCRYPTION_INFO_64`) estão ativos; e **(4) SAST sobre Swift/Objective-C**!

## Exemplo
```bash
# Enviar um pacote iOS (.ipa) e acionar o scan estatico via API REST do MobSF para auditar ATS e protecoes Mach-O
MOBSF_API_KEY="sua_chave_api_mobsf_aqui"
UPLOAD_JSON=$(curl -sS -F "file=@/cases/mobile/ios-banking.ipa" -H "Authorization: ${MOBSF_API_KEY}" http://127.0.0.1:8000/api/v1/upload)
FILE_HASH=$(echo "${UPLOAD_JSON}" | jq -r '.hash')

curl -sS -X POST http://127.0.0.1:8000/api/v1/scan \
  -H "Authorization: ${MOBSF_API_KEY}" \
  -d "hash=${FILE_HASH}" | jq '.macho_analysis, .ats_analysis'
```

## Limites e trade-offs
Entenda por que verificar **`ARC` (*Automatic Reference Counting*)**, **`PIE`** e **`Stack Canary`** na seção `macho_analysis` do MobSF é obrigatório no **OWASP MASVS**: em código Objective-C/C++ compilado sem `-fobjc-arc` ou sem `-fstack-protector-all`, falhas de gerenciamento manual de memória (`retain`/`release`) levam diretamente a vulnerabilidades *Use-After-Free (UAF)*!

## Como verificar
Se o aplicativo `.ipa` tiver sido baixado diretamente da App Store (com o segmento `__TEXT` criptografado pelo FairPlay DRM da Apple, `cryptid = 1`), peça ao time de desenvolvimento o `.ipa` de homologação (Ad-Hoc / Enterprise) ou extraia o binário descriptografado da memória com **Objection / `frida-ios-dump`**.

## Conexões
- [[mobsf-analise-estatica-android-manifest-certificados-apkid-niap]] — Veja também: MobSF **Android Static Analyzer**: Auditoria de Assinaturas (`apksigtool` v1–v4), Detecção de Packers (**`APKiD`**), `AndroidManifest.xml`, **NIAP** e Bibliotecas `.so` (`LIEF`).
- [[mobsf-analise-dinamica-android-ios-frida-emulator-corellium-mitm]] — Veja também: MobSF **Dynamic Analyzer**: Instrumentação Interativa com **Frida**, Emuladores Android (**AVD / Genymotion**) e **Corellium iOS** com Interceptação HTTPS.
- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — Referência cruzada direta com mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx.
- [[objection-exploracao-ios-keychain-dump-nsuserdefaults-plist-bypasses]] — Referência cruzada direta com objection-exploracao-ios-keychain-dump-nsuserdefaults-plist-bypasses.
- [[mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif]] — Referência cruzada direta com mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
