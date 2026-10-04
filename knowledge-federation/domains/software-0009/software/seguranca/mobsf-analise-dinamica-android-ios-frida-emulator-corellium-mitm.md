---
id: software.seguranca.tranche11.001034
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

# MobSF **Dynamic Analyzer**: Instrumentação Interativa com **Frida**, Emuladores Android (**AVD / Genymotion**) e **Corellium iOS** com Interceptação HTTPS

## Em uma frase
A análise estática encontra vulnerabilidades no código e no manifesto, mas apenas a **Análise Dinâmica (DAST / IAST Mobile)** revela o que o aplicativo realmente grava no banco SQLite/SharedPreferences em tempo de execução, quais chamadas criptográficas faz e quais dados envia pela rede!

## Por que importa
O **Dynamic Analyzer** do MobSF conecta-se a um **Emulador Android (`Android Studio AVD` sem Google Play — imagem `google_apis`, ou `Genymotion`)** via ADB ou a uma instância virtual **iOS no Corellium**!

## Como funciona
Quando você inicia o teste dinâmico no MobSF, ele realiza automaticamente quatro passos de instrumentação que economizam horas do pentester: **(1)** Instala o certificado CA raiz do proxy do MobSF (`http-tools` na porta `1337`) no repositório de certificados confiáveis de sistema do Android (`/system/etc/security/cacerts/`); **(2)** Injeta scripts **Frida** padrão para **Bypass automático de SSL Pinning, Root Detection e Debugger Detection**; **(3)** Monitora em tempo real APIs sensíveis (Criptografia, Rede, File I/O, Binder IPC, Content Providers, Clipboard); e **(4)** Ao encerrar o teste, baixa um dump completo do diretório `/data/data/<pacote>/`, extraindo bancos SQLite, XMLs e logs para o relatório!

## Exemplo
```bash
# Configurar a variavel de ambiente do MobSF apontando para o emulador Android (ADB) na máquina host antes de iniciar o Dynamic Analyzer
docker run -d --name mobsf-dynamic \
  -p 8000:8000 -p 1337:1337 \
  -e MOBSF_ANALYZER_IDENTIFIER="host.docker.internal:5555" \
  --add-host=host.docker.internal:host-gateway \
  opensecurity/mobile-security-framework-mobsf:latest
```

## Limites e trade-offs
Nota técnica essencial documentada pelo MobSF para Android AVD: ao criar o emulador no Android Studio para uso com o Dynamic Analyzer, escolha uma imagem de sistema **`Google APIs` (sem Google Play Store)**, pois as imagens `Google Play` de produção bloqueiam `adb root` e `adb remount`, impedindo que o MobSF instale a CA raiz no sistema!

## Como verificar
Use os componentes **`Activity Tester`** e **`Exported Activity Tester`** dentro do Dynamic Analyzer do MobSF para disparar automaticamente todas as Activities do aplicativo e capturar screenshots de telas desprotegidas.

## Conexões
- [[mobsf-analise-estatica-ios-ipa-plist-ats-macho-pie-arc-canary]] — Veja também: MobSF **iOS Static Analyzer**: Auditoria de Pacotes `.ipa`, **`Info.plist` (`App Transport Security / ATS`)**, Entitlements e Binários **Mach-O (`PIE`, `ARC`, `Canary`)**.
- [[mobsf-instrumentacao-frida-live-api-monitor-scripts-auxiliares]] — Veja também: MobSF **Live API Monitor & Frida Code Editor**: Monitoramento de Criptografia/Rede em Tempo Real e Scripts Auxiliares (`SSL Pinning`, `Root Bypass`, `Hook`).
- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — Referência cruzada direta com mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx.
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
