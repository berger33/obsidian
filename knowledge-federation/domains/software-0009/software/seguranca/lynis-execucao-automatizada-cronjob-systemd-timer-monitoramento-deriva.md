---
id: software.seguranca.tranche05.000459
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

# CISOfy Lynis: Auditoria Contínua Automatizada (`--cronjob`, `systemd timer`) e Detecção de Deriva de Hardening Index

## Em uma frase
A flag **`--cronjob`** do Lynis executa a auditoria completa em modo silencioso e sem cores ANSI, exibindo na saída padrão apenas alertas críticos enquanto atualiza `/var/log/lynis-report.dat` para coleta por agentes de monitoramento (Prometheus Node Exporter Textfile Collector, Wazuh ou SIEM).

## Por que importa
O *hardening* inicial de uma imagem base (*Golden Image*) degrada ao longo do tempo quando pacotes são instalados ou configurações são alteradas manualmente; monitorar o `hardening_index` e a contagem de `warning[]` diariamente detecta deriva de configuração (*configuration drift*).

## Como funciona
Um `systemd timer` diário executa `lynis audit system --cronjob` e um script pós-execução extrai `hardening_index`, `lynis_tests_done` e o total de `warning[]` e `suggestion[]` de `/var/log/lynis-report.dat`, exportando métricas `.prom` para alerta no Alertmanager caso o índice caia abaixo do limiar mínimo (ex.: `< 82`).

## Exemplo
```bash
#!/usr/bin/env bash
set -euo pipefail
/usr/sbin/lynis audit system --cronjob > /dev/null
INDEX=$(grep "^hardening_index=" /var/log/lynis-report.dat | cut -d= -f2)
WARNINGS=$(grep -c "^warning\[\]=" /var/log/lynis-report.dat || true)
cat <<EOF > /var/lib/node_exporter/textfile_collector/lynis.prom
# HELP lynis_hardening_index Pontuacao de hardening calculada pelo CISOfy Lynis (0-100)
# TYPE lynis_hardening_index gauge
lynis_hardening_index ${INDEX}
lynis_warnings_total ${WARNINGS}
EOF
```

## Limites e trade-offs
Certifique-se de que o diretório `/var/lib/node_exporter/textfile_collector` e o script executável pelo timer possuam permissão `0700`/`0755` de propriedade exclusiva do `root:root`.

## Como verificar
Execute o script acima manualmente e verifique o arquivo `/var/lib/node_exporter/textfile_collector/lynis.prom` gerado.

## Conexões
- [[lynis-hardening-sistemas-arquivos-montagens-suid-permissoes-boot]] — Veja também: CISOfy Lynis: Hardening de Sistemas de Arquivos (`FILE-*`), Opções de Montagem (`nodev`, `nosuid`, `noexec`), `/proc` `hidepid` e GRUB.
- [[lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins]] — Veja também: CISOfy Lynis: Escrita de Testes e Plugins Customizados (`CUST-*`) com Funções Internas (`Register`, `Display`) e `lynis-sdk`.
- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — Referência cruzada direta com lynis-arquitetura-auditoria-hardening-unix-linux-test-categories.
- [[lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details]] — Referência cruzada direta com lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
