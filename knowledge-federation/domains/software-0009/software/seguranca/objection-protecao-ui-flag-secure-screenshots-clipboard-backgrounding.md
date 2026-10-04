---
id: software.seguranca.tranche11.001050
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
fontes: ["https://raw.githubusercontent.com/sensepost/objection/master/README.md", "https://github.com/sensepost/objection/wiki/Patching-Android-Applications"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria de Proteções de Interface e Vazamento em Background no `objection`: **`android ui FLAG_SECURE`**, Pasteboard/Clipboard e Snapshots de Tela

## Em uma frase
Dois requisitos clássicos da seção **`MASVS-PLATFORM`** do guia OWASP para aplicativos financeiros e de saúde são: **(1)** Impedir que telas contendo dados sensíveis (saldos, senhas, chaves PIX, prontuários) possam sofrer captura de tela por malwares de acessibilidade ou tenham **Snapshots de Tela gerados pelo sistema operacional quando o usuário minimiza o aplicativo (*App Switcher / Background Snapshot*)**; e **(2)** Evitar o vazamento de códigos e senhas pela Área de Transferência (**Clipboard / UIPasteboard**)!

## Por que importa
No `objection`, você testa e audita ambos os controles em segundos: no Android, **`android ui FLAG_SECURE false`** (ou `true`) altera dinamicamente a flag `WindowManager.LayoutParams.FLAG_SECURE` das janelas da Activity atual (permitindo tanto tirar screenshots durante o pentest quanto verificar se a flag estava ativa!); e **`android clipboard monitor`** (ou **`ios pasteboard monitor`** no iOS) escuta em tempo real tudo o que é copiado para a área de transferência!

## Como funciona
Já no iOS, quando o aplicativo vai para segundo plano (`applicationDidEnterBackground:`), o iOS tira automaticamente uma foto da tela atual e a salva em texto claro na pasta **`Library/SplashBoard/Snapshots/`** do sandbox do app — a menos que o desenvolvedor oculte a view ou aplique um efeito de blur antes do snapshot!

## Exemplo
```text
# Auditar vazamento de dados no Clipboard/Pasteboard e inspecionar a pasta de Snapshots de tela no iOS e FLAG_SECURE no Android
com.empresa.mobileapp on (Android: 14) [usb] # android clipboard monitor
com.empresa.mobileapp on (Android: 14) [usb] # android ui FLAG_SECURE false
```

## Limites e trade-offs
Durante o pentest de um aplicativo iOS com o `objection`, abra uma tela com dados bancários/pessoais, minimize o aplicativo (botão Home / swipe up) e navegue no REPL do `objection` até `Library/SplashBoard/Snapshots/` (ou `Library/Caches/Snapshots/`) usando `file download`: se a imagem `.ktx` / `.png` baixada contiver os dados confidenciais legíveis, reporte a vulnerabilidade de **Background Screen Caching (`MSTG-STORAGE-9`)**!

## Como verificar
No Android, mantenha `getWindow().setFlags(LayoutParams.FLAG_SECURE, LayoutParams.FLAG_SECURE)` ativo nas Activities sensíveis em builds de produção.

## Conexões
- [[objection-sistema-plugins-customizados-importacao-scripts-frida-api]] — Veja também: Extensibilidade do `objection`: Sistema de **Plugins (`plugin load`)**, Execução de Scripts Frida (`import`) e API REST (`--api-host` / `--api-port`).
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Referência cruzada direta com objection-arquitetura-runtime-mobile-exploration-frida-repl-usb.
- [[objection-exploracao-ios-keychain-dump-nsuserdefaults-plist-bypasses]] — Referência cruzada direta com objection-exploracao-ios-keychain-dump-nsuserdefaults-plist-bypasses.
- [[mobsf-analise-dinamica-android-ios-frida-emulator-corellium-mitm]] — Referência cruzada direta com mobsf-analise-dinamica-android-ios-frida-emulator-corellium-mitm.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
