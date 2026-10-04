---
id: software.devops.tranche08.000707
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md", "https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md", "https://github.com/kata-containers/kata-containers"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kata Containers: ferramentas de diagnóstico e depuração (kata-ctl, agent-ctl, kata-debug e trace-forwarder)

## Em uma frase
O ecossistema de utilitários do Kata Containers inclui `kata-ctl` (comandos avançados e debug), `agent-ctl` (testes de baixo nível do `kata-agent`), `kata-debug` (coleta de diagnósticos em clusters Kubernetes) e `trace-forwarder` (encaminhamento de traces do agente).

## Por que importa
Depurar um container que roda dentro de uma máquina virtual isolada é mais complexo do que depurar um processo local no host, pois o `kata-agent` está separado do host pela fronteira do hipervisor (comunicando-se via `vsock`) e seus traces e estados internos não são visíveis diretamente via `ps` ou `strace` no servidor físico. A tabela `Additional components` do README oficial do Kata Containers apresenta quatro ferramentas dedicadas para resolver essa visibilidade.

## Como funciona
(1) **`kata-ctl` (`src/tools/kata-ctl`)**: utilitário em Rust que fornece comandos avançados de verificação de ambiente, inspeção de métricas, monitoria e facilidades de debug do runtime; (2) **`agent-ctl` (`src/tools/agent-ctl`)**: ferramenta de baixo nível que permite conectar diretamente ao `kata-agent` (via vsock/mock) e enviar requisições da API TT-RPC do agente para testar criação de sandbox e containers de forma isolada; (3) **`kata-debug` (`tools/packaging/kata-debug`)**: utilitário projetado para coletar automaticamente informações de depuração e logs do Kata Containers a partir de nós de um cluster Kubernetes; e (4) **`trace-forwarder` (`src/tools/trace-forwarder`)**: componente auxiliar que recebe spans de tracing distribuído (OpenTelemetry) gerados pelo `kata-agent` dentro da VM guest via `vsock` e os encaminha ao coletor no host.

## Exemplo
```bash
# Executar verificações de sistema e ambiente usando o utilitário moderno kata-ctl
kata-ctl check
kata-ctl env
```

## Limites e trade-offs
O uso de `agent-ctl` para enviar comandos diretos ao `kata-agent` de uma VM ou o acionamento de tracing completo via `trace-forwarder` são voltados para ambientes de desenvolvimento, CI e diagnóstico profundo; em produção, o canal de controle `vsock` da VM deve permanecer gerenciado exclusivamente pelo processo `containerd-shim-kata-v2` para evitar inconsistências de estado entre o containerd e o agente guest.

## Como verificar
Execute `kata-ctl version` e `kata-ctl check` no nó hospedeiro para validar o funcionamento do utilitário de diagnóstico em Rust e inspecionar os relatórios de capacidade do host.

## Conexões
- [[kata-packaging-kata-deploy-helm-kubernetes-runtimeclass]] — Veja também: Kata Containers: empacotamento de binários e implantação em Kubernetes com o Helm chart kata-deploy e RuntimeClass.
- [[kata-webhook-admissao-mutacao-pods-runtimeclass]] — Veja também: Kata Containers: mutating admission webhook (kata-webhook) para injeção transparente de RuntimeClass em Pods.
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[kata-componentes-principais-shimv2-runtime-rs-agent-dragonball]] — Referência cruzada direta com kata-componentes-principais-shimv2-runtime-rs-agent-dragonball.
- [[kata-requisitos-hardware-arquiteturas-kata-runtime-check]] — Referência cruzada direta com kata-requisitos-hardware-arquiteturas-kata-runtime-check.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
