---
id: software.seguranca.tranche05.000492
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

# SELinux: Modos `Enforcing` vs `Permissive`, Domínios Permissivos por Processo (`semanage permissive`) e *Booleans* (`getsebool` / `setsebool -P`)

## Em uma frase
O SELinux opera globalmente em modo **`Enforcing`** (bloqueia e audita qualquer acesso não permitido pela política) ou **`Permissive`** (não bloqueia, mas registra os eventos `AVC: denied` que teriam ocorrido), além de suportar **domínios permissivos individuais** e **SELinux Booleans** para ajustar políticas em tempo de execução sem recompilar módulos.

## Por que importa
Quando apenas um serviço novo apresenta problemas de política SELinux, colocar o servidor inteiro em `setenforce 0` (*Permissive* global) expõe todos os outros daemons e containers da máquina; usar `sudo semanage permissive -a myapp_t` coloca **exclusivamente** o domínio `myapp_t` em modo permissivo mantendo o resto do host em `Enforcing`.

## Como funciona
Para cenários comuns de arquitetura (como permitir que o Nginx/Apache no domínio `httpd_t` faça conexões de rede reversas para um backend de aplicação), a política `targeted` já inclui chaves booleanas pré-compiladas listadas por `semanage boolean -l` e ativadas permanentemente com **`setsebool -P`** (que persiste no disco via `libsemanage`).

## Exemplo
```bash
# Listar booleans do servidor HTTP com suas descricoes e habilitar conexoes de proxy reverso permanentemente (-P)
sudo semanage boolean -l | grep httpd_can_network
sudo setsebool -P httpd_can_network_connect on
```

## Limites e trade-offs
Esquecer a flag **`-P`** em `setsebool httpd_can_network_connect on` altera apenas a chave em memória no kernel (`/sys/fs/selinux/booleans/`), fazendo com que o serviço pare de funcionar misteriosamente após o próximo reboot do servidor.

## Como verificar
Execute `sudo semanage boolean -l -C` (que lista apenas as customizações locais persistidas) e confirme que `httpd_can_network_connect` consta como `on`.

## Conexões
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Veja também: SELinux: Arquitetura de Controle de Acesso Obrigatório Baseada em Rótulos (`user:role:type:level`) e *Type Enforcement* (TE).
- [[selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon]] — Veja também: SELinux: Persistência de Rótulos de Arquivos com `semanage fcontext` e Aplicação com `restorecon -Rv` (Armadilha do `chcon`).
- [[selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert]] — Referência cruzada direta com selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
