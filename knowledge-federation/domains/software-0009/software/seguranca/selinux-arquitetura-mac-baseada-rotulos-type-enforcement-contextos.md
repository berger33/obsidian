---
id: software.seguranca.tranche05.000491
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
fontes: ["https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md", "https://github.com/SELinuxProject/selinux/wiki", "https://github.com/SELinuxProject/selinux/wiki/Tools"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SELinux: Arquitetura de Controle de Acesso Obrigatório Baseada em Rótulos (`user:role:type:level`) e *Type Enforcement* (TE)

## Em uma frase
**Security-Enhanced Linux (SELinux)** (`SELinuxProject/selinux`, GPLv2) é a implementação de *Mandatory Access Control* (MAC) baseada na arquitetura Flask integrada ao kernel Linux (padrão em RHEL, Fedora, CentOS Stream, Rocky, AlmaLinux, CoreOS e Android) que governa todas as interações entre sujeitos (processos) e objetos (arquivos, portas, sockets, memória) através de rótulos de segurança.

## Por que importa
Diferente de sistemas baseados em caminho, o SELinux grava o rótulo de segurança diretamente nos atributos estendidos do *inode* do sistema de arquivos (`security.selinux` em `xattr`): mesmo que um arquivo seja renomeado ou referenciado por *hard link*, o seu rótulo permanece anexado ao objeto físico.

## Como funciona
Cada contexto SELinux possui quatro campos separados por dois-pontos: **`user:role:type:level`** (ex.: `system_u:object_r:httpd_sys_content_t:s0`). Na política padrão **`targeted`**, o motor principal é o **Type Enforcement (TE)** (o 3º campo, terminado em `_t`): uma regra na política binária do kernel (`allow httpd_t httpd_sys_content_t:file { open read getattr };`) define exatamente quais operações o domínio do processo (`httpd_t`) pode realizar sobre objetos daquele tipo.

## Exemplo
```bash
# Inspecionar o status completo do SELinux, a versao da politica do kernel (>= 30) e os contextos de processos/arquivos
sestatus -v
ps -eZ | head -n 10
ls -laZ /var/www/html
```

## Limites e trade-offs
Nunca desative o SELinux em produção (`SELINUX=disabled` em `/etc/selinux/config`), pois além de remover toda a camada de isolamento MAC de processos e containers, reativá-lo posteriormente exige um *relabel* completo de todo o sistema de arquivos no boot.

## Como verificar
Execute `getenforce` e confirme que a saída retorna **`Enforcing`** com `Loaded policy name: targeted` em `sestatus`.

## Conexões
- [[selinux-modos-enforcing-permissive-booleans-getsebool-setsebool]] — Veja também: SELinux: Modos `Enforcing` vs `Permissive`, Domínios Permissivos por Processo (`semanage permissive`) e *Booleans* (`getsebool` / `setsebool -P`).
- [[selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon]] — Referência cruzada direta com selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon.
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Referência cruzada direta com apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
