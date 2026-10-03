---
id: software.seguranca.tranche05.000483
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
fontes: ["https://gitlab.com/apparmor/apparmor/-/raw/master/README.md", "https://gitlab.com/apparmor/apparmor/-/wikis/home", "https://gitlab.com/apparmor/apparmor/-/wikis/Documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# AppArmor: Sintaxe de Regras de Perfil — Permissões de Arquivos (`r`, `w`, `a`, `k`, `l`, `m`), `capability`, `network`, `mount`, `ptrace` e `signal`

## Em uma frase
Um perfil AppArmor funciona sob o modelo **default-deny** (*tudo o que não é explicitamente permitido dentro do bloco `{ ... }` é negado*): ele governa acesso a arquivos (com globs `*`, `**`, `?`, `{a,b}`), capabilities POSIX (`capability net_bind_service,`), sockets de rede (`network inet tcp,`), montagens (`mount`), `ptrace`, `signal` e IPC D-Bus/Unix.

## Por que importa
Permite restringir um microserviço para que ele possa apenas abrir sockets TCP IPv4/IPv6 (`network inet stream,`), usar `capability setgid`/`setuid`, ler seus próprios certificados TLS (`owner /etc/myapp/tls/** r,`) e gravar apenas em `/var/log/myapp/*.log` (`w` ou `a` *append-only*).

## Como funciona
Nas regras de arquivo, **`r`** permite leitura, **`w`** escrita completa, **`a`** apenas anexação ao final do arquivo (*append* — impede que um atacante apague linhas anteriores de um log!), **`k`** trava de arquivo (`flock`), **`l`** criação de links e **`m`** mapeamento de memória executável (`mmap` com `PROT_EXEC`). O prefixo **`owner`** exige que o UID do processo coincida com o proprietário do arquivo.

## Exemplo
```nginx
#include <tunables/global>

profile myapp /usr/local/bin/myapp flags=(attach_disconnected) {
  #include <abstractions/base>
  #include <abstractions/nameservice>

  capability net_bind_service,
  network inet stream,
  network inet6 stream,

  /usr/local/bin/myapp mr,
  owner /etc/myapp/config.yaml r,
  owner /var/log/myapp/** a,
  deny /etc/shadow r,
}
```

## Limites e trade-offs
Nunca conceda `/ rw,` ou `capability sys_admin,` / `capability sys_module,` em um perfil de aplicação, pois `sys_admin` e `sys_module` permitem escapar do confinamento montando sistemas de arquivos ou injetando código no kernel.

## Como verificar
Valide a sintaxe e compile o perfil sem carregá-lo usando `apparmor_parser -p /etc/apparmor.d/usr.local.bin.myapp > /dev/null`.

## Conexões
- [[apparmor-modos-operacao-enforce-complain-audit-deny-aa-enforce]] — Veja também: AppArmor: Modos de Operação de Perfis (`enforce`, `complain`, `unconfined`, `kill`) e Comandos `aa-enforce`, `aa-complain` e `aa-disable`.
- [[apparmor-transicoes-execucao-ix-px-cx-ux-scrubbing-ambiente]] — Veja também: AppArmor: Modos de Transição de Execução (`ix`, `px`/`Px`, `cx`/`Cx`, `ux`/`Ux`) e Limpeza de Ambiente (*Environment Scrubbing*).
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Referência cruzada direta com apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles.
- [[apparmor-abstracoes-tunables-local-overrides-manutencao-perfis]] — Referência cruzada direta com apparmor-abstracoes-tunables-local-overrides-manutencao-perfis.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
