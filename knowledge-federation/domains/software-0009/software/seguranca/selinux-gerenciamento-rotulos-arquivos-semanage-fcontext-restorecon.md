---
id: software.seguranca.tranche05.000493
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

# SELinux: Persistência de Rótulos de Arquivos com `semanage fcontext` e Aplicação com `restorecon -Rv` (Armadilha do `chcon`)

## Em uma frase
Quando uma aplicação utiliza um diretório fora do caminho padrão da distribuição (por exemplo, servindo arquivos web a partir de `/srv/webapp/public` em vez de `/var/www/html`), o diretório recebe o rótulo genérico `var_t` ou `default_t` e o domínio `httpd_t` tem o acesso negado pelo SELinux.

## Por que importa
Alterar o rótulo manualmente apenas com `chcon -R -t httpd_sys_content_t /srv/webapp/public` modifica o atributo estendido `xattr` no disco, mas **não registra a regra no banco de dados de política do SELinux**; na próxima execução de `restorecon` ou atualização de pacote, o rótulo será revertido para `var_t` e o serviço cairá.

## Como funciona
O procedimento correto em duas etapas consiste em: **(1)** declarar a regra de mapeamento de expressão regular no banco do `libsemanage` com **`sudo semanage fcontext -a -t httpd_sys_content_t '/srv/webapp/public(/.*)?'`** e **(2)** aplicar os rótulos do banco de dados nos inodes reais com **`sudo restorecon -Rv /srv/webapp/public`**.

## Exemplo
```bash
# Cadastrar permanentemente o rotulo somente-leitura para o diretorio web customizado e aplica-lo no filesystem
sudo semanage fcontext -a -t httpd_sys_content_t '/srv/webapp/public(/.*)?'
sudo restorecon -Rv /srv/webapp/public
matchpathcon -V /srv/webapp/public/index.html
```

## Limites e trade-offs
Cuidado ao mover arquivos (`mv`) de `/home/admin/` ou `/tmp/` para `/var/www/html/`: o comando `mv` no mesmo filesystem preserva o inode original e, portanto, carrega consigo o rótulo antigo (`user_home_t` ou `user_tmp_t`), causando erro `403 Forbidden`; use `cp` (que herda o rótulo do diretório de destino) ou `mv -Z` / `restorecon`.

## Como verificar
Execute `matchpathcon -V /srv/webapp/public/index.html` e confirme a mensagem `verified` (o rótulo no inode coincide com a política persistida).

## Conexões
- [[selinux-modos-enforcing-permissive-booleans-getsebool-setsebool]] — Veja também: SELinux: Modos `Enforcing` vs `Permissive`, Domínios Permissivos por Processo (`semanage permissive`) e *Booleans* (`getsebool` / `setsebool -P`).
- [[selinux-gerenciamento-portas-rede-semanage-port-http-ssh]] — Veja também: SELinux: Controle de Acesso a Portas TCP/UDP com `semanage port` (`http_port_t`, `ssh_port_t`, `mysqld_port_t`).
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.
- [[selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert]] — Referência cruzada direta com selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
