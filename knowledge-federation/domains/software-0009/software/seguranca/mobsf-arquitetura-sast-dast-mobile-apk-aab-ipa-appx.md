---
id: software.seguranca.tranche11.001031
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

# **Mobile Security Framework (`MobSF`)**: Arquitetura da Plataforma All-in-One de **SAST, DAST e Análise de Malware Mobile** (`APK`, `AAB`, `XAPK`, `IPA`, `APPX`)

## Em uma frase
Criado por Ajin Abraham e mantido pela comunidade **OpenSecurity** (`MobSF/Mobile-Security-Framework-MobSF`, licença GPL-3.0, escrito em Python 3.12+ / Django), o **Mobile Security Framework (MobSF)** é a principal plataforma open-source automatizada para **Testes de Segurança de Aplicações Móveis (MAST), Pentest, Análise de Malware e Privacidade** em **Android, iOS e Windows Mobile**.

## Por que importa
Diferente de ferramentas que analisam apenas um formato isolado, o **Analisador Estático (*Static Analyzer*)** do MobSF aceita tanto binários compilados (**Android `.apk`, `.aab`, `.xapk`, `.apks`, iOS `.ipa`, bibliotecas `.aar`/`.jar`/`.so`/`.dylib`/`.a` e Windows `.appx`**) quanto pacotes `.zip` de código-fonte (Android Studio / Xcode)!

## Como funciona
Conforme detalha o `pyproject.toml` oficial da versão 4.5+, o MobSF orquestra sob o capô um ecossistema completo de bibliotecas especializadas: **`libsast`** (motor de pattern matching e Semgrep), **`apkid`** (detecção de empacotadores/ofuscadores Android), **`apksigtool`** (verificação de assinaturas APK v1/v2/v3/v4), **`lief`** e **`macholib`** (análise de binários nativos ELF e Mach-O), **`frida` / `frida-tools`** (instrumentação dinâmica) e **`http-tools` / `mitmproxy`** (interceptação de tráfego)!

## Exemplo
```bash
# Iniciar o Mobile Security Framework (MobSF) via container Docker oficial persistindo os dados de analise
docker run -d --name mobsf \
  -p 8000:8000 \
  -p 1337:1337 \
  -v mobsf_data:/home/mobsf/.MobSF \
  opensecurity/mobile-security-framework-mobsf:latest
```

## Limites e trade-offs
Ao subir a imagem Docker oficial (`opensecurity/mobile-security-framework-mobsf`), a porta `8000` expõe a interface web e a **API REST** (credenciais iniciais padrão: `mobsf`/`mobsf`), enquanto a porta `1337` é utilizada pelo proxy de interceptação HTTPS do **Dynamic Analyzer**!

## Como verificar
Altere sempre a senha padrão e proteja a chave de API (`Mobsf-Api-Key`) ao implantar o MobSF em servidores compartilhados da equipe de AppSec.

## Conexões
- [[mobsf-analise-estatica-android-manifest-certificados-apkid-niap]] — Veja também: MobSF **Android Static Analyzer**: Auditoria de Assinaturas (`apksigtool` v1–v4), Detecção de Packers (**`APKiD`**), `AndroidManifest.xml`, **NIAP** e Bibliotecas `.so` (`LIEF`).
- [[mobsf-analise-estatica-ios-ipa-plist-ats-macho-pie-arc-canary]] — Referência cruzada direta com mobsf-analise-estatica-ios-ipa-plist-ats-macho-pie-arc-canary.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
