---
id: software.seguranca.tranche13.001276
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

# Protegendo o Servidor Gráfico e o Barramento IPC no Firejail: Isolamento de **X11 (`--x11=xephyr`/`xpra`)**, **Wayland** e Filtragem de **D-Bus (`--dbus-user`)**

## Em uma frase
Existe uma vulnerabilidade arquitetural histórica no protocolo gráfico **X11 (Xorg)** do Linux que muitos usuários desconhecem: no X11 clássico, **todas as janelas gráficas conectadas ao mesmo servidor X11 compartilham o mesmo espaço de eventos** — o que significa que qualquer programa gráfico rodando no X11 pode usar APIs como `XQueryKeymap` / `XRecord` para funcionar como um **Keylogger silencioso de todas as outras janelas** ou capturar screenshots da sua tela inteira!

## Por que importa
Como o Firejail resolve o problema de isolamento do X11 e do barramento **D-Bus**? Em duas frentes: **(1) Isolamento X11 (`--x11` / `--x11=xephyr` / `--x11=xpra` / `--x11=xvfb` / `--x11=none`)** — para aplicações de linha de comando ou servidores, `x11 none` bloqueia o socket X11; e para aplicações gráficas não confiáveis em Xorg, `--x11=xephyr` ou `--x11=xpra` inicia um **servidor X11 aninhado dedicado exclusivamente para aquela sandbox**, impedindo que o aplicativo espie o teclado ou a tela das suas outras janelas! (Em sessões **Wayland** nativas, o protocolo Wayland já isola as janelas por design!); e **(2) Filtragem de D-Bus (`dbus-user filter` / `dbus-user none` e `dbus-system none`)**!

## Como funciona
Por que filtrar o **D-Bus (`dbus-user none` ou `dbus-user filter` via `xdg-dbus-proxy`)** é igualmente crítico? Porque sem filtro D-Bus, um processo dentro da sandbox poderia enviar uma mensagem RPC pelo socket D-Bus da sessão pedindo para o `systemd --user`, para o `org.freedesktop.secrets` ou para o gerenciador de arquivos executar uma ação fora da sandbox!

## Exemplo
```bash
# Executar um aplicativo grafico nao confiavel isolando o barramento D-Bus de usuario/sistema e confinando o X11 em um servidor Xephyr dedicado
firejail --private --dbus-user=none --dbus-system=none --x11=xephyr --xephyr-screen=1280x800 galculator
```

## Limites e trade-offs
Nos perfis modernos do Firejail, sempre que um aplicativo não precisa falar com serviços D-Bus, adicione **`dbus-user none`** e **`dbus-system none`**; e quando ele precisa de apenas uma interface específica (como notificações desktop), use **`dbus-user filter`** com **`dbus-user.talk org.freedesktop.Notifications`**!

## Como verificar
Isso impede ataques de *Sandbox Escape via D-Bus IPC* mantendo a integração visual necessária com o desktop.

## Conexões
- [[firejail-isolamento-rede-net-none-veth-netfilter-dns-sandboxing]] — Veja também: Isolamento de Rede no Firejail: **`--net=none`**, Interfaces Virtuais **`veth` (`--net=eth0` / `br0`)**, Firewall Interno **`--netfilter`** e **`--protocol`**.
- [[firejail-integracao-apparmor-cgroups-rlimits-controle-recursos]] — Veja também: Defesa em Profundidade no Firejail: Integração com **AppArmor (`--apparmor`)**, Limites de Recursos (**`rlimits`**) e **Control Groups (`--cgroup`)**.
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.
- [[keepassxc-freedesktop-secret-service-substituicao-gnome-keyring-linux]] — Referência cruzada direta com keepassxc-freedesktop-secret-service-substituicao-gnome-keyring-linux.
- [[keepassxc-autotype-sequencias-customizadas-protecao-window-title]] — Referência cruzada direta com keepassxc-autotype-sequencias-customizadas-protecao-window-title.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
