---
id: software.seguranca.tranche05.000458
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

# CISOfy Lynis: Hardening de Sistemas de Arquivos (`FILE-*`), Opções de Montagem (`nodev`, `nosuid`, `noexec`), `/proc` `hidepid` e GRUB

## Em uma frase
A categoria **`FILE-*`** e **`BOOT-*`** do Lynis audita a separação de partições críticas (`/tmp`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit`, `/home`, `/dev/shm`), as flags de montagem em `/etc/fstab` (`nodev`, `nosuid`, `noexec`), o isolamento de processos em `/proc` (`hidepid=2`) e a proteção por senha PBKDF2 do bootloader GRUB2.

## Por que importa
Se `/tmp` ou `/dev/shm` forem montados com permissão de execução (`exec`) e `suid`, um processo web comprometido pode gravar um binário malicioso ou script ELF em `/dev/shm` e executá-lo diretamente da memória compartilhada.

## Como funciona
O Lynis verifica se `/tmp`, `/var/tmp` e `/dev/shm` possuem `nodev,nosuid,noexec`, se `/home` possui `nodev,nosuid`, se `/proc` está montado com `hidepid=2` (impedindo que um usuário veja os processos e argumentos de linha de comando de outros usuários no host) e se a configuração do GRUB (`/boot/grub/grub.cfg` com permissão `0600`) exige autenticação `grub_pbkdf2` para edição de parâmetros de boot.

## Exemplo
```fstab
# Trecho de /etc/fstab endurecido conforme recomendações FILE-6310 do Lynis
tmpfs   /tmp        tmpfs   defaults,rw,nosuid,nodev,noexec,relatime,size=2G   0  0
tmpfs   /dev/shm    tmpfs   defaults,rw,nosuid,nodev,noexec,relatime           0  0
proc    /proc       proc    defaults,nosuid,nodev,noexec,hidepid=2             0  0
```

## Limites e trade-offs
Aplicar `noexec` em `/tmp` pode quebrar instaladores legados ou agentes que extraem e executam binários temporários em `/tmp`; configure a variável `TMPDIR` desses agentes específicos para um diretório controlado pelo administrador antes de remontar `/tmp` com `noexec`.

## Como verificar
Execute `sudo lynis audit system --tests-from-group filesystems,boot_services --quick` e confirme a aprovação das montagens.

## Conexões
- [[lynis-modo-pentest-nao-privilegiado-enumeracao-escalacao-privilegio]] — Veja também: CISOfy Lynis: Execução em Modo `--pentest` (Auditoria Não-Privilegiada e Avaliação de Vetores de Escalação Local).
- [[lynis-execucao-automatizada-cronjob-systemd-timer-monitoramento-deriva]] — Veja também: CISOfy Lynis: Auditoria Contínua Automatizada (`--cronjob`, `systemd timer`) e Detecção de Deriva de Hardening Index.
- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — Referência cruzada direta com lynis-arquitetura-auditoria-hardening-unix-linux-test-categories.
- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — Referência cruzada direta com usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
