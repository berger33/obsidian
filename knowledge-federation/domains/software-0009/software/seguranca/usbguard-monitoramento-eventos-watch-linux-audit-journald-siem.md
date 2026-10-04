---
id: software.seguranca.tranche05.000478
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

# USBGuard: Monitoramento em Tempo Real (`usbguard watch`), Integração com `LinuxAudit` (`AUDIT_USER_DEVICE`) e SIEM

## Em uma frase
O USBGuard registra todas as inserções de dispositivos, mudanças de estado (`Present`, `Insert`, `Update`, `Remove`) e decisões de política (`allow` -> `block` / `reject`) tanto no fluxo de eventos IPC (`usbguard watch`) quanto diretamente no subsistema **Linux Audit (`auditd`)** e `journald`.

## Por que importa
Detectar que alguém tentou inserir um dispositivo USB que se apresentou como teclado HID ou placa de rede em um servidor de datacenter ou estação de trabalho é um alerta de segurança física de altíssima fidelidade para o SOC.

## Como funciona
Quando `AuditBackend=LinuxAudit` está habilitado em `/etc/usbguard/usbguard-daemon.conf` (e o binário foi compilado com `libaudit`), cada tentativa bloqueada gera um registro `USER_DEVICE` no `/var/log/audit/audit.log` contendo o `device_rule`, `hash`, `id`, `name`, `via-port` e `with-interface` do dispositivo rejeitado.

## Exemplo
```bash
# Consultar no Linux Audit (auditd) todos os eventos de dispositivos USB registrados pelo USBGuard hoje
sudo ausearch -m USER_DEVICE -ts today -i
```

## Limites e trade-offs
Em quiosques de autoatendimento, caixas eletrônicos ou servidores de borda, configure uma regra no SIEM que dispare incidente imediato sempre que o `auditd` registrar um evento `USER_DEVICE` com `result=ERROR` ou `target=block`/`reject`.

## Como verificar
Execute `usbguard watch -o` em um terminal de teste ou consulte `sudo journalctl -u usbguard.service` para validar os campos de telemetria emitidos.

## Conexões
- [[usbguard-controle-acesso-ipc-polkit-dbus-allow-device-temporario]] — Veja também: USBGuard: Administração Dinâmica (`allow-device`, `block-device`, `append-rule -t`) e Controle de Acesso IPC / Polkit.
- [[usbguard-integracao-ldap-centralizada-frotas-corporativas-sssd]] — Veja também: USBGuard: Gerenciamento Centralizado de Políticas USB em Frotas Corporativas via Backend LDAP (`--with-ldap` / `usbguard-ldap`).
- [[usbguard-configuracao-daemon-conf-implicit-policy-present-device]] — Referência cruzada direta com usbguard-configuracao-daemon-conf-implicit-policy-present-device.
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Referência cruzada direta com auditd-investigacao-forense-ausearch-aureport-auid-correlacao.
- [[lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins]] — Referência cruzada direta com lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
