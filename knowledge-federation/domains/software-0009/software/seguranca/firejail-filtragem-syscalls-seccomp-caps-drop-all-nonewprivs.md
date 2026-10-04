---
id: software.seguranca.tranche13.001274
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

# Redução de Superfície de Ataque do Kernel no Firejail: **`--seccomp`**, **`--caps.drop=all`**, **`--nonewprivs`** e **`--noroot` (User Namespace)**

## Em uma frase
Isolar os arquivos do disco não basta se um binário malicioso dentro da sandbox tentar explorar uma vulnerabilidade de escalação de privilégios no próprio Kernel Linux (via syscalls exóticas como `kexec_load`, `init_module`, `bpf`, `userfaultfd`, `io_uring`, `ptrace` ou `mount`) ou executar um binário SUID `root` do sistema!

## Por que importa
Para blindar o Kernel Linux contra processos confinados, o Firejail aplica **quatro barreiras de nível de kernel** que devem estar presentes em todo perfil de segurança: **(1) `nonewprivs` (`prctl(PR_SET_NO_NEW_PRIVS, 1)`)** — garante no nível do Kernel que o processo e todos os seus filhos jamais possam ganhar novos privilégios via binários SUID/SGID ou File Capabilities!; **(2) `caps.drop all`** — zera todas as **Linux Capabilities** (`CAP_SYS_ADMIN`, `CAP_NET_RAW`, `CAP_SYS_PTRACE`, etc.) no conjunto de capabilities da thread; **(3) `noroot`** — cria um **User Namespace** onde a conta `root` (`UID 0`) não é mapeada para o root real do sistema; e **(4) `seccomp` (`seccomp-bpf`)**!

## Como funciona
Com **`seccomp`** (e `seccomp.block-secondary` para bloquear syscalls de arquiteturas 32-bit em sistemas 64-bit!), o filtro BPF no kernel intercepta qualquer chamada de sistema proibida e mata imediatamente o processo infrator com `SIGSYS` (ou retorna `EPERM` conforme `seccomp-error-action`)!

## Exemplo
```bash
# Auditar em tempo real quais filtros seccomp, capabilities e restricoes NoNewPrivs estao aplicados a uma sandbox Firejail ativa
firejail --caps.print=<PID_OU_NOME_SANDBOX>
firejail --seccomp.print=<PID_OU_NOME_SANDBOX>
```

## Limites e trade-offs
Além do conjunto padrão de syscalls perigosas bloqueadas por `--seccomp`, você pode usar **`--seccomp.drop=syscall1,syscall2`** (Blacklist adicional), **`--seccomp.keep=syscall1,syscall2`** (Allowlist estrita de syscalls!) e **`memory-deny-write-execute` (`W^X`)** — que bloqueia chamadas `mmap`/`mprotect` com `PROT_WRITE | PROT_EXEC` simultâneos para impedir injeção de shellcode JIT na memória!

## Como verificar
No arquivo global `/etc/firejail/firejail.config`, a diretiva **`force-nonewprivs yes`** pode ser ativada para forçar `PR_SET_NO_NEW_PRIVS` obrigatoriamente em 100% das sandboxes do sistema.

## Conexões
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Veja também: Isolamento Efêmero de Sistema de Arquivos no Firejail: **`--private`**, **`--private-dev`**, **`--private-etc`**, **`--private-bin`** e **`--private-tmp`**.
- [[firejail-isolamento-rede-net-none-veth-netfilter-dns-sandboxing]] — Veja também: Isolamento de Rede no Firejail: **`--net=none`**, Interfaces Virtuais **`veth` (`--net=eth0` / `br0`)**, Firewall Interno **`--netfilter`** e **`--protocol`**.
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.
- [[firejail-hardening-global-firejail-config-suid-firejail-users-grupos]] — Referência cruzada direta com firejail-hardening-global-firejail-config-suid-firejail-users-grupos.
- [[keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866]] — Referência cruzada direta com keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
