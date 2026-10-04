---
id: software.seguranca.tranche05.000476
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc", "https://usbguard.github.io/documentation/rule-language.html", "https://usbguard.github.io/documentation/configuration.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# USBGuard: Hardening de `/etc/usbguard/usbguard-daemon.conf` (`ImplicitPolicyTarget`, `PresentDevicePolicy`, `PresentControllerPolicy`)

## Em uma frase
O arquivo **`/etc/usbguard/usbguard-daemon.conf`** controla o comportamento global do `usbguard-daemon`, incluindo o destino padrão quando nenhuma regra casa (`ImplicitPolicyTarget`), o tratamento de dispositivos já conectados antes do daemon subir (`PresentDevicePolicy`) e o controle de acesso IPC (`IPCAllowedUsers` / `IPCAllowedGroups`).

## Por que importa
Se um atacante físico conectar um dispositivo malicioso durante o boot antes do `usbguard-daemon` iniciar e `PresentDevicePolicy` estiver configurado como `allow`, o dispositivo escapará da avaliação das regras de `/etc/usbguard/rules.conf`.

## Como funciona
Em ambientes endurecidos, configure **`PresentDevicePolicy=apply-policy`** (avalia todos os dispositivos já presentes contra `rules.conf` assim que o daemon inicia), **`InsertedDevicePolicy=apply-policy`**, **`ImplicitPolicyTarget=block`** (ou `reject`), **`RestoreControllerDeviceState=false`** e **`DeviceRulesWithPort=true`**.

## Exemplo
```ini
# /etc/usbguard/usbguard-daemon.conf — Configuracao endurecida para servidores e estacoes criticas
RuleFile=/etc/usbguard/rules.conf
ImplicitPolicyTarget=block
PresentDevicePolicy=apply-policy
PresentControllerPolicy=keep
InsertedDevicePolicy=apply-policy
RestoreControllerDeviceState=false
AuditBackend=LinuxAudit
IPCAllowedUsers=root
IPCAllowedGroups=secops-usb-admins
```

## Limites e trade-offs
Alterar `PresentDevicePolicy=block` sem ter os hubs e dispositivos internos cadastrados em `/etc/usbguard/rules.conf` bloqueará imediatamente todos os dispositivos presentes no boot; use `apply-policy` com um `rules.conf` previamente validado.

## Como verificar
Inspecione `sudo grep -v '^#' /etc/usbguard/usbguard-daemon.conf | grep -v '^$'` e confirme `PresentDevicePolicy=apply-policy` e `AuditBackend=LinuxAudit`.

## Conexões
- [[usbguard-geracao-politica-inicial-generate-policy-port-specific-hash]] — Veja também: USBGuard: Geração Segura de Política Inicial com `usbguard generate-policy` (`-p`, `-P`, `-H` e `-t`).
- [[usbguard-controle-acesso-ipc-polkit-dbus-allow-device-temporario]] — Veja também: USBGuard: Administração Dinâmica (`allow-device`, `block-device`, `append-rule -t`) e Controle de Acesso IPC / Polkit.
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
