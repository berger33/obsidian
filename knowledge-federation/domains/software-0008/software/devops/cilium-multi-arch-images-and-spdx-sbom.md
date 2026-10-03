---
id: software.devops.tranche02.000129
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
fontes: ["https://raw.githubusercontent.com/cilium/cilium/main/README.rst", "https://docs.cilium.io/en/stable/overview/component-overview/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Distribuição de imagens AMD64/AArch64 e SBOM em formato SPDX desde a v1.13.0

## Em uma frase
As subseções `Architectures` e `Software Bill of Materials` do `README.rst` documentam que as imagens do Cilium são distribuídas para as arquiteturas `AMD64` e `AArch64` e que, desde a versão `1.13.0`, todas as imagens incluem uma Software Bill of Materials (SBOM) gerada no formato `SPDX` (`spdx.dev`), com detalhes adicionais em `docs.cilium.io/en/latest/configuration/sbom/`.

## Por que importa
Em ambientes corporativos que combinam nós x86_64 e ARM64 (como instâncias AWS Graviton) e exigem auditoria de cadeia de suprimentos de software, contar com imagens multi-arquitetura e SBOM SPDX nativo acelera a homologação de segurança.

## Como funciona
Incorpore a verificação da SBOM SPDX das imagens do Cilium em seu pipeline de conformidade e replique as imagens homologadas para o registro corporativo (como o Harbor, visto nos itens 141–150).

## Exemplo
Uma equipe de segurança extrai o manifesto SPDX das imagens `v1.20.2` do Cilium para inventariar dependências em clusters AMD64 e AArch64.

## Limites e trade-offs
Certifique-se de que todos os DaemonSets auxiliares no cluster também possuam imagens multi-arquitetura antes de adicionar nós ARM64 (`AArch64`) ao pool.

## Como verificar
Conferi as subseções Architectures e Software Bill of Materials em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-stable-releases-and-three-minor-support-policy]] — Veja também: Política de manutenção das três últimas versões menores estáveis do Cilium.
- [[cilium-dual-licensing-userspace-and-bpf-templates]] — Veja também: Licenciamento Apache 2.0 em espaço de usuário e duplo licenciamento GPL-2.0/BSD-2-Clause em BPF.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
