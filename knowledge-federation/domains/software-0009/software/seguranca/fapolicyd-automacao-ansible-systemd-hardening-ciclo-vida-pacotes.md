---
id: software.seguranca.tranche15.001440
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md", "https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Operação em Escala do fapolicyd com **Ansible (`rhel-system-roles.fapolicyd`)**, Integração **`dnf` / `rpm`** e Proteção do Daemon contra Parada Indevida

## Em uma frase
Como implantar e gerenciar o **`fapolicyd`** de forma padronizada em centenas de servidores Linux via **Ansible / GitOps**, garantindo que atualizações normais de pacotes (`dnf update`) nunca quebrem o banco de confiança e que o serviço seja monitorado continuamente?

## Por que importa
Primeiro: o pacote **`fapolicyd-dnf-plugin`** (instalado junto com o `fapolicyd` no RHEL/Fedora/AlmaLinux/Rocky) engancha-se nas transações do `dnf` / `rpm` e notifica o daemon `fapolicyd` via pipe FIFO (`/run/fapolicyd/fapolicyd.fifo`) a cada pacote instalado, atualizado ou removido — atualizando o banco LMDB automaticamente durante a manutenção!

## Como funciona
Segundo: no Ansible, você gerencia declarativamente o `/etc/fapolicyd/fapolicyd.conf` (`integrity = sha256`, `permissive = 0`), os arquivos de confiança em `/etc/fapolicyd/trust.d/` e as regras customizadas em `/etc/fapolicyd/rules.d/` acionando um handler `fagenrules --load && fapolicyd-cli --update`!

## Exemplo
```bash
# Validar a consistencia completa do banco de confianca LMDB, listar os arquivos de trust.d ativos e verificar o servico systemd do fapolicyd
fapolicyd-cli --check-trustdb
ls -la /etc/fapolicyd/trust.d/ /etc/fapolicyd/rules.d/
systemctl is-active fapolicyd
```

## Limites e trade-offs
Atenção a um cuidado operacional importante ao atualizar sistemas que instalam aplicações via scripts fora do `rpm`/`dnf` (como instaladores `.run` ou tarballs): durante a janela de deploy automatizado via Ansible, o playbook deve copiar os novos arquivos para `/opt/...`, rodar **`fapolicyd-cli --file add /opt/... --trust-file <app>`** (ou `--file update`) e executar **`fapolicyd-cli --update`** **antes** de reiniciar o serviço da aplicação!

## Como verificar
Combine o **`fapolicyd` (`integrity = sha256`)** com o **SELinux em modo `Enforcing`** e auditoria **OpenSCAP** para atingir o padrão ouro de defesa em profundidade exigido pelos perfis **DISA STIG** e **OSPP**.

## Conexões
- [[fapolicyd-auditoria-auditd-fanotify-syslog-format-correlacao-siem]] — Veja também: Correlação de Bloqueios do fapolicyd com **`auditd` (`FANOTIFY`)** e Customização do **`syslog_format`** para Detecção Imediata no SIEM.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.
- [[fapolicyd-gerenciamento-trust-database-fapolicyd-cli-file-add-trust-d]] — Referência cruzada direta com fapolicyd-gerenciamento-trust-database-fapolicyd-cli-file-add-trust-d.
- [[openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html]] — Referência cruzada direta com openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
