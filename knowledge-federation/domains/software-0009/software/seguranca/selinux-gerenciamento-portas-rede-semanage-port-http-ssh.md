---
id: software.seguranca.tranche05.000494
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

# SELinux: Controle de Acesso a Portas TCP/UDP com `semanage port` (`http_port_t`, `ssh_port_t`, `mysqld_port_t`)

## Em uma frase
No SELinux, além de arquivos e processos, as **portas de rede TCP, UDP, SCTP e DCCP** também possuem rótulos de tipo (ex.: `http_port_t`, `ssh_port_t`, `postgresql_port_t`, `redis_port_t`), restringindo em quais portas cada domínio de processo pode fazer `name_bind` (escutar) ou `name_connect` (conectar).

## Por que importa
Se um atacante comprometer um processo confinado em `httpd_t`, ele não conseguirá abrir um *bind shell* na porta `4444` nem fazer o servidor web escutar na porta `8443` ou `9090` se essa porta não estiver rotulada como `http_port_t`.

## Como funciona
Para autorizar que um serviço legítimo escute em uma porta não-padrão (por exemplo, o OpenSSH na porta `2222` ou um proxy web na porta `8448`), o administrador consulta as portas atuais com `sudo semanage port -l` e adiciona a nova porta ao tipo correspondente via **`sudo semanage port -a -t ssh_port_t -p tcp 2222`** (ou `-m` *modify* caso a porta já esteja associada a outro tipo).

## Exemplo
```bash
# Verificar quais portas pertencem a http_port_t e autorizar a porta TCP 8448 para servidores HTTP
sudo semanage port -l | grep "^http_port_t"
sudo semanage port -a -t http_port_t -p tcp 8448
sudo semanage port -l -C
```

## Limites e trade-offs
Tentar iniciar o `sshd` em uma porta customizada no `/etc/ssh/sshd_config` **antes** de executar `sudo semanage port -a -t ssh_port_t -p tcp <PORTA>` fará o `sshd` falhar imediatamente no `bind()` com `Permission denied` (`AVC denied { name_bind }`).

## Como verificar
Execute `sudo semanage port -l -C` para listar todas as portas customizadas adicionadas localmente e confirme que o serviço faz bind sem erros AVC.

## Conexões
- [[selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon]] — Veja também: SELinux: Persistência de Rótulos de Arquivos com `semanage fcontext` e Aplicação com `restorecon -Rv` (Armadilha do `chcon`).
- [[selinux-isolamento-containers-mcs-svirt-lxc-net-t-container-file-t-z]] — Veja também: SELinux: Isolamento Multi-Tenant de Containers e Pods Kubernetes com **MCS** (`s0:cX,cY`), `container_t`, `container_file_t` e Montagens `:z` / `:Z`.
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.
- [[lynis-hardening-openssh-ssh-7408-autenticacao-pam-limites]] — Referência cruzada direta com lynis-hardening-openssh-ssh-7408-autenticacao-pam-limites.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
