---
id: software.seguranca.tranche05.000497
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

# SELinux: Desenvolvimento e Gerenciamento de Módulos de Política (`.te` / `.cil`), `checkmodule`, `semodule_package`, `secilc` e `semodule`

## Em uma frase
Quando uma aplicação proprietária ou container (`udica`) requer regras de *Type Enforcement* que não são cobertas por rótulos (`semanage fcontext`), portas (`semanage port`) ou *Booleans*, o conjunto de ferramentas do `SELinuxProject/selinux` permite compilar e instalar módulos de política modulares (`.pp` ou **CIL** — *Common Intermediate Language* `.cil`).

## Por que importa
Embora `audit2allow -M meu_modulo` gere rapidamente um arquivo `.te` a partir de logs AVC, o módulo gerado deve sempre ser revisado linha por linha antes de ser instalado com `semodule -i` para garantir que ele não conceda acesso excessivo.

## Como funciona
O pipeline clássico de compilação converte o fonte `.te` em módulo binário `.mod` via **`checkmodule -M -m -o myapp.mod myapp.te`**, empacota em `.pp` via **`semodule_package -o myapp.pp -m myapp.mod`** (e opcionalmente `.fc` de file contexts) e instala na loja de políticas ativa via **`sudo semodule -i myapp.pp`** (com prioridade padrão `400`, acima dos módulos da distribuição em `100`).

## Exemplo
```bash
# Gerar esqueleto para revisao humana, compilar manualmente e listar modulos locais instalados em prioridade 400
sudo ausearch -m AVC -ts recent | audit2allow -m myapp_custom > myapp_custom.te
checkmodule -M -m -o myapp_custom.mod myapp_custom.te
semodule_package -o myapp_custom.pp -m myapp_custom.mod
sudo semodule -i myapp_custom.pp
sudo semodule -lfull | grep "^400"
```

## Limites e trade-offs
Nunca execute `ausearch -m AVC | audit2allow -M hack && semodule -i hack.pp` sem ler o arquivo `.te` gerado! Se um log AVC continha uma tentativa bloqueada de ler `shadow_t` ou `etc_t` amplo, o `audit2allow` escreverá `allow myapp_t shadow_t:file read;` e abrirá uma falha crítica na política.

## Como verificar
Inspecione `sudo semodule -lfull | grep "^400"` e revise o código-fonte `.te`/`.cil` de todos os módulos customizados de prioridade `400`.

## Conexões
- [[selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert]] — Veja também: SELinux: Diagnóstico Forense de Negativas `AVC` com `ausearch -m AVC`, `audit2why` e `sealert`.
- [[selinux-confinamento-usuarios-semanage-login-user-staff-u-sysadm-u]] — Veja também: SELinux: Confinamento RBAC de Usuários Humanos e Administradores SSH (`semanage login`, `user_u`, `staff_u`, `sysadm_u` e `sudo -r`).
- [[selinux-analise-politicas-setools-sesearch-seinfo-auditoria]] — Referência cruzada direta com selinux-analise-politicas-setools-sesearch-seinfo-auditoria.
- [[selinux-isolamento-containers-mcs-svirt-lxc-net-t-container-file-t-z]] — Referência cruzada direta com selinux-isolamento-containers-mcs-svirt-lxc-net-t-container-file-t-z.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
