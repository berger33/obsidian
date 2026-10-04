---
id: software.seguranca.tranche13.001278
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

# Geração Automática de Perfis de Segurança sob Medida com **`firejail --build`** e Auditoria de Sandboxes em Execução (**`--join`**, **`--ls`**, **`--get`**)

## Em uma frase
E quando você desenvolveu um microserviço interno em Python/Go/Node.js, ou baixou uma ferramenta de linha de comando que ainda não possui um arquivo `.profile` oficial em `/etc/firejail/`, e quer criar rapidamente um perfil de segurança sob medida seguindo o **Princípio do Privilégio Mínimo**?

## Por que importa
O Firejail possui um gerador automático de perfis baseado em *tracing* de execução: o comando **`firejail --build=meu-app.profile ./meu-app`**!

## Como funciona
Quando você executa o aplicativo com **`--build`**, o Firejail monitora em tempo real (via `strace` interno) todos os arquivos lidos/escritos, bibliotecas carregadas, sockets de rede abertos e chamadas de sistema utilizadas durante a sessão de teste; no instante em que você fecha o aplicativo, o Firejail **escreve automaticamente um arquivo `meu-app.profile` enxuto contendo as diretivas `whitelist`, `private-bin`, `private-etc`, `seccomp`, `caps.drop all`, `nonewprivs` e `net none` ajustadas exatamente para o que o programa realmente precisou usar**!

## Exemplo
```bash
# Gerar automaticamente um perfil .profile sob medida observando a execucao de um binario e inspecionar arquivos de uma sandbox ativa
firejail --build=./meu_servico.profile ./meu_servico --self-test
firejail --name=sandbox_analise --private --net=none sleep 60 &
firejail --ls=sandbox_analise ~
```

## Limites e trade-offs
Além do `--build`, quando você nomeia uma sandbox em execução com **`--name=sandbox_analise`**, pode auditar seu interior a partir de outro terminal sem interrompê-la usando: **`firejail --ls=sandbox_analise ~`** (listar arquivos dentro do Mount Namespace da sandbox), **`firejail --get=sandbox_analise ~/relatorio.txt`** (copiar com segurança um arquivo gerado lá dentro para o diretório atual do host!) ou **`firejail --join=sandbox_analise`**!

## Como verificar
Para encerrar imediatamente todos os processos de uma sandbox nomeada, execute **`firejail --shutdown=sandbox_analise`**.

## Conexões
- [[firejail-integracao-apparmor-cgroups-rlimits-controle-recursos]] — Veja também: Defesa em Profundidade no Firejail: Integração com **AppArmor (`--apparmor`)**, Limites de Recursos (**`rlimits`**) e **Control Groups (`--cgroup`)**.
- [[firejail-hardening-global-firejail-config-suid-firejail-users-grupos]] — Veja também: Hardening Global do Próprio Firejail (**`/etc/firejail/firejail.config`** e **`firejail.users`**): Mitigando Riscos de Binários SUID no Linux.
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.
- [[firejail-anatomia-perfis-profile-blacklist-whitelist-read-only-include]] — Referência cruzada direta com firejail-anatomia-perfis-profile-blacklist-whitelist-read-only-include.
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Referência cruzada direta com firejail-isolamento-filesystem-private-private-dev-private-etc-bin.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
