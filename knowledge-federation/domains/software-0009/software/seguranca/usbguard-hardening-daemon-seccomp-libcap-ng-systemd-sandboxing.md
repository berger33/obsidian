---
id: software.seguranca.tranche05.000480
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

# USBGuard: Hardening do Próprio `usbguard-daemon` (Filtro `libseccomp`, Drop de Capabilities `libcap-ng` e Sandboxing `systemd`)

## Em uma frase
Como o `usbguard-daemon` analisa descritores binários fornecidos diretamente pelo firmware de dispositivos USB físicos potencialmente hostis antes da autorização, o projeto incorpora camadas de autoproteção via **`libseccomp`**, **`libcap-ng`** e isolamento no unit file do `systemd`.

## Por que importa
Um dispositivo USB malicioso projetado especificamente para explorar um bug de parsing nos descritores USB encontrar-se-á confinado dentro de um processo com *capabilities* mínimas e uma *allowlist* estrita de chamadas de sistema.

## Como funciona
O daemon utiliza `libcap-ng` para descartar todas as capabilities POSIX desnecessárias na inicialização, aplica um filtro `seccomp` quando iniciado com `-s` (ou via diretivas `SystemCallFilter=` e `ProtectSystem=strict` no `usbguard.service`) e valida a gramática das regras usando o parser formal PEGTL.

## Exemplo
```bash
# Verificar o status de confinamento, capabilities efetivas (CapEff) e filtro Seccomp do processo usbguard-daemon
PID=$(pidof usbguard-daemon)
grep -E "^(CapEff|Seccomp|NoNewPrivs):" "/proc/${PID}/status"
```

## Limites e trade-offs
Certifique-se de que `/etc/usbguard/` (`0700`) e `/etc/usbguard/rules.conf` (`0600`) pertençam exclusivamente a `root:root`, pois qualquer processo capaz de modificar `rules.conf` pode desativar toda a proteção USB no próximo reload.

## Como verificar
Execute o comando acima sobre `/proc/${PID}/status` e confirme que `NoNewPrivs: 1` e o filtro Seccomp estão ativos no daemon em execução.

## Conexões
- [[usbguard-integracao-ldap-centralizada-frotas-corporativas-sssd]] — Veja também: USBGuard: Gerenciamento Centralizado de Políticas USB em Frotas Corporativas via Backend LDAP (`--with-ldap` / `usbguard-ldap`).
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.
- [[usbguard-configuracao-daemon-conf-implicit-policy-present-device]] — Referência cruzada direta com usbguard-configuracao-daemon-conf-implicit-policy-present-device.
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Referência cruzada direta com apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
