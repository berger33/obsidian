---
id: software.seguranca.tranche05.000496
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

# SELinux: Diagnóstico Forense de Negativas `AVC` com `ausearch -m AVC`, `audit2why` e `sealert`

## Em uma frase
Toda negação do Access Vector Cache (AVC) do SELinux no kernel gera registros `type=AVC`, `type=SYSCALL`, `type=CWD` e `type=PATH` no `/var/log/audit/audit.log`, contendo o contexto de origem (`scontext=`), o contexto do alvo (`tcontext=`), a classe do objeto (`tclass=file|tcp_socket|dir`) e a permissão negada (`{ read write open }`).

## Por que importa
Antes de criar qualquer módulo de política customizado, **`audit2why`** analisa o registro AVC contra a política carregada e explica a causa raiz exata: se falta apenas ativar um *Boolean* existente, se o arquivo no disco está com o rótulo errado (*mislabeled file*) ou se realmente falta uma regra de *Type Enforcement*.

## Como funciona
O fluxo padrão de diagnóstico executa `sudo ausearch -m AVC,USER_AVC,SELINUX_ERR -ts recent` e canaliza a saída para `audit2why` (ou `sealert -a /var/log/audit/audit.log` do `setroubleshoot-server` em ambientes de homologação), resolvendo mais de 90% dos casos apenas com `restorecon` ou `setsebool -P`.

## Exemplo
```bash
# Diagnosticar a causa raiz de todas as negacoes AVC recentes explicando se ha boolean ou erro de rotulo
sudo ausearch -m AVC,USER_AVC -ts recent | audit2why
```

## Limites e trade-offs
Certifique-se de que o daemon `auditd` esteja rodando; se o `auditd` estiver parado, as mensagens AVC caem no buffer do kernel (`dmesg` / `journalctl -t setroubleshoot`) sem os registros auxiliares `SYSCALL` e `PATH` completos.

## Como verificar
Execute o comando `ausearch -m AVC -ts recent | audit2why` após simular um erro de permissão e valide a recomendação retornada.

## Conexões
- [[selinux-isolamento-containers-mcs-svirt-lxc-net-t-container-file-t-z]] — Veja também: SELinux: Isolamento Multi-Tenant de Containers e Pods Kubernetes com **MCS** (`s0:cX,cY`), `container_t`, `container_file_t` e Montagens `:z` / `:Z`.
- [[selinux-compilacao-modulos-customizados-te-cil-udica-semodule]] — Veja também: SELinux: Desenvolvimento e Gerenciamento de Módulos de Política (`.te` / `.cil`), `checkmodule`, `semodule_package`, `secilc` e `semodule`.
- [[selinux-modos-enforcing-permissive-booleans-getsebool-setsebool]] — Referência cruzada direta com selinux-modos-enforcing-permissive-booleans-getsebool-setsebool.
- [[selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon]] — Referência cruzada direta com selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon.
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Referência cruzada direta com auditd-investigacao-forense-ausearch-aureport-auid-correlacao.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
