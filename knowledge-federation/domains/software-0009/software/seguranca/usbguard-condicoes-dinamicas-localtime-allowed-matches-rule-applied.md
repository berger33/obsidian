---
id: software.seguranca.tranche05.000474
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

# USBGuard: Condições Contextuais de Regras (`if !allowed-matches(...)`, `localtime(...)` e `rule-applied`)

## Em uma frase
As regras do USBGuard suportam cláusulas condicionais **`if [!]condition`** (ou conjuntos `if all-of { ... }`) que avaliam o estado dinâmico do sistema no exato instante em que um novo dispositivo USB é conectado.

## Por que importa
Permite expressar a política defensiva mais eficaz para estações de trabalho corporativas: *"permita conectar um teclado USB **somente se** ainda não houver nenhum teclado USB autorizado conectado à máquina"* (`if !allowed-matches(with-interface one-of { 03:00:01 03:01:01 })`).

## Como funciona
Além de `allowed-matches(query)` (que verifica os dispositivos atualmente autorizados no barramento), a linguagem suporta **`localtime(HH:MM-HH:MM)`** (autorizando dispositivos de backup apenas dentro da janela de manutenção comercial) e **`rule-applied(past_duration)`** / **`rule-evaluated`** para controle temporal.

## Exemplo
```ini
# Autorizar um teclado USB somente se nenhum outro teclado HID (03:00:01 ou 03:01:01) ja estiver ativo no host
allow with-interface one-of { 03:00:01 03:01:01 } if !allowed-matches(with-interface one-of { 03:00:01 03:01:01 })

# Bloquear qualquer teclado adicional inserido enquanto o teclado principal estiver conectado (anti-Rubber Ducky)
block with-interface one-of { 03:00:01 03:01:01 }
```

## Limites e trade-offs
Em notebooks cujos teclados internos são conectados via barramento PS/2 ou I2C (e não USB), `allowed-matches` verá `0` teclados USB conectados; para notebooks, bloqueie teclados USB externos por padrão ou autorize apenas o hash específico da dock station homologada.

## Como verificar
Verifique com `usbguard list-devices` quantos dispositivos `03:01:01` já constam como `allow` no host antes de calibrar a condição `!allowed-matches(...)`.

## Conexões
- [[usbguard-protecao-badusb-operadores-with-interface-hid-storage]] — Veja também: USBGuard: Prevenção contra Dispositivos Compostos (*BadUSB*) usando Operadores de Conjunto em `with-interface` (`equals`, `none-of`, `one-of`).
- [[usbguard-geracao-politica-inicial-generate-policy-port-specific-hash]] — Veja também: USBGuard: Geração Segura de Política Inicial com `usbguard generate-policy` (`-p`, `-P`, `-H` e `-t`).
- [[usbguard-linguagem-regras-targets-allow-block-reject-atributos]] — Referência cruzada direta com usbguard-linguagem-regras-targets-allow-block-reject-atributos.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
