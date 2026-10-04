---
id: software.seguranca.tranche05.000460
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
fontes: ["https://raw.githubusercontent.com/CISOfy/lynis/master/README.md", "https://cisofy.com/documentation/lynis/get-started/", "https://github.com/CISOfy/lynis-sdk"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CISOfy Lynis: Escrita de Testes e Plugins Customizados (`CUST-*`) com Funções Internas (`Register`, `Display`) e `lynis-sdk`

## Em uma frase
O Lynis permite que equipes de engenharia de segurança escrevam seus próprios testes internos (`include/tests_custom` com IDs `CUST-xxxx`) e plugins para validar políticas corporativas específicas e testá-los com o **`lynis-sdk`**.

## Por que importa
Organizações frequentemente possuem controles internos obrigatórios (ex.: verificar se o agente do EDR corporativo está ativo, se o certificado da CA interna está instalado ou se o `usbguard.service` está em execução) que precisam entrar no cálculo do *Hardening Index* junto com os testes nativos.

## Como funciona
Cada teste customizado utiliza a função `Register` (declarando `--test-no CUST-0010`, `--weight L`, `--network NO`, `--category security`, `--description "..."`) e funções utilitárias do Lynis como `IsRunning`, `FileExists`, `Display` e `AddHP <pontos> <maximo>` (que adiciona pontos diretamente ao cálculo do *Hardening Index*).

## Exemplo
```sh
# Exemplo de teste customizado em include/tests_custom verificando se o usbguard-daemon está ativo
Register --test-no CUST-0010 --weight L --network NO --category security --description "Check active USBGuard daemon"
if [ ${SKIPTEST} -eq 0 ]; then
    IsRunning "usbguard-daemon"
    if [ ${RUNNING} -eq 1 ]; then
        Display --indent 2 --text "- Checking USBGuard daemon status" --result "${STATUS_FOUND}" --color GREEN
        AddHP 3 3
    else
        Display --indent 2 --text "- Checking USBGuard daemon status" --result "${STATUS_NOT_FOUND}" --color YELLOW
        AddHP 0 3
        ReportSuggestion "${TEST_NO}" "Enable and start usbguard.service to block unauthorized USB devices"
    fi
fi
```

## Limites e trade-offs
Sempre utilize o prefixo reservado `CUST-` para IDs de testes internos customizados, evitando colisão com IDs oficiais futuros do repositório `CISOfy/lynis`.

## Como verificar
Execute `sudo lynis audit system --tests CUST-0010 --quick` e confirme que o teste customizado é executado, pontua via `AddHP` e aparece listado em `/var/log/lynis-report.dat`.

## Conexões
- [[lynis-execucao-automatizada-cronjob-systemd-timer-monitoramento-deriva]] — Veja também: CISOfy Lynis: Auditoria Contínua Automatizada (`--cronjob`, `systemd timer`) e Detecção de Deriva de Hardening Index.
- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — Referência cruzada direta com lynis-arquitetura-auditoria-hardening-unix-linux-test-categories.
- [[lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh]] — Referência cruzada direta com lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh.
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
