---
id: software.seguranca.tranche13.001272
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/netblue30/firejail/master/README.md", "https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Anatomia dos Perfis **`.profile`** e Customizações **`.local`** no Firejail: `blacklist`, `whitelist`, `read-only`, `noexec` e Herança `include`

## Em uma frase
Como funcionam os mais de 1.000 perfis de segurança em **`/etc/firejail/*.profile`** e como personalizar as regras de um aplicativo (por exemplo, permitir que o Firefox acesse uma pasta específica `~/Downloads-Firefox`) sem que uma atualização de pacote do Linux sobrescreva a sua alteração?

## Por que importa
Todo perfil `.profile` do Firejail combina diretivas declarativas de isolamento de sistema de arquivos, rede e kernel: **(1) `blacklist <caminho>`** — oculta ou desmonta completamente o diretório/arquivo dentro do Mount Namespace da aplicação (de modo que para o aplicativo o caminho nem sequer existe!); **(2) `whitelist <caminho>`** — o modelo positivo mais seguro (*Allowlist*): cria um `/home/usuario` vazio em `tmpfs` (RAM) e monta lá dentro **exclusivamente** os caminhos explicitamente listados em `whitelist`!; **(3) `read-only <caminho>`** e **`noexec <caminho>`** (impede execução de binários/scripts em pastas graváveis como `/tmp` e `~/Downloads`); e **(4) `include <arquivo>`**!

## Como funciona
No topo de cada `/etc/firejail/<app>.profile`, existe a diretiva **`include <app>.local`**: assim, você coloca todas as suas customizações em **`~/.config/firejail/<app>.local`** (para o seu usuário) ou **`/etc/firejail/<app>.local`** (para todo o sistema) — preservando 100% da sua configuração através de atualizações!

## Exemplo
```text
# Exemplo de customizacao em ~/.config/firejail/firefox.local aplicando modelo positivo (whitelist) estrito na pasta home
whitelist ~/Downloads
read-only ~/.bashrc
noexec ~/Downloads
```

## Limites e trade-offs
Além dos perfis específicos de cada aplicativo (`firefox.profile`, `vlc.profile`, `evince.profile`), o Firejail inclui ao final de quase todos os perfis os arquivos base **`disable-common.inc`**, **`disable-passwdmgr.inc`**, **`disable-programs.inc`** e **`disable-devel.inc`** — que já bloqueiam automaticamente o acesso de aplicativos comuns a `~/.ssh`, `~/.gnupg`, `~/.keepassxc`, `~/.aws`, `~/.kube` e compiladores (`gcc`/`gdb`)!

## Como verificar
Para inspecionar o que um perfil fará antes ou durante a execução, rode **`firejail --debug <aplicativo>`** para ver cada montagem e filtro aplicado pelo namespace.

## Conexões
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Veja também: Arquitetura do **Firejail (`netblue30/firejail`)**: Isolamento de Aplicações Linux com **Kernel Namespaces, `seccomp-bpf`, Linux Capabilities e AppArmor**.
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Veja também: Isolamento Efêmero de Sistema de Arquivos no Firejail: **`--private`**, **`--private-dev`**, **`--private-etc`**, **`--private-bin`** e **`--private-tmp`**.
- [[firejail-construcao-perfis-customizados-build-auditoria-sandbox]] — Referência cruzada direta com firejail-construcao-perfis-customizados-build-auditoria-sandbox.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
