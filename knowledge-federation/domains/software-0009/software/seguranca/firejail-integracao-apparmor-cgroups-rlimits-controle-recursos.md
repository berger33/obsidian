---
id: software.seguranca.tranche13.001277
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

# Defesa em Profundidade no Firejail: Integração com **AppArmor (`--apparmor`)**, Limites de Recursos (**`rlimits`**) e **Control Groups (`--cgroup`)**

## Em uma frase
Como combinar o isolamento baseado em Namespaces e `seccomp-bpf` do Firejail com o Controle de Acesso Obrigatório (**MAC — *Mandatory Access Control***) do Kernel Linux (**AppArmor**) e impedir que uma aplicação confinada execute uma **Fork Bomb** ou consuma 100% da memória RAM da estação?

## Por que importa
Combinar sandboxing de namespaces com LSMs e limites estritos de recursos do kernel garante contenção tanto contra tentativas de escape quanto contra ataques de exaustão local (DoS).

## Como funciona
O Firejail integra nativamente três mecanismos complementares: **(1) Perfil AppArmor (`--apparmor` / diretiva `apparmor` no `.profile`)** — o pacote do Firejail instala o perfil MAC `/etc/apparmor.d/firejail-default`; ao carregar esse perfil (`sudo aa-enforce firejail-default`), o Kernel Linux aplica uma segunda camada independente de controle de acesso obrigatório sobre os processos da sandbox!; **(2) Resource Limits POSIX (`--rlimit-nproc`, `--rlimit-as`, `--rlimit-fsize`, `--rlimit-nofile`)** — limita diretamente no kernel o número máximo de processos/threads (`rlimit-nproc`, neutralizando *fork bombs*!), tamanho máximo de arquivos criados e descritores abertos; e **(3) Limites de CPU e Afinidade (`--cpu`, `--nice`, `--oom` e `--cgroup`)**!

## Exemplo
```bash
# Verificar o status do perfil AppArmor firejail-default e iniciar uma sandbox com limite estrito de processos (rlimit-nproc) e nucleos de CPU
sudo aa-status | grep -i firejail || true
firejail --apparmor --rlimit-nproc=64 --cpu=0,1 --oom=500 ./processador_arquivos_externos
```

## Limites e trade-offs
Repare na flag **`--oom=500`** (*Out-Of-Memory killer score adjustment*, de `-1000` a `1000`): ao atribuir uma pontuação alta de OOM (`300` a `800`) para sandboxes de navegadores ou processadores de mídia pesados, se a estação de trabalho ficar sem memória RAM, o **OOM Killer do Kernel Linux encerrará primeiro o processo dentro da sandbox** em vez de matar seu ambiente gráfico principal ou seu banco de dados local!

## Como verificar
Use **`firejail --rlimits.print=<PID_OU_NOME>`** para auditar todos os limites POSIX ativos em uma sandbox em execução.

## Conexões
- [[firejail-isolamento-grafico-x11-xephyr-xvfb-xpra-wayland-dbus]] — Veja também: Protegendo o Servidor Gráfico e o Barramento IPC no Firejail: Isolamento de **X11 (`--x11=xephyr`/`xpra`)**, **Wayland** e Filtragem de **D-Bus (`--dbus-user`)**.
- [[firejail-construcao-perfis-customizados-build-auditoria-sandbox]] — Veja também: Geração Automática de Perfis de Segurança sob Medida com **`firejail --build`** e Auditoria de Sandboxes em Execução (**`--join`**, **`--ls`**, **`--get`**).
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.
- [[firejail-filtragem-syscalls-seccomp-caps-drop-all-nonewprivs]] — Referência cruzada direta com firejail-filtragem-syscalls-seccomp-caps-drop-all-nonewprivs.
- [[firejail-hardening-global-firejail-config-suid-firejail-users-grupos]] — Referência cruzada direta com firejail-hardening-global-firejail-config-suid-firejail-users-grupos.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
