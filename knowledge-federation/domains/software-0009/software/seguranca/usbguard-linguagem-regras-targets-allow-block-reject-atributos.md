---
id: software.seguranca.tranche05.000472
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

# USBGuard: Gramática da Linguagem de Regras — Alvos (`allow`, `block`, `reject`), `device_id` e Atributos (`hash`, `serial`, `via-port`)

## Em uma frase
O daemon do USBGuard avalia as regras de `/etc/usbguard/rules.conf` sequencialmente de cima para baixo (*first-match wins*) segundo a gramática `rule ::= target device_id device_attributes conditions`.

## Por que importa
Diferenciar os três alvos (`allow`, `block` e `reject`) e combinar atributos criptográficos (`hash`) e físicos (`via-port`) permite criar políticas precisas de *allowlisting* que resistem à falsificação simples de `VendorID:ProductID`.

## Como funciona
Os três alvos são: **`allow`** (autoriza o dispositivo para uso pelo sistema), **`block`** (desautoriza o dispositivo mantendo-o visível em `list-devices` para eventual aprovação temporária) e **`reject`** (remove completamente o nó do dispositivo do subsistema do kernel). Os atributos suportam `id VENDOR:PRODUCT`, `hash "HEX32"` (calculado pelo USBGuard sobre os descritores via libsodium/libgcrypt/OpenSSL), `name "..."`, `serial "..."`, `via-port "b-n"` e `with-interface cc:ss:pp`.

## Exemplo
```ini
# Autorizar um token YubiKey especifico validando simultaneamente ID, hash de descritor e interface
allow id 1050:0407 name "YubiKey OTP+FIDO+CCID" hash "a1b2c3d4e5f60123456789abcdef0123" with-interface { 03:01:01 03:00:00 0b:00:00 }

# Rejeitar e remover imediatamente do kernel qualquer dispositivo não autorizado ao final da lista
reject
```

## Limites e trade-offs
Confiar apenas no par `id VENDOR:PRODUCT` (ex.: `allow id 046d:c52b`) sem restringir `with-interface` ou `hash` é inseguro, pois ferramentas de BadUSB permitem clonar qualquer `VendorID:ProductID` de um fabricante conhecido em segundos.

## Como verificar
Execute `usbguard list-rules` e valide a ordem sequencial das regras carregadas pelo daemon.

## Conexões
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Veja também: USBGuard: Arquitetura de Autorização de Dispositivos USB no Linux e Defesa contra Ataques *BadUSB* / *Rubber Ducky*.
- [[usbguard-protecao-badusb-operadores-with-interface-hid-storage]] — Veja também: USBGuard: Prevenção contra Dispositivos Compostos (*BadUSB*) usando Operadores de Conjunto em `with-interface` (`equals`, `none-of`, `one-of`).
- [[usbguard-condicoes-dinamicas-localtime-allowed-matches-rule-applied]] — Referência cruzada direta com usbguard-condicoes-dinamicas-localtime-allowed-matches-rule-applied.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
