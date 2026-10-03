---
id: software.seguranca.tranche05.000455
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

# CISOfy Lynis: Remediação de `SSH-7408` e `AUTH-*` — Hardening de OpenSSH (`sshd_config`), PAM e Contas Locais

## Em uma frase
A categoria de testes **`SSH-7408`** e **`AUTH-*`** do Lynis audita a configuração do daemon OpenSSH (`/etc/ssh/sshd_config`), políticas de complexidade e expiração de senhas (`/etc/login.defs` e `pam_pwquality`), `umask` padrão (`027`) e limites de recursos (`/etc/security/limits.conf`).

## Por que importa
O serviço SSH é a principal porta de administração remota de servidores Linux; configurações permissivas padrão permitem ataques de força bruta, encaminhamento de portas TCP não autorizado ou persistência via `X11Forwarding` e `PermitUserEnvironment`.

## Como funciona
Para satisfazer integralmente o teste `SSH-7408`, configure um drop-in `/etc/ssh/sshd_config.d/10-lynis-hardening.conf` com `PermitRootLogin no`, `PasswordAuthentication no`, `MaxAuthTries 3`, `MaxSessions 2`, `ClientAliveCountMax 2`, `AllowTcpForwarding no`, `AllowAgentForwarding no`, `X11Forwarding no`, `LogLevel VERBOSE` e `TCPKeepAlive no`, validando a sintaxe com `sshd -t` antes do reload.

## Exemplo
```bash
# Validar a configuração efetiva do sshd e executar apenas o grupo de testes SSH do Lynis
sudo sshd -t
sudo lynis audit system --tests-from-group ssh --quick
sudo lynis show details SSH-7408
```

## Limites e trade-offs
Antes de aplicar `PasswordAuthentication no`, `AllowTcpForwarding no` ou alterar a porta `Port` do SSH, garanta que sua chave pública Ed25519/ECDSA e uma sessão de terminal reserva estão ativas para evitar bloqueio administrativo (*lockout*).

## Como verificar
Execute `sudo lynis show details SSH-7408` e confirme que todos os parâmetros avaliados aparecem marcados como `[ OK ]`.

## Conexões
- [[lynis-hardening-kernel-sysctl-krnl-6000-aslr-ptrace-bpf-rede]] — Veja também: CISOfy Lynis: Remediação de `KRNL-6000` — Hardening de Parâmetros `sysctl` de Kernel, Memória e Pilha de Rede.
- [[lynis-auditoria-dockerfiles-lynis-audit-dockerfile-containers]] — Veja também: CISOfy Lynis: Auditoria Estática de Imagens de Container com `lynis audit dockerfile`.
- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — Referência cruzada direta com lynis-arquitetura-auditoria-hardening-unix-linux-test-categories.
- [[lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details]] — Referência cruzada direta com lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details.
- [[auditd-regras-monitoramento-arquivos-identidade-sudoers-ssh-w]] — Referência cruzada direta com auditd-regras-monitoramento-arquivos-identidade-sudoers-ssh-w.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
