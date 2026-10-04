---
id: software.seguranca.tranche13.001279
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/netblue30/firejail/master/README.md", "https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Hardening Global do Próprio Firejail (**`/etc/firejail/firejail.config`** e **`firejail.users`**): Mitigando Riscos de Binários SUID no Linux

## Em uma frase
Como engenheiro de segurança sênior, você deve sempre avaliar os **trade-offs e a superfície de ataque das próprias ferramentas de defesa**: o Firejail funciona como um binário **SUID `root` (`/usr/bin/firejail` com bit `4755`)** para poder criar namespaces privilegiados, montar sistemas de arquivos e aplicar perfis AppArmor/interfaces de rede. Em servidores multiusuário onde há contas não confiáveis, qualquer binário SUID `root` pode ser um vetor se surgir uma vulnerabilidade local de escalação de privilégios!

## Por que importa
Como mitigar esse risco e aplicar **Hardening rigoroso ao próprio Firejail**?

## Como funciona
Primeiro, restrinja quem pode executar o binário SUID `/usr/bin/firejail`: use **`/etc/firejail/firejail.users`** (ou altere o grupo dono de `/usr/bin/firejail` para um grupo dedicado `firejail` com permissão **`4750` (`-rwsr-x--- root:firejail`)**), de modo que contas de serviço (`www-data`, `postgres`, `nobody`) jamais possam sequer invocar o binário SUID! Segundo, edite o arquivo de políticas globais **`/etc/firejail/firejail.config`** para desabilitar recursos desnecessários no nível do sistema: **`force-nonewprivs yes`**, **`disable-mnt yes`** (bloqueia acesso a `/mnt`, `/media` e pendrives em todas as sandboxes!), **`restricted-network yes`** (restringe `--net=...` apenas ao `root`), **`chroot no`** e **`userns no`** (se não precisar de `--noroot`)!

## Exemplo
```bash
# Auditar as permissoes do binario SUID /usr/bin/firejail e verificar diretivas de hardening ativas em /etc/firejail/firejail.config
ls -la /usr/bin/firejail
grep -E "^(force-nonewprivs|disable-mnt|restricted-network|chroot)" /etc/firejail/firejail.config
```

## Limites e trade-offs
Em servidores de produção *headless* (sem interface gráfica desktop), prefira confinar daemons e serviços diretamente através das diretivas nativas de sandboxing do **`systemd` (`ProtectSystem=strict`, `PrivateTmp=yes`, `PrivateDevices=yes`, `NoNewPrivileges=yes`, `SystemCallFilter=@system-service`)** ou containers rootless, reservando o Firejail para **estações de trabalho Linux Desktop** e laboratórios de análise!

## Como verificar
Essa combinação de **grupos Unix (`4750 root:firejail`)** + **`/etc/firejail/firejail.config`** entrega o melhor dos dois mundos: isolamento poderoso para aplicações desktop do usuário sem expor o binário SUID para contas de serviço sem privilégio.

## Conexões
- [[firejail-construcao-perfis-customizados-build-auditoria-sandbox]] — Veja também: Geração Automática de Perfis de Segurança sob Medida com **`firejail --build`** e Auditoria de Sandboxes em Execução (**`--join`**, **`--ls`**, **`--get`**).
- [[firejail-sandboxing-navegadores-leitores-pdf-analise-artefatos-dfir]] — Veja também: Sandboxing Prático de **Navegadores Web, Clientes de E-mail e Triagem de Artefatos Suspeitos (DFIR)** no Desktop Linux com Firejail.
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.
- [[firejail-filtragem-syscalls-seccomp-caps-drop-all-nonewprivs]] — Referência cruzada direta com firejail-filtragem-syscalls-seccomp-caps-drop-all-nonewprivs.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
