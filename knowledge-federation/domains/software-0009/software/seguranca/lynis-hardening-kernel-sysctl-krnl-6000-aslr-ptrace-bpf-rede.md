---
id: software.seguranca.tranche05.000454
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

# CISOfy Lynis: Remediação de `KRNL-6000` — Hardening de Parâmetros `sysctl` de Kernel, Memória e Pilha de Rede

## Em uma frase
O teste **`KRNL-6000`** do Lynis audita dezenas de parâmetros do kernel Linux expostos em `/proc/sys/` (`sysctl`), cobrindo proteção de memória/ponteiros, restrição de depuração `ptrace`, endurecimento de eBPF e blindagem da pilha TCP/IPv4/IPv6.

## Por que importa
Parâmetros padrão de distribuições Linux priorizam compatibilidade e depuração; endurecer `sysctl` em `/etc/sysctl.d/99-hardening.conf` impede que usuários locais não-privilegiados leiam endereços de memória do kernel (`kptr_restrict`), anexem `gdb`/`strace` em outros processos do mesmo UID (`yama.ptrace_scope`) ou sofram spoofing de pacotes ICMP/ARP.

## Como funciona
Os principais controles verificados pelo `KRNL-6000` incluem `kernel.randomize_va_space = 2` (ASLR total), `kernel.kptr_restrict = 2`, `kernel.dmesg_restrict = 1`, `kernel.yama.ptrace_scope = 1` (ou `2`/`3` em produção), `kernel.unprivileged_bpf_disabled = 1`, `net.core.bpf_jit_harden = 2`, `fs.suid_dumpable = 0`, `fs.protected_hardlinks = 1`, `fs.protected_symlinks = 1`, `net.ipv4.conf.all.rp_filter = 1`, `net.ipv4.conf.all.accept_redirects = 0` e `net.ipv4.tcp_syncookies = 1`.

## Exemplo
```ini
# /etc/sysctl.d/99-lynis-hardening.conf
kernel.randomize_va_space = 2
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
kernel.yama.ptrace_scope = 2
kernel.unprivileged_bpf_disabled = 1
net.core.bpf_jit_harden = 2
fs.suid_dumpable = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.log_martians = 1
```

## Limites e trade-offs
Em nós Kubernetes que atuam como roteadores de CNI (Cilium/Calico), definir `net.ipv4.ip_forward = 0` ou `rp_filter = 1` estrito nas interfaces de overlay quebrará o roteamento de pods; adapte o perfil `custom.prf` para nós de cluster.

## Como verificar
Aplique `sudo sysctl --system` e reexecute `sudo lynis audit system --tests KRNL-6000 --quick`, confirmando que todos os itens de `KRNL-6000` passam com status `OK`.

## Conexões
- [[lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh]] — Veja também: CISOfy Lynis: Customização de Políticas com Perfis `custom.prf` (`skip-test`, `config-data` e `--profile`).
- [[lynis-hardening-openssh-ssh-7408-autenticacao-pam-limites]] — Veja também: CISOfy Lynis: Remediação de `SSH-7408` e `AUTH-*` — Hardening de OpenSSH (`sshd_config`), PAM e Contas Locais.
- [[lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details]] — Referência cruzada direta com lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details.
- [[apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal]] — Referência cruzada direta com apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
