---
id: software.devops.tranche20.001907
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
fontes: ["https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md", "https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md", "https://github.com/linuxkit/linuxkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# LinuxKit Packages (`linuxkit pkg`): construção reprodutível e multi-arquitetura de pacotes de sistema em containers

## Em uma frase
No ecossistema LinuxKit, todo componente de sistema (`pkg/init`, `pkg/containerd`, `pkg/runc`, `pkg/sshd`, `pkg/ntpd`, `pkg/ rngd`, `pkg/mount`) é construído como um pacote OCI imutável e determinístico gerenciado pelo subcomando **`linuxkit pkg`** (`build`, `push`, `show-tag`) a partir de um arquivo `build.yml` e um `Dockerfile`.

## Por que importa
Se uma imagem de sistema operacional referenciar tags flutuantes como `:latest` sem fixar o hash do conteúdo do código-fonte do pacote, dois builds executados em semanas diferentes produzirão binários diferentes, quebrando a reprodutibilidade.

## Como funciona
O utilitário `linuxkit pkg show-tag` calcula uma tag baseada no **hash Git da árvore do diretório do pacote**: qualquer modificação no `Dockerfile`, no `build.yml` ou no código-fonte altera o hash da tag automaticamente, garantindo cache determinístico e builds multi-arquitetura (`amd64`, `arm64`, `s390x`) assináveis.

## Exemplo
```bash
# Inspecionando a tag determinística baseada em hash de um pacote LinuxKit e construindo-o:
linuxkit pkg show-tag ./pkg/sshd
linuxkit pkg build ./pkg/sshd
```

## Limites e trade-offs
No arquivo `build.yml` de cada pacote em `pkg/`, já ficam declarados os metadados recomendados de runtime (como `capabilities`, `binds`, `net: host` ou `pid: host`), que são herdados automaticamente quando o pacote é referenciado no `linuxkit.yml`, sem exigir repetir dezenas de linhas de configuração.

## Como verificar
Execute `linuxkit pkg show-tag` em um diretório de pacote para verificar o identificador de versão determinístico calculado a partir da árvore Git.

## Conexões
- [[linuxkit-run-hipervisores-locais-qemu-hyperkit-virtualization-framework-cloud]] — Veja também: LinuxKit `linuxkit run`: execução e teste de imagens em QEMU, macOS `Virtualization.Framework`, Hyper-V, VMware e Cloud.
- [[linuxkit-armazenamento-persistente-format-mount-extend-var-lib-docker]] — Veja também: LinuxKit Armazenamento Persistente: particionamento e montagem automática no boot com pacotes `format`, `extend` e `mount`.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
