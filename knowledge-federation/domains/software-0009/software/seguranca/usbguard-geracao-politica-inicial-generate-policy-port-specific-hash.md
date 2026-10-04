---
id: software.seguranca.tranche05.000475
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

# USBGuard: Geração Segura de Política Inicial com `usbguard generate-policy` (`-p`, `-P`, `-H` e `-t`)

## Em uma frase
O subcomando **`usbguard generate-policy`** inspeciona todos os dispositivos USB conectados ao sistema no momento da execução e gera um conjunto de regras `allow` prontas para `/etc/usbguard/rules.conf`.

## Por que importa
Dispositivos USB baratos frequentemente não exportam um número de série único (`iSerial` vazio); para impedir que um atacante desconecte um periférico em outra porta ou use um dispositivo clonado em qualquer porta livre, o `generate-policy` vincula automaticamente dispositivos sem serial à sua porta física exata (`via-port "b-n"`).

## Como funciona
As opções da CLI permitem ajustar a rigidez da política gerada: **`-p`** força regras vinculadas à porta (`via-port`) para **todos** os dispositivos (mesmo os que possuem serial), **`-P`** desativa `via-port` para dispositivos sem serial, **`-H`** gera regras baseadas apenas no atributo `hash` (ocultando nome/serial em claro) e **`-t reject`** adiciona uma regra explícita *catch-all* ao final.

## Exemplo
```bash
# Gerar politica vinculando todos os dispositivos atuais às suas portas fisicas exatas e rejeitando o restante
sudo usbguard generate-policy -p -t reject > /tmp/rules.conf.candidate
cat /tmp/rules.conf.candidate
```

## Limites e trade-offs
Ao usar `-p` (vinculação estrita a `via-port` para todos os dispositivos), se o usuário desconectar o mouse da porta USB esquerda e conectá-lo na porta USB direita, o dispositivo será bloqueado até voltar para a porta original.

## Como verificar
Revise `/tmp/rules.conf.candidate` antes de movê-lo para `/etc/usbguard/rules.conf` e valide a presença dos hubs internos (`09:00:*`).

## Conexões
- [[usbguard-condicoes-dinamicas-localtime-allowed-matches-rule-applied]] — Veja também: USBGuard: Condições Contextuais de Regras (`if !allowed-matches(...)`, `localtime(...)` e `rule-applied`).
- [[usbguard-configuracao-daemon-conf-implicit-policy-present-device]] — Veja também: USBGuard: Hardening de `/etc/usbguard/usbguard-daemon.conf` (`ImplicitPolicyTarget`, `PresentDevicePolicy`, `PresentControllerPolicy`).
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.
- [[usbguard-linguagem-regras-targets-allow-block-reject-atributos]] — Referência cruzada direta com usbguard-linguagem-regras-targets-allow-block-reject-atributos.

## Fontes
- [USBGuard Official GitHub — Device Authorization Framework](https://raw.githubusercontent.com/USBGuard/usbguard/main/README.adoc) — documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy; consultado em 2026-10-03.
- [USBGuard Official Documentation — Rule Language Grammar](https://usbguard.github.io/documentation/rule-language.html) — especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições); consultado em 2026-10-03.
- [USBGuard Official Documentation — Daemon Configuration](https://usbguard.github.io/documentation/configuration.html) — referência de configuração do usbguard-daemon.conf e controle IPC; consultado em 2026-10-03.
