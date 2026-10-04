---
id: software.seguranca.tranche13.001271
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

# Arquitetura do **Firejail (`netblue30/firejail`)**: Isolamento de Aplicações Linux com **Kernel Namespaces, `seccomp-bpf`, Linux Capabilities e AppArmor**

## Em uma frase
Em uma estação de trabalho Linux de um engenheiro, desenvolvedor ou analista de segurança, qual é o risco de abrir um navegador Web (Firefox, Chrome), um leitor de PDF (`evince`, `okular`), um reprodutor de mídia (`vlc`), um cliente de e-mail (`thunderbird`) ou um cliente BitTorrent rodando diretamente como o seu usuário normal sem isolamento?

## Por que importa
Sem sandboxing, **qualquer aplicação que você executa com o seu UID possui acesso de leitura e escrita a 100% da sua pasta `/home/usuario/`** — incluindo seu cofre `.kdbx`, suas chaves `~/.ssh/`, seus tokens `~/.aws/` e `~/.kube/config`, seus cookies de outros navegadores e seu código-fonte! Se um exploit em um PDF malicioso ou pacote npm/PyPI comprometer um desses aplicativos, ele pode exfiltrar imediatamente todos os seus segredos pessoais!

## Como funciona
Escrito em C puro quase sem dependências externas, o **Firejail** é um programa SUID de sandboxing de segurança que utiliza recursos nativos do Kernel Linux — **Namespaces (Mount, PID, Network, IPC, UTS, User)**, filtros de chamadas de sistema **`seccomp-bpf`**, remoção de **Linux Capabilities**, **Control Groups (`cgroups`)** e integração com **AppArmor** — para confinar qualquer aplicação gráfica ou de servidor dentro de uma caixa de areia (*sandbox*) estrita com mais de **1.000 perfis `.profile` prontos de fábrica** em `/etc/firejail/`!

## Exemplo
```bash
# Executar um aplicativo (ex.: leitor de PDF ou navegador) confinado na sandbox do Firejail e listar todas as sandboxes ativas
firejail evince ./documento_externo_nao_confiavel.pdf
firejail --list
firejail --tree
```

## Limites e trade-offs
O comando **`firejail --tree`** exibe em tempo real a árvore hierárquica de processos de todas as sandboxes Firejail em execução no sistema, enquanto **`firejail --top`** mostra um monitor em tempo real do consumo de CPU e memória RAM de cada sandbox isolada!

## Como verificar
Você pode integrar o Firejail de forma transparente a todos os ícones da sua interface gráfica e ao terminal executando **`sudo firecfg`**, que cria links simbólicos em `/usr/local/bin/` para os aplicativos suportados.

## Conexões
- [[firejail-anatomia-perfis-profile-blacklist-whitelist-read-only-include]] — Veja também: Anatomia dos Perfis **`.profile`** e Customizações **`.local`** no Firejail: `blacklist`, `whitelist`, `read-only`, `noexec` e Herança `include`.
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Referência cruzada direta com firejail-isolamento-filesystem-private-private-dev-private-etc-bin.
- [[keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866]] — Referência cruzada direta com keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
