---
id: software.seguranca.tranche05.000471
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

# USBGuard: Arquitetura de Autorização de Dispositivos USB no Linux e Defesa contra Ataques *BadUSB* / *Rubber Ducky*

## Em uma frase
**USBGuard** (`USBGuard/usbguard`, GPLv2, mantido originalmente pela Red Hat) é o framework de segurança de endpoint para Linux que implementa políticas de autorização de dispositivos USB (*quais* dispositivos podem conectar) e políticas de modo de uso (*quais interfaces* cada dispositivo pode expor ao kernel).

## Por que importa
Bloqueia ataques físicos de **BadUSB**, *USB Rubber Ducky*, *OMG Cable* e adaptadores de rede USB maliciosos (onde um pendrive ou cabo aparentemente inocente emula um teclado HID `03:*:*` ou placa Ethernet para injetar comandos ou sequestrar rotas em milissegundos).

## Como funciona
O `usbguard-daemon` interage diretamente com a interface de autorização do subsistema USB do kernel Linux (`/sys/bus/usb/devices/*/authorized` e `authorized_default`), bloqueando o dispositivo no nível do barramento antes que os drivers de classe do kernel (HID, Mass Storage, CDC Ethernet) sejam inicializados, a menos que uma regra explícita em `/etc/usbguard/rules.conf` o autorize.

## Exemplo
```bash
# Gerar a politica inicial para nao bloquear o teclado/mouse atuais ANTES de iniciar o usbguard-daemon
sudo sh -c 'usbguard generate-policy > /etc/usbguard/rules.conf'
sudo chmod 0600 /etc/usbguard/rules.conf
sudo systemctl enable --now usbguard.service
```

## Limites e trade-offs
Nunca inicie o `usbguard.service` pela primeira vez em uma estação de trabalho ou servidor físico com console USB sem antes gerar `/etc/usbguard/rules.conf` via `usbguard generate-policy`, caso contrário a política implícita `block` desautorizará imediatamente o seu teclado USB.

## Como verificar
Execute `usbguard list-devices` e confirme que todos os dispositivos atualmente conectados aparecem com o alvo `allow`.

## Conexões
- [[usbguard-linguagem-regras-targets-allow-block-reject-atributos]] — Veja também: USBGuard: Gramática da Linguagem de Regras — Alvos (`allow`, `block`, `reject`), `device_id` e Atributos (`hash`, `serial`, `via-port`).
- [[usbguard-protecao-badusb-operadores-with-interface-hid-storage]] — Referência cruzada direta com usbguard-protecao-badusb-operadores-with-interface-hid-storage.
- [[lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins]] — Referência cruzada direta com lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
