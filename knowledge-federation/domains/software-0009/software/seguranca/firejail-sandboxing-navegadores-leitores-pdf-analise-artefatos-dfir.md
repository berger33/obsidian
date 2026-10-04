---
id: software.seguranca.tranche13.001280
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

# Sandboxing Prático de **Navegadores Web, Clientes de E-mail e Triagem de Artefatos Suspeitos (DFIR)** no Desktop Linux com Firejail

## Em uma frase
Como organizar na prática o seu desktop Linux diário com o Firejail para separar diferentes níveis de confiança (por exemplo: um navegador para o banco e produção corporativa, um segundo navegador para pesquisa geral na web e uma sandbox ultra-restrita para abrir PDFs/arquivos recebidos de terceiros)?

## Por que importa
A compartimentalização de sessões impede que o comprometimento de uma aba de pesquisa web ou documento externo alcance credenciais de produção.

## Como funciona
Com a flag **`--private=<diretorio>`**, você pode criar **múltiplos ambientes persistentes mas 100% isolados entre si** para o mesmo navegador: **(1) Perfil Corporativo/Produção**: `firejail --private=~/Perfis-Isolados/navegador-prod firefox --no-remote` (só enxerga os arquivos dentro de `~/Perfis-Isolados/navegador-prod`); **(2) Perfil Pesquisa Geral / Redes Sociais**: `firejail --private=~/Perfis-Isolados/navegador-web firefox --no-remote` (mesmo que um site malicioso ou extensão comprometida explore esse segundo navegador, ele **não consegue ler nenhum cookie, token ou arquivo do navegador de produção nem da sua `/home` principal**!); e **(3) Sandbox Descartável Offline para Triagem de Arquivos Externos**: `firejail --private --net=none --nonewprivs --caps.drop=all --seccomp --noroot`!

## Exemplo
```bash
# Abrir um arquivo PDF suspeito copiando-o automaticamente para uma sandbox 100% em RAM (--private-cwd) e totalmente sem rede (--net=none)
firejail \
  --private \
  --private-dev \
  --private-tmp \
  --net=none \
  --caps.drop=all \
  --nonewprivs \
  --seccomp \
  evince
```

## Limites e trade-offs
Para copiar apenas um único arquivo específico do host para dentro de uma sandbox `--private` em RAM sem expor a pasta original onde o arquivo estava, utilize a diretiva **`--private-home`** ou copie o arquivo via **`firejail --put=<nome_sandbox> ./arquivo_suspeito.pdf /tmp/`** após iniciar a sandbox vazia!

## Como verificar
Essa arquitetura de compartimentalização por contexto no Linux transforma sua estação de trabalho em um ambiente de defesa em profundidade próximo ao modelo de domínios isolados, porém com custo zero de máquina virtual e velocidade nativa!

## Conexões
- [[firejail-hardening-global-firejail-config-suid-firejail-users-grupos]] — Veja também: Hardening Global do Próprio Firejail (**`/etc/firejail/firejail.config`** e **`firejail.users`**): Mitigando Riscos de Binários SUID no Linux.
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Referência cruzada direta com firejail-isolamento-filesystem-private-private-dev-private-etc-bin.
- [[firejail-isolamento-rede-net-none-veth-netfilter-dns-sandboxing]] — Referência cruzada direta com firejail-isolamento-rede-net-none-veth-netfilter-dns-sandboxing.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
