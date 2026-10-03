---
id: software.seguranca.tranche05.000479
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

# USBGuard: Gerenciamento Centralizado de Políticas USB em Frotas Corporativas via Backend LDAP (`--with-ldap` / `usbguard-ldap`)

## Em uma frase
Quando compilado com suporte a LDAP (`--with-ldap`), o USBGuard pode buscar as regras de autorização de dispositivos diretamente de um diretório **OpenLDAP / FreeIPA / Active Directory** em vez de depender exclusivamente de arquivos `/etc/usbguard/rules.conf` locais estáticos.

## Por que importa
Em frotas de milhares de estações de trabalho Linux, distribuir novos hashes de tokens FIDO2/YubiKey ou pendrives criptografados homologados via LDAP permite atualizar a política de dispositivos autorizados centralmente por host (`USBGuardHost`) ou para toda a frota (`*`).

## Como funciona
O esquema LDAP do USBGuard define objetos `USBGuardPolicy` contendo atributos `USBGuardRule`, `USBGuardHost` e `USBGuardRuleOrder`, consultados pelo daemon conforme configurado em `/etc/usbguard/usbguard-ldap.conf` (ou integrados via SSSD).

## Exemplo
```ini
# Exemplo de regra distribuída centralmente para autorizar a familia de chaves FIDO2 corporativas
allow id 1050:0402 with-interface equals { 03:01:01 }
allow id 1050:0407 with-interface equals { 03:01:01 03:00:00 0b:00:00 }
```

## Limites e trade-offs
Ao usar o backend LDAP, proteja obrigatoriamente a conexão com **LDAPS / StartTLS** e validação estrita do certificado da CA interna, impedindo que um ataque *Man-in-the-Middle* na rede local injete uma regra `allow *:*` para o `usbguard-daemon`.

## Como verificar
Verifique os logs do `usbguard-daemon` na inicialização para confirmar a leitura e ordenação correta dos objetos `USBGuardRuleOrder`.

## Conexões
- [[usbguard-monitoramento-eventos-watch-linux-audit-journald-siem]] — Veja também: USBGuard: Monitoramento em Tempo Real (`usbguard watch`), Integração com `LinuxAudit` (`AUDIT_USER_DEVICE`) e SIEM.
- [[usbguard-hardening-daemon-seccomp-libcap-ng-systemd-sandboxing]] — Veja também: USBGuard: Hardening do Próprio `usbguard-daemon` (Filtro `libseccomp`, Drop de Capabilities `libcap-ng` e Sandboxing `systemd`).
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.
- [[usbguard-configuracao-daemon-conf-implicit-policy-present-device]] — Referência cruzada direta com usbguard-configuracao-daemon-conf-implicit-policy-present-device.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
