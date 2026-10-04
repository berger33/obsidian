---
id: software.seguranca.tranche05.000499
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

# SELinux: Auditoria e Consulta Formal da Política Binária com `setools` (`sesearch`, `seinfo` e Desativação Temporária de `dontaudit`)

## Em uma frase
A suíte **`setools-console`** (`sesearch` e `seinfo`) permite interrogar matematicamente a política binária ativa do SELinux no kernel para provar quais domínios podem acessar um recurso sensível (como `shadow_t` ou `container_file_t`) e investigar bloqueios silenciosos causados por regras **`dontaudit`**.

## Por que importa
A política padrão do SELinux inclui milhares de regras `dontaudit` para evitar que sondagens inofensivas de bibliotecas poluam o `/var/log/audit/audit.log`; porém, durante a depuração de uma falha misteriosa onde nenhum `AVC` aparece no log, essas regras `dontaudit` precisam ser temporariamente desabilitadas.

## Como funciona
Com **`sudo semodule -DB`** (*Disable Dontaudit and Build*), o SELinux recompila a política expondo todos os bloqueios ocultos no `audit.log`; encerrado o diagnóstico, **`sudo semodule -B`** restaura as regras `dontaudit` normais. Já **`sesearch -A -s httpd_t -t httpd_sys_content_t -c file`** lista todas as regras `allow` (incluindo as condicionais governadas por *Booleans*) entre a origem e o destino.

## Exemplo
```bash
# Consultar na politica binaria ativa quais dominios possuem permissao de escrita no tipo shadow_t
sesearch -A -t shadow_t -c file -p write

# Verificar regras condicionais de httpd_t para conexoes TCP
sesearch -A -s httpd_t -c tcp_socket -p name_connect
```

## Limites e trade-offs
Nunca esqueça a política com `dontaudit` desabilitado (`semodule -DB`) em produção após terminar um diagnóstico, pois o volume de eventos `AVC` benignos aumentará drasticamente e encherá `/var/log/audit`.

## Como verificar
Execute `seinfo` para inspecionar as estatísticas da política carregada (classes, tipos, atributos, booleans e regras `allow`) e valide consultas `sesearch`.

## Conexões
- [[selinux-confinamento-usuarios-semanage-login-user-staff-u-sysadm-u]] — Veja também: SELinux: Confinamento RBAC de Usuários Humanos e Administradores SSH (`semanage login`, `user_u`, `staff_u`, `sysadm_u` e `sudo -r`).
- [[selinux-exportacao-importacao-customizacoes-semanage-export-ansible]] — Veja também: SELinux: Backup, Replicação Atômica (`semanage export` / `semanage import`) e Automação Idempotente de Políticas em Frota.
- [[selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert]] — Referência cruzada direta com selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert.
- [[selinux-compilacao-modulos-customizados-te-cil-udica-semodule]] — Referência cruzada direta com selinux-compilacao-modulos-customizados-te-cil-udica-semodule.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
