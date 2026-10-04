---
id: software.devops.tranche02.000130
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/cilium/cilium/main/README.rst", "https://github.com/cilium/cilium"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Licenciamento Apache 2.0 em espaço de usuário e duplo licenciamento GPL-2.0/BSD-2-Clause em BPF

## Em uma frase
A seção `License` do `README.rst` detalha o modelo de licenciamento do projeto: os componentes em espaço de usuário (`user space components`) do Cilium são licenciados sob `Apache License, Version 2.0`, enquanto os templates de código BPF (`bpf/`) possuem licenciamento duplo sob `General Public License, Version 2.0 (only)` (`bpf/LICENSE.GPL-2.0`) e `2-Clause BSD License` (`bpf/LICENSE.BSD-2-Clause`), permitindo utilizar os termos de qualquer uma das duas licenças à escolha do usuário, além de listar a governança (`GOVERNANCE.md`), os adotantes (`USERS.md`), as reuniões semanais de desenvolvedores às quartas-feiras e a livestream semanal `eCHO`.

## Por que importa
No kernel Linux, certos helpers e funcionalidades de eBPF exigem que o programa carregado no kernel declare compatibilidade com GPL; o duplo licenciamento dos templates BPF em GPL-2.0 e BSD-2-Clause atende simultaneamente às exigências técnicas do kernel e à flexibilidade jurídica de distribuição.

## Como funciona
Ao realizar auditoria jurídica de software livre (como no FOSSA), registre separadamente a licença Apache 2.0 do espaço de usuário e o licenciamento duplo GPL-2.0 / 2-Clause BSD dos programas BPF em `bpf/`.

## Exemplo
O departamento jurídico aprova o uso do Cilium após verificar a seção License de `README.rst` e os arquivos `LICENSE`, `bpf/LICENSE.GPL-2.0` e `bpf/LICENSE.BSD-2-Clause`.

## Limites e trade-offs
Não confunda a licença do código em espaço de usuário (Go, Apache 2.0) com os requisitos de licença dos bytecodes eBPF carregados no kernel Linux.

## Como verificar
Conferi as seções Community, Governance, Adopters e License em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-multi-arch-images-and-spdx-sbom]] — Veja também: Distribuição de imagens AMD64/AArch64 e SBOM em formato SPDX desde a v1.13.0.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium — Repositório Oficial no GitHub](https://github.com/cilium/cilium) — Repositório oficial do Cilium graduado na CNCF com código-fonte, templates BPF, USERS.md e MAINTAINERS.md.; consultado em 2026-10-03.
