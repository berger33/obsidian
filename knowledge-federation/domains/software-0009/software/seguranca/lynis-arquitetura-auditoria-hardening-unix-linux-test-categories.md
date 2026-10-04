---
id: software.seguranca.tranche05.000451
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

# CISOfy Lynis: Arquitetura de Auditoria Local e Hardening de Sistemas Linux/Unix (`lynis audit system`)

## Em uma frase
**Lynis** (`CISOfy/lynis`, GPLv3) é a ferramenta open-source padrão para auditoria profunda de segurança, avaliação de conformidade (ISO 27001, PCI-DSS, HIPAA) e recomendação de *hardening* em sistemas Linux, macOS e BSD, escrita em POSIX shell sem dependências compiladas.

## Por que importa
Executa centenas de testes modulares diretamente no host (inspecionando boot/GRUB, kernel `sysctl`, PAM/autenticação, SSH, sistemas de arquivos, firewalls, auditd, AppArmor/SELinux, criptografia e containers) e calcula um **Hardening Index** numérico de `0` a `100`.

## Como funciona
Os testes são organizados por categorias (`boot_services`, `kernel`, `memory_processes`, `authentication`, `shells`, `filesystems`, `storage`, `networking`, `firewalls`, `ssh`, `logging`, `crypto`, `mac_frameworks`), gerando três saídas complementares: o resumo visual no terminal, o log detalhado de execução (`/var/log/lynis.log`) e o arquivo estruturado de dados (`/var/log/lynis-report.dat`).

## Exemplo
```bash
# Garantir propriedade root:root exigida pelo Lynis e executar auditoria completa sem pausas
sudo chown -R 0:0 /usr/local/lynis
sudo /usr/local/lynis/lynis audit system --quick --auditor "SecOps Platform Team"
```

## Limites e trade-offs
Se os scripts do Lynis pertencerem a um usuário não-privilegiado (UID != 0) mas forem executados com `sudo`, o próprio Lynis emitirá um alerta de segurança no início da execução devido ao risco de escalação de privilégio por modificação do script.

## Como verificar
Verifique no final da execução a pontuação `Hardening index` e inspecione `/var/log/lynis-report.dat` com `sudo grep "^hardening_index=" /var/log/lynis-report.dat`.

## Conexões
- [[lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details]] — Veja também: CISOfy Lynis: Análise de `Warnings` vs `Suggestions`, `/var/log/lynis-report.dat` e `lynis show details <TEST-ID>`.
- [[lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh]] — Referência cruzada direta com lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh.
- [[lynis-execucao-automatizada-cronjob-systemd-timer-monitoramento-deriva]] — Referência cruzada direta com lynis-execucao-automatizada-cronjob-systemd-timer-monitoramento-deriva.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
