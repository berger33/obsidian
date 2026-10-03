---
id: software.seguranca.tranche05.000473
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

# USBGuard: Prevenção contra Dispositivos Compostos (*BadUSB*) usando Operadores de Conjunto em `with-interface` (`equals`, `none-of`, `one-of`)

## Em uma frase
Um ataque clássico de *BadUSB* consiste em um dispositivo composto que se apresenta inicialmente como um pendrive (*Mass Storage*, classe `08:*:*`), mas também expõe uma interface oculta de teclado (*HID Keyboard*, classe `03:01:01` ou `03:*:*`) ou placa de rede (`02:*:*` / `e0:*:*`).

## Por que importa
Se uma regra de armazenamento USB usar `with-interface 08:*:*` sem operador restritivo ou usar `one-of`, um dispositivo malicioso que exponha `{ 08:06:50 03:01:01 }` será autorizado e injetará comandos como se fosse um teclado.

## Como funciona
A linguagem do USBGuard resolve esse vetor exigindo operadores de conjunto estritos em `with-interface`: **`equals { 08:*:* }`** (o conjunto de interfaces do dispositivo deve conter **exclusivamente** armazenamento em massa e nada mais) combinado com uma regra anterior de bloqueio explícito para qualquer dispositivo que misture armazenamento e HID ou que tente adicionar um segundo teclado quando já houver um conectado.

## Exemplo
```ini
# Permitir dispositivos de armazenamento USB SOMENTE se eles expuserem exclusivamente a classe Mass Storage (08:*:*)
allow with-interface equals { 08:*:* }

# Rejeitar imediatamente qualquer dispositivo composto que combine Mass Storage (08) com HID (03)
reject with-interface all-of { 08:*:* 03:*:* }
```

## Limites e trade-offs
As classes USB-IF são expressas em três octetos hexadecimais `cc:ss:pp` (`03` = HID, `08` = Mass Storage, `09` = Hub, `0b` = Smart Card/CCID, `0e` = Video/Webcam); lembre-se de que se usar `*` na subclasse (`ss`), a gramática exige `*` também no protocolo (`08:*:*`).

## Como verificar
Teste a sintaxe da política e confirme via `usbguard list-rules` que a regra `reject with-interface all-of { 08:*:* 03:*:* }` precede quaisquer regras gerais.

## Conexões
- [[usbguard-linguagem-regras-targets-allow-block-reject-atributos]] — Veja também: USBGuard: Gramática da Linguagem de Regras — Alvos (`allow`, `block`, `reject`), `device_id` e Atributos (`hash`, `serial`, `via-port`).
- [[usbguard-condicoes-dinamicas-localtime-allowed-matches-rule-applied]] — Veja também: USBGuard: Condições Contextuais de Regras (`if !allowed-matches(...)`, `localtime(...)` e `rule-applied`).
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
