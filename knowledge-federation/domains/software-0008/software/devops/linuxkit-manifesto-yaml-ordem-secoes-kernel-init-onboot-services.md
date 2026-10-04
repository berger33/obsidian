---
id: software.devops.tranche20.001902
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md", "https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md", "https://github.com/linuxkit/linuxkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# LinuxKit Manifesto YAML (`docs/yaml.md`): ordem de processamento de `kernel`, `init`, `volumes`, `onboot`, `onshutdown`, `services` e `files`

## Em uma frase
O arquivo de configuração YAML do LinuxKit é processado pelo comando `linuxkit build` em uma sequência estrita de sete seções — **`kernel`**, **`init`**, **`volumes`**, **`onboot`**, **`onshutdown`**, **`services`** e **`files`** — onde cada seção adiciona arquivos e metadados ao sistema de arquivos raiz da imagem final.

## Por que importa
Compreender a diferença exata de ciclo de vida entre imagens listadas em `init`, `onboot`, `onshutdown` e `services` evita colocar daemons contínuos em `onboot` (o que travaria a sequência de boot) ou assumir ordem fixa de partida em `services`.

## Como funciona
Na especificação oficial (`docs/yaml.md`): 1) `kernel` fornece o binário de kernel (`bzImage`), `kernel.tar` (módulos), `cmdline` e `ucode` (`intel-ucode.cpio`); 2) `init` desempacota imagens diretamente na raiz para subir o `containerd`; 3) `volumes` prepara diretórios ou layouts OCI; 4) `onboot` executa containers *one-shot* sequencialmente (cada um deve terminar antes do próximo iniciar, como `sysctl` ou `dhcpcd`); 5) `onshutdown` roda scripts de desligamento limpo; 6) `services` inicia daemons de longa duração no `containerd` (como `ntpd`, `sshd` ou `kubelet`); e 7) `files` injeta arquivos estáticos no rootfs.

## Exemplo
```yaml
kernel:
  image: linuxkit/kernel:6.6.13
  cmdline: "console=tty0 console=ttyS0"
init:
  - linuxkit/init:v1.2.0
  - linuxkit/runc:v1.2.0
  - linuxkit/containerd:v1.2.0
onboot:
  - name: sysctl
    image: linuxkit/sysctl:v1.0.0
services:
  - name: getty
    image: linuxkit/getty:v1.0.0
    env:
      - INSECURE=true
```

## Limites e trade-offs
Como a ordem de inicialização dos containers listados em `services` não é determinística, qualquer daemon em `services` deve aguardar ativamente que recursos dependentes (como rede ou mounts) estejam prontos.

## Como verificar
Valide a montagem do sistema de arquivos gerando um tarball de inspeção com `linuxkit build --format tar linuxkit.yml` e listando seu conteúdo com `tar -tvf linuxkit.tar`.

## Conexões
- [[linuxkit-arquitetura-os-imutavel-containers-containerd-runc]] — Veja também: LinuxKit: arquitetura de distribuições Linux mínimas e imutáveis construídas com containers sobre `containerd` e `runc`.
- [[linuxkit-alocacao-automatica-uid-gid-isolamento-containers-files]] — Veja também: LinuxKit Isolamento de Identidades: alocação automática de `uid` e `gid` por nome de container entre `services` e `files`.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
