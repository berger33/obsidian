---
id: software.seguranca.tranche05.000477
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

# USBGuard: Administração Dinâmica (`allow-device`, `block-device`, `append-rule -t`) e Controle de Acesso IPC / Polkit

## Em uma frase
A CLI **`usbguard`** comunica-se com o `usbguard-daemon` através de um socket UNIX local baseado em `libqb` e mensagens serializadas em Protobuf (ou via `usbguard-dbus` integrado ao Polkit), permitindo autorizar ou bloquear dispositivos em tempo de execução.

## Por que importa
Permite que um administrador ou analista do grupo autorizado conceda acesso **temporário** (em memória, apenas até o próximo reboot ou desconexão) a um dispositivo específico sem precisar editar `/etc/usbguard/rules.conf` permanentemente.

## Como funciona
Ao omitir a flag `-p` (`--permanent`), `usbguard allow-device <ID>` autoriza o dispositivo apenas para a sessão atual. Se for necessário criar uma regra temporária com expiração automática, `usbguard append-rule -t <segundos> "allow ..."` remove a regra automaticamente após o tempo estipulado. O arquivo `IPCAccessControlFiles` em `/etc/usbguard/IPCAccessControl.d/` permite conceder privilégios granulares (`Devices=listen,list` vs `Policy=modify`) por usuário ou grupo.

## Exemplo
```bash
# Listar apenas dispositivos atualmente bloqueados e autorizar temporariamente o dispositivo de indice 14
usbguard list-devices --blocked
sudo usbguard allow-device 14
```

## Limites e trade-offs
Nunca adicione o grupo de usuários comuns (`users` ou `wheel` amplo) em `IPCAllowedGroups` com permissão de modificação de `Devices` ou `Policy`, pois isso permitiria ao próprio usuário aprovar qualquer dispositivo USB não autorizado que ele mesmo conectasse.

## Como verificar
Configure `usbguard add-user <usuario> --group --devices=listen,list` para permitir que o applet gráfico apenas exiba notificações sem poder aprovar dispositivos sem senha administrativa.

## Conexões
- [[usbguard-configuracao-daemon-conf-implicit-policy-present-device]] — Veja também: USBGuard: Hardening de `/etc/usbguard/usbguard-daemon.conf` (`ImplicitPolicyTarget`, `PresentDevicePolicy`, `PresentControllerPolicy`).
- [[usbguard-monitoramento-eventos-watch-linux-audit-journald-siem]] — Veja também: USBGuard: Monitoramento em Tempo Real (`usbguard watch`), Integração com `LinuxAudit` (`AUDIT_USER_DEVICE`) e SIEM.
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
